# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBullpenSessionInfoForPlayer(Tool):
    """
    Return bullpen sessions for a given player with optional filters.

    Inputs (exact names; case-sensitive):
      - playerid (int)          : Required. Player ID to filter on (matches 'player_id').
      - date (str, optional)    : Exact session date 'YYYY-MM-DD' (matches 'session_date').
      - type (str, optional)    : Exact pitch type (matches 'pitch_type_canonical').

    Behavior:
      - Exact matching on the provided filters (no normalization).
      - Results are sorted deterministically by session_date ASC, then session_id ASC.
      - If no matching records are found, returns a structured error.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], date, playerid, type) -> str:
        date_filter = date
        type_filter = type

        # 1) Check for mandatory input validity
        if playerid is None:
            return json.dumps({"error": "Missing required field: playerid"}, indent=2)

        # 2) Connect to the database
        sessions: List[Dict[str, Any]] = list(data.get("bullpen_sessions", {}).values())

        # 3) Apply filters based on specific fields.
        def match(session: Dict[str, Any]) -> bool:
            if session.get("player_id") != playerid:
                return False
            if date_filter is not None and session.get("session_date") != date_filter:
                return False
            if type_filter is not None and session.get("pitch_type_canonical") != type_filter:
                return False
            return True

        matches = [s for s in sessions if match(s)]

        if not matches:
            # Create a detailed, organized error message.
            parts = [f"player_id {playerid}"]
            if date_filter is not None:
                parts.append(f"date {date_filter}")
            if type_filter is not None:
                parts.append(f"type {type_filter}")
            return json.dumps({"error": f"No bullpen sessions found for {'; '.join(parts)}"}, indent=2)

        # 4) Fixed sequence
        matches.sort(key=lambda s: (s.get("session_date", ""), int(s.get("session_id", 0))))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_bullpen_session_info_for_player",
                "description": "Fetch bullpen sessions for a player with optional exact filters on date and pitch type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "playerid": {
                            "type": "integer",
                            "description": "Exact player ID (matches 'player_id')."
                        },
                        "date": {
                            "type": "string",
                            "description": "Exact session date in YYYY-MM-DD (matches 'session_date')."
                        },
                        "type": {
                            "type": "string",
                            "description": "Exact pitch type (matches 'pitch_type_canonical')."
                        }
                    },
                    "required": ["playerid"]
                }
            }
        }
