# base-packages

[![Build Status](https://travis-ci.org/infOpen/ansible-role-base-packages.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-base-packages)

Install base-packages package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
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
- http://www.infopen.pro
- a.chaussier [at] infopen.pro
