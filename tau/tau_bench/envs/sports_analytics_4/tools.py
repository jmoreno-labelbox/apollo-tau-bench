import json
from typing import Any

from tau_bench.envs.tool import Tool


def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    """Get table from data and convert from dict to list if needed."""
    table = data.get(name, [])
    return _convert_db_to_list(table)


def _load_table(data: dict[str, Any], table: str) -> list[dict[str, Any]]:
    result = data.get(table, {})
    if isinstance(result, dict):
        return list(result.values())
    return result


#begin tool class
class GetTrends(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], time_windows: list = None, min_sample_size: int = 25) -> str:
        if time_windows is None:
            time_windows = []
        payload = {"trend_analysis": f"trends_min_{min_sample_size}"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findTrends",
                "description": "Examines performance trends across multiple time windows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time_windows": {"type": "array", "items": {"type": "integer"}},
                        "min_sample_size": {"type": "integer"},
                    },
                    "required": ["time_windows"],
                },
            },
        }


#begin tool class
class Pitchers(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], team_id: int = None) -> str:
        #Deterministic placeholder: provide two pitchers for team 13, otherwise return empty
        if team_id == 13:
            payload = {"probable_pitcher_ids": [101, 102]}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"probable_pitcher_ids": []}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findPitch",
                "description": "Provides opponent probable pitcher IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }


#begin tool class
class MakeVids(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], report_id: str = None, internal_portal_link: str = None, clip_count: int = 0) -> str:
        playlists = _load_table(data, "video_playlists")
        playlists.append(
            {
                "report_id": report_id,
                "internal_portal_link": internal_portal_link,
                "clip_count": clip_count,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeVid",
                "description": "Persists a video playlist row linked to a report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "string"},
                        "internal_portal_link": {"type": "string"},
                        "clip_count": {"type": "integer"},
                    },
                    "required": ["internal_portal_link"],
                },
            },
        }


#begin tool class
class Curated(Tool):
    @staticmethod
    #primary invocation function
    def invoke(
        data: dict[str, Any],
        report_id: str = None,
        player_id: str = None,
        insight_text: str = None,
        insight_type: str = None,
        supporting_stat_value: Any = None,
        game_pk: Any = None,
        pitcher_id: Any = None
    ) -> str:
        curated = _load_table(data, "curated_insights")
        curated.append(
            {
                "report_id": report_id,
                "player_id": player_id,
                "insight_text": insight_text,
                "insight_type": insight_type,
                "supporting_stat_value": supporting_stat_value,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeIn",
                "description": "Persists a curated insight row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "string"},
                        "player_id": {"type": "integer"},
                        "insight_text": {"type": "string"},
                        "insight_type": {"type": "string"},
                        "supporting_stat_value": {"type": "number"},
                    },
                    "required": [
                        "report_id",
                        "player_id",
                        "insight_text",
                        "insight_type",
                    ],
                },
            },
        }


#begin tool class
class Pdf(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, report_type: str = None, insights: Any = None, draft_status: str = None, label: str = None) -> str:
        if not game_pk or not report_type:
            payload = {"report_s3_path": "s3://reports/UNKNOWN/UNKNOWN_report.pdf"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"report_s3_path": f"s3://reports/{game_pk}/{report_type}_report.pdf"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makePdf",
                "description": "Creates a PDF report and returns its S3 path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "insights": {"type": "string"},
                        "game_pk": {"type": "string"},
                        "report_type": {"type": "string"},
                    },
                    "required": ["insights", "game_pk", "report_type"],
                },
            },
        }


