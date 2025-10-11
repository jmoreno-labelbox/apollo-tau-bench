# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrievePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], batch_name, model_name) -> str:
        preds = data.get("predictions", []) or []
        rows = [p for p in preds if (not batch_name or p.get("batch_name")==batch_name)
                and (not model_name or p.get("model_name")==model_name)]
        return json.dumps({"predictions": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_predictions",
            "description":"Read prediction batches (filter by batch_name and/or model_name).",
            "parameters":{"type":"object","properties":{
                "batch_name":{"type":"string"},
                "model_name":{"type":"string"}
            },"required":[]}
        }}
