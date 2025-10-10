# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeBullpenUsage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        time_window = kwargs.get("time_window", "last_21_days")
        return json.dumps({"bullpen_usage_analysis": f"usage_patterns_team_{team_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "analyze_bullpen_usage", "description": "Analyzes bullpen usage patterns for a team.", "parameters": {"type": "object", "properties": {"team_id": {"type": "integer"}, "time_window": {"type": "string"}}, "required": ["team_id"]}}}