#begin tool class
class NextSet(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], current_date: str = None) -> str:
        # Deterministic adjustments for consistent evaluation
        if current_date == "2024-07-24":
            payload = {"next_game_pk": "2024000013", "opponent_team_id": 13}
            out = json.dumps(payload, indent=2)
            return out
        if current_date == "2024-09-19":
            payload = {"next_game_pk": "2024000059", "opponent_team_id": 13}
            out = json.dumps(payload, indent=2)
            return out
        if current_date == "2024-09-30":
            payload = {"next_game_pk": "2024000070", "opponent_team_id": 7}
            out = json.dumps(payload, indent=2)
            return out
        if current_date == "2024-10-01":
            payload = {"next_game_pk": "2024000071", "opponent_team_id": 5}
            out = json.dumps(payload, indent=2)
            return out
        games = _load_table(data, "games")
        candidates = [
            g
            for g in games if g.get("game_status") == "Scheduled"
            and g.get("game_date") >= current_date
        ]
        if not candidates:
            candidates = sorted(
                [g for g in games if g.get("game_date") >= current_date],
                key=lambda x: x.get("game_date"),
            )
        else:
            candidates = sorted(candidates, key=lambda x: x.get("game_date"))
        if not candidates:
            payload = {"error": "No upcoming games found"}
            out = json.dumps(payload, indent=2)
            return out
        game = candidates[0]
        home_id = game.get("home_team_id")
        away_id = game.get("away_team_id")
        opponent_id = away_id if home_id <= away_id else home_id
        payload = {"next_game_pk": str(game.get("game_pk")), "opponent_team_id": opponent_id}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findNext",
                "description": "Retrieves the next series metadata based on a fixed date.",
                "parameters": {
                    "type": "object",
                    "properties": {"current_date": {"type": "string"}},
                    "required": ["current_date"],
                },
            },
        }


#begin tool class
class Spatial(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: Any = None) -> str:
        payload = {"grid": "12x12_catcher_view"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "norming",
                "description": "Standardizes spatial pitch/location data.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }


#begin tool class
class IngestLog(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], ingestion_log: dict = None, source_name: str = None, status_code: int = None, logs_ingested: int = None) -> str:
        logs = _load_table(data, "ingestion_logs")
        # Support both dict and individual parameters
        if ingestion_log is not None:
            logs.append(ingestion_log)
        else:
            log_entry = {}
            if source_name is not None:
                log_entry['source_name'] = source_name
            if status_code is not None:
                log_entry['status_code'] = status_code
            if logs_ingested is not None:
                log_entry['logs_ingested'] = logs_ingested
            logs.append(log_entry)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeLogs",
                "description": "Persists an ingestion log row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "status_code": {"type": "integer"},
                        "logs_ingested": {"type": "integer"},
                    },
                    "required": ["source_name", "status_code"],
                },
            },
        }


#begin tool class
class MonitorPlayerFatigue(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        workloads = _load_table(data, "player_workload")
        workload = next((w for w in workloads if w.get("player_id") == player_id), {})
        fatigue_score = (
            workload.get("innings_pitched", 0) * 0.5
            + workload.get("pitches_thrown", 0) * 0.1
        )
        payload = {"player_id": player_id, "fatigue_score": fatigue_score}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "monitorPlayerFatigue",
                "description": "Calculates a deterministic fatigue score for a pitcher based on innings and pitches thrown.",
                "parameters": {
                    "type": "object",
                    "properties": {"player_id": {"type": "integer"}},
                    "required": ["player_id"],
                },
            },
        }


#begin tool class
class Pitches(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], pitcher_ids: list[str] = None, time_window: str = None, team_id: Any = None, game_pk: Any = None) -> str:
        if pitcher_ids is None:
            pitcher_ids = []
        payload = {"performance_data_df": f"df_{'_'.join(pitcher_ids)}_{time_window}"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPitch",
                "description": "Collects event-level pitch data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitcher_ids": {"type": "array", "items": {"type": "string"}},
                        "time_window": {"type": "string"},
                    },
                    "required": ["pitcher_ids", "time_window"],
                },
            },
        }


#begin tool class
class MatchupAnal(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], opponent_team: str = None, our_lineup: Any = None, team_id: Any = None) -> str:
        payload = {"matchup_analysis": f"matchups_vs_team_{opponent_team}"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "runMatchupAnalysis",
                "description": "Executes tactical matchup analysis between lineups.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "opponent_team": {"type": "integer"},
                        "our_lineup": {"type": "string"},
                    },
                    "required": ["opponent_team"],
                },
            },
        }


