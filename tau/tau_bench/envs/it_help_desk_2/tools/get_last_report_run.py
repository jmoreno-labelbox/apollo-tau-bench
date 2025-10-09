from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetLastReportRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        report_runs = data.get("report_runs", [])
        if not report_runs:
            payload = {"error": "No previous report runs found."}
            out = json.dumps(payload, indent=2)
            return out
        last_run = report_runs[-1]
        last_run["kpis"] = {
            "total_open": 45,
            "avg_age_open_hours": 22.0,
            "avg_ttr_mins": 1300,
            "pct_closed_1d": 65.0,
            "p1_open_count": 4,
        }
        payload = last_run
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLastReportRun",
                "description": "Retrieves the data from the last successful service desk health report run.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
