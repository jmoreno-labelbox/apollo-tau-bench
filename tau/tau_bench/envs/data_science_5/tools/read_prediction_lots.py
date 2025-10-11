# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadPredictionLots(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], batch_name, model_name) -> str:
        preds = list(data.get("predictions", {}).values()) or []
        rows = [
            p for p in preds
            if (not batch_name or p.get("batch_name") == batch_name)
               and (not model_name or p.get("model_name") == model_name)
        ]
        return json.dumps({"predictions": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_prediction_lots",
            "description": "Read prediction batches (filter by batch or model).",
            "parameters": {"type": "object", "properties": {
                "batch_name": {"type": "string"},
                "model_name": {"type": "string"}
            }, "required": []}
        }}
