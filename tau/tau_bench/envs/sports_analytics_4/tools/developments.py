# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Developments(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        week_of = kwargs.get("week_of")
        active_players = kwargs.get("active_players")
        data.setdefault("player_dev_goals", []).append({
            "goal_id": f"goal_{len(data.get('player_dev_goals', []))+1}",
            "week_of": week_of,
            "active_players": active_players
        })
        # return result
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "playersaims", "description": "Persists player development goals to database.", "parameters": {"type": "object", "properties": {"week_of": {"type": "string"}, "active_players": {"type": "integer"}}, "required": ["week_of"]}}}
