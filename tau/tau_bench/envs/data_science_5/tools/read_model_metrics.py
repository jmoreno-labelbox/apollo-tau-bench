from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadModelMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, metric_name: str = None, dataset_split: str = None) -> str:
        metrics = data.get("metrics", []) or []
        rows = [
            m
            for m in metrics
            if (not model_name or m.get("model_name") == model_name)
            and (not metric_name or m.get("metric_name") == metric_name)
            and (not dataset_split or m.get("dataset_split") == dataset_split)
        ]
        payload = {"metrics": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadModelMetrics",
                "description": "Read metrics filtered by model/metric/split.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "dataset_split": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
