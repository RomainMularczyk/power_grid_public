class IndustrialSite:
    def __init__(self, pload: int) -> None:
        self._pload = pload

    @property
    def pload(self) -> int:
        return self._pload

