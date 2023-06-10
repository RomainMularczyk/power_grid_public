class ESSMaximumChargeReachedError(Exception):
    """
    Exception raised when the maximal charge power capability of the ESS
    is exceeded.
    """
    def __init__(self, ess_max_ch: int, current_ch: int) -> None:
        msg = "Maximum charge power capability is reached." \
        + f" Current charge is : {str(current_ch)}." \
        + f" Maximum charge is : {str(ess_max_ch)}."
        super().__init__(msg)


class ESSMaximumDischargeReachedError(Exception):
    """
    Exception raised when the minimal charge power capability of the ESS
    is exceeded.
    """
    def __init__(self, ess_max_disch: int, current_ch: int) -> None:
        msg = "Maximum discharge power capability is reached. " \
        + f" Current charge is : {str(current_ch)}." \
        + f" Maximum discharge is : {str(ess_max_disch)}."
        super().__init__(msg)

class ESSPositiveMaximumChargeError(Exception):
    """
    Exception raised when the maximal charge power capability os the ESS
    is more than zero.
    """
    def __init__(self, ess_max_ch: int) -> None:
        msg = "Charge of the ESS cannot be positive." \
        + f" Maximal charge computed is : {str(ess_max_ch)}."
        super().__init__(msg)

class ESSNegativeMaximumDischargeError(Exception):
    """
    Exception raised when the maximal discharge power capability os the ESS
    is less than zero.
    """
    def __init__(self, ess_max_ch: int) -> None:
        msg = "Discharge of the ESS cannot be negative." \
        + f" Maximal discharge computed is : {str(ess_max_ch)}."
        super().__init__(msg)

