# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveMetricsToDatabase(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], database_table, metrics_path, report_date) -> str:
        metrics_db = data.setdefault("daily_metrics", [])
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {"run_id": run_id, "report_date": report_date, "database_table": database_table}
        metrics_db.append(new_metric)
        return json.dumps({"status": "success", "run_id": run_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "save_metrics_to_database", "description": "Save calculated metrics to database.", "parameters": {"type": "object", "properties": {"metrics_path": {"type": "string"}, "database_table": {"type": "string"}, "report_date": {"type": "string"}}, "required": ["metrics_path", "database_table", "report_date"]}}}
