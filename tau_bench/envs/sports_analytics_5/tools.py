import json
import re
from typing import Any

from tau_bench.envs.tool import Tool


def _check_required(kwargs: dict[str, Any], required: list[str]) -> str | None:
    pass
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None


def _require_tables(data: dict[str, Any], required: list[str]) -> str | None:
    pass
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None


def _next_id(rows: list[dict[str, Any]], key: str) -> int:
    pass
    max_id = 0
    for r in rows:
        try:
            max_id = max(max_id, int(r.get(key, 0)))
        except Exception:
            pass
    return max_id + 1


def _now_utc_iso() -> str:
    pass
    return _today_iso() + "T00:00:00Z"


def _today_iso() -> str:
    pass
    return "2025-08-14"


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


def _grade_execution(miss_distance_inches: float | None) -> str:
    pass
    if miss_distance_inches is None:
        return "Major miss"
    if miss_distance_inches <= 3.0:
        return "Executed"
    if miss_distance_inches <= 9.0:
        return "Minor miss"
    return "Major miss"


#——————— READS & LISTS ———————


class GetGameDetails(Tool):
    """Retrieve complete game row using game_pk."""

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: str = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not game_pk:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        row = next((g for g in data["games"] if g.get("game_pk") == game_pk), None)
        payload = row or {"error": f"Game '{game_pk}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGameDetails",
                "description": "Returns the games row for a given game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "integer"}},
                    "required": ["game_pk"],
                },
            },
        }


class ListGamesByStatus(Tool):
    """Retrieve games based on game_status filter."""

    @staticmethod
    def invoke(data, game_status: str = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not game_status:
            payload = {"error": "game_status is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [g for g in data["games"] if (g.get("game_status") == game_status)]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listGamesByStatus",
                "description": "Lists games by exact game_status (e.g., 'Scheduled','Final','Cancelled').",
                "parameters": {
                    "type": "object",
                    "properties": {"game_status": {"type": "string"}},
                    "required": ["game_status"],
                },
            },
        }


class GetPlayerDetails(Tool):
    """Retrieve a player using player_id or full_name."""

    @staticmethod
    def invoke(data, player_id: str = None, full_name: str = None) -> str:
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        pid = player_id
        name = full_name
        row = None
        if pid is not None:
            row = next((p for p in data["players"] if p.get("player_id") == pid), None)
        elif name:
            row = next((p for p in data["players"] if p.get("full_name") == name), None)
        else:
            payload = {"error": "Provide player_id or full_name."}
            out = json.dumps(payload, indent=2)
            return out
        payload = row or {"error": "Player not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPlayerDetails",
                "description": "Fetch player by ID or exact full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class ListPlayersByRosterStatus(Tool):
    """Retrieve players based on specified roster_status (e.g., 'Active', 'IL-15')."""

    @staticmethod
    def invoke(data, roster_status: str = None) -> str:
        pass
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not roster_status:
            payload = {"error": "roster_status is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [p for p in data["players"] if p.get("roster_status") == roster_status]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listPlayersByRosterStatus",
                "description": "Returns players matching a specific roster_status.",
                "parameters": {
                    "type": "object",
                    "properties": {"roster_status": {"type": "string"}},
                    "required": ["roster_status"],
                },
            },
        }


class GetActiveRoster(Tool):
    """Snapshot of the active roster for a team, omitting IL/Taxi unless include_il=True."""

    @staticmethod
    def invoke(data, team_id, include_il=False) -> str:
        pass
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if team_id is None:
            payload = {"error": "team_id is required."}
            out = json.dumps(payload, indent=2)
            return out

        def _eligible(p):
            pass
            rs = (p.get("roster_status") or "").upper()
            if include_il:
                return True
            return rs == "ACTIVE"

        rows = [
            p
            for p in data["players"]
            if p.get("current_team_id") == team_id and _eligible(p)
        ]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetActiveRoster",
                "description": "Returns active roster for a team_id. Excludes IL/Taxi by default.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "integer"},
                        "include_il": {"type": "boolean"},
                    },
                    "required": ["team_id"],
                },
            },
        }


#——————— GAME DAY EVENTS ———————


