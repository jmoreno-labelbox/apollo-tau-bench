from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetBullpenSessionInfoForPlayer(Tool):
    """
    Retrieve bullpen sessions for a specified player with optional filters.

    Inputs (exact names; case-sensitive):
      - playerid (int)          : Required. Player ID to filter on (matches 'player_id').
      - date (str, optional)    : Exact session date 'YYYY-MM-DD' (matches 'session_date').
      - type (str, optional)    : Exact pitch type (matches 'pitch_type_canonical').

    Behavior:
      - Exact matching on the provided filters (without normalization).
      - Results are sorted deterministically by session_date in ascending order, then session_id in ascending order.
      - If no matching records are found, returns a structured error.
    """

    @staticmethod
    def invoke(data: dict[str, Any], playerid: str = None, date: str = None, type: str = None) -> str:
        pass
        date_filter = date
        type_filter = type

        #1) Confirm required input
        if playerid is None:
            payload = {"error": "Missing required field: playerid"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Access DB
        sessions: list[dict[str, Any]] = data.get("bullpen_sessions", [])

        #3) Filter based on exact fields
        def match(session: dict[str, Any]) -> bool:
            pass
            if session.get("player_id") != playerid:
                return False
            if date_filter is not None and session.get("session_date") != date_filter:
                return False
            if (
                type_filter is not None
                and session.get("pitch_type_canonical") != type_filter
            ):
                return False
            return True

        matches = [s for s in sessions if match(s)]

        if not matches:
            #Construct a clear, structured error
            parts = [f"player_id {playerid}"]
            if date_filter is not None:
                parts.append(f"date {date_filter}")
            if type_filter is not None:
                parts.append(f"type {type_filter}")
            payload = {"error": f"No bullpen sessions found for {'; '.join(parts)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matches.sort(
            key=lambda s: (s.get("session_date", ""), int(s.get("session_id", 0)))
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getBullpenSessionInfoForPlayer",
                "description": "Fetch bullpen sessions for a player with optional exact filters on date and pitch type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "playerid": {
                            "type": "integer",
                            "description": "Exact player ID (matches 'player_id').",
                        },
                        "date": {
                            "type": "string",
                            "description": "Exact session date in YYYY-MM-DD (matches 'session_date').",
                        },
                        "type": {
                            "type": "string",
                            "description": "Exact pitch type (matches 'pitch_type_canonical').",
                        },
                    },
                    "required": ["playerid"],
                },
            },
        }
