import pytest
from edf_test_technique.src.entities.EnergyStorageSystem import EnergyStorageSystem
from edf_test_technique.src.errors.EssStockError import (
    ESSMinimumEssCapacityError,
    ESSMinimumEessStockError
)
from edf_test_technique.src.errors.EssChargeError import ( 
    ESSMaximumDischargeReachedError, 
    ESSMaximumChargeReachedError,
)

@pytest.fixture
def ess():
    ess = EnergyStorageSystem(
        eess=0,
        ess_capacity=10_000
    )
    return ess

def test_create_ess(ess):
    """
    Verify that an instance of EnergyStorageSystem is properly created
    and returns valid metadata.
    """
    assert (
        ess.pess == 0 and ess.eess == 0 and ess.ess_capacity == 10_000
    )

def test_ess_set_point_exceeding_maximum_charge(ess):
    """
    Verify that an exception is raised when trying to set a point-pess
    exceeding the maximum charge.
    """
    with pytest.raises(ESSMaximumChargeReachedError):
        ess.setpointPess(11_000)

def test_ess_set_point_exceeding_maximum_discharge(ess):
    """
    Verify that an exception is raised when trying to set a point-pess
    exceeding the maximum discharge.
    """
    with pytest.raises(ESSMaximumDischargeReachedError):
        ess.setpointPess(-15_000)

def test_ess_set_point_is_set_properly(ess):
    """
    Verify that a point-pess is properly set when complying with constraints.
    """
    ess.setpointPess(9_000)
    assert ess.pess == 9_000

def test_ess_compute_pmaxdisch_properly(ess):
    """
    Verify that the pmaxdisch is properly computed.
    """
    assert ess.pmaxdisch == ess.eess

def test_ess_compute_pmaxch_properly(ess):
    """
    Verify that the pmaxch is properly computed.
    """
    assert ess.pmaxch == ess.pess - ess.ess_capacity

def test_ess_cannot_have_negative_eess_stock():
    """
    Verify that ESS cannot have negative eess values.
    """
    with pytest.raises(ESSMinimumEessStockError):
        EnergyStorageSystem(
            eess=-1_000,
            ess_capacity=-10_000
        )

def test_ess_cannot_have_negative_ess_capacity():
    """
    Verify that ESS cannot have negative ess_capacity values.
    """
    with pytest.raises(ESSMinimumEssCapacityError):
        EnergyStorageSystem(
            eess=1_000,
            ess_capacity=-10_000
    )
