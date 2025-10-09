from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class WritePlayerDevGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        week_of = kwargs.get("week_of")
        active_players = kwargs.get("active_players")
        data.setdefault("player_dev_goals", []).append(
            {
                "goal_id": f"goal_{len(data.get('player_dev_goals', {}))+1}",
                "week_of": week_of,
                "active_players": active_players,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WritePlayerDevGoals",
                "description": "Writes player development goals to database.",
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
