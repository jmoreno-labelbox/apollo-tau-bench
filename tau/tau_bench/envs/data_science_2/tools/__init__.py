# Copyright Sierra

from .get_project_config_by_city import GetProjectConfigByCity
from .get_file_text_by_path import GetFileTextByPath
from .get_terminal_log_command_result import GetTerminalLogCommandResult
from .get_geocoding_result_by_city import GetGeocodingResultByCity
from .get_weather_forecast_by_city import GetWeatherForecastByCity
from .get_stations_by_location import GetStationsByLocation
from .get_water_levels_window import GetWaterLevelsWindow
from .get_tide_predictions_window import GetTidePredictionsWindow
from .get_processed_timeseries_summary import GetProcessedTimeseriesSummary
from .get_features_by_csv_path import GetFeaturesByCsvPath
from .get_model_by_name import GetModelByName
from .get_predictions_by_model_name import GetPredictionsByModelName
from .get_metrics_by_model_name import GetMetricsByModelName
from .get_mcp_tool_calls_by_server import GetMcpToolCallsByServer
from .get_gmail_message_by_subject import GetGmailMessageBySubject
from .upsert_project_config import UpsertProjectConfig
from .add_file_directory_record import AddFileDirectoryRecord
from .upsert_file_store_text import UpsertFileStoreText
from .append_terminal_log_entry import AppendTerminalLogEntry
from .record_geocoding_result import RecordGeocodingResult
from .insert_weather_forecast import InsertWeatherForecast
from .register_etl_run import RegisterEtlRun
from .register_processed_timeseries import RegisterProcessedTimeseries
from .generate_features_from_processed import GenerateFeaturesFromProcessed
from .save_model_config import SaveModelConfig
from .create_time_based_dataset_split import CreateTimeBasedDatasetSplit
from .save_model_record import SaveModelRecord
from .save_predictions_record import SavePredictionsRecord
from .save_metrics_record import SaveMetricsRecord
from .publish_stakeholder_outputs import PublishStakeholderOutputs

ALL_TOOLS = [
    GetProjectConfigByCity,
    GetFileTextByPath,
    GetTerminalLogCommandResult,
    GetGeocodingResultByCity,
    GetWeatherForecastByCity,
    GetStationsByLocation,
    GetWaterLevelsWindow,
    GetTidePredictionsWindow,
    GetProcessedTimeseriesSummary,
    GetFeaturesByCsvPath,
    GetModelByName,
    GetPredictionsByModelName,
    GetMetricsByModelName,
    GetMcpToolCallsByServer,
    GetGmailMessageBySubject,
    UpsertProjectConfig,
    AddFileDirectoryRecord,
    UpsertFileStoreText,
    AppendTerminalLogEntry,
    RecordGeocodingResult,
    InsertWeatherForecast,
    RegisterEtlRun,
    RegisterProcessedTimeseries,
    GenerateFeaturesFromProcessed,
    SaveModelConfig,
    CreateTimeBasedDatasetSplit,
    SaveModelRecord,
    SavePredictionsRecord,
    SaveMetricsRecord,
    PublishStakeholderOutputs,
]
