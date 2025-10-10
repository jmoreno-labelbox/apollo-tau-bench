# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Curated(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        curated = data.get("curated_insights", [])
        curated.append({
            "report_id": kwargs.get("report_id"),
            "player_id": kwargs.get("player_id"),
            "insight_text": kwargs.get("insight_text"),
            "insight_type": kwargs.get("insight_type"),
            "supporting_stat_value": kwargs.get("supporting_stat_value")
        })
        # return outcome
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "makeIn", "description": "Persists a curated insight row.", "parameters": {"type": "object", "properties": {"report_id": {"type": "string"}, "player_id": {"type": "integer"}, "insight_text": {"type": "string"}, "insight_type": {"type": "string"}, "supporting_stat_value": {"type": "number"}}, "required": ["report_id", "player_id", "insight_text", "insight_type"]}}}