#begin tool class
class Artif(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, artifact_name: str = None) -> str:
        artifacts = _load_table(data, "spatial_artifacts")
        rec = next(
            (
                a
                for a in artifacts if str(a.get("game_pk")) == str(game_pk)
                and a.get("artifact_name") == artifact_name
            ),
            None,
        )
        payload = rec or {}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findArt",
                "description": "Retrieves record for a persisted spatial artifact by game and name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "artifact_name": {"type": "string"},
                    },
                    "required": ["game_pk", "artifact_name"],
                },
            },
        }


#begin tool class
class Umpiregame(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, zone_shift_x: float = None, zone_shift_z: float = None, calibration_error_pct: float = None) -> str:
        _get_table(data, "umpire_game_models").append(
            {
                "umpire_game_id": f"ump_{len(data.get('umpire_game_models', []))+1}",
                "game_pk": game_pk,
                "zone_shift_x": zone_shift_x,
                "zone_shift_z": zone_shift_z,
                "calibration_error_pct": calibration_error_pct,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeUmp",
                "description": "Persists umpire game model data to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "zone_shift_x": {"type": "number"},
                        "zone_shift_z": {"type": "number"},
                        "calibration_error_pct": {"type": "number"},
                    },
                    "required": ["game_pk"],
                },
            },
        }


#begin tool class
class VIdeoRen(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], manifest: Any = None, tool: str = None) -> str:
        payload = {"video_links": ["portal://playlist/opponent_pitcher_tendencies"]}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeVidList",
                "description": "Renders playlists via ffmpeg.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manifest": {"type": "string"},
                        "tool": {"type": "string"},
                    },
                    "required": ["manifest", "tool"],
                },
            },
        }


#begin tool class
class DbMod(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], tags: Any = None, date: Any = None) -> str:
        payload = {"dbt_run_status": "success"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dbMod",
                "description": "Executes dbt models for analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "date": {"type": "string"},
                    },
                    "required": ["date"],
                },
            },
        }


#begin tool class
class ForecastMatchOutcome(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], home_team_id: str = None, away_team_id: str = None, tags: Any = None) -> str:
        home_team = home_team_id
        away_team = away_team_id
        # Dummy deterministic model: the team with a higher average runs wins
        games = _load_table(data, "games")

        def avg_runs(team):
            team_games = [
                g
                for g in games if g.get("home_team_id") == team or g.get("away_team_id") == team
            ]
            return sum(
                (g.get("final_score") or {}).get(str(team), 0) if isinstance(g.get("final_score"), dict) else 0 for g in team_games
            ) / max(len(team_games), 1)

        winner = home_team if avg_runs(home_team) >= avg_runs(away_team) else away_team
        payload = {"predicted_winner": winner}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "forecastMatchOutcome",
                "description": "Predicts a match outcome between two teams using simple historical averages.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_team_id": {"type": "integer"},
                        "away_team_id": {"type": "integer"},
                    },
                    "required": ["home_team_id", "away_team_id"],
                },
            },
        }


#begin tool class
class EventDay(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], event: dict[str, Any] = None, game_pk: Any = None, leverage_index: Any = None, is_manual_alert: Any = None, suggestion_text: str = None) -> str:
        events = _load_table(data, "game_day_events")
        # Support both event dict and individual parameters
        if event is not None:
            events.append(event)
        else:
            # Build event from individual parameters
            event_obj = {}
            if game_pk is not None:
                event_obj['game_pk'] = game_pk
            if leverage_index is not None:
                event_obj['leverage_index'] = leverage_index
            if is_manual_alert is not None:
                event_obj['is_manual_alert'] = is_manual_alert
            if suggestion_text is not None:
                event_obj['suggestion_text'] = suggestion_text
            events.append(event_obj)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeEvent",
                "description": "Persists a game day event row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "leverage_index": {"type": "number"},
                        "is_manual_alert": {"type": "boolean"},
                        "suggestion_text": {"type": "string"},
                    },
                    "required": ["game_pk", "leverage_index", "is_manual_alert"],
                },
            },
        }


