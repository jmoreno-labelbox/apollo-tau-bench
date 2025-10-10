# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        team = next((t for t in data.get("teams", []) if t.get("team_id") == team_id), None)
        return json.dumps(team or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_team_details", "description": "Gets details for a team id.", "parameters": {"type": "object", "properties": {"team_id": {"type": "integer"}}, "required": ["team_id"]}}}