class ListGameDayEvents(Tool):
    """Retrieves events for a game with optional filters. Note: min_leverage serves as a general ≥ filter; 'high leverage' according to policy applies strict > 1.5."""
    @staticmethod
    def invoke(data, game_pk: int, min_leverage: float = None, is_manual_alert: bool = None, draft_status: str = None) -> str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if game_pk is None:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [e for e in data["game_day_events"] if e.get("game_pk") == game_pk]
        if min_leverage is not None:
            rows = [e for e in rows if (e.get("leverage_index") or 0) >= float(min_leverage)]
        if is_manual_alert is not None:
            rows = [
                e for e in rows if bool(e.get("is_manual_alert")) == bool(is_manual_alert)
            ]
        if draft_status:
            rows = [e for e in rows if e.get("draft_status") == draft_status]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListGameDayEvents",
                "description": "Lists game_day_events for a game with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "min_leverage": {"type": "number"},
                        "is_manual_alert": {"type": "boolean"},
                        "draft_status": {"type": "string"},
                    },
                    "required": ["game_pk"],
                },
            },
        }


class CreateManualAlertEvent(Tool):
    """Generate a manual in-game alert (is_manual_alert=true)."""

    @staticmethod
    def invoke(data, game_pk, suggestion_text, pitch_id=None, leverage_index=0.0, draft_status="draft", is_manual_alert: Any = None, timestamp_utc: str = None, title: str = None, message: str = None, operator_note: str = None, coach_visible: Any = None) -> str:
        pass
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"game_pk": game_pk, "suggestion_text": suggestion_text}, ["game_pk", "suggestion_text"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        events = data["game_day_events"]
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": leverage_index,
            "is_manual_alert": True,
            "suggestion_text": suggestion_text,
            "draft_status": draft_status,
        }
        events.append(row)
        payload = {"event_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateManualAlertEvent",
                "description": "Creates a manual alert event with draft_status default 'draft'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "pitch_id": {"type": "integer"},
                        "leverage_index": {"type": "number"},
                        "suggestion_text": {"type": "string"},
                        "draft_status": {"type": "string"},
                    },
                    "required": ["game_pk", "suggestion_text"],
                },
            },
        }


class CreateAutoBookmarkEvent(Tool):
    """Establish an automatic high-leverage bookmark (is_manual_alert=false). Requires leverage_index > 1.5."""

    @staticmethod
    def invoke(data, game_pk, pitch_id, leverage_index, narration, timestamp_utc: Any = None, is_manual_alert: Any = None, coach_visible: Any = None, draft_status: str = None) -> str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {"game_pk": game_pk, "pitch_id": pitch_id, "leverage_index": leverage_index, "narration": narration},
            ["game_pk", "pitch_id", "leverage_index", "narration"]
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        if float(leverage_index) <= 1.5:
            payload = {"error": "auto-bookmarks require leverage_index > 1.5"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        events = data["game_day_events"]
        new_id = _next_id(events, "event_id")
        row = {
            "event_id": new_id,
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": _now_utc_iso(),
            "leverage_index": leverage_index,
            "is_manual_alert": False,
            "suggestion_text": narration,
            "draft_status": "draft",
        }
        events.append(row)
        payload = {"event_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateAutoBookmarkEvent",
                "description": "Creates an automatic high-leverage bookmark (is_manual_alert=false).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "pitch_id": {"type": "integer"},
                        "leverage_index": {"type": "number"},
                        "narration": {"type": "string"},
                    },
                    "required": ["game_pk", "pitch_id", "leverage_index", "narration"],
                },
            },
        }


class UpdateEventStatus(Tool):
    """Modify draft_status for a game_day_event to either: draft|published|archived, and log the transition."""

    @staticmethod
    def invoke(data, event_id: str = None, draft_status: str = None, changed_at_utc: str = None) -> str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if event_id is None or draft_status is None:
            payload = {"error": "event_id and draft_status are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if draft_status not in ("draft", "published", "archived"):
            payload = {"error": "draft_status must be one of draft|published|archived."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        row = next(
            (e for e in data["game_day_events"] if e.get("event_id") == event_id), None
        )
        if not row:
            payload = {"error": f"Event '{event_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        previous = row.get("draft_status")
        row["draft_status"] = draft_status
        audits = data.setdefault("event_status_audits", [])
        audits.append(
            {
                "event_id": event_id,
                "previous_status": previous,
                "new_status": draft_status,
                "changed_at_utc": changed_at_utc if changed_at_utc is not None else _now_utc_iso(),
            }
        )
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateEventStatus",
                "description": "Sets draft_status on a game_day_event and audits the transition.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {"type": "integer"},
                        "draft_status": {"type": "string"},
                    },
                    "required": ["event_id", "draft_status"],
                },
            },
        }


