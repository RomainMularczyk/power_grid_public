from edf_test_technique.src.errors.PvChargeError import PVMinimumChargeError

class PhotovoltaicPowerPlant:
    """
    Class responsible for providing measures to evaluate the power production
    of the photovoltaic power plant.

    Attributes
    ----------
    ppv : int
        Current PV active power output (in W).
    """

    def __init__(self, ppv: int) -> None:
        if ppv < 0:
            raise PVMinimumChargeError 
        self._ppv = ppv

    @property
    def ppv(self) -> int:
        return self._ppv

