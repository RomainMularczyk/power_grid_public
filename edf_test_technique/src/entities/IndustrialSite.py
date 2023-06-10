class IndustrialSite:
    """
    Class responsible for providing measures to evaluate the power consumption
    of the industrial site.

    Attributes
    ----------
    pload : int
        Total amount of power consumed by the industrial site.
    """
    def __init__(self, pload: int) -> None:
        self._pload = pload

    @property
    def pload(self) -> int:
        return self._pload

