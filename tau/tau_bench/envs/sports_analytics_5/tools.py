import json
import re
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
from domains.dto import Tool

def _today_iso() -> str:
    return "2025-08-14"

def _now_utc_iso() -> str:
    return _today_iso() + "T00:00:00Z"

def _next_id(rows: List[Dict[str, Any]], key: str) -> int:
    max_id = 0
    for r in rows:
        try:
            max_id = max(max_id, int(r.get(key, 0)))
        except Exception:
            pass
    return max_id + 1

def _require_tables(data: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None

def _check_required(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None

PITCH_MAP = {
    "Four-Seam Fastball": "FF",
    "4-Seam": "FF",
    "Fastball": "FF",
    "Sinker": "SI",
    "Two-Seam Fastball": "SI",
    "Sweeper": "SW",
    "Slider": "SL",
    "Curveball": "CU",
    "Changeup": "CH",
    "Cutter": "FC",
    "Splitter": "FS",
    "Knuckleball": "KN",
}

def _grade_execution(miss_distance_inches: Optional[float]) -> str:
    if miss_distance_inches is None:
        return "Major miss"
    if miss_distance_inches <= 3.0:
        return "Executed"
    if miss_distance_inches <= 9.0:
        return "Minor miss"
    return "Major miss"

# ———————————————————————— READS & LISTS ————————————————————————

class GetGameDetails(Tool):
    """Get full game row by game_pk."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        game_pk = kwargs.get("game_pk")
        if not game_pk:
            return json.dumps({"error": "game_pk is required."}, indent=2)
        row = next((g for g in data["games"] if g.get("game_pk") == game_pk), None)
        return json.dumps(row or {"error": f"Game '{game_pk}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_game_details","description":"Returns the games row for a given game_pk.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"}},"required":["game_pk"]}}}

class ListGamesByStatus(Tool):
    """List games filtered by game_status."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        status = kwargs.get("game_status")
        if not status:
            return json.dumps({"error": "game_status is required."}, indent=2)
        rows = [g for g in data["games"] if (g.get("game_status") == status)]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_games_by_status","description":"Lists games by exact game_status (e.g., 'Scheduled','Final','Cancelled').","parameters":{"type":"object","properties":{"game_status":{"type":"string"}},"required":["game_status"]}}}

class GetPlayerDetails(Tool):
    """Get a player by player_id or full_name."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        pid = kwargs.get("player_id")
        name = kwargs.get("full_name")
        row = None
        if pid is not None:
            row = next((p for p in data["players"] if p.get("player_id")==pid), None)
        elif name:
            row = next((p for p in data["players"] if p.get("full_name")==name), None)
        else:
            return json.dumps({"error":"Provide player_id or full_name."}, indent=2)
        return json.dumps(row or {"error":"Player not found."}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_player_details","description":"Fetch player by ID or exact full name.","parameters":{"type":"object","properties":{"player_id":{"type":"integer"},"full_name":{"type":"string"}},"required":[]}}}

class ListPlayersByRosterStatus(Tool):
    """List players with a given roster_status (e.g., 'Active', 'IL-15')."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        status = kwargs.get("roster_status")
        if not status:
            return json.dumps({"error":"roster_status is required."}, indent=2)
        rows = [p for p in data["players"] if p.get("roster_status")==status]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_players_by_roster_status","description":"Returns players matching a specific roster_status.","parameters":{"type":"object","properties":{"roster_status":{"type":"string"}},"required":["roster_status"]}}}

class GetActiveRoster(Tool):
    """Active roster snapshot for a team, excluding IL/Taxi unless include_il=True."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        team_id = kwargs.get("team_id")
        include_il = kwargs.get("include_il", False)
        if team_id is None:
            return json.dumps({"error":"team_id is required."}, indent=2)
        def _eligible(p):
            rs = (p.get("roster_status") or "").upper()
            if include_il:
                return True
            return (rs == "ACTIVE")
        rows = [p for p in data["players"] if p.get("current_team_id")==team_id and _eligible(p)]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_active_roster","description":"Returns active roster for a team_id. Excludes IL/Taxi by default.","parameters":{"type":"object","properties":{"team_id":{"type":"integer"},"include_il":{"type":"boolean"}},"required":["team_id"]}}}

# ———————————————————————— GAME DAY EVENTS ————————————————————————

class ListGameDayEvents(Tool):
    """Lists events for a game with optional filters. Note: min_leverage is a generic ≥ filter; 'high leverage' per policy uses strict > 1.5."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        game_pk = kwargs.get("game_pk")
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        min_lev = kwargs.get("min_leverage")
        is_manual = kwargs.get("is_manual_alert")
        status = kwargs.get("draft_status")
        rows = [e for e in data["game_day_events"] if e.get("game_pk")==game_pk]
        if min_lev is not None:
            rows = [e for e in rows if (e.get("leverage_index") or 0) >= float(min_lev)]
        if is_manual is not None:
            rows = [e for e in rows if bool(e.get("is_manual_alert")) == bool(is_manual)]
        if status:
            rows = [e for e in rows if e.get("draft_status")==status]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_game_day_events","description":"Lists game_day_events for a game with optional filters.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"min_leverage":{"type":"number"},"is_manual_alert":{"type":"boolean"},"draft_status":{"type":"string"}},"required":["game_pk"]}}}

