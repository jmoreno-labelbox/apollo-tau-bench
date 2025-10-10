# Copyright owned by Sierra.



# Utility function
def _require(data, key, error_msg=None):
    """Require a key to exist in data."""
    if key not in data or data[key] is None:
        raise ValueError(error_msg or f"Required key '{key}' not found or is None")
    return data[key]

from .set_project_config import SetProjectConfig
from .create_directory import CreateDirectory
from .write_file_text import WriteFileText
from .append_terminal_log import AppendTerminalLog
from .store_geocoding_result import StoreGeocodingResult
from .store_weather_forecast import StoreWeatherForecast
from .store_noaa_station_search import StoreNoaaStationSearch
from .set_primary_station import SetPrimaryStation
from .store_water_levels import StoreWaterLevels
from .store_tide_predictions import StoreTidePredictions
from .store_coastal_meteorology import StoreCoastalMeteorology
from .compute_and_store_merged_timeseries import ComputeAndStoreMergedTimeseries
from .register_qc_figure import RegisterQcFigure
from .store_features import StoreFeatures
from .write_model_config import WriteModelConfig
from .create_time_based_split import CreateTimeBasedSplit
from .register_model import RegisterModel
from .store_predictions import StorePredictions
from .store_metrics import StoreMetrics
from .record_stakeholder_outputs import RecordStakeholderOutputs
from .zotero_search_items import ZoteroSearchItems
from .zotero_item_metadata import ZoteroItemMetadata
from .zotero_item_fulltext import ZoteroItemFulltext
from .notion_create_page import NotionCreatePage
from .notion_append_sections import NotionAppendSections
from .notion_update_page_properties import NotionUpdatePageProperties
from .gmail_draft_email import GmailDraftEmail
from .gmail_send_email import GmailSendEmail
from .log_mcp_tool_call import LogMcpToolCall
from .compute_tide_anomaly_summary import ComputeTideAnomalySummary

ALL_TOOLS = [
    SetProjectConfig,
    CreateDirectory,
    WriteFileText,
    AppendTerminalLog,
    StoreGeocodingResult,
    StoreWeatherForecast,
    StoreNoaaStationSearch,
    SetPrimaryStation,
    StoreWaterLevels,
    StoreTidePredictions,
    StoreCoastalMeteorology,
    ComputeAndStoreMergedTimeseries,
    RegisterQcFigure,
    StoreFeatures,
    WriteModelConfig,
    CreateTimeBasedSplit,
    RegisterModel,
    StorePredictions,
    StoreMetrics,
    RecordStakeholderOutputs,
    ZoteroSearchItems,
    ZoteroItemMetadata,
    ZoteroItemFulltext,
    NotionCreatePage,
    NotionAppendSections,
    NotionUpdatePageProperties,
    GmailDraftEmail,
    GmailSendEmail,
    LogMcpToolCall,
    ComputeTideAnomalySummary,
]
