from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetNextGame(Tool):
    """
    Retrieve the next Scheduled game that occurs strictly after a specified date.
    If team_id is provided, only consider games where that team is either home or away.

    Inputs:
      - current_date (YYYY-MM-DD) [required]
      - team_id (int) [optional]

    Selection criteria:
      - Only games with game_status == "Scheduled"
      - game_date must be > current_date (strictly after)
      - If there are multiple options, select the earliest game_date; use smallest game_pk
        as a tie-breaker for determinism.
    """

    @staticmethod
    def invoke(data: dict[str, Any], current_date: str = None, team_id: str = None) -> str:
        #1) Confirm validity
        if not isinstance(current_date, str) or current_date == "":
            payload = {"error": "Missing required field: current_date (YYYY-MM-DD)"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", [])

        #3) Filter future games that are eligible
        def is_eligible(g: dict[str, Any]) -> bool:
            if g.get("game_status") != "Scheduled":
                return False
            if g.get("game_date", "") <= current_date:
                return False
            if team_id is None:
                return True
            return g.get("home_team_id") == team_id or g.get("away_team_id") == team_id

        future = [g for g in games if is_eligible(g)]

        if not future:
            target = (
                f"after {current_date}"
                if team_id is None
                else f"for team_id {team_id} after {current_date}"
            )
            payload = {"error": f"No next scheduled game {target}"}
            out = json.dumps(payload, indent=2)
            return out

        #4) Deterministic selection: earliest date first, then smallest game_pk
        future.sort(key=lambda g: (g.get("game_date", ""), g.get("game_pk", 0)))
        payload = future[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNextGame",
                "description": "Return the next Scheduled game strictly after current_date; optionally filter by team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_date": {
                            "type": "string",
                            "description": "Current date in YYYY-MM-DD; next game must be strictly after this date.",
                        },
                        "team_id": {
                            "type": "integer",
                            "description": "Optional team filter; include games where this team is home or away.",
                        },
                    },
                    "required": ["current_date"],
                },
            },
        }