class ComputeGameLeverageSummary(Tool):
    """Summarize the number of events exceeding the high-leverage threshold (strict > threshold; default 1.5)."""

    @staticmethod
    def invoke(data, game_pk: int = None, threshold: float = 1.5, leverage_threshold: float = None) -> str:
        # Use leverage_threshold if provided, otherwise use threshold
        if leverage_threshold is not None:
            threshold = leverage_threshold
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if game_pk is None:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [e for e in data["game_day_events"] if e.get("game_pk") == game_pk]
        total = len(rows)
        high = len(
            [e for e in rows if (e.get("leverage_index") or 0) > float(threshold)]
        )
        manual = len([e for e in rows if e.get("is_manual_alert") is True])
        payload = {
                "game_pk": game_pk,
                "events_total": total,
                "events_high_leverage": high,
                "events_manual": manual,
                "threshold_used": threshold,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ComputeGameLeverageSummary",
                "description": "Returns counts of events and those above leverage threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "threshold": {"type": "number"},
                    },
                    "required": ["game_pk"],
                },
            },
        }


#——————— REPORTS / INSIGHTS / DEV ———————


class CreateScoutingReport(Tool):
    """Add a new entry to scouting_reports with consistent links; enforces post-game restrictions for report_type='post-game'."""

    @staticmethod
    def invoke(
        data, 
        report_type: str = None, 
        game_pk: int = None, 
        core_narrative_text: str = None, 
        gslides_link: str = None, 
        s3_pdf_path: str = None,
        draft_status: str = None,
        label: str = None
    ) -> str:
        err = _require_tables(data, ["scouting_reports", "games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "report_type": report_type,
                "game_pk": game_pk,
                "core_narrative_text": core_narrative_text,
                "gslides_link": gslides_link,
                "s3_pdf_path": s3_pdf_path,
            },
            [
                "report_type",
                "game_pk",
                "core_narrative_text",
                "gslides_link",
                "s3_pdf_path",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rtype = report_type
        gpk = game_pk
        if rtype == "post-game":
            g = next((g for g in data["games"] if g.get("game_pk") == gpk), None)
            if not g or g.get("game_status") != "Final":
                payload = {
                        "error": "post-game reports require games.game_status == 'Final'."
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        rows = data["scouting_reports"]
        new_id = _next_id(rows, "report_id")
        row = {
            "report_id": new_id,
            "report_type": rtype,
            "game_pk": gpk,
            "created_at": _now_utc_iso(),
            "s3_pdf_path": s3_pdf_path,
            "gslides_link": gslides_link,
            "core_narrative_text": core_narrative_text,
        }
        rows.append(row)
        payload = {"report_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateScoutingReport",
                "description": "Creates a scouting_reports row with deterministic links and post-game gate enforcement.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string"},
                        "game_pk": {"type": "integer"},
                        "core_narrative_text": {"type": "string"},
                        "gslides_link": {"type": "string"},
                        "s3_pdf_path": {"type": "string"},
                    },
                    "required": [
                        "report_type",
                        "game_pk",
                        "core_narrative_text",
                        "gslides_link",
                        "s3_pdf_path",
                    ],
                },
            },
        }


class AddCuratedInsight(Tool):
    """Insert a curated_insights entry associated with a report and player. Enforces structured insight_text and permitted insight_type."""

    @staticmethod
    def invoke(
        data,
        report_id: str = None,
        player_id: str = None,
        insight_text: str = None,
        insight_type: str = None,
        supporting_stat_value: float = None,
    ) -> str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "report_id": report_id,
                "player_id": player_id,
                "insight_text": insight_text,
                "insight_type": insight_type,
                "supporting_stat_value": supporting_stat_value,
            },
            [
                "report_id",
                "player_id",
                "insight_text",
                "insight_type",
                "supporting_stat_value",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        # Ensure a consistent template and permitted types
        allowed_types = {
            "tendency",
            "execution",
            "stamina",
            "situational",
            "predictability",
        }
        if insight_type not in allowed_types:
            payload = {"error": f"insight_type must be one of {sorted(list(allowed_types))}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pattern = r"^(tendency|execution|stamina|situational|predictability)_[a-z0-9]+_[a-z0-9]+$"
        if not re.match(pattern, insight_text):
            payload = {
                "error": "insight_text must match '{category}_{metric}_{bucket}' using lowercase letters/digits."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        rows = data["curated_insights"]
        new_id = _next_id(rows, "insight_id")
        row = {
            "insight_id": new_id,
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value,
        }
        rows.append(row)
        payload = {"insight_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddCuratedInsight",
                "description": "Inserts a curated insight row (templated text enforced).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
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
                        "supporting_stat_value",
                    ],
                },
            },
        }


