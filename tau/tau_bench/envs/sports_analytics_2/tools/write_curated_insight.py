# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteCuratedInsight(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], insight_text, insight_type, player_id, report_id, supporting_stat_value) -> str:
        curated = data.get("curated_insights", [])
        curated.append({
            "report_id": report_id,
            "player_id": player_id,
            "insight_text": insight_text,
            "insight_type": insight_type,
            "supporting_stat_value": supporting_stat_value
        })
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_curated_insight", "description": "Writes a curated insight row.", "parameters": {"type": "object", "properties": {"report_id": {"type": "string"}, "player_id": {"type": "integer"}, "insight_text": {"type": "string"}, "insight_type": {"type": "string"}, "supporting_stat_value": {"type": "number"}}, "required": ["report_id", "player_id", "insight_text", "insight_type"]}}}