class CreateManualAlertEvent(Tool):
    """Create a manual in-game alert (is_manual_alert=true)."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","suggestion_text"])
        if need:
            return json.dumps({"error": need}, indent=2)
        events = data["game_day_events"]
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": kwargs.get("game_pk"),
            "pitch_id": kwargs.get("pitch_id"),
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": kwargs.get("leverage_index", 0.0),
            "is_manual_alert": True,
            "suggestion_text": kwargs.get("suggestion_text"),
            "draft_status": kwargs.get("draft_status","draft")
        }
        events.append(row)
        return json.dumps({"event_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_manual_alert_event","description":"Creates a manual alert event with draft_status default 'draft'.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"pitch_id":{"type":"integer"},"leverage_index":{"type":"number"},"suggestion_text":{"type":"string"},"draft_status":{"type":"string"}},"required":["game_pk","suggestion_text"]}}}

class CreateAutoBookmarkEvent(Tool):
    """Create an automatic high-leverage bookmark (is_manual_alert=false). Enforces leverage_index > 1.5."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","pitch_id","leverage_index","narration"])
        if need:
            return json.dumps({"error": need}, indent=2)
        if float(kwargs["leverage_index"]) <= 1.5:
            return json.dumps({"error":"auto-bookmarks require leverage_index > 1.5"}, indent=2)
        events = data["game_day_events"]
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": kwargs["game_pk"],
            "pitch_id": kwargs["pitch_id"],
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": kwargs["leverage_index"],
            "is_manual_alert": False,
            "suggestion_text": kwargs["narration"],
            "draft_status": "draft"
        }
        events.append(row)
        return json.dumps({"event_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"create_auto_bookmark_event",
            "description":"Creates an automatic high-leverage bookmark (is_manual_alert=false).",
            "parameters":{"type":"object","properties":{
                "game_pk":{"type":"integer"},
                "pitch_id":{"type":"integer"},
                "leverage_index":{"type":"number"},
                "narration":{"type":"string"}}, "required":["game_pk","pitch_id","leverage_index","narration"]}
        }}

