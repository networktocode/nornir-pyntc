# v3.0.0 Release Notes

## [3.0.0] 01-2024

### Changed

- Updated `pyntc` dependency to 2.0.0, which contains updates related to changes in netmiko 4.0. In short `delay_factor` was deprecated in favor of `read_timeout`.

  Refer to this blog post for more info about changes in netmiko 4.0: https://pynet.twb-tech.com/blog/netmiko-read-timeout.html

### Removed

- Dropped support for python3.7
