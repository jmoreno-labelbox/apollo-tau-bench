# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Pitchers(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], team_id) -> str:
        # Deterministic stub: return two pitchers for team 13; otherwise, return empty.
        if team_id == 13:
        # return output
            return json.dumps({"probable_pitcher_ids": [101, 102]}, indent=2)
        # return output
        return json.dumps({"probable_pitcher_ids": []}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "findPitch", "description": "Provides opponent probable pitcher IDs.", "parameters": {"type": "object", "properties": {"team_id": {"type": "string"}}, "required": ["team_id"]}}}
