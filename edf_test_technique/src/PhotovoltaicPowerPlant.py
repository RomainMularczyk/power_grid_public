from .errors.PvChargeError import PVMinimumChargeError

class PhotovoltaicPowerPlant:
    """
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

