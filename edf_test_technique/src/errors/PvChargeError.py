class PVMinimumChargeError(Exception):
    """
    Exception raised when the charge power capability of the PV
    is negative.
    """
    def __init__(self) -> None:
        msg = "PV charge power capability cannot be negative."
        super().__init__(msg)

