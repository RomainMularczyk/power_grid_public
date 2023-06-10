from edf_test_technique.src.EnergyStorageSystem import EnergyStorageSystem
from edf_test_technique.src.PhotovoltaicPowerPlant import PhotovoltaicPowerPlant
from edf_test_technique.src.PointOfConnection import PointOfConnection


class Grid:
    def getEssMeasure(ess: EnergyStorageSystem) -> tuple[int, int, int, int]:
        """
        Measures all the values readable by the energy storage system.

        Parameters
        ----------
        ess : EnergyStorageSystem
            Instance of an EnergyStorageSystem object.

        Returns
        -------
        tuple[int, int, int, int]
            Tuple containing :
            - Measure of the amout of power flowing in/out of the 
            energy storage system (in kW)
            - Measure of the maximum charge power of the
            energy storage system (in kW)
            - Measure of the maximum discharge power of the
            energy storage system (in kW)
            - Current amount of power stored in the
            energy storage system (in kWh)
        """
        return (ess.pess, ess.pmaxch, ess.pmaxdisch, ess.eess)

    @staticmethod
    def getPvMeasure(pv: PhotovoltaicPowerPlant, kw: bool = False) -> int:
        """
        Measures the photovoltaic power plant power production (in W or kW)self.

        Parameters
        ----------
        pv : PhotovoltaicPowerPlant
            Instance of a PhotovoltaicPowerPlant object.
        kw : bool, default=False
            If True, converts the measure to killowatts.

        Returns
        -------
        int
            Power production of the photovoltaic power plant.
        """
        if kw:
            return pv.ppv / 1000
        return pv.ppv

    @staticmethod
    def getPocMeterMeasure(poc: PointOfConnection) -> int:
        """
        Measures the power available at the point of connection.

        Parameters
        ----------
        poc : PointOfConnection
            Instance of a PointOfConnection object.

        Returns
        -------
        int
            Power available at the point of connection.
        """
        return poc.ppoc

    @classmethod
    def getPloadMeasure(
        cls,
        ess: EnergyStorageSystem,
        poc: PointOfConnection,
        pv: PhotovoltaicPowerPlant
    ) -> int:
        """
        Measures the industrial site power consumption (in kW).

        Parameters
        ----------
        ess : EnergyStorageSystem
            Instance of an EnergyStorageSystem object.
        poc : PointOfConnection
            Instance of a PointOfConnection object.
        pv : PhotovoltaicPowerPlant
            Instance of a PhotovoltaicPowerPlant object.

        Returns
        -------
        int
            Power consumption of the industrial site.
        """
        ess = cls.getEssMeasure(ess)[0]
        poc = cls.getPocMeterMeasure(poc)
        ppv = cls.getPvMeasure(pv, kw=True)

        return poc + -ess + -ppv

    @staticmethod
    def setEssSetpoint(ess, amount_power: int) -> None:
        """
        Controls the setpoint of power flowing in/out of the energy
        storage system.

        Parameters
        ----------
        ess : EnergyStorageSystem
            Instance of an EnergyStorageSystem object.
        amount_power : int
            Amount of power flowing in/out of the energy storage system.
        """
        ess.setpointPess(amount_power)

