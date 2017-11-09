<p><img src="https://i.stack.imgur.com/NCbzK.png" alt="benchmark logo" title="benchmark" align="right" height="60" /></p>

Ansible Role: benchmark
=======================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-benchmark.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-benchmark) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.benchmark-blue.svg)](https://galaxy.ansible.com/SoInteractive/benchmark/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-benchmark.svg)](https://github.com/SoInteractive/ansible-benchmark/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

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
    - SoInteractive.benchmark
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- cleanup
- cleaner result file
- idempotency tests (add to Jenkinsfile, remove custom test from molecule.yml)
- tests