class ListCuratedInsights(Tool):
    """Retrieve curated_insights by player_id and/or report_id, with an optional minimum supporting_stat_value. Sorted by value in descending order, player_id in ascending order."""

    @staticmethod
    def invoke(data, player_id=None, report_id=None, min_supporting_stat_value=None) -> str:
        err = _require_tables(data, ["curated_insights"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["curated_insights"]
        if player_id is not None:
            rows = [r for r in rows if r.get("player_id") == player_id]
        if report_id is not None:
            rows = [r for r in rows if r.get("report_id") == report_id]
        if min_supporting_stat_value is not None:
            rows = [
                r
                for r in rows
                if (r.get("supporting_stat_value") or 0) >= float(min_supporting_stat_value)
            ]
        rows = sorted(
            rows,
            key=lambda r: (
                -float(r.get("supporting_stat_value") or 0),
                int(r.get("player_id") or 0),
            ),
        )
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListCuratedInsights",
                "description": "Lists curated insights filtered by player/report and threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"},
                        "report_id": {"type": "integer"},
                        "min_supporting_stat_value": {"type": "number"},
                    },
                    "required": [],
                },
            },
        }


class CreatePlayerDevReport(Tool):
    """Generate a player_dev_reports entry with a consistent s3 path if one is not given."""

    @staticmethod
    def invoke(data, player_id: str, week_of_date: str, s3_pdf_path: str = None) -> str:
        err = _require_tables(data, ["player_dev_reports"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"player_id": player_id, "week_of_date": week_of_date}, ["player_id", "week_of_date"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["player_dev_reports"]
        new_id = _next_id(rows, "dev_report_id")
        path = s3_pdf_path or f"s3://reports/player_dev/{player_id}/{week_of_date}.pdf"
        row = {
            "dev_report_id": new_id,
            "player_id": player_id,
            "week_of_date": week_of_date,
            "created_at": _now_utc_iso(),
            "s3_pdf_path": path,
        }
        rows.append(row)
        payload = {"dev_report_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePlayerDevReport",
                "description": "Creates a player_dev_reports row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"},
                        "week_of_date": {"type": "string"},
                        "s3_pdf_path": {"type": "string"},
                    },
                    "required": ["player_id", "week_of_date"],
                },
            },
        }


class CreatePlayerDevGoal(Tool):
    """Add a player_dev_goals entry (status defaults to 'Proposed')."""

    @staticmethod
    def invoke(
        data, 
        dev_report_id: int, 
        player_id: int, 
        goal_text: str, 
        coach_id: int, 
        target_review_date: str,
        goal_status: str = None
    ) -> str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "dev_report_id": dev_report_id,
                "player_id": player_id,
                "goal_text": goal_text,
                "coach_id": coach_id,
                "target_review_date": target_review_date,
            },
            [
                "dev_report_id",
                "player_id",
                "goal_text",
                "coach_id",
                "target_review_date",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["player_dev_goals"]
        new_id = _next_id(rows, "goal_id")
        row = {
            "goal_id": new_id,
            "dev_report_id": dev_report_id,
            "player_id": player_id,
            "goal_text": goal_text,
            "goal_status": goal_status if goal_status is not None else "Proposed",
            "coach_id": coach_id,
            "target_review_date": target_review_date,
        }
        rows.append(row)
        payload = {"goal_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreatePlayerDevGoal",
                "description": "Creates a 'Proposed' goal linked to a dev report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dev_report_id": {"type": "integer"},
                        "player_id": {"type": "integer"},
                        "goal_text": {"type": "string"},
                        "coach_id": {"type": "integer"},
                        "target_review_date": {"type": "string"},
                    },
                    "required": [
                        "dev_report_id",
                        "player_id",
                        "goal_text",
                        "coach_id",
                        "target_review_date",
                    ],
                },
            },
        }


