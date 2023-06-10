import pytest
from edf_test_technique.src.EnergyStorageSystem import EnergyStorageSystem
from edf_test_technique.src.Grid import Grid
from edf_test_technique.src.PhotovoltaicPowerPlant import PhotovoltaicPowerPlant
from edf_test_technique.src.PointOfConnection import PointOfConnection

@pytest.fixture
def ess():
    ess = EnergyStorageSystem(
        eess=0,
        ess_capacity=10_000
    )
    return ess
    
@pytest.fixture
def poc():
    poc = PointOfConnection(pmaxsite=200)
    poc.setPpoc(ppoc=150)
    return poc

@pytest.fixture
def pv():
    pv = PhotovoltaicPowerPlant(ppv=200_000)
    return pv

def test_ess_measures_are_valid(ess):
    """
    Verify that the ESS measures are valid.
    """
    assert Grid.getEssMeasure(ess) == (0, -10_000, 0, 0)

def test_pv_measures_are_valid(pv):
    """
    Verify that the PV measures are valid.
    """
    assert Grid.getPvMeasure(pv) == 200_000

def test_pv_measures_in_kw_are_valid(pv):
    """
    Verify that conversion in kW is valid.
    """
    assert Grid.getPvMeasure(pv, kw=True) == 200

def test_poc_meter_measures_are_valid(poc):
    """
    Verify that the POC measures are valid.
    """
    assert Grid.getPocMeterMeasure(poc) == 150

def test_pload_measures_are_valid(ess, poc, pv):
    """
    Verify that the Pload measures are valid.
    """
    assert Grid.getPloadMeasure(ess, poc, pv) == 150 - 0 - 200

def test_set_ess_setpoint(ess):
    """
    Verify that the grid can control the setpoint of the energy storage
    system and that the setup values are valid.
    """
    Grid.setEssSetpoint(ess, 10_000)
    ess.pess == 10_000

