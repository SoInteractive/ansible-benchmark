Ansible role to check server parameters
=====================================================

Role copies all information about the server to the file
and finally the file is copying to your computer. At the
beginning there are collecting information about CPU and
then role checks is there need to install necessary software
Next it checks write and read speed of your disk drive and
at the end CPU speed.

Requirements
------------

None

Examples
--------

Use it in a playbook as follows, assuming you already have docker setup:
```yaml
- hosts: all
  become: yes
  gather_facts: True
  roles:
    - check-server
```
