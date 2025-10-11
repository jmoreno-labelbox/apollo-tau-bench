# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLastReportRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_runs = list(data.get("report_runs", {}).values())
        if not report_runs:
            return json.dumps({"error": "No previous report runs found."}, indent=2)
        last_run = report_runs[-1]
        # Simulating the KPIs that would have been recorded during the execution.
        last_run["kpis"] = {"total_open": 45, "avg_age_open_hours": 22.0, "avg_ttr_mins": 1300, "pct_closed_1d": 65.0, "p1_open_count": 4}
        return json.dumps(last_run, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_report_run", "description": "Retrieves the data from the last successful service desk health report run.", "parameters": {"type": "object", "properties": {}, "required": []}}}
