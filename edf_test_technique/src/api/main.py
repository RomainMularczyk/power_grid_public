from edf_test_technique.src.entities.PhotovoltaicPowerPlant import PhotovoltaicPowerPlant
from edf_test_technique.src.entities.PointOfConnection import PointOfConnection
from fastapi import FastAPI
from edf_test_technique.src.Grid import Grid
from edf_test_technique.src.entities.EnergyStorageSystem import EnergyStorageSystem
from edf_test_technique.src.api.models.EssMeasure import EssMeasure
from edf_test_technique.src.api.models.PvMeasure import PvMeasure
from edf_test_technique.src.api.models.PocMeasure import PocMeasure

app = FastAPI()

@app.post("/ess")
async def get_ess_measures(ess_measures: EssMeasure):
    eess, ess_capacity = ess_measures.eess, ess_measures.ess_capacity
    ess = EnergyStorageSystem(eess, ess_capacity) 
    return Grid.getEssMeasure(ess)

@app.post("/pv")
async def get_pv_measure(pv_measure: PvMeasure):
    ppv = pv_measure.ppv
    pv = PhotovoltaicPowerPlant(ppv)
    return Grid.getPvMeasure(pv)

@app.post("/poc")
async def get_pov_measure(poc_measure: PocMeasure):
    ppoc, pmaxsite = poc_measure.ppoc, poc_measure.pmaxsite
    poc = PointOfConnection(pmaxsite)
    poc.setPpoc(ppoc)
    return Grid.getPocMeterMeasure(poc)

@app.post("/pload")
async def get_pload_measure(
    ess_measures: EssMeasure,
    pv_measure: PvMeasure, 
    poc_measure: PocMeasure
):
    eess, ess_capacity = ess_measures.eess, ess_measures.ess_capacity
    ess = EnergyStorageSystem(eess, ess_capacity)
    ppv = pv_measure.ppv
    pv = PhotovoltaicPowerPlant(ppv)
    ppoc, pmaxsite = poc_measure.ppoc, poc_measure.pmaxsite
    poc = PointOfConnection(pmaxsite)
    poc.setPpoc(ppoc)
    return Grid.getPloadMeasure(ess, poc, pv)
    
@app.post("/set_ess_pess")
async def set_ess_pess(ess_measures: EssMeasure):
    eess, ess_capacity = ess_measures.eess, ess_measures.ess_capacity
    amount_power = ess_measures.amount_power
    ess = EnergyStorageSystem(eess, ess_capacity)
    Grid.setEssSetpoint(ess, amount_power)
    return Grid.getEssMeasure(ess)

