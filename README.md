# base-packages

[![Build Status](https://travis-ci.org/infOpen/ansible-role-base-packages.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-base-packages)

Install base-packages package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

If you want disabled package installation, set `base_packages_install_enabled`
to "False".

If `base_packages_simples_list` is not customized, os specific var will used,
else it's the custom list of package.

### Default role variables

```yaml
# Defaults file for base-packages
base_packages_simples_list : []
base_packages_install_enabled : True
```

### Specific debian variables

```yaml
base_packages_list: "{{
  _base_packages_common
  + _base_packages_os_specific[ansible_os_family | lower] }}"

_base_packages_common:
  - 'acl'       # Useful for extended permissions on fs
  - 'curl'      # Get files from internet or check url
  - 'dstat'     # iotop/vmstat/iftop in a same tool
  - 'git'       # Versionning
  - 'htop'      # top ehanced
  - 'iftop'     # Top for netword traffic
  - 'iotop'     # Top for i/o
  - 'mtr'       # To complete traceroute
  - 'rssh'      # To used restricted shell
  - 'sshfs'     # Used to mount fs by ssh
  - 'sysstat'   # Used to monitor system stats
  - 'tree'      # A tree view of directory
  - 'vim'       # Because loving color ;)

_base_packages_os_specific:
  debian:
    - 'cron-apt'                # To keep an package database updated
    - 'debian-goodies'          # Provide checkrestart
    - 'di'                      # Better than df
    - 'molly-guard'             # Not reboot by accident
    - 'nagios-plugins'          # Usefull monitoring scripts
    - 'nagios-plugins-contrib'  # Another usefull monitoring scripts

  redhat:
    - 'nagios-plugins-all'      # Usefull monitoring scripts
    - 'yum-cron'                # To keep an package database updated
    - 'yum-utils'               # Provide checkrestart
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.base-packages }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
