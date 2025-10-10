# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WritePredictionLot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        preds = data.get("predictions", [])
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
            "batch_name": kwargs.get("batch_name"),
            "model_name": kwargs.get("model_name"),
            "items": kwargs.get("items") or [],
            "created_at": _now_iso_fixed(),
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
