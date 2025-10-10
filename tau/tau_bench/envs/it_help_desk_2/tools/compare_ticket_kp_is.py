# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareTicketKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_kpis = kwargs.get("current_kpis")
        previous_kpis = kwargs.get("previous_kpis")
        delta = {
            "total_open_delta": current_kpis.get("total_open", 0) - previous_kpis.get("total_open", 0),
            "p1_open_delta": current_kpis.get("p1_open_count", 0) - previous_kpis.get("p1_open_count", 0)
        }
        analysis_summary = f"KPI comparison complete. Open tickets changed by {delta['total_open_delta']}. P1 tickets changed by {delta['p1_open_delta']}."
        return json.dumps({"analysis_summary": analysis_summary, "delta": delta}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compare_ticket_kpis", "description": "Compares two sets of ticket KPIs to find the delta.", "parameters": {"type": "object", "properties": {"current_kpis": {"type": "object"}, "previous_kpis": {"type": "object"}}, "required": ["current_kpis", "previous_kpis"]}}}
