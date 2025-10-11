# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], export_path) -> str:
        if not "Tickets_Export.csv" in export_path:
            return json.dumps({"error": "Invalid export path provided."}, indent=2)
        kpis = {"total_open": 46, "avg_age_open_hours": 23.5, "avg_ttr_mins": 1440, "pct_closed_1d": 60.0, "p1_open_count": 5}
        return json.dumps(kpis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_ticket_kpis", "description": "Calculates standard service desk KPIs from a ticket export CSV.", "parameters": {"type": "object", "properties": {"export_path": {"type": "string"}}, "required": ["export_path"]}}}
