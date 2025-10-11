# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeSituationalSplits(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id, situations = []) -> str:
        return json.dumps({"situational_splits": f"splits_data_team_{team_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compute_situational_splits", "description": "Computes situational performance splits for a team.", "parameters": {"type": "object", "properties": {"team_id": {"type": "integer"}, "situations": {"type": "array", "items": {"type": "string"}}}, "required": ["team_id"]}}}