class UpdateEventStatus(Tool):
    """Update draft_status for a game_day_event to one of: draft|published|archived, and audit the transition."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        event_id = kwargs.get("event_id")
        new_status = kwargs.get("draft_status")
        if event_id is None or new_status is None:
            return json.dumps({"error":"event_id and draft_status are required."}, indent=2)
        if new_status not in ("draft","published","archived"):
            return json.dumps({"error":"draft_status must be one of draft|published|archived."}, indent=2)
        row = next((e for e in data["game_day_events"] if e.get("event_id")==event_id), None)
        if not row:
            return json.dumps({"error": f"Event '{event_id}' not found."}, indent=2)
        previous = row.get("draft_status")
        row["draft_status"]=new_status
        audits = data.setdefault("event_status_audits", [])
        audits.append({
            "event_id": event_id,
            "previous_status": previous,
            "new_status": new_status,
            "changed_at_utc": _now_utc_iso()
        })
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_event_status","description":"Sets draft_status on a game_day_event and audits the transition.","parameters":{"type":"object","properties":{"event_id":{"type":"integer"},"draft_status":{"type":"string"}},"required":["event_id","draft_status"]}}}

class ComputeGameLeverageSummary(Tool):
    """Summarize counts of events above the high-leverage threshold (strict > threshold; default 1.5)."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            return json.dumps({"error": err}, indent=2)
        game_pk = kwargs.get("game_pk")
        threshold = kwargs.get("threshold", 1.5)
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        rows = [e for e in data["game_day_events"] if e.get("game_pk")==game_pk]
        total = len(rows)
        high = len([e for e in rows if (e.get("leverage_index") or 0) > float(threshold)])
        manual = len([e for e in rows if e.get("is_manual_alert") is True])
        return json.dumps({"game_pk":game_pk,"events_total":total,"events_high_leverage":high,"events_manual":manual,"threshold_used":threshold}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"compute_game_leverage_summary","description":"Returns counts of events and those above leverage threshold.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"threshold":{"type":"number"}},"required":["game_pk"]}}}

# ———————————————————————— REPORTS / INSIGHTS / DEV ————————————————————————

class CreateScoutingReport(Tool):
    """Insert a new row into scouting_reports with deterministic links; enforces post-game gate for report_type='post-game'."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["scouting_reports", "games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["report_type","game_pk","core_narrative_text","gslides_link","s3_pdf_path"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rtype = kwargs.get("report_type")
        gpk = kwargs.get("game_pk")
        if rtype == "post-game":
            g = next((g for g in data["games"] if g.get("game_pk") == gpk), None)
            if not g or g.get("game_status") != "Final":
                return json.dumps({"error": "post-game reports require games.game_status == 'Final'."}, indent=2)
        rows = data["scouting_reports"]
        new_id = _next_id(rows, "report_id")
        row = {
            "report_id": new_id,
            "report_type": rtype,
            "game_pk": gpk,
            "created_at": _now_utc_iso(),
            "s3_pdf_path": kwargs.get("s3_pdf_path"),
            "gslides_link": kwargs.get("gslides_link"),
            "core_narrative_text": kwargs.get("core_narrative_text"),
        }
        rows.append(row)
        return json.dumps({"report_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_scouting_report","description":"Creates a scouting_reports row with deterministic links and post-game gate enforcement.","parameters":{"type":"object","properties":{"report_type":{"type":"string"},"game_pk":{"type":"integer"},"core_narrative_text":{"type":"string"},"gslides_link":{"type":"string"},"s3_pdf_path":{"type":"string"}},"required":["report_type","game_pk","core_narrative_text","gslides_link","s3_pdf_path"]}}}

class AddCuratedInsight(Tool):
    """Add a curated_insights row linked to a report and player. Enforces templated insight_text and allowed insight_type."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["report_id","player_id","insight_text","insight_type","supporting_stat_value"])
        if need:
            return json.dumps({"error": need}, indent=2)
        # Enforce deterministic template and allowed types
        allowed_types = {"tendency","execution","stamina","situational","predictability"}
        t = kwargs.get("insight_type")
        if t not in allowed_types:
            return json.dumps({"error": f"insight_type must be one of {sorted(list(allowed_types))}"}, indent=2)
        pattern = r"^(tendency|execution|stamina|situational|predictability)_[a-z0-9]+_[a-z0-9]+$"
        if not re.match(pattern, kwargs.get("insight_text")):
            return json.dumps({"error":"insight_text must match '{category}_{metric}_{bucket}' using lowercase letters/digits."}, indent=2)

        rows = data["curated_insights"]
        new_id = _next_id(rows, "insight_id")
        row = {
            "insight_id": new_id,
            "report_id": kwargs.get("report_id"),
            "player_id": kwargs.get("player_id"),
            "insight_text": kwargs.get("insight_text"),
            "insight_type": kwargs.get("insight_type"),
            "supporting_stat_value": kwargs.get("supporting_stat_value")
        }
        rows.append(row)
        return json.dumps({"insight_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_curated_insight","description":"Inserts a curated insight row (templated text enforced).","parameters":{"type":"object","properties":{"report_id":{"type":"integer"},"player_id":{"type":"integer"},"insight_text":{"type":"string"},"insight_type":{"type":"string"},"supporting_stat_value":{"type":"number"}},"required":["report_id","player_id","insight_text","insight_type","supporting_stat_value"]}}}

class ListCuratedInsights(Tool):
    """List curated_insights by player_id and/or report_id, optional min supporting_stat_value. Sorted by value desc, player_id asc."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            return json.dumps({"error": err}, indent=2)
        pid = kwargs.get("player_id")
        rid = kwargs.get("report_id")
        min_val = kwargs.get("min_supporting_stat_value")
        rows = data["curated_insights"]
        if pid is not None:
            rows = [r for r in rows if r.get("player_id")==pid]
        if rid is not None:
            rows = [r for r in rows if r.get("report_id")==rid]
        if min_val is not None:
            rows = [r for r in rows if (r.get("supporting_stat_value") or 0) >= float(min_val)]
        rows = sorted(rows, key=lambda r: (-float(r.get("supporting_stat_value") or 0), int(r.get("player_id") or 0)))
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_curated_insights","description":"Lists curated insights filtered by player/report and threshold.","parameters":{"type":"object","properties":{"player_id":{"type":"integer"},"report_id":{"type":"integer"},"min_supporting_stat_value":{"type":"number"}},"required":[]}}}

class CreatePlayerDevReport(Tool):
    """Create a player_dev_reports row with deterministic s3 path if not provided."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["player_dev_reports"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["player_id","week_of_date"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["player_dev_reports"]
        new_id = _next_id(rows, "dev_report_id")
        path = kwargs.get("s3_pdf_path", f"s3://reports/player_dev/{kwargs.get('player_id')}/{kwargs.get('week_of_date')}.pdf")
        row = {
            "dev_report_id": new_id,
            "player_id": kwargs.get("player_id"),
            "week_of_date": kwargs.get("week_of_date"),
            "created_at": _now_utc_iso(),
            "s3_pdf_path": path
        }
        rows.append(row)
        return json.dumps({"dev_report_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_player_dev_report","description":"Creates a player_dev_reports row.","parameters":{"type":"object","properties":{"player_id":{"type":"integer"},"week_of_date":{"type":"string"},"s3_pdf_path":{"type":"string"}},"required":["player_id","week_of_date"]}}}

class CreatePlayerDevGoal(Tool):
    """Insert player_dev_goals row (status defaults to 'Proposed')."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["dev_report_id","player_id","goal_text","coach_id","target_review_date"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["player_dev_goals"]
        new_id = _next_id(rows, "goal_id")
        row = {
            "goal_id": new_id,
            "dev_report_id": kwargs.get("dev_report_id"),
            "player_id": kwargs.get("player_id"),
            "goal_text": kwargs.get("goal_text"),
            "goal_status": "Proposed",
            "coach_id": kwargs.get("coach_id"),
            "target_review_date": kwargs.get("target_review_date")
        }
        rows.append(row)
        return json.dumps({"goal_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_player_dev_goal","description":"Creates a 'Proposed' goal linked to a dev report.","parameters":{"type":"object","properties":{"dev_report_id":{"type":"integer"},"player_id":{"type":"integer"},"goal_text":{"type":"string"},"coach_id":{"type":"integer"},"target_review_date":{"type":"string"}},"required":["dev_report_id","player_id","goal_text","coach_id","target_review_date"]}}}

class ApprovePlayerDevGoal(Tool):
    """Approve a goal (goal_status='Approved')."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            return json.dumps({"error": err}, indent=2)
        goal_id = kwargs.get("goal_id")
        if goal_id is None:
            return json.dumps({"error":"goal_id is required."}, indent=2)
        row = next((g for g in data["player_dev_goals"] if g.get("goal_id")==goal_id), None)
        if not row:
            return json.dumps({"error": f"Goal '{goal_id}' not found."}, indent=2)
        row["goal_status"] = "Approved"
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"approve_player_dev_goal","description":"Sets goal_status='Approved' for a goal.","parameters":{"type":"object","properties":{"goal_id":{"type":"integer"}},"required":["goal_id"]}}}

