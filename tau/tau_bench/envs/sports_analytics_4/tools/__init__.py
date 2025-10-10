# Copyright held by Sierra

from .get_trends import GetTrends
from .pitchers import Pitchers
from .make_vids import MakeVids
from .curated import Curated
from .pdf import Pdf
from .next_set import NextSet
from .spatial import Spatial
from .ingest_log import IngestLog
from .monitor_player_fatigue import MonitorPlayerFatigue
from .pitches import Pitches
from .matchup_anal import MatchupAnal
from .artif import Artif
from .umpiregame import Umpiregame
from .v_ideo_ren import VIdeoRen
from .db_mod import DbMod
from .forecast_match_outcome import ForecastMatchOutcome
from .event_day import EventDay
from .all_games import AllGames
from .video_creation import VideoCreation
from .all_rules import AllRules
from .create_reps import CreateReps
from .all_stats import AllStats
from .pithcmapping import Pithcmapping
from .aims import Aims
from .summarize_player_performance import SummarizePlayerPerformance
from .insight_action import InsightAction
from .insight_lev import InsightLev
from .spatials import Spatials
from .compare_team_stats import CompareTeamStats
from .quality_checks import QualityChecks
from .filtering import Filtering
from .developments import Developments
from .developments_reports import DevelopmentsReports
from .workflows import Workflows
from .flitering_samples import FliteringSamples
from .track_injury_reports import TrackInjuryReports
from .sending_to_slack import SendingToSlack
from .exec_data import ExecData

ALL_TOOLS = [
    GetTrends,
    Pitchers,
    MakeVids,
    Curated,
    Pdf,
    NextSet,
    Spatial,
    IngestLog,
    MonitorPlayerFatigue,
    Pitches,
    MatchupAnal,
    Artif,
    Umpiregame,
    VIdeoRen,
    DbMod,
    ForecastMatchOutcome,
    EventDay,
    AllGames,
    VideoCreation,
    AllRules,
    CreateReps,
    AllStats,
    Pithcmapping,
    Aims,
    SummarizePlayerPerformance,
    InsightAction,
    InsightLev,
    Spatials,
    CompareTeamStats,
    QualityChecks,
    Filtering,
    Developments,
    DevelopmentsReports,
    Workflows,
    FliteringSamples,
    TrackInjuryReports,
    SendingToSlack,
    ExecData,
]
