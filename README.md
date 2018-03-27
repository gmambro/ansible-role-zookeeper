Ansible role for Zookeeper
==========================

[![Build Status](https://travis-ci.org/gmambro/ansible-role-zookeeper.svg?branch=master)](https://travis-ci.org/gmambro/ansible-role-zookeeper)


Requirements
------------

Ansible version at least 2.4. Java should be installed on the nodes
 (check https://github.com/geerlingguy/ansible-role-java)

Role Variables
--------------

```yaml
---
zookeeper_version: 3.4.11

zookeeper_node_id: 1
zookeeper_ensemble:
  - localhost

zookeeper_dir: /opt/zookeeper

zookeeper_client_port: 2181
zookeeper_init_limit: 5
zookeeper_sync_limit: 2
zookeeper_tick_time: 2000
'''

The node id can be se using the zookeeper_node_id variables (e.g. coming from
   the inventory)

When zookeeper_node_id is not set it automatically generated from the
zookeeper_ensemble, which can can be a list of hostnames or a list of dictionaries.
When it is a list of dictionaries the id is supposed to in the 'id' field,
otherwise the id is given by the position of the host in the list.


Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: localhost
      roles:
        - name: gmambro.zookeeper
          vars:
            zookeeper_node_id: 1

Zookeeper cluster.

    - hosts: zookeeper
      roles:
        - name: gmambro.zookeeper
          vars:
            zookeeper_ensemble: "{{groups['zookeeper']}}"



License
-------

Apache

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