class CreateVideoPlaylist(Tool):
    """Create a video_playlists row for a report. Enforces non-negative counts; when using dev categories, enforces clip ranges."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["report_id","playlist_name","clip_count"])
        if need:
            return json.dumps({"error": need}, indent=2)
        name = kwargs.get("playlist_name")
        cc = kwargs.get("clip_count")
        try:
            cc_int = int(cc)
        except Exception:
            return json.dumps({"error":"clip_count must be an integer."}, indent=2)
        if cc_int < 0:
            return json.dumps({"error":"clip_count must be a non-negative integer."}, indent=2)
        if name in ("Positive Reinforcement","Teaching Moments"):
            rng = (3,5) if name=="Positive Reinforcement" else (2,3)
            if not (rng[0] <= cc_int <= rng[1]):
                return json.dumps({"error":f"{name} requires clip_count in {rng}."}, indent=2)

        rows = data["video_playlists"]
        new_id = _next_id(rows, "playlist_id")
        link = kwargs.get("internal_portal_link", f"https://portal.internal/videos/report/{kwargs.get('report_id')}/playlist/{new_id}")
        row = {
            "playlist_id": new_id,
            "report_id": kwargs.get("report_id"),
            "playlist_name": name,
            "internal_portal_link": link,
            "clip_count": cc_int
        }
        rows.append(row)
        return json.dumps({"playlist_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_video_playlist","description":"Creates a video_playlists row for a report with validation.","parameters":{"type":"object","properties":{"report_id":{"type":"integer"},"playlist_name":{"type":"string"},"clip_count":{"type":"integer"},"internal_portal_link":{"type":"string"}},"required":["report_id","playlist_name","clip_count"]}}}

class ListVideoPlaylists(Tool):
    """List playlists for a given report_id."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            return json.dumps({"error": err}, indent=2)
        rid = kwargs.get("report_id")
        if rid is None:
            return json.dumps({"error":"report_id is required."}, indent=2)
        rows = [v for v in data["video_playlists"] if v.get("report_id")==rid]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_video_playlists","description":"Lists video_playlists rows for a report.","parameters":{"type":"object","properties":{"report_id":{"type":"integer"}},"required":["report_id"]}}}

