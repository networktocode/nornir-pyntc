"""Test reboot."""

from pyntc.devices import IOSDevice, NXOSDevice
from pyntc.errors import CommandError

from nornir_pyntc.tasks import pyntc_config


def test_pyntc_config_nxos(nornir_conn, monkeypatch):
    def mock_config(cls, command):  # pylint:disable=unused-argument
        return "hostname router1"

    monkeypatch.setattr(NXOSDevice, "config", mock_config)
    device = nornir_conn.filter(name="router1")
    result = device.run(pyntc_config, commands="hostname router1")
    assert len(result["router1"]) == 1
    assert result["router1"].result == "hostname router1"
    assert result["router1"].failed is False
    assert result["router1"].changed is True


def test_pyntc_config_ios(nornir_conn, monkeypatch):
    def mock_config(cls, command):  # pylint:disable=unused-argument
        return ["hostname router2", "ntp server 1.1.1.1"]

    monkeypatch.setattr(IOSDevice, "config", mock_config)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_config, commands=["hostname router2", "ntp server 1.1.1.1"])
    assert len(result["router2"]) == 1
    assert result["router2"].result == ["hostname router2", "ntp server 1.1.1.1"]
    assert result["router2"].failed is False
    assert result["router2"].changed is True


def test_pyntc_config_exception(nornir_conn, monkeypatch):
    def mock_config(cls, command):  # pylint:disable=unused-argument
        raise CommandError(message="invalid command", command="interface nethernet1/1")

    monkeypatch.setattr(IOSDevice, "config", mock_config)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_config, commands=["interface nethernet1/1"])
    assert len(result["router2"]) == 1
    assert isinstance(result["router2"].exception, CommandError)
    assert result["router2"].failed is True
    assert result["router2"].changed is False
