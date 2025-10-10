# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProbablePitchers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        # Deterministic stub: return two pitchers for team 13, else empty
        if team_id == 13:
            return json.dumps({"probable_pitcher_ids": [101, 102]}, indent=2)
        return json.dumps({"probable_pitcher_ids": []}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_probable_pitchers", "description": "Returns opponent probable pitcher IDs.", "parameters": {"type": "object", "properties": {"team_id": {"type": "string"}}, "required": ["team_id"]}}}
