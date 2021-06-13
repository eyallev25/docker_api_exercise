import docker
import time
import concurrent.futures

images_list = [
    'bfirsh/reticulate-splines',
    'nginx'
]

client = docker.from_env()  # Instantiate docker client
timeout = 30  # Seconds


def print_container_stats():
    """Main method, allocate a new thread for each image from image_list and print stats when done.
            Arguments:

    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(pull_image_and_run_container, images_list)

    for result in results:
        print(f"For image name: '{result.image_name}' the max mem usage is: {result.max_mem}, and max cpu usage is:"
              f" {result.max_cpu}")


def pull_image_and_run_container(image_name):
    """Pull image from dockerhub, run docker container and find max metrics.
            Arguments:
                image_name (str) : The image name.
            Return:
                container_response (object) : The container metrics.
    """
    container_response = ContainerResponse(image_name)

    image = get_images_from_dockerhub(image_name)
    container = client.containers.run(image, detach=True)

    timeout_start = time.time()

    # TODO While container is still running.
    while time.time() < timeout_start + timeout:
        mem_usage, total_cpu_usage = _get_container_stats(container)
        container_response.max_mem_usage(mem_usage)
        container_response.max_cpu_usage(total_cpu_usage)

    # stop container.
    container.stop()
    return container_response


def get_images_from_dockerhub(image_name):
    """Pull image from dockerhub.
                Arguments:
                    image_name (str) : The image name.
                Return:
                    image (object) : The image.
    """
    image = client.images.pull(image_name)
    return image


def _get_container_stats(container):
    """Pull image from dockerhub.
                    Arguments:
                        container (object) : The container object.
                    Return:
                        mem_usage (int) : container's mem usage metric.
                        total_cpu_usage (int) : container's total cpu usage metric.
    """
    status = container.stats(decode=None, stream=False)
    mem_usage = status['memory_stats']['usage']
    total_cpu_usage = status['cpu_stats']['cpu_usage']['total_usage']

    return mem_usage, total_cpu_usage


class ContainerResponse:
    def __init__(self, image_name):
        self.image_name = image_name
        self.max_mem = 0
        self.max_cpu = 0
        self.container_id = ""

    def max_mem_usage(self, mem_usage):
        if mem_usage > self.max_mem:
            self.max_mem = mem_usage

    def max_cpu_usage(self, cpu_usage):
        if cpu_usage > self.max_cpu:
            self.max_cpu = cpu_usage


if __name__ == '__main__':
    print_container_stats()
