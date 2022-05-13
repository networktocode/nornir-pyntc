"""Test show."""

from nornir_pyntc.tasks import pyntc_show
from pyntc.devices import IOSDevice, NXOSDevice


def test_pyntc_show_nxos(nr, monkeypatch):
    def mock_show(cls, command):  # pylint:disable=unused-argument
        return "version 1.1.1"

    monkeypatch.setattr(NXOSDevice, "show", mock_show)
    device = nr.filter(name="router1")
    result = device.run(pyntc_show, command="show version")
    assert len(result["router1"]) == 1
    assert result["router1"].result == "version 1.1.1"
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_show_ios(nr, monkeypatch):
    def mock_show(cls, command):  # pylint:disable=unused-argument
        return "version 1.1.1"

    monkeypatch.setattr(IOSDevice, "show", mock_show)
    device = nr.filter(name="router2")
    result = device.run(pyntc_show, command="show version")
    assert len(result["router2"]) == 1
    assert result["router2"].result == "version 1.1.1"
    assert result["router2"].failed is False
    assert result["router2"].changed is False
