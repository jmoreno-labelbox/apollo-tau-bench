# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveModelRecord(Tool):
    """
    Appends a models record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"model_name", "model_type", "training_ts", "model_path", "feature_names", "target_name"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("models", []).append(record)
        return json.dumps({"status": "inserted", "model_name": record.get("model_name")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_model_record",
                "description": "Appends a models record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
