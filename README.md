# base-packages

[![CI](https://github.com/infOpen/ansible-role-base-packages/workflows/CI/badge.svg)](https://github.com/infOpen/ansible-role-base-packages/actions)
[![Mergify Status][mergify-status]][mergify]
[![Updates](https://pyup.io/repos/github/infOpen/ansible-role-base-packages/shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-base-packages/)
[![Python 3](https://pyup.io/repos/github/infOpen/ansible-role-base-packages/python-3-shield.svg)](https://pyup.io/repos/github/infOpen/ansible-role-base-packages/)
[![Ansible Role](https://img.shields.io/ansible/role/12448.svg)](https://galaxy.ansible.com/infOpen/base-packages/)

Install misc packages on systems to manage base of all deployments.

## Requirements

This role requires Ansible 2.8 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/ansible-community/molecule) to run tests.

Local and Github Actions tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- CentOS 8
- Debian Buster
- Debian Stretch
- Ubuntu Bionic
- Ubuntu Focal

and use:
- Ansible 2.8.x
- Ansible 2.9.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

If a package must removed, add `state` key with 'absent' value.

### Default role variables

```yaml
base_packages_items: "{{ _base_packages_items }}"
base_packages_repository_cache_valid_time: 3600
```

### Specific Debian family variables

```yaml
_base_packages_items:
  - name: 'acl'
  - name: 'curl'
  - name: 'dstat'
  - name: 'git'
  - name: 'htop'
  - name: 'iftop'
  - name: 'iotop'
  - name: 'mtr'
  - name: 'rssh'
  - name: 'sshfs'
  - name: 'sysstat'
  - name: 'tree'
  - name: 'vim'
  - name: 'cron-apt'
  - name: 'debian-goodies'
  - name: 'di'
  - name: 'molly-guard'
  - name: 'nagios-plugins'
  - name: 'nagios-plugins-contrib'
```

### Specific RedHat family variables

```yaml
_base_packages_items:
  - name: 'acl'
  - name: 'curl'
  - name: 'dstat'
  - name: 'git'
  - name: 'htop'
  - name: 'iftop'
  - name: 'iotop'
  - name: 'mtr'
  - name: 'rssh'
  - name: 'sshfs'
  - name: 'sysstat'
  - name: 'tree'
  - name: 'vim'
  - name: 'nagios-plugins-all'
  - name: 'yum-cron'
  - name: 'yum-utils'
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
- https://www.infopen.pro
- a.chaussier [at] infopen.pro

[mergify]: https://mergify.io
[mergify-status]: https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/infOpen/ansible-role-base-packages&style=flat