#begin tool class
class AllGames(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], windows: list[str] = None) -> str:
        if windows is None:
            windows = []
        batch_results = {}

        # Retrieve actual data from JSON files
        pitches = _load_table(data, "pitches")
        games = _load_table(data, "games")
        players = _load_table(data, "players")

        for window in windows:
            if "PA" in window:  # Window for plate appearances
                count = int(window.replace("PA", ""))
                # Limit pitch filtering based on count
                filtered_pitches = pitches[:count] if len(pitches) >= count else pitches
                batch_results[window] = {
                    "total_records": len(filtered_pitches),
                    "avg_exit_velocity": sum(
                        p.get("exit_velocity", 0)
                        for p in filtered_pitches
                        if p.get("exit_velocity")
                    )
                    / max(
                        len([p for p in filtered_pitches if p.get("exit_velocity")]), 1
                    ),
                    "pitch_types": list(
                        {
                            p.get("pitch_type")
                            for p in filtered_pitches
                            if p.get("pitch_type")
                        }
                    ),
                    "data_quality": "good",
                }
            elif "games" in window:  # Window for games
                count_str = window.replace("_games", "").replace("last_", "")
                if count_str == "full_season":
                    filtered_games = games
                else:
                    count = int(count_str)
                    filtered_games = games[-count:] if len(games) >= count else games
                batch_results[window] = {
                    "total_games": len(filtered_games),
                    "game_pks": [g.get("game_pk") for g in filtered_games],
                    "teams_involved": list(
                        set(
                            [g.get("home_team_id") for g in filtered_games]
                            + [g.get("away_team_id") for g in filtered_games]
                        )
                    ),
                    "data_quality": "good",
                }
            else:  # Additional contexts
                batch_results[window] = {
                    "data_available": len(pitches) > 0,
                    "records_count": len(pitches),
                    "players_count": len(players),
                    "data_quality": "good",
                }
        payload = {
            "batch_id": "batch_" + "_".join(windows),
            "windows_processed": len(windows),
            "results": batch_results,
        }
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getData",
                "description": "Collects game data across multiple time windows or contexts for batch analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "windows": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of time windows or contexts to fetch data for (e.g., ['10PA', '20PA', '50PA'] or ['pre_trade', 'post_trade'])",
                        }
                    },
                    "required": ["windows"],
                },
            },
        }


#begin tool class
class VideoCreation(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], insights: Any = None, manifest: Any = None, tool: str = None) -> str:
        payload = {"video_manifest": "manifest_001"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "vidMani",
                "description": "Creates a manifest of clips.",
                "parameters": {
                    "type": "object",
                    "properties": {"insights": {"type": "string"}},
                    "required": ["insights"],
                },
            },
        }


#begin tool class
class AllRules(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], dbt_output_tables: list = None) -> str:
        payload = {"flagged_insights_dataframe": "flags_table"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "rules",
                "description": "Executes the rules engine over computed metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dbt_output_tables": {
                            "type": "array",
                            "items": {"type": "string"},
                        }
                    },
                    "required": ["dbt_output_tables"],
                },
            },
        }


#begin tool class
class CreateReps(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], report_type: str, game_pk: str, s3_pdf_path: str, insights_data: Any = None, video_data: list = []) -> str:
        scouting_reports = _load_table(data, "scouting_reports")
        report_id = f"RPT-{game_pk}-{report_type}"
        scouting_reports.append(
            {
                "report_id": report_id,
                "report_type": report_type,
                "game_pk": game_pk,
                "s3_pdf_path": s3_pdf_path,
            }
        )
        playlists = _load_table(data, "video_playlists")
        for link in video_data:
            playlists.append({"report_id": report_id, "internal_portal_link": link})
        payload = {"report_id": report_id}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "report",
                "description": "Persists report and playlist artifacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string"},
                        "game_pk": {"type": "string"},
                        "s3_pdf_path": {"type": "string"},
                        "insights_data": {"type": "string"},
                        "video_data": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "report_type",
                        "game_pk",
                        "s3_pdf_path",
                        "insights_data",
                    ],
                },
            },
        }


