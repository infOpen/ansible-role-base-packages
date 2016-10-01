"""
Role tests
"""
import pytest

# To run all the tests on given docker images:
pytestmark = pytest.mark.docker_images(
    'infopen/ubuntu-trusty-ssh:0.1.0',
    'infopen/ubuntu-xenial-ssh-py27:0.2.0'
)


def test_packages(Package):

    packages = [
        'acl',
        'cron-apt',
        'curl',
        'debian-goodies',
        'di',
        'dstat',
        'git',
        'htop',
        'iftop',
        'iotop',
        'molly-guard',
        'mtr',
        'nagios-plugins',
        'nagios-plugins-contrib',
        'rssh',
        'sshfs',
        'sysstat',
        'tree',
        'vim'
    ]

    for package in packages:
        assert Package(package).is_installed
