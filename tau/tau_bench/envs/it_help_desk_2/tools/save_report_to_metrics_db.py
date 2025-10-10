# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveReportToMetricsDB(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        kpis = kwargs.get("kpis")
        report_date = FIXED_NOW.split('T')[0]
        metrics_db = data.setdefault("daily_metrics", [])
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {"run_id": run_id, "report_date": report_date, **kpis}
        metrics_db.append(new_metric)
        return json.dumps({"status": "success", "run_id": run_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "save_report_to_metrics_db", "description": "Saves the calculated daily KPIs to the historical metrics database.", "parameters": {"type": "object", "properties": {"kpis": {"type": "object"}}, "required": ["kpis"]}}}
