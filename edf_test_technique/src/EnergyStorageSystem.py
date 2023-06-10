from edf_test_technique.src.errors.EssStockError import (
    ESSMinimumEessStockError, 
    ESSMinimumEssCapacityError,
)
from edf_test_technique.src.errors.EssChargeError import (
    ESSMaximumChargeReachedError, 
    ESSMaximumDischargeReachedError, 
    ESSNegativeMaximumDischargeError, 
    ESSPositiveMaximumChargeError 
)

class EnergyStorageSystem:
    """
    Class responsible for providing measures to control the flow of power 
    going in and out of the energy storage system.

    Attributes
    ----------
    p_ess : int
        Current active power output (in kW).
    pmaxch : int
        Current ESS maximal charge power capability (in kW).
    pmaxdisch : int
        Current ESS maximal discharge power capability (in kW).
    eess : int
        Current ESS stored energy (in kWh).
    ess_capacity : int
        Maximum storage capacity of the ESS (in kWh).
    """
    def __init__(self, eess: int, ess_capacity: int) -> None:
        if eess < 0:
            raise ESSMinimumEessStockError
        self._eess = eess # kWh
        if ess_capacity < 0:
            raise ESSMinimumEssCapacityError
        self._ess_capacity = ess_capacity #kWh
        self._pess = 0

    @property
    def eess(self) -> int:
        return self._eess

    @property
    def pess(self) -> int:
        return self._pess

    @property
    def ess_capacity(self) -> int:
        return self._ess_capacity

    @property
    def pmaxch(self) -> int:
        """
        Maximum charge power capability (in kW).

        It is the amount of room for power currently left on the energy
        storage system and should be a negative value because it indicates
        how much we can add more on the device.
        """
        pmaxch = (self.eess - self.ess_capacity)
        if pmaxch > 0:
            raise ESSPositiveMaximumChargeError(pmaxch)
        return pmaxch

    @property
    def pmaxdisch(self) -> int:
        """
        Maximum discharge power capability (in kW).

        It is the amount of power storred currently on the energy storage
        system and should be a positive value because it indicates how much
        we can retrieve from the device.
        """
        pmaxdisch = self.eess
        if pmaxdisch < 0:
            raise ESSNegativeMaximumDischargeError(pmaxdisch)
        return pmaxdisch 

    def setpointPess(self, amount_power: int) -> None:
        """
        Compute the new ESS stored energy amount.
        
        It also verifies that the updated charge of the ESS fullfils
        the different minimal/maximal requirements :
        - The current charge does not exceed the maximal power capability (pmaxch)
        - The current charge is not inferior to the minimal power capability (pmaxdisch)

        Parameters
        ----------
        amount_power : int
            Amount of power flowing in or out of the ESS (in kW).

        Raises
        ------
        ESSMaximumChargeReachedError
            If the newly updated charge of the ESS exceeds the maximum
            charge power capability.
        ESSMaximumDischargeReachedError
            If the newly updated charge of the ESS exceeds the maximum
            discharge power capability.
        """
        if amount_power > -self.pmaxch:
            raise ESSMaximumChargeReachedError(
                ess_max_ch=self.pmaxch, 
                current_ch=self.pess
            )
        elif amount_power < self.pmaxdisch:
            raise ESSMaximumDischargeReachedError(
                ess_max_disch=self.pmaxdisch,
                current_ch=self.pess
            )
        else:
            self._pess = amount_power               

