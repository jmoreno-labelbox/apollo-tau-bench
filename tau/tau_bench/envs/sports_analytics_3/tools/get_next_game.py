# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetNextGame(Tool):
    """
    Return the next Scheduled game strictly after a given date.
    If team_id is provided, only consider games where that team is home or away.

    Inputs:
      - current_date (YYYY-MM-DD) [required]
      - team_id (int) [optional]

    Selection rule:
      - Only games with game_status == "Scheduled"
      - game_date must be > current_date (strictly after)
      - If multiple candidates, pick the earliest game_date; tie-break by smallest game_pk
        for determinism.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_date= kwargs.get("current_date")
        team_id= kwargs.get("team_id")

        # 1) Verify
        if not isinstance(current_date, str) or current_date == "":
            return json.dumps({"error": "Missing required field: current_date (YYYY-MM-DD)"}, indent=2)

        # Retrieve database.
        games: List[Dict[str, Any]] = list(data.get("games", {}).values())

        # 3) Select qualifying upcoming games
        def is_eligible(g: Dict[str, Any]) -> bool:
            if g.get("game_status") != "Scheduled":
                return False
            if g.get("game_date", "") <= current_date:
                return False
            if team_id is None:
                return True
            return g.get("home_team_id") == team_id or g.get("away_team_id") == team_id

        future = [g for g in games if is_eligible(g)]

        if not future:
            target = f"after {current_date}" if team_id is None else f"for team_id {team_id} after {current_date}"
            return json.dumps({"error": f"No next scheduled game {target}"}, indent=2)

        # 4) Deterministic selection: prioritize earliest date, followed by the smallest game_pk.
        future.sort(key=lambda g: (g.get("game_date", ""), g.get("game_pk", 0)))
        return json.dumps(future[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_next_game",
                "description": "Return the next Scheduled game strictly after current_date; optionally filter by team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_date": {
                            "type": "string",
                            "description": "Current date in YYYY-MM-DD; next game must be strictly after this date."
                        },
                        "team_id": {
                            "type": "integer",
                            "description": "Optional team filter; include games where this team is home or away."
                        }
                    },
                    "required": ["current_date"]
                }
            }
        }