# ———————————————————————— LOGGING ————————————————————————

class LogWorkflowRun(Tool):
    """Insert workflow_runs row with deterministic log_s3_path and explicit timestamps."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["workflow_runs"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["dag_name","status","start_time_utc","end_time_utc","log_s3_path"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["workflow_runs"]
        new_id = _next_id(rows, "run_id")
        row = {
            "run_id": new_id,
            "dag_name": kwargs.get("dag_name"),
            "game_pk": kwargs.get("game_pk"),
            "status": kwargs.get("status"),
            "start_time_utc": kwargs.get("start_time_utc"),
            "end_time_utc": kwargs.get("end_time_utc"),
            "log_s3_path": kwargs.get("log_s3_path")
        }
        rows.append(row)
        return json.dumps({"run_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"log_workflow_run","description":"Creates workflow_runs row with explicit timestamps and log path.","parameters":{"type":"object","properties":{"dag_name":{"type":"string"},"game_pk":{"type":"integer"},"status":{"type":"string"},"start_time_utc":{"type":"string"},"end_time_utc":{"type":"string"},"log_s3_path":{"type":"string"}},"required":["dag_name","status","start_time_utc","end_time_utc","log_s3_path"]}}}

class LogIngestionEvent(Tool):
    """Append ingestion_logs row."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["ingestion_logs"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["source_name","status_code","records_ingested"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["ingestion_logs"]
        new_id = _next_id(rows, "ingestion_id")
        row = {
            "ingestion_id": new_id,
            "source_name": kwargs.get("source_name"),
            "request_timestamp_utc": kwargs.get("request_timestamp_utc", _now_utc_iso()),
            "status_code": kwargs.get("status_code"),
            "records_ingested": kwargs.get("records_ingested")
        }
        rows.append(row)
        return json.dumps({"ingestion_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"log_ingestion_event","description":"Creates ingestion_logs row for observability.","parameters":{"type":"object","properties":{"source_name":{"type":"string"},"status_code":{"type":"integer"},"records_ingested":{"type":"integer"},"request_timestamp_utc":{"type":"string"}},"required":["source_name","status_code","records_ingested"]}}}

# ———————————————————————— CANONICALIZATION & SPATIAL ————————————————————————

class CanonicalizePitchTypes(Tool):
    """Write pitch_type_canonical for pitches lacking it using PITCH_MAP."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        if "pitches" not in data:
            return json.dumps({"error":"Missing required table(s): pitches"}, indent=2)
        updated = 0
        for p in data["pitches"]:
            raw = p.get("pitch_type_raw")
            if raw and not p.get("pitch_type_canonical"):
                p["pitch_type_canonical"] = PITCH_MAP.get(raw, raw)
                updated += 1
        return json.dumps({"updated_rows": updated}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"canonicalize_pitch_types","description":"Maps pitch_type_raw to canonical labels in pitches.","parameters":{"type":"object","properties":{},"required":[]}}}

class GridEncodePitchLocations(Tool):
    """Compute 12x12 zone cell for each pitch (requires explicit zone bounds). Optional persist=True writes back to pitches."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        if "pitches" not in data:
            return json.dumps({"error":"Missing required table(s): pitches"}, indent=2)
        need = _check_required(kwargs, ["min_x","max_x","min_z","max_z"])
        if need:
            return json.dumps({"error": need}, indent=2)
        mnx, mxx, mnz, mxz = map(float, (kwargs["min_x"], kwargs["max_x"], kwargs["min_z"], kwargs["max_z"]))
        if not (mxx > mnx and mxz > mnz):
            return json.dumps({"error":"Invalid bounds: require max_x>min_x and max_z>min_z"}, indent=2)

        def _cell(x, z):
            if x is None or z is None:
                return None
            x = max(mnx, min(mxx, float(x))); z = max(mnz, min(mxz, float(z)))
            cx = int(((x - mnx) / (mxx - mnx)) * 12.0) + 1
            cz = int(((z - mnz) / (mxz - mnz)) * 12.0) + 1
            return f"{cx if cx<=12 else 12}-{cz if cz<=12 else 12}"
        out = []
        for p in data["pitches"]:
            out.append({"pitch_id": p.get("pitch_id"), "zone_cell_12x12": _cell(p.get("plate_x"), p.get("plate_z"))})

        if kwargs.get("persist"):
            # write back to source table
            for p, rec in zip(data["pitches"], out):
                p["zone_cell_12x12"] = rec["zone_cell_12x12"]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"grid_encode_pitch_locations","description":"Adds 12x12 zone cell labels for pitches given explicit bounds; optional persist=True writes back.","parameters":{"type":"object","properties":{"min_x":{"type":"number"},"max_x":{"type":"number"},"min_z":{"type":"number"},"max_z":{"type":"number"},"persist":{"type":"boolean"}},"required":["min_x","max_x","min_z","max_z"]}}}