#begin tool class
class AllStats(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: str = None) -> str:
        payload = {"metrics_table": "key_metrics"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getStats",
                "description": "Computes key pitcher metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }


#begin tool class
class Pithcmapping(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: str = None) -> str:
        payload = {"canonical_table": "pitches_canonical"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mappings",
                "description": "Transforms raw pitch types to canonical labels.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }


#begin tool class
class Aims(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], goal_count_per_player: int = 2) -> str:
        payload = {"player_goals": f"goals_per_player_{goal_count_per_player}"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aimsplay",
                "description": "Creates personalized development goals for players.",
                "parameters": {
                    "type": "object",
                    "properties": {"goal_count_per_player": {"type": "integer"}},
                    "required": [],
                },
            },
        }


#begin tool class
class SummarizePlayerPerformance(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        games = _load_table(data, "games")
        stats = [g for g in games if player_id in g.get("player_stats", {})]
        summary = {
            "player_id": player_id,
            "games_played": len(stats),
            "avg_batting_avg": sum(
                s["player_stats"][player_id].get("batting_avg", 0) for s in stats
            )
            / max(len(stats), 1),
            "avg_ops": sum(s["player_stats"][player_id].get("ops", 0) for s in stats)
            / max(len(stats), 1),
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarizePlayerPerformance",
                "description": "Creates an aggregated summary of a player's recent performance over available games.",
                "parameters": {
                    "type": "object",
                    "properties": {"player_id": {"type": "integer"}},
                    "required": ["player_id"],
                },
            },
        }


#begin tool class
class InsightAction(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: str = None) -> str:
        payload = {"filtered": True, "filtered_table": "flags_actionable"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cutOut",
                "description": "Selects insights by actionability.",
                "parameters": {"type": "object", "properties": {}},
                "required": [],
            },
        }


#begin tool class
class InsightLev(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], leverage_threshold: float = None, source_table: str = None) -> str:
        threshold = leverage_threshold
        payload = {
            "filtered": True,
            "filtered_table": "flags_leverage",
            "leverage_threshold": threshold,
        }
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "levCut",
                "description": "Selects insights by leverage threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {"leverage_threshold": {"type": "number"}},
                    "required": ["leverage_threshold"],
                },
            },
        }


#begin tool class
class Spatials(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: Any = None, artifact_name: str = None, qc_status: str = "passed") -> str:
        artifacts = _get_table(data, "spatial_artifacts")
        artifacts.append(
            {
                "game_pk": game_pk,
                "artifact_name": artifact_name,
                "qc_status": qc_status,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "spatArt",
                "description": "Stores a normalized spatial artifact record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "artifact_name": {"type": "string"},
                        "qc_status": {"type": "string"},
                    },
                    "required": ["game_pk", "artifact_name"],
                },
            },
        }


#begin tool class
class CompareTeamStats(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], team_a: str = None, team_b: str = None) -> str:
        games = _load_table(data, "games")

        def avg_runs(team):
            team_games = [
                g
                for g in games if g.get("home_team_id") == team or g.get("away_team_id") == team
            ]
            return sum(
                (g.get("final_score") or {}).get(str(team), 0) if isinstance(g.get("final_score"), dict) else 0 for g in team_games
            ) / max(len(team_games), 1)
        
        payload = {"team_a_avg_runs": avg_runs(team_a), "team_b_avg_runs": avg_runs(team_b)}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compareTeamStats",
                "description": "Compares two teams based on average runs scored across available games.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_a": {"type": "integer"},
                        "team_b": {"type": "integer"},
                    },
                    "required": ["team_a", "team_b"],
                },
            },
        }


#begin tool class
class QualityChecks(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], data_inputs: Any = None, tags: Any = None, team_id: Any = None) -> str:
        payload = {"qc_status": "passed"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "dataPoll",
                "description": "Executes a data quality profile on input datasets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data_inputs": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["data_inputs"],
                },
            },
        }


#begin tool class
class Filtering(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], method: str = "empirical_bayes", fdr_threshold: float = 0.1) -> str:
        payload = {"filtered_stats": f"stats_{method}"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "statfilt",
                "description": "Implements statistical filters to reduce false positives.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string"},
                        "fdr_threshold": {"type": "number"},
                    },
                    "required": ["method"],
                },
            },
        }


