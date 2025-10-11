# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SavePredictionsRecord(Tool):
    """
    Appends a predictions record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"model_name", "predictions_csv_path", "row_count", "columns", "generated_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("predictions", []).append(record)
        return json.dumps({"status": "inserted", "model_name": record.get("model_name"), "predictions_csv_path": record.get("predictions_csv_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_predictions_record",
                "description": "Appends a predictions record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
