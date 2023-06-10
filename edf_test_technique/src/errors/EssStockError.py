class ESSMinimumEessStockError(Exception):
    """
    Exception raised when the amount of power stored on the
    energy storage system is negative.
    """
    def __init__(self) -> None:
        msg = "ESS storage power capability cannot be negative."
        super().__init__(msg)

class ESSMinimumEssCapacityError(Exception):
    """
    Exception raised when the maximum capacity of the energy storage
    system is negative.
    """
    def __init__(self) -> None:
        msg = "ESS maximal capacity cannot be negative."
        super().__init__(msg)

