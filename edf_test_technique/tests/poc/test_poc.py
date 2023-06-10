import pytest
from edf_test_technique.src.entities.PointOfConnection import PointOfConnection
from edf_test_technique.src.errors.PocChargeError import POCMaxSiteChargeReachedError


@pytest.fixture
def poc():
    poc = PointOfConnection(pmaxsite=200)
    return poc

def test_ppoc_cannot_be_inferior_to_pmaxsite(poc):
    """
    Verify that an exception is raised when ppoc
    is inferior to pmaxsite.
    """
    with pytest.raises(POCMaxSiteChargeReachedError):
        poc.setPpoc(300)

def test_ppoc_is_set_properly(poc):
    """
    Verify that the ppoc measure is set properly.
    """
    poc.setPpoc(150)
    assert poc.ppoc == 150

def test_ppoc_is_inferior_to_pmaxsite(poc):
    """
    Verify that the ppoc is inferior to the pmaxsite limit.
    """
    poc.setPpoc(100)
    assert poc.ppoc < poc.pmaxsite

