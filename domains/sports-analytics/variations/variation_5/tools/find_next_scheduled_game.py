from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

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
