# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

class WritePredictionLot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], batch_name, items, model_name) -> str:
        preds = list(data.get("predictions", {}).values())
        max_id = 0
        for p in preds:
            try:
                pid = int(p.get("prediction_id", 0))
                if pid > max_id:
                    max_id = pid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "prediction_id": new_id,
            "batch_name": batch_name,
            "model_name": model_name,
            "items": items or [],
            "created_at": _fixed_now_iso(),
        }
        preds.append(row)
        return json.dumps({"prediction_id": new_id, "batch_name": row["batch_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_prediction_lot",
            "description": "Insert a named prediction batch for a model.",
            "parameters": {"type": "object", "properties": {
                "batch_name": {"type": "string"},
                "model_name": {"type": "string"},
                "items": {"type": "array", "items": {"type": "object"}}
            }, "required": ["batch_name", "model_name", "items"]}
        }}
