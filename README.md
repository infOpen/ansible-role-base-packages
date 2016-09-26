# base-packages

[![Build Status](https://travis-ci.org/infOpen/ansible-role-base-packages.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-base-packages)

Install base packages on servers.

## Requirements

This role requires Ansible 1.5 or higher, and platform requirements are listed
in the metadata file.

## Testing

This role contains two tests methods :
- locally using Vagrant
- automatically with Travis

Local tests should be passed with Vagrant before push to Github.

## Role Variables

If you want disabled package installation, set base_packages_install_enabled to
"False".

If base_packages_simples_list is not customized, os specific var will used,
else it's the custom list of package.

### Default role variables

```
# Defaults file for base-packages
base_packages_simples_list : []
base_packages_install_enabled : True
```

### Specific debian variables

```
# Debian specific vars
base_packages_simples_list :
  - sysstat           # Used to monitor system stats
  - vim               # Because loving color ;)
  - cron-apt          # To keep an package database updated
  - debian-goodies    # Provide checkrestart
  - nagios-plugins    # Usefull monitoring scripts
  - tree              # A tree view of directory
  - htop              # top ehanced
  - iotop             # Top for i/o
  - iftop             # Top for netword traffic
  - di                # Better than df
  - dstat             # iotop/vmstat/iftop in a same tool
  - mtr               # To complete traceroute
  - molly-guard       # Not reboot by accident
  - git               # Versionning
  - curl              # Get files from internet or check url
  - rssh              # To used restricted shell
  - sshfs             # Used to mount fs by ssh
  - acl               # Useful for extended permissions on fs
```

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: achaussier.base-packages }

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://www.infopen.pro
- a.chaussier [at] infopen.pro

