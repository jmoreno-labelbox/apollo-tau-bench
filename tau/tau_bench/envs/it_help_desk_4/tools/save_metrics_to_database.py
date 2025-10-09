from tau_bench.envs.tool import Tool
import json
from typing import Any

class SaveMetricsToDatabase(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], metrics_path: str = None, database_table: str = None, report_date: str = None) -> str:
        metrics_db = data.setdefault("daily_metrics", [])
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {
            "run_id": run_id,
            "report_date": report_date,
            "database_table": database_table,
        }
        metrics_db.append(new_metric)
        payload = {"status": "success", "run_id": run_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveMetricsToDatabase",
                "description": "Save calculated metrics to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "metrics_path": {"type": "string"},
                        "database_table": {"type": "string"},
                        "report_date": {"type": "string"},
                    },
                    "required": ["metrics_path", "database_table", "report_date"],
                },
            },
        }
