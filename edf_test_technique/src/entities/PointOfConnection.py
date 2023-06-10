from edf_test_technique.src.errors.PocChargeError import POCMaxSiteChargeReachedError


class PointOfConnection:
    """
    Class responsible for providing measures to control the flow of power
    going in/out of the point of control in the grid.

    Attributes
    ----------
    pmaxsite : int
        Maximum power consumption allowed on the industrial site.
    ppoc : int
        Actual power flowing in/out of the local smart grid.
    """
    def __init__(self, pmaxsite: int) -> None:
        self._pmaxsite = pmaxsite 
        self._ppoc = None

    @property
    def pmaxsite(self) -> int:
        return self._pmaxsite

    @property
    def ppoc(self) -> int:
        return self._ppoc

    def setPpoc(self, ppoc: int) -> int:
        """
        Get a measure of the power flowing in/out of the local smart grid (in kW).
        """
        if ppoc > self.pmaxsite:
            raise POCMaxSiteChargeReachedError(pmaxsite=self.pmaxsite)
        self._ppoc = ppoc

