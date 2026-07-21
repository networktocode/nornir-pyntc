# Library Overview

nornir-pyntc is a [Nornir Plugin](https://nornir.readthedocs.io/en/latest/plugins/index.html). It extends the main functionality that Nornir provides by adding a plugin wrapping around [pyntc](https://github.com/networktocode/pyntc) library. nornir-pyntc comes with a `connection` plugin and `task` definitions that can be used via the Nornir core library.

## Supported Platforms

- Cisco AireOS - uses netmiko (SSH)
- Cisco ASA - uses netmiko (SSH)
- Cisco IOS platforms - uses netmiko (SSH)
- Cisco NX-OS - uses pynxos (NX-API)
- Arista EOS - uses pyeapi (eAPI)
- Juniper Junos - uses PyEz (NETCONF)
- F5 Networks - uses f5-sdk (ReST)
