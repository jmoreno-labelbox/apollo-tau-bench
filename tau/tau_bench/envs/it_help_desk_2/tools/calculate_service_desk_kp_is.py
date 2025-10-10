# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateServiceDeskKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        input_path = kwargs.get("input_path")
        metrics = kwargs.get("metrics")
        output_path = kwargs.get("output_path")
        kpis = {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}
        return json.dumps({"kpis": kpis, "output_path": output_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_service_desk_kpis", "description": "Calculate service desk KPIs from ticket data.", "parameters": {"type": "object", "properties": {"input_path": {"type": "string"}, "metrics": {"type": "array", "items": {"type": "string"}}, "output_path": {"type": "string"}}, "required": ["input_path", "metrics", "output_path"]}}}
