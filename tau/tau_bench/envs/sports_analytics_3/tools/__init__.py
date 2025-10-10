# Copyright owned by Sierra

from .get_player_details_by_name import GetPlayerDetailsByName
from .get_player_details_by_id import GetPlayerDetailsById
from .get_all_players_of_team import GetAllPlayersOfTeam
from .update_player_details import UpdatePlayerDetails
from .get_team_details_by_id import GetTeamDetailsById
from .get_team_details_by_name import GetTeamDetailsByName
from .get_team_details_by_abbreviation import GetTeamDetailsByAbbreviation
from .get_all_teams_in_league import GetAllTeamsInLeague
from .get_game_details_by_game_pk import GetGameDetailsByGamePk
from .update_game_details import UpdateGameDetails
from .create_new_game import CreateNewGame
from .find_games_on_date import FindGamesOnDate
from .get_next_game import GetNextGame
from .get_game_by_home_away import GetGameByHomeAway
from .get_venue_by_id import GetVenueById
from .get_venue_by_name import GetVenueByName
from .get_all_venue_in_city import GetAllVenueInCity
from .get_umpires_details_by_name import GetUmpiresDetailsByName
from .get_umpires_details_by_id import GetUmpiresDetailsById
from .get_umpires_by_experience import GetUmpiresByExperience
from .get_all_eevnts_by_game_pk import GetAllEevntsByGamePk
from .create_game_day_event import CreateGameDayEvent
from .update_game_event_status import UpdateGameEventStatus
from .get_all_goals_by_for_player import GetAllGoalsByForPlayer
from .create_new_goal import CreateNewGoal
from .create_new_report import CreateNewReport
from .get_all_report_for_player import GetAllReportForPlayer
from .get_pitch_details_by_id import GetPitchDetailsById
from .get_all_pitches_by_pitcher_ids import GetAllPitchesByPitcherIds
from .get_all_pitches_by_hitter_ids import GetAllPitchesByHitterIds
from .get_all_pitches_for_game import GetAllPitchesForGame
from .create_new_pitch import CreateNewPitch
from .get_grade_by_pitch_id import GetGradeByPitchId
from .get_grades_by_pitch_ids import GetGradesByPitchIds
from .get_filtered_grades_by_pitch_ids import GetFilteredGradesByPitchIds
from .create_new_grade import CreateNewGrade
from .get_grades_by_grade_for_game import GetGradesByGradeForGame
from .get_highlights_by_name import GetHighlightsByName
from .add_new_highlight import AddNewHighlight
from .get_highlight_by_report_id import GetHighlightByReportId
from .get_player_insights_by_playerid_and_type import GetPlayerInsightsByPlayeridAndType
from .create_new_insight import CreateNewInsight
from .get_insightbyreportid import GetInsightbyreportid
from .get_scouting_report_by_gamepk_and_type import GetScoutingReportByGamepkAndType
from .create_scouting_report import CreateScoutingReport
from .get_scouting_report_by_id import GetScoutingReportById
from .create_workflow import CreateWorkflow
from .get_bullpen_session_info_for_player import GetBullpenSessionInfoForPlayer
from .create_ingestion_log import CreateIngestionLog
from .get_model_detail_by_game import GetModelDetailByGame

ALL_TOOLS = [
    GetPlayerDetailsByName,
    GetPlayerDetailsById,
    GetAllPlayersOfTeam,
    UpdatePlayerDetails,
    GetTeamDetailsById,
    GetTeamDetailsByName,
    GetTeamDetailsByAbbreviation,
    GetAllTeamsInLeague,
    GetGameDetailsByGamePk,
    UpdateGameDetails,
    CreateNewGame,
    FindGamesOnDate,
    GetNextGame,
    GetGameByHomeAway,
    GetVenueById,
    GetVenueByName,
    GetAllVenueInCity,
    GetUmpiresDetailsByName,
    GetUmpiresDetailsById,
    GetUmpiresByExperience,
    GetAllEevntsByGamePk,
    CreateGameDayEvent,
    UpdateGameEventStatus,
    GetAllGoalsByForPlayer,
    CreateNewGoal,
    CreateNewReport,
    GetAllReportForPlayer,
    GetPitchDetailsById,
    GetAllPitchesByPitcherIds,
    GetAllPitchesByHitterIds,
    GetAllPitchesForGame,
    CreateNewPitch,
    GetGradeByPitchId,
    GetGradesByPitchIds,
    GetFilteredGradesByPitchIds,
    CreateNewGrade,
    GetGradesByGradeForGame,
    GetHighlightsByName,
    AddNewHighlight,
    GetHighlightByReportId,
    GetPlayerInsightsByPlayeridAndType,
    CreateNewInsight,
    GetInsightbyreportid,
    GetScoutingReportByGamepkAndType,
    CreateScoutingReport,
    GetScoutingReportById,
    CreateWorkflow,
    GetBullpenSessionInfoForPlayer,
    CreateIngestionLog,
    GetModelDetailByGame,
]
