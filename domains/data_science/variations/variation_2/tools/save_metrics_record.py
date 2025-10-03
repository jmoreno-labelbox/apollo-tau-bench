from tau_bench.envs.tool import Tool
import json
from typing import Any

class SaveMetricsRecord(Tool):
    """Adds a metrics record."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str, metrics_csv_path: str, generated_ts: str) -> str:
        req = {"model_name", "metrics_csv_path", "generated_ts"}
        record = {
            "model_name": model_name,
            "metrics_csv_path": metrics_csv_path,
            "generated_ts": generated_ts
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("metrics", []).append(record)
        payload = {
            "status": "inserted",
            "model_name": record.get("model_name"),
            "metrics_csv_path": record.get("metrics_csv_path"),
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveMetricsRecord",
                "description": "Appends a metrics record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
