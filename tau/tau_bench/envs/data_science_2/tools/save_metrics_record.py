# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveMetricsRecord(Tool):
    """
    Appends a metrics record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"model_name", "metrics_csv_path", "generated_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("metrics", []).append(record)
        return json.dumps({"status": "inserted", "model_name": record.get("model_name"), "metrics_csv_path": record.get("metrics_csv_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_metrics_record",
                "description": "Appends a metrics record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
