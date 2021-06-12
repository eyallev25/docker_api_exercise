from support.docker_utils import *


def test_get_images_from_dockerhub():
    """"""
    image = get_images_from_dockerhub('nginx')
    assert image.tags[0] == "nginx:latest"


def test_pull_image_and_run_container():
    """"""
    container_response = pull_image_and_run_container('bfirsh/reticulate-splines')
    assert container_response.image_name == "bfirsh/reticulate-splines"