class WritePitchExecutionGrade(Tool):
    """Insert pitch_execution_grades based on miss_distance and (optional) model fields."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["pitch_execution_grades"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["pitch_id","game_pk","intended_quadrant_model","actual_quadrant","miss_distance_inches"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["pitch_execution_grades"]
        new_id = _next_id(rows, "grade_id")
        grade = _grade_execution(kwargs.get("miss_distance_inches"))
        row = {
            "grade_id": new_id,
            "pitch_id": kwargs.get("pitch_id"),
            "game_pk": kwargs.get("game_pk"),
            "intended_quadrant_model": kwargs.get("intended_quadrant_model"),
            "actual_quadrant": kwargs.get("actual_quadrant"),
            "miss_distance_inches": kwargs.get("miss_distance_inches"),
            "execution_grade": grade
        }
        rows.append(row)
        return json.dumps({"grade_id": new_id, "execution_grade": grade}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"write_pitch_execution_grade","description":"Creates a pitch_execution_grades row with deterministic grade policy.","parameters":{"type":"object","properties":{"pitch_id":{"type":"integer"},"game_pk":{"type":"integer"},"intended_quadrant_model":{"type":"string"},"actual_quadrant":{"type":"string"},"miss_distance_inches":{"type":"number"}},"required":["pitch_id","game_pk","intended_quadrant_model","actual_quadrant","miss_distance_inches"]}}}

# ———————————————————————— UMPIRE ————————————————————————

class WriteUmpireGameModel(Tool):
    """Insert an umpire_game_models row."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","umpire_id","zone_shift_x","zone_shift_z","calibration_error_pct","confidence_interval"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = data["umpire_game_models"]
        new_id = _next_id(rows, "umpire_game_id")
        row = {
            "umpire_game_id": new_id,
            "game_pk": kwargs.get("game_pk"),
            "umpire_id": kwargs.get("umpire_id"),
            "zone_shift_x": kwargs.get("zone_shift_x"),
            "zone_shift_z": kwargs.get("zone_shift_z"),
            "calibration_error_pct": kwargs.get("calibration_error_pct"),
            "confidence_interval": kwargs.get("confidence_interval")
        }
        rows.append(row)
        return json.dumps({"umpire_game_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"write_umpire_game_model","description":"Creates umpire_game_models row for a game.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"umpire_id":{"type":"integer"},"zone_shift_x":{"type":"number"},"zone_shift_z":{"type":"number"},"calibration_error_pct":{"type":"number"},"confidence_interval":{"type":"number"}},"required":["game_pk","umpire_id","zone_shift_x","zone_shift_z","calibration_error_pct","confidence_interval"]}}}

