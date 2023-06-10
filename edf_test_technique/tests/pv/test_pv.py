import pytest
from edf_test_technique.src.PhotovoltaicPowerPlant import PhotovoltaicPowerPlant
from edf_test_technique.src.errors.PvChargeError import PVMinimumChargeError

def test_pv_with_negative_power():
    """
    Verify that an exception is raised when trying to
    create an instance of PhotovoltaicPowerPlant with
    negative values.
    """
    with pytest.raises(PVMinimumChargeError):
        PhotovoltaicPowerPlant(ppv=-100_000)

def test_create_pv():
    """
    Verify that ppv is accessible after created an instance
    of PhotovoltaicPowerPlant.
    """
    pv = PhotovoltaicPowerPlant(ppv=100_000)
    assert pv.ppv == 100_000