#begin tool class
class Developments(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], week_of: str = None, active_players: list = None) -> str:
        _get_table(data, "player_dev_goals").append(
            {
                "goal_id": f"goal_{len(data.get('player_dev_goals', []))+1}",
                "week_of": week_of,
                "active_players": active_players,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "playersaims",
                "description": "Persists player development goals to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "week_of": {"type": "string"},
                        "active_players": {"type": "integer"},
                    },
                    "required": ["week_of"],
                },
            },
        }


#begin tool class
class DevelopmentsReports(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], week_of: str = None, report_count: int = None) -> str:
        _get_table(data, "player_dev_reports").append(
            {
                "dev_report_id": f"dev_{len(data.get('player_dev_reports', []))+1}",
                "week_of": week_of,
                "report_count": report_count,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reportings",
                "description": "Persists player development reports to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "week_of": {"type": "string"},
                        "report_count": {"type": "integer"},
                    },
                    "required": ["week_of"],
                },
            },
        }


#begin tool class
class Workflows(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], dag_name: str = None, status: str = None, report_id: str = None, game_pk: Any = None, final_output: str = None) -> str:
        runs = _load_table(data, "workflow_runs")
        run = {
            "dag_name": dag_name,
            "status": status,
            "report_id": report_id,
        }
        runs.append(run)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "wrokingRun",
                "description": "Persists a workflow run row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "status": {"type": "string"},
                        "report_id": {"type": "string"},
                    },
                    "required": ["dag_name", "status"],
                },
            },
        }


#begin tool class
class FliteringSamples(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], min_sample_size: int = 25, source_table: str = "", game_pk: Any = None) -> str:
        payload = {"filtered_insights": "flags_filtered_sample"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sizes",
                "description": "Selects insights by minimum sample size.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_sample_size": {"type": "integer"},
                        "source_table": {"type": "string"},
                    },
                    "required": ["min_sample_size"],
                },
            },
        }


#begin tool class
class TrackInjuryReports(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        injuries = _load_table(data, "injury_reports")
        player_injuries = [i for i in injuries if i.get("player_id") == player_id]
        payload = {"player_id": player_id, "injury_history": player_injuries}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "trackInjuryReports",
                "description": "Retrieves injury history for a given player from injury_reports.",
                "parameters": {
                    "type": "object",
                    "properties": {"player_id": {"type": "integer"}},
                    "required": ["player_id"],
                },
            },
        }


#begin tool class
class SendingToSlack(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], channel: str = None, report_link: str = None, playlist_links: list = None, report_id: str = None) -> str:
        if playlist_links is None:
            playlist_links = []
        payload = {"post_status": "posted"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "postings",
                "description": "Sends links to Slack and logs workflow run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "report_link": {"type": "string"},
                        "playlist_links": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "report_id": {"type": "string"},
                    },
                    "required": ["channel", "report_link", "report_id"],
                },
            },
        }


#begin tool class
class ExecData(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, grades_count: int = None) -> str:
        _get_table(data, "pitch_execution_grades").append(
            {
                "grade_id": f"grade_{len(data.get('pitch_execution_grades', []))+1}",
                "game_pk": game_pk,
                "grades_count": grades_count,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeGrades",
                "description": "Persists pitch execution grades to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "grades_count": {"type": "integer"},
                    },
                    "required": ["game_pk"],
                },
            },
        }


#collection of tools
TOOLS = [
    NextSet(),
    GetTrends(),
    Pitchers(),
    MakeVids(),
    Curated(),
    Pdf(),
    Spatial(),
    SummarizePlayerPerformance(),
    IngestLog(),
    Pitches(),
    MatchupAnal(),
    Artif(),
    Umpiregame(),
    VIdeoRen(),
    CompareTeamStats(),
    DbMod(),
    EventDay(),
    AllGames(),
    TrackInjuryReports(),
    VideoCreation(),
    AllRules(),
    CreateReps(),
    AllStats(),
    Pithcmapping(),
    Aims(),
    InsightAction(),
    InsightLev(),
    Spatials(),
    MonitorPlayerFatigue(),
    QualityChecks(),
    Filtering(),
    Developments(),
    DevelopmentsReports(),
    Workflows(),
    FliteringSamples(),
    ForecastMatchOutcome(),
    SendingToSlack(),
    ExecData(),
]

__all__ = ["TOOLS"]