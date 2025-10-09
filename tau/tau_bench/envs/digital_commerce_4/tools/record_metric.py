from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordMetric(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject_id: str, metric: str, value: float) -> str:
        subject_id = _sid(subject_id)
        payload = {"metric": metric, "value": float(value)}
        _ws_append(data, subject_id, "METRIC_RECORDED", payload)
        payload = {"subject_id": subject_id, "metric": metric, "value": float(value)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordMetric",
                "description": "Record a simple metric value for the subject.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject_id": {"type": "string"},
                        "metric": {"type": "string"},
                        "value": {"type": "number"},
                    },
                    "required": ["subject_id", "metric", "value"],
                },
            },
        }
