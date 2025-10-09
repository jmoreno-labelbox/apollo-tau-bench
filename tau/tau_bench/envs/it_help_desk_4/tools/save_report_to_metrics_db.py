from tau_bench.envs.tool import Tool
import json
from typing import Any

class SaveReportToMetricsDB(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        kpis: dict[str, Any],
        report_date: Any = None,
        timestamp: Any = None,
    ) -> str:
        report_date = FIXED_NOW.split("T")[0]
        metrics_db = data.setdefault("daily_metrics", [])
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {"run_id": run_id, "report_date": report_date, **kpis}
        metrics_db.append(new_metric)
        payload = {"status": "success", "run_id": run_id}
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SaveReportToMetricsDb",
                "description": "Saves the calculated daily KPIs to the historical metrics database.",
                "parameters": {
                    "type": "object",
                    "properties": {"kpis": {"type": "object"}},
                    "required": ["kpis"],
                },
            },
        }
