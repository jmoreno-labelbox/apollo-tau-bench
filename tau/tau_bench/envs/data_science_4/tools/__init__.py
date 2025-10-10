# Copyright © Sierra

from .set_project_config import SetProjectConfig
from .set_geocode_city import SetGeocodeCity
from .set_project_directories import SetProjectDirectories
from .find_noaa_station import FindNoaaStation
from .set_weather_forecast import SetWeatherForecast
from .set_water_levels import SetWaterLevels
from .set_tide_predictions import SetTidePredictions
from .set_coastal_meteorology import SetCoastalMeteorology
from .create_features import CreateFeatures
from .set_model_config import SetModelConfig
from .create_model import CreateModel
from .get_model import GetModel
from .create_dataset_split import CreateDatasetSplit
from .train_model import TrainModel
from .evaluate_model import EvaluateModel
from .prepare_stakeholder_outputs import PrepareStakeholderOutputs
from .create_summary_plots import CreateSummaryPlots
from .create_gmail_json import CreateGmailJson
from .create_notion_page_json import CreateNotionPageJson
from .enrich_notion import EnrichNotion
from .append_terminal_log import AppendTerminalLog
from .start_etl_run import StartEtlRun
from .register_processed_timeseries import RegisterProcessedTimeseries
from .create_qc_figures import CreateQCFigures

ALL_TOOLS = [
    SetProjectConfig,
    SetGeocodeCity,
    SetProjectDirectories,
    FindNoaaStation,
    SetWeatherForecast,
    SetWaterLevels,
    SetTidePredictions,
    SetCoastalMeteorology,
    CreateFeatures,
    SetModelConfig,
    CreateModel,
    GetModel,
    CreateDatasetSplit,
    TrainModel,
    EvaluateModel,
    PrepareStakeholderOutputs,
    CreateSummaryPlots,
    CreateGmailJson,
    CreateNotionPageJson,
    EnrichNotion,
    AppendTerminalLog,
    StartEtlRun,
    RegisterProcessedTimeseries,
    CreateQCFigures,
]
