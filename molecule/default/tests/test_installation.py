"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
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
    'sshfs',
    'sysstat',
    'tree',
    'vim'
])
def test_debian_packages(host, name):
    """
    Tests packages are installed
    """

    if host.system_info.distribution not in ['debian', 'ubuntu']:
        pytest.skip('{} ({}) distribution not managed'.format(
            host.system_info.distribution, host.system_info.release))

    assert host.package(name).is_installed


@pytest.mark.parametrize('name', [
    'acl',
    'curl',
    'git',
    'iotop',
    'mtr',
    'sysstat',
    'tree',
    'vim-enhanced',
    'yum-utils'
])
def test_centos_packages(host, name):
    """
    Tests packages are installed
    """

    if host.system_info.distribution not in ['centos']:
        pytest.skip('{} ({}) distribution not managed'.format(
            host.system_info.distribution, host.system_info.release))

    assert host.package(name).is_installed
