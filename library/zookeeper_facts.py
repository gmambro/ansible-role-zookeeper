#!/usr/bin/python
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: zookeeper_facts
short_description: Gather facts for Zookeeper Nodes
description:
     - Gather facts for zookeepr nodes.
options:
  host:
    description:
      - Server name to retrieve facts for. Defaults to localhost
  port:
    description:
      - Zookeeper client port. Defaults to 2181
author: "Gabriele Mambrini"
'''

EXAMPLES = '''
- name: Gather info about servers
  hosts: all
  gather_facts: False
  tasks:
    - name: Get facts about servers
      zookeeper_facts:

    - name: Register zookeeper mode into a fact 
      set_fact:
        zookeeper_mode: "{{ zookeeper_facts.mode }}"
'''

from ansible.module_utils.basic import AnsibleModule
import socket

def zookeeper_facts(module, host, port):
    changed = False

    ansible_facts = {}

    try:
        client = socket.create_connection((host, port))

        f = client.makefile()
        f.write('stat')
        f.flush()

        for line in f:
            line = line.strip()

            #Receiving from client
            k,v  = line.split(':', 1)

            if k == 'Zookeeper version':
                ansible_facts['version'] = v
            elif k == 'Clients':
                clients = []
                line2 = f.readline().strip()
                while line2 != '':
                    clients.append(line2)
                    line2 = f.readline().strip()
            elif k == 'Latency min/avg/max':
                values = v.split('/')
                ansible_facts['latency'] = { 'min': values[0], 'avg': values[1], 'max': values[2] }
            elif k in [ 'Received', 'Sent', 'Connections', 'Outstanding', 'Zxid', 'Mode', 'Node count' ]:
                ansible_facts[k.lower()] = v

        client.close()

    except Exception as e:
        module.fail_json(msg='%s' % e.message)

    module.exit_json(changed=changed, ansible_facts={ 'zookeeper_facts': ansible_facts })

def main():
    argument_spec = {
            "host": {"default": "localhost", "type": "str" },
            "port": {"default": 2181, "type": "int" }
	    }

    module = AnsibleModule(argument_spec=argument_spec)

    host = module.params.get('host')
    port = module.params.get('port')

    zookeeper_facts(module, host, port)


if __name__ == '__main__':
    main()
