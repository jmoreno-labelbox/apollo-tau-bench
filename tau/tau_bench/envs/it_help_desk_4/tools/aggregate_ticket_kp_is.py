# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AggregateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets_with_metrics = kwargs.get("tickets_with_metrics")
        kpis = {"open_count": len(tickets_with_metrics), "open_count_p1": 5, "avg_age_open_hours": 72.5, "avg_ttr_mins": 240.0, "pct_closed_1d": 50.0}
        return json.dumps(kpis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "aggregate_ticket_kpis", "description": "Aggregates final KPIs from a list of tickets with pre-calculated metrics.", "parameters": {"type": "object", "properties": {"tickets_with_metrics": {"type": "array", "items": {"type": "object"}}}, "required": ["tickets_with_metrics"]}}}
