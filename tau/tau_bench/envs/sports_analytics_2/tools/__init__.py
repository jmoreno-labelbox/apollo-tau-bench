# Copyright Sierra


# Helper function
def _load_table(data, table_name):
    """Load table from data, return as list of values."""
    table = data.get(table_name, {})
    if isinstance(table, dict):
        return list(table.values())
    return table

from .get_next_series_info import GetNextSeriesInfo
from .get_probable_pitchers import GetProbablePitchers
from .fetch_pitch_data import FetchPitchData
from .run_data_quality_check import RunDataQualityCheck
from .run_dbt_models import RunDbtModels
from .run_rules_engine import RunRulesEngine
from .generate_video_manifest import GenerateVideoManifest
from .render_video_playlists import RenderVideoPlaylists
from .generate_pdf_report import GeneratePdfReport
from .write_report_artifacts import WriteReportArtifacts
from .post_to_slack import PostToSlack
from .write_workflow_run import WriteWorkflowRun
from .write_video_playlist import WriteVideoPlaylist
from .get_series_schedule import GetSeriesSchedule
from .get_team_details import GetTeamDetails
from .get_venue_details import GetVenueDetails
from .fetch_park_factors import FetchParkFactors
from .get_umpire_rotation import GetUmpireRotation
from .run_canonical_pitch_map import RunCanonicalPitchMap
from .compute_key_metrics import ComputeKeyMetrics
from .normalize_spatial_data import NormalizeSpatialData
from .filter_insights_by_sample_size import FilterInsightsBySampleSize
from .filter_insights_by_actionability import FilterInsightsByActionability
from .filter_insights_by_leverage import FilterInsightsByLeverage
from .write_curated_insight import WriteCuratedInsight
from .write_game_day_event import WriteGameDayEvent
from .write_ingestion_log import WriteIngestionLog
from .get_report_by_id import GetReportById
from .analyze_bullpen_usage import AnalyzeBullpenUsage
from .compute_situational_splits import ComputeSituationalSplits
from .run_matchup_analysis import RunMatchupAnalysis
from .fetch_bullpen_sessions import FetchBullpenSessions
from .run_trend_analysis import RunTrendAnalysis
from .apply_statistical_filters import ApplyStatisticalFilters
from .generate_player_goals import GeneratePlayerGoals
from .write_player_dev_goals import WritePlayerDevGoals
from .write_player_dev_reports import WritePlayerDevReports
from .write_pitch_execution_grades import WritePitchExecutionGrades
from .write_umpire_game_model import WriteUmpireGameModel
from .write_spatial_artifact import WriteSpatialArtifact
from .get_spatial_artifact import GetSpatialArtifact
from .fetch_batch_game_data import FetchBatchGameData

ALL_TOOLS = [
    GetNextSeriesInfo,
    GetProbablePitchers,
    FetchPitchData,
    RunDataQualityCheck,
    RunDbtModels,
    RunRulesEngine,
    GenerateVideoManifest,
    RenderVideoPlaylists,
    GeneratePdfReport,
    WriteReportArtifacts,
    PostToSlack,
    WriteWorkflowRun,
    WriteVideoPlaylist,
    GetSeriesSchedule,
    GetTeamDetails,
    GetVenueDetails,
    FetchParkFactors,
    GetUmpireRotation,
    RunCanonicalPitchMap,
    ComputeKeyMetrics,
    NormalizeSpatialData,
    FilterInsightsBySampleSize,
    FilterInsightsByActionability,
    FilterInsightsByLeverage,
    WriteCuratedInsight,
    WriteGameDayEvent,
    WriteIngestionLog,
    GetReportById,
    AnalyzeBullpenUsage,
    ComputeSituationalSplits,
    RunMatchupAnalysis,
    FetchBullpenSessions,
    RunTrendAnalysis,
    ApplyStatisticalFilters,
    GeneratePlayerGoals,
    WritePlayerDevGoals,
    WritePlayerDevReports,
    WritePitchExecutionGrades,
    WriteUmpireGameModel,
    WriteSpatialArtifact,
    GetSpatialArtifact,
    FetchBatchGameData,
]
