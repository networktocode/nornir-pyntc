# nornir-pyntc

Nornir-Pyntc is a [Nornir Plugin](https://nornir.readthedocs.io/en/latest/plugins/index.html).  It comes with a `connection` plugin and some basic `task` definitions.  It extends the main functionality that [Pyntc](https://github.com/networktocode/pyntc) comes with and supports natively.

## Connection Plugin

The Pyntc connection plugin allows Nornir to manage connections with devices using the Pyntc connection methods.

## Tasks

This plugin comes with pre-built Nornir tasks that line up with the basic Pyntc functionality.

- pyntc_config - Used to pass configuration commands to a network device.
- pyntc_file_copy - Used to copy a file to a network device.
- pyntc_install_os - Used to install an operating system for an OS upgrade.
- pyntc_reboot - Used to reboot a network device.
- pyntc_save - Used to save the running configuration of a network device.
- pyntc_show - Can be used to send a singular `show` command to a network device.
- pyntc_show_list - Same as pyntc_show but can send a list of commands.

For detailed information on the Pyntc methods, view the [Pyntc documentation](https://github.com/networktocode/pyntc).

## Examples

```python
from nornir import InitNornir
from nornir_pyntc.tasks.pyntc_show import pyntc_show
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

result = nr.run(task=pyntc_show, command="show version")

print_result(result)
```

```raw
pyntc_show**********************************************************************
* n5k1 ** changed : False ******************************************************
vvvv pyntc_show ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'bios_cmpl_time': '05/09/2012',
  'bios_ver_str': '3.6.0',
  'bootflash_size': 2007040,
  'chassis_id': 'Nexus5548 Chassis',
  'cpu_name': 'Intel(R) Xeon(R) CPU        ',
  'header_str': 'Cisco Nexus Operating System (NX-OS) Software\n'
                'TAC support: http://www.cisco.com/tac\n'
                'Documents: '
                'http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html\n'
                'Copyright (c) 2002-2022, Cisco Systems, Inc. All rights '
                'reserved.\n'
                'The copyrights to certain works contained herein are owned '
                'by\n'
                'other third parties and are used and distributed under '
                'license.\n'
                'Some parts of this software are covered under the GNU Public\n'
                'License. A copy of the license is available at\n'
                'http://www.gnu.org/licenses/gpl.html.\n',
  'host_name': 'Nexus5K-1',
  'isan_cmpl_time': ' 2/8/2022 3:00:00',
  'isan_file_name': 'bootflash:///n5000-uk9.7.3.11.N1.1.bin',
  'isan_tmstmp': '02/08/2022 14:26:50',
  'kern_uptm_days': 0,
  'kern_uptm_hrs': 1,
  'kern_uptm_mins': 3,
  'kern_uptm_secs': 49,
  'kick_cmpl_time': ' 2/8/2022 3:00:00',
  'kick_file_name': 'bootflash:///n5000-uk9-kickstart.7.3.11.N1.1.bin',
  'kick_tmstmp': '02/08/2022 12:31:24',
  'kickstart_ver_str': '7.3(11)N1(1)',
  'mem_type': 'kB',
  'memory': 8253792,
  'module_id': 'O2 32X10GE/Modular Universal Platform Supervisor',
  'power_seq_ver_str': [ '             Module 1: v3.0',
                         '             Module 2: v2.0',
                         '             Module not detected',
                         '             Module not detected'],
  'proc_board_id': 'FOC190386H4',
  'rr_ctime': ' Tue Jan 26 14:22:12 2016\n',
  'rr_reason': 'Reset due to upgrade',
  'rr_service': '',
  'rr_sys_ver': '7.3(8)N1(1)',
  'rr_usecs': 628308,
  'sys_ver_str': '7.3(11)N1(1)',
  'ucontroller_ver_str': 'v1.2.0.1'}
^^^^ END pyntc_show ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* n5k2 ** changed : False ******************************************************
vvvv pyntc_show ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'bios_cmpl_time': '05/09/2012',
  'bios_ver_str': '3.6.0',
  'bootflash_size': 2007040,
  'chassis_id': 'Nexus5548 Chassis',
  'cpu_name': 'Intel(R) Xeon(R) CPU        ',
  'header_str': 'Cisco Nexus Operating System (NX-OS) Software\n'
                'TAC support: http://www.cisco.com/tac\n'
                'Documents: '
                'http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html\n'
                'Copyright (c) 2002-2022, Cisco Systems, Inc. All rights '
                'reserved.\n'
                'The copyrights to certain works contained herein are owned '
                'by\n'
                'other third parties and are used and distributed under '
                'license.\n'
                'Some parts of this software are covered under the GNU Public\n'
                'License. A copy of the license is available at\n'
                'http://www.gnu.org/licenses/gpl.html.\n',
  'host_name': 'Nexus5K-2',
  'isan_cmpl_time': ' 2/8/2022 3:00:00',
  'isan_file_name': 'bootflash:///n5000-uk9.7.3.11.N1.1.bin',
  'isan_tmstmp': '02/08/2022 14:26:50',
  'kern_uptm_days': 0,
  'kern_uptm_hrs': 1,
  'kern_uptm_mins': 37,
  'kern_uptm_secs': 48,
  'kick_cmpl_time': ' 2/8/2022 3:00:00',
  'kick_file_name': 'bootflash:///n5000-uk9-kickstart.7.3.11.N1.1.bin',
  'kick_tmstmp': '02/08/2022 12:31:24',
  'kickstart_ver_str': '7.3(11)N1(1)',
  'mem_type': 'kB',
  'memory': 8253792,
  'module_id': 'O2 32X10GE/Modular Universal Platform Supervisor',
  'power_seq_ver_str': [ '             Module 1: v3.0',
                         '             Module 2: v2.0',
                         '             Module not detected',
                         '             Module not detected'],
  'proc_board_id': 'FOC190386H2',
  'rr_ctime': ' Tue Jan 26 14:33:19 2016\n',
  'rr_reason': 'Reset due to upgrade',
  'rr_service': '',
  'rr_sys_ver': '7.3(8)N1(1)',
  'rr_usecs': 68494,
  'sys_ver_str': '7.3(11)N1(1)',
  'ucontroller_ver_str': 'v1.2.0.1'}
^^^^ END pyntc_show ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Questions
---------

For any questions or comments, please feel free to swing by the [networktocode slack channel](https://networktocode.slack.com).

Sign up [here](http://slack.networktocode.com/)
