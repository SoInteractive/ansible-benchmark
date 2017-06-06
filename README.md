<p><img src="https://avatars2.githubusercontent.com/u/18436491?v=3&s=200" alt="sointeractive logo" title="sointeractive" align="right" height="60" /></p>

Ansible Role: check server
==========================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/check-server/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fcheck-server/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/99999.svg)](https://galaxy.ansible.com/SoInteractive/check-server/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Check server parameters

Role copies all information about the server to the file which is copied to your computer. At the beginning there are collecting information about CPU and then role checks is there need to install necessary software. Next it checks write and read speed of your disk drive and at the end CPU speed.

Disclaimer
----------

Role isn't tested for idempotence

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.check-server
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
