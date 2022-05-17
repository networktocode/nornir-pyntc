"""Test show."""

from pyntc.devices import IOSDevice, NXOSDevice
from pyntc.errors import CommandError

from nornir_pyntc.tasks import pyntc_show


def test_pyntc_show_nxos(nornir_conn, monkeypatch):
    def mock_show(cls, command):  # pylint:disable=unused-argument
        return "version 1.1.1"

    monkeypatch.setattr(NXOSDevice, "show", mock_show)
    device = nornir_conn.filter(name="router1")
    result = device.run(pyntc_show, command="show version")
    assert len(result["router1"]) == 1
    assert result["router1"].result == "version 1.1.1"
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_show_ios(nornir_conn, monkeypatch):
    def mock_show(cls, command):  # pylint:disable=unused-argument
        return "version 1.1.1"

    monkeypatch.setattr(IOSDevice, "show", mock_show)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_show, command="show version")
    assert len(result["router2"]) == 1
    assert result["router2"].result == "version 1.1.1"
    assert result["router2"].failed is False
    assert result["router2"].changed is False


def test_pyntc_show_exception(nornir_conn, monkeypatch):
    def mock_config(cls, command):  # pylint:disable=unused-argument
        raise CommandError(message="invalid command", command="show xversion")

    monkeypatch.setattr(IOSDevice, "show", mock_config)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_show, command="show xversion")
    assert len(result["router2"]) == 1
    assert isinstance(result["router2"].exception, CommandError)
    assert result["router2"].failed is True
    assert result["router2"].changed is False