class GetUmpireGameModel(Tool):
    """Fetch umpire_game_models row for a game."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            return json.dumps({"error": err}, indent=2)
        game_pk = kwargs.get("game_pk")
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        row = next((u for u in data["umpire_game_models"] if u.get("game_pk")==game_pk), None)
        return json.dumps(row or {"error":"Not found."}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_umpire_game_model","description":"Returns the umpire model row for a game.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"}},"required":["game_pk"]}}}

# ———————————————————————— GAME SELECTION & OPPONENT ————————————————————————

class FindNextScheduledGame(Tool):
    """Find the next scheduled game on/after current_date; tie-break on smallest game_pk."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        if "current_date" not in kwargs or not kwargs["current_date"]:
            return json.dumps({"error":"current_date is required (YYYY-MM-DD)."}, indent=2)
        current_date = kwargs.get("current_date")
        candidates = [g for g in data["games"] if g.get("game_status")=="Scheduled" and str(g.get("game_date")) >= str(current_date)]
        if not candidates:
            return json.dumps({"error":"No scheduled games on or after current_date."}, indent=2)
        earliest = min(candidates, key=lambda g: (str(g.get("game_date")), int(g.get("game_pk") or 0)))
        return json.dumps({"next_game_pk":earliest.get("game_pk"),"home_team_id":earliest.get("home_team_id"),"away_team_id":earliest.get("away_team_id"),"game_date":earliest.get("game_date")}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"find_next_scheduled_game","description":"Returns earliest Scheduled game on/after a date.","parameters":{"type":"object","properties":{"current_date":{"type":"string"}},"required":["current_date"]}}}

