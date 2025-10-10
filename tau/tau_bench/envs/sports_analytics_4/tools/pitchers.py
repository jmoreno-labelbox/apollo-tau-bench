# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Pitchers(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        # Deterministic stub: return two pitchers for team 13, else empty
        if team_id == 13:
        # return result
            return json.dumps({"probable_pitcher_ids": [101, 102]}, indent=2)
        # return result
        return json.dumps({"probable_pitcher_ids": []}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "findPitch", "description": "Provides opponent probable pitcher IDs.", "parameters": {"type": "object", "properties": {"team_id": {"type": "string"}}, "required": ["team_id"]}}}
