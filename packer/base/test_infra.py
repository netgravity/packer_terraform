def test_git_is_installed(host):
    git = host.package("git")
    assert git.is_installed

def test_docker_running_and_enabled(host):
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled

