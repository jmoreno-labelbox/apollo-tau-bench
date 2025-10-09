from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogModelMetric(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        model_name: str = None, 
        metric_name: str = None, 
        value: float = None, 
        dataset_split: str = None
    ) -> str:
        metrics = data.get("metrics", [])
        max_id = 0
        for m in metrics:
            try:
                mid = int(m.get("metric_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "metric_id": new_id,
            "model_name": model_name,
            "metric_name": metric_name,
            "value": value,
            "dataset_split": dataset_split,
            "timestamp": _now_iso_fixed(),
        }
        metrics.append(row)
        payload = {
            "metric_id": new_id,
            "model_name": row["model_name"],
            "metric_name": row["metric_name"],
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogModelMetric",
                "description": "Insert a metric row for a model+split.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "value": {"type": "number"},
                        "dataset_split": {"type": "string"},
                    },
                    "required": ["model_name", "metric_name", "value", "dataset_split"],
                },
            },
        }