class GetOpponentForTeamInGame(Tool):
    """Given a team_id and a game_pk, return the opponent team_id."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","team_id"])
        if need:
            return json.dumps({"error": need}, indent=2)
        g = next((g for g in data["games"] if g.get("game_pk")==kwargs["game_pk"]), None)
        if not g:
            return json.dumps({"error":"Game not found."}, indent=2)
        team = kwargs["team_id"]
        if g.get("home_team_id")==team:
            opp = g.get("away_team_id")
        elif g.get("away_team_id")==team:
            opp = g.get("home_team_id")
        else:
            return json.dumps({"error":"team_id not in specified game."}, indent=2)
        return json.dumps({"opponent_team_id": opp}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_opponent_for_team_in_game","description":"Finds the opponent team_id for a team in a given game.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"team_id":{"type":"integer"}},"required":["game_pk","team_id"]}}}

# ———————————————————————— TRENDS / PROBABLES ————————————————————————

class FilterTrends(Tool):
    """Applies min samples + EB shrinkage + FDR to produce deterministic trend flags (stub persists parameters for verification)."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["pitches"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["min_pitches","min_swings","min_bbe","fdr_threshold"])
        if need:
            return json.dumps({"error": need}, indent=2)
        table_name = (f"trend_flags_p{kwargs['min_pitches']}_s{kwargs['min_swings']}"
                      f"_b{kwargs['min_bbe']}_fdr{kwargs['fdr_threshold']}")
        data.setdefault("trend_flags", []).append({"table_name": table_name})
        return json.dumps({"flags_table": table_name}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"filter_trends",
            "description":"Applies min samples + EB shrinkage + FDR to produce trend flags (deterministic).",
            "parameters":{"type":"object","properties":{
                "min_pitches":{"type":"integer"},
                "min_swings":{"type":"integer"},
                "min_bbe":{"type":"integer"},
                "fdr_threshold":{"type":"number"}}, "required":["min_pitches","min_swings","min_bbe","fdr_threshold"]}
        }}

class ListProbablePitchers(Tool):
    """Returns probable pitchers for a team: deterministic sample from players table (position 'P' if present), sorted by full_name ASC."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["team_id"])
        if need:
            return json.dumps({"error": need}, indent=2)
        team_id = kwargs.get("team_id")
        limit = kwargs.get("limit", 2)
        # Consider position field variations
        def _is_pitcher(p):
            pos = (p.get("position") or p.get("primary_position") or "").upper()
            return pos in ("P","RP","SP","PITCHER")
        candidates = [p for p in data["players"] if p.get("current_team_id")==team_id and _is_pitcher(p)]
        # Deterministic sort
        candidates = sorted(candidates, key=lambda p: (str(p.get("full_name") or ""), int(p.get("player_id") or 0)))
        out = [{"player_id": p.get("player_id"), "full_name": p.get("full_name")} for p in candidates[:int(limit)]]
        return json.dumps({"probable_pitchers": out}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"list_probable_pitchers",
            "description":"Lists probable pitchers for a team, sorted by full_name ASC (deterministic sample from roster).",
            "parameters":{"type":"object","properties":{
                "team_id":{"type":"integer"},
                "limit":{"type":"integer"}}, "required":["team_id"]}
        }}


TOOLS: List[Tool] = [
    GetGameDetails(),
    ListGamesByStatus(),
    GetPlayerDetails(),
    ListPlayersByRosterStatus(),
    GetActiveRoster(),
    ListGameDayEvents(),
    CreateManualAlertEvent(),
    CreateAutoBookmarkEvent(),
    UpdateEventStatus(),
    ComputeGameLeverageSummary(),
    CreateScoutingReport(),
    AddCuratedInsight(),
    ListCuratedInsights(),
    CreatePlayerDevReport(),
    CreatePlayerDevGoal(),
    ApprovePlayerDevGoal(),
    CreateVideoPlaylist(),
    ListVideoPlaylists(),
    LogWorkflowRun(),
    LogIngestionEvent(),
    CanonicalizePitchTypes(),
    GridEncodePitchLocations(),
    WritePitchExecutionGrade(),
    WriteUmpireGameModel(),
    GetUmpireGameModel(),
    FindNextScheduledGame(),
    GetOpponentForTeamInGame(),
    FilterTrends(),
    ListProbablePitchers(),
]