class ApprovePlayerDevGoal(Tool):
    """Authorize a goal (goal_status='Approved')."""

    @staticmethod
    def invoke(data, goal_id: str = None) -> str:
        err = _require_tables(data, ["player_dev_goals"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if goal_id is None:
            payload = {"error": "goal_id is required."}
            out = json.dumps(payload, indent=2)
            return out
        row = next(
            (g for g in data["player_dev_goals"] if g.get("goal_id") == goal_id), None
        )
        if not row:
            payload = {"error": f"Goal '{goal_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        row["goal_status"] = "Approved"
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ApprovePlayerDevGoal",
                "description": "Sets goal_status='Approved' for a goal.",
                "parameters": {
                    "type": "object",
                    "properties": {"goal_id": {"type": "integer"}},
                    "required": ["goal_id"],
                },
            },
        }


class CreateVideoPlaylist(Tool):
    """Generate a video_playlists entry for a report. Requires non-negative counts; when utilizing dev categories, enforces clip ranges."""

    @staticmethod
    def invoke(data, report_id: str = None, playlist_name: str = None, clip_count: int = None, internal_portal_link: str = None) -> str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"report_id": report_id, "playlist_name": playlist_name, "clip_count": clip_count}, ["report_id", "playlist_name", "clip_count"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        name = playlist_name
        cc = clip_count
        try:
            cc_int = int(cc)
        except Exception:
            payload = {"error": "clip_count must be an integer."}
            out = json.dumps(payload, indent=2)
            return out
        if cc_int < 0:
            payload = {"error": "clip_count must be a non-negative integer."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if name in ("Positive Reinforcement", "Teaching Moments"):
            rng = (3, 5) if name == "Positive Reinforcement" else (2, 3)
            if not (rng[0] <= cc_int <= rng[1]):
                payload = {"error": f"{name} requires clip_count in {rng}."}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        rows = data["video_playlists"]
        new_id = _next_id(rows, "playlist_id")
        link = internal_portal_link or f"https://portal.internal/videos/report/{report_id}/playlist/{new_id}"
        row = {
            "playlist_id": new_id,
            "report_id": report_id,
            "playlist_name": name,
            "internal_portal_link": link,
            "clip_count": cc_int,
        }
        rows.append(row)
        payload = {"playlist_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateVideoPlaylist",
                "description": "Creates a video_playlists row for a report with validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "integer"},
                        "playlist_name": {"type": "string"},
                        "clip_count": {"type": "integer"},
                        "internal_portal_link": {"type": "string"},
                    },
                    "required": ["report_id", "playlist_name", "clip_count"],
                },
            },
        }


class ListVideoPlaylists(Tool):
    """Retrieve playlists associated with a specific report_id."""

    @staticmethod
    def invoke(data, report_id: str = None) -> str:
        err = _require_tables(data, ["video_playlists"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if report_id is None:
            payload = {"error": "report_id is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [v for v in data["video_playlists"] if v.get("report_id") == report_id]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListVideoPlaylists",
                "description": "Lists video_playlists rows for a report.",
                "parameters": {
                    "type": "object",
                    "properties": {"report_id": {"type": "integer"}},
                    "required": ["report_id"],
                },
            },
        }


#——————— LOGGING ———————


class LogWorkflowRun(Tool):
    """Add a workflow_runs entry with a consistent log_s3_path and defined timestamps."""

    @staticmethod
    def invoke(
        data, 
        dag_name: str, 
        status: str, 
        start_time_utc: str, 
        end_time_utc: str, 
        log_s3_path: str, 
        game_pk: str = None,
        workflow_name: str = None,
        timestamp_utc: str = None
    ) -> str:
        err = _require_tables(data, ["workflow_runs"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "dag_name": dag_name,
                "status": status,
                "start_time_utc": start_time_utc,
                "end_time_utc": end_time_utc,
                "log_s3_path": log_s3_path,
            },
            ["dag_name", "status", "start_time_utc", "end_time_utc", "log_s3_path"],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["workflow_runs"]
        new_id = _next_id(rows, "run_id")
        row = {
            "run_id": new_id,
            "dag_name": dag_name,
            "game_pk": game_pk,
            "status": status,
            "start_time_utc": start_time_utc,
            "end_time_utc": end_time_utc,
            "log_s3_path": log_s3_path,
        }
        rows.append(row)
        payload = {"run_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogWorkflowRun",
                "description": "Creates workflow_runs row with explicit timestamps and log path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dag_name": {"type": "string"},
                        "game_pk": {"type": "integer"},
                        "status": {"type": "string"},
                        "start_time_utc": {"type": "string"},
                        "end_time_utc": {"type": "string"},
                        "log_s3_path": {"type": "string"},
                    },
                    "required": [
                        "dag_name",
                        "status",
                        "start_time_utc",
                        "end_time_utc",
                        "log_s3_path",
                    ],
                },
            },
        }


