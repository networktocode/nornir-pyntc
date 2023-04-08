"""Test reboot."""

from builtins import ValueError
from pyntc.devices import IOSDevice, NXOSDevice
from pyntc.errors import RebootTimeoutError
from requests.exceptions import ReadTimeout

from nornir_pyntc.tasks import pyntc_reboot


def test_pyntc_reboot_nxos(nornir_conn, monkeypatch):
    def mock_reboot(cls, wait_for_reload):  # pylint:disable=unused-argument
        return True

    monkeypatch.setattr(NXOSDevice, "reboot", mock_reboot)
    device = nornir_conn.filter(name="router1")
    result = device.run(pyntc_reboot)
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is True


def test_pyntc_reboot_ios(nornir_conn, monkeypatch):
    def mock_reboot(cls, wait_for_reload):  # pylint:disable=unused-argument
        return False

    monkeypatch.setattr(IOSDevice, "reboot", mock_reboot)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_reboot)
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False


def test_pyntc_reboot_reboottimer_exception(nornir_conn, monkeypatch):
    def mock_reboot(cls, wait_for_reload):  # pylint:disable=unused-argument
        raise RebootTimeoutError(wait_time=10, hostname="router2")

    monkeypatch.setattr(IOSDevice, "reboot", mock_reboot)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_reboot)
    assert len(result["router2"]) == 1
    assert isinstance(result["router2"].exception, RebootTimeoutError)
    assert result["router2"].failed is True
    assert result["router2"].changed is False


def test_pyntc_reboot_timeout_exception(nornir_conn, monkeypatch):
    def mock_reboot(cls, wait_for_reload):  # pylint:disable=unused-argument
        raise ReadTimeout

    monkeypatch.setattr(IOSDevice, "reboot", mock_reboot)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_reboot)
    assert len(result["router2"]) == 1
    assert result["router2"].result == "Connection Closed. Reboot In Progress."
    assert result["router2"].failed is False
    assert result["router2"].changed is True


def test_pyntc_reboot_other_exception(nornir_conn, monkeypatch):
    def mock_reboot(cls, wait_for_reload):  # pylint:disable=unused-argument
        raise ValueError

    monkeypatch.setattr(IOSDevice, "reboot", mock_reboot)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_reboot)
    assert len(result["router2"]) == 1
    assert isinstance(result["router2"].exception, ValueError)
    assert result["router2"].failed is True
    assert result["router2"].changed is False
