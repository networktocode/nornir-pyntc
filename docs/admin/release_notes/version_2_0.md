# v2.0.0 Release Notes

## [2.0.0] 04-2023

### Added

- Add `wait_for_reload` kwarg in `pyntc_reboot` task to mirror updated pyntc methods as of `1.0.0` of pyntc.

### Fixed

- `pyntc_config` - Update docstrings and support both list|str inputs.

### Deprecated

- Remove `pyntc_show_list` tasks, as `pyntc_show` now accepts a list or a str argument.
- Remove `timer` argument from `pyntc_reboot` task as it was deprecated in underlying `pyntc` library in `1.0.0`.