class LogIngestionEvent(Tool):
    """Add an entry to ingestion_logs."""

    @staticmethod
    def invoke(data, source_name: str, status_code: int, records_ingested: int, request_timestamp_utc: str = None, ingested_at_utc: str = None, timestamp_utc: str = None, message: str = None, game_pk: Any = None) -> str:
        err = _require_tables(data, ["ingestion_logs"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {"source_name": source_name, "status_code": status_code, "records_ingested": records_ingested},
            ["source_name", "status_code", "records_ingested"]
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["ingestion_logs"]
        new_id = _next_id(rows, "ingestion_id")
        # Use ingested_at_utc if provided, otherwise request_timestamp_utc, otherwise current time
        timestamp = ingested_at_utc or request_timestamp_utc or _now_utc_iso()
        row = {
            "ingestion_id": new_id,
            "source_name": source_name,
            "request_timestamp_utc": timestamp,
            "status_code": status_code,
            "records_ingested": records_ingested,
        }
        rows.append(row)
        payload = {"ingestion_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "LogIngestionEvent",
                "description": "Creates ingestion_logs row for observability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string"},
                        "status_code": {"type": "integer"},
                        "records_ingested": {"type": "integer"},
                        "request_timestamp_utc": {"type": "string"},
                    },
                    "required": ["source_name", "status_code", "records_ingested"],
                },
            },
        }


#——————— CANONICALIZATION & SPATIAL ———————


class CanonicalizePitchTypes(Tool):
    """Assign pitch_type_canonical for pitches missing it by utilizing PITCH_MAP."""

    @staticmethod
    def invoke(data: dict[str, Any], ingested_at_utc: Any = None, game_pk: Any = None, scope: str = None) -> str:
        if "pitches" not in data:
            payload = {"error": "Missing required table(s): pitches"}
            out = json.dumps(payload, indent=2)
            return out
        updated = 0
        for p in data["pitches"]:
            raw = p.get("pitch_type_raw")
            if raw and not p.get("pitch_type_canonical"):
                p["pitch_type_canonical"] = PITCH_MAP.get(raw, raw)
                updated += 1
        payload = {"updated_rows": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CanonicalizePitchTypes",
                "description": "Maps pitch_type_raw to canonical labels in pitches.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GridEncodePitchLocations(Tool):
    """Calculate a 12x12 zone cell for each pitch (requires defined zone bounds). Optional persist=True will return data to pitches."""

    @staticmethod
    def invoke(data, min_x: float, max_x: float, min_z: float, max_z: float, persist: bool = False, game_pk: Any = None, scope: Any = None, cells_x: int = None, cells_z: int = None, return_rows: bool = None) -> str:
        pass
        if "pitches" not in data:
            payload = {"error": "Missing required table(s): pitches"}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"min_x": min_x, "max_x": max_x, "min_z": min_z, "max_z": max_z}, ["min_x", "max_x", "min_z", "max_z"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        mnx, mxx, mnz, mxz = map(float, (min_x, max_x, min_z, max_z))
        if not (mxx > mnx and mxz > mnz):
            payload = {"error": "Invalid bounds: require max_x>min_x and max_z>min_z"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        def _cell(x, z):
            pass
            if x is None or z is None:
                return None
            x = max(mnx, min(mxx, float(x)))
            z = max(mnz, min(mxz, float(z)))
            cx = int(((x - mnx) / (mxx - mnx)) * 12.0) + 1
            cz = int(((z - mnz) / (mxz - mnz)) * 12.0) + 1
            return f"{cx if cx<=12 else 12}-{cz if cz<=12 else 12}"

        out = []
        for p in data["pitches"]:
            out.append(
                {
                    "pitch_id": p.get("pitch_id"),
                    "zone_cell_12x12": _cell(p.get("plate_x"), p.get("plate_z")),
                }
            )

        if persist:
            #return data to the source table
            for p, rec in zip(data["pitches"], out):
                p["zone_cell_12x12"] = rec["zone_cell_12x12"]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GridEncodePitchLocations",
                "description": "Adds 12x12 zone cell labels for pitches given explicit bounds; optional persist=True writes back.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_x": {"type": "number"},
                        "max_x": {"type": "number"},
                        "min_z": {"type": "number"},
                        "max_z": {"type": "number"},
                        "persist": {"type": "boolean"},
                    },
                    "required": ["min_x", "max_x", "min_z", "max_z"],
                },
            },
        }


