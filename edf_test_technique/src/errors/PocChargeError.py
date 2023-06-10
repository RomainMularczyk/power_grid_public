class POCMaxSiteChargeReachedError(Exception):
    """
    Exception raised when the maximal charge of the industrial
    site is reached.
    """
    def __init__(self, pmaxsite: int) -> None:
        msg = "Maximum charge reached for the industrial site." \
        + f" Maximum charge is : {str(pmaxsite)}"
        super().__init__(msg)

