"""Test Install OS."""

from builtins import ValueError
from pyntc.devices import IOSDevice, NXOSDevice
from requests.exceptions import ReadTimeout

from nornir_pyntc.tasks import pyntc_install_os


def test_pyntc_install_os_nxos(nornir_conn, monkeypatch):
    def mock_install_os(cls, image_name):  # pylint:disable=unused-argument
        return True

    monkeypatch.setattr(NXOSDevice, "install_os", mock_install_os)
    device = nornir_conn.filter(name="router1")
    result = device.run(pyntc_install_os, image_name="test-os")
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is True


def test_pyntc_install_os_ios(nornir_conn, monkeypatch):
    def mock_install_os(cls, image_name):  # pylint:disable=unused-argument
        return False

    monkeypatch.setattr(IOSDevice, "install_os", mock_install_os)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_install_os, image_name="test-os")
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False


def test_pyntc_install_os_timeout_exception(nornir_conn, monkeypatch):
    def mock_install_os(cls, image_name):  # pylint:disable=unused-argument
        raise ReadTimeout

    monkeypatch.setattr(IOSDevice, "install_os", mock_install_os)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_install_os, image_name="test-os")
    assert len(result["router2"]) == 1
    assert result["router2"].result == "Connection Closed. Install In Progress."
    assert result["router2"].failed is False
    assert result["router2"].changed is True


def test_pyntc_install_os_other_exception(nornir_conn, monkeypatch):
    def mock_install_os(cls, image_name):  # pylint:disable=unused-argument
        raise ValueError

    monkeypatch.setattr(IOSDevice, "install_os", mock_install_os)
    device = nornir_conn.filter(name="router2")
    result = device.run(pyntc_install_os, image_name="test-os")
    assert len(result["router2"]) == 1
    assert isinstance(result["router2"].exception, ValueError)
    assert result["router2"].failed is True
    assert result["router2"].changed is False