class WritePitchExecutionGrade(Tool):
    """Add pitch_execution_grades based on miss_distance and (optional) model fields."""

    @staticmethod
    def invoke(
        data,
        pitch_id: int,
        game_pk: int,
        intended_quadrant_model: str,
        actual_quadrant: str,
        miss_distance_inches: float,
        grade: str = None
    ) -> str:
        err = _require_tables(data, ["pitch_execution_grades"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "pitch_id": pitch_id,
                "game_pk": game_pk,
                "intended_quadrant_model": intended_quadrant_model,
                "actual_quadrant": actual_quadrant,
                "miss_distance_inches": miss_distance_inches,
            },
            [
                "pitch_id",
                "game_pk",
                "intended_quadrant_model",
                "actual_quadrant",
                "miss_distance_inches",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["pitch_execution_grades"]
        new_id = _next_id(rows, "grade_id")
        # Use provided grade if given, otherwise compute it
        exec_grade = grade if grade is not None else _grade_execution(miss_distance_inches)
        row = {
            "grade_id": new_id,
            "pitch_id": pitch_id,
            "game_pk": game_pk,
            "intended_quadrant_model": intended_quadrant_model,
            "actual_quadrant": actual_quadrant,
            "miss_distance_inches": miss_distance_inches,
            "execution_grade": exec_grade,
        }
        rows.append(row)
        payload = {"grade_id": new_id, "execution_grade": exec_grade}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "WritePitchExecutionGrade",
                "description": "Creates a pitch_execution_grades row with deterministic grade policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {"type": "integer"},
                        "game_pk": {"type": "integer"},
                        "intended_quadrant_model": {"type": "string"},
                        "actual_quadrant": {"type": "string"},
                        "miss_distance_inches": {"type": "number"},
                    },
                    "required": [
                        "pitch_id",
                        "game_pk",
                        "intended_quadrant_model",
                        "actual_quadrant",
                        "miss_distance_inches",
                    ],
                },
            },
        }


#——————— UMPIRE ———————


class WriteUmpireGameModel(Tool):
    """Add an entry for umpire_game_models."""

    @staticmethod
    def invoke(
        data,
        game_pk=None,
        umpire_id=None,
        zone_shift_x=None,
        zone_shift_z=None,
        calibration_error_pct=None,
        confidence_interval=None,
    ) -> str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "game_pk": game_pk,
                "umpire_id": umpire_id,
                "zone_shift_x": zone_shift_x,
                "zone_shift_z": zone_shift_z,
                "calibration_error_pct": calibration_error_pct,
                "confidence_interval": confidence_interval,
            },
            [
                "game_pk",
                "umpire_id",
                "zone_shift_x",
                "zone_shift_z",
                "calibration_error_pct",
                "confidence_interval",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["umpire_game_models"]
        new_id = _next_id(rows, "umpire_game_id")
        row = {
            "umpire_game_id": new_id,
            "game_pk": game_pk,
            "umpire_id": umpire_id,
            "zone_shift_x": zone_shift_x,
            "zone_shift_z": zone_shift_z,
            "calibration_error_pct": calibration_error_pct,
            "confidence_interval": confidence_interval,
        }
        rows.append(row)
        payload = {"umpire_game_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "WriteUmpireGameModel",
                "description": "Creates umpire_game_models row for a game.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "umpire_id": {"type": "integer"},
                        "zone_shift_x": {"type": "number"},
                        "zone_shift_z": {"type": "number"},
                        "calibration_error_pct": {"type": "number"},
                        "confidence_interval": {"type": "number"},
                    },
                    "required": [
                        "game_pk",
                        "umpire_id",
                        "zone_shift_x",
                        "zone_shift_z",
                        "calibration_error_pct",
                        "confidence_interval",
                    ],
                },
            },
        }


class GetUmpireGameModel(Tool):
    """Retrieve the umpire_game_models entry for a game."""

    @staticmethod
    def invoke(data, game_pk=None) -> str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if game_pk is None:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        row = next(
            (u for u in data["umpire_game_models"] if u.get("game_pk") == game_pk), None
        )
        payload = row or {"error": "Not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUmpireGameModel",
                "description": "Returns the umpire model row for a game.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "integer"}},
                    "required": ["game_pk"],
                },
            },
        }


#——————— GAME SELECTION & OPPONENT ———————


