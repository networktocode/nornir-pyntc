"""Test reboot."""

from nornir_pyntc.tasks import pyntc_file_copy
from pyntc.devices import IOSDevice, NXOSDevice


def test_pyntc_filecopy_nxos(nr, monkeypatch):
    def mock_file_copy(cls, src):  # pylint:disable=unused-argument
        return True

    monkeypatch.setattr(NXOSDevice, "file_copy", mock_file_copy)
    device = nr.filter(name="router1")
    result = device.run(pyntc_file_copy, src="source")
    assert len(result["router1"]) == 1
    assert result["router1"].result is True
    assert result["router1"].failed is False
    assert result["router1"].changed is False


def test_pyntc_filecopy_ios(nr, monkeypatch):
    def mock_file_copy(cls, src):  # pylint:disable=unused-argument
        return False

    monkeypatch.setattr(IOSDevice, "file_copy", mock_file_copy)
    device = nr.filter(name="router2")
    result = device.run(pyntc_file_copy, src="source")
    assert len(result["router2"]) == 1
    assert result["router2"].result is False
    assert result["router2"].failed is False
    assert result["router2"].changed is False