class FindNextScheduledGame(Tool):
    """Locate the next scheduled game on or after current_date; resolve ties using the smallest game_pk."""

    @staticmethod
    def invoke(data, current_date: str = None, team_id: Any = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not current_date:
            payload = {"error": "current_date is required (YYYY-MM-DD)."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        candidates = [
            g
            for g in data["games"]
            if g.get("game_status") == "Scheduled"
            and str(g.get("game_date")) >= str(current_date)
        ]
        if not candidates:
            payload = {"error": "No scheduled games on or after current_date."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        earliest = min(
            candidates,
            key=lambda g: (str(g.get("game_date")), int(g.get("game_pk") or 0)),
        )
        payload = {
                "next_game_pk": earliest.get("game_pk"),
                "home_team_id": earliest.get("home_team_id"),
                "away_team_id": earliest.get("away_team_id"),
                "game_date": earliest.get("game_date"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindNextScheduledGame",
                "description": "Returns earliest Scheduled game on/after a date.",
                "parameters": {
                    "type": "object",
                    "properties": {"current_date": {"type": "string"}},
                    "required": ["current_date"],
                },
            },
        }


class GetOpponentForTeamInGame(Tool):
    """Using a team_id and a game_pk, return the opposing team_id."""

    @staticmethod
    def invoke(data, game_pk, team_id: Any = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"game_pk": game_pk, "team_id": team_id}, ["game_pk", "team_id"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        g = next(
            (g for g in data["games"] if g.get("game_pk") == game_pk), None
        )
        if not g:
            payload = {"error": "Game not found."}
            out = json.dumps(payload, indent=2)
            return out
        team = team_id
        if g.get("home_team_id") == team:
            opp = g.get("away_team_id")
        elif g.get("away_team_id") == team:
            opp = g.get("home_team_id")
        else:
            payload = {"error": "team_id not in specified game."}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"opponent_team_id": opp}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOpponentForTeamInGame",
                "description": "Finds the opponent team_id for a team in a given game.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "team_id": {"type": "integer"},
                    },
                    "required": ["game_pk", "team_id"],
                },
            },
        }


#——————— TRENDS / PROBABLES ———————


class FilterTrends(Tool):
    """Utilizes minimum samples + EB shrinkage + FDR to generate consistent trend flags (stub retains parameters for validation)."""

    @staticmethod
    def invoke(data, min_pitches, min_swings, min_bbe, fdr_threshold, use_eb_shrinkage: Any = None, control: str = None, min_effect_size: Any = None, game_pk: Any = None) -> str:
        err = _require_tables(data, ["pitches"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {"min_pitches": min_pitches, "min_swings": min_swings, "min_bbe": min_bbe, "fdr_threshold": fdr_threshold},
            ["min_pitches", "min_swings", "min_bbe", "fdr_threshold"]
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        table_name = (
            f"trend_flags_p{min_pitches}_s{min_swings}"
            f"_b{min_bbe}_fdr{fdr_threshold}"
        )
        data.setdefault("trend_flags", []).append({"table_name": table_name})
        payload = {"flags_table": table_name}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "FilterTrends",
                "description": "Applies min samples + EB shrinkage + FDR to produce trend flags (deterministic).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_pitches": {"type": "integer"},
                        "min_swings": {"type": "integer"},
                        "min_bbe": {"type": "integer"},
                        "fdr_threshold": {"type": "number"},
                    },
                    "required": [
                        "min_pitches",
                        "min_swings",
                        "min_bbe",
                        "fdr_threshold",
                    ],
                },
            },
        }


class ListProbablePitchers(Tool):
    """Provides probable pitchers for a team: consistent sample from players table (position 'P' if available), sorted by full_name in ascending order."""

    @staticmethod
    def invoke(data, team_id, limit=2, use_eb_shrinkage: Any = None, order_by: str = None) -> str:
        pass
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"team_id": team_id}, ["team_id"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out

        # Take into account variations in position fields
        def _is_pitcher(p):
            pass
            pos = (p.get("position") or p.get("primary_position") or "").upper()
            return pos in ("P", "RP", "SP", "PITCHER")

        candidates = [
            p
            for p in data["players"]
            if p.get("current_team_id") == team_id and _is_pitcher(p)
        ]
        # Consistent sorting
        candidates = sorted(
            candidates,
            key=lambda p: (str(p.get("full_name") or ""), int(p.get("player_id") or 0)),
        )
        out = [
            {"player_id": p.get("player_id"), "full_name": p.get("full_name")}
            for p in candidates[: int(limit)]
        ]
        payload = {"probable_pitchers": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListProbablePitchers",
                "description": "Lists probable pitchers for a team, sorted by full_name ASC (deterministic sample from roster).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "integer"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["team_id"],
                },
            },
        }


TOOLS: list[Tool] = [
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
