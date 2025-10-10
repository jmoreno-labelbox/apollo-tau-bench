# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class AddModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        models = list(data.get("models", {}).values())
        max_id = 0
        for m in models:
            try:
                mid = int(m.get("model_id", 0))
                if mid > max_id: max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "model_id": new_id,
            "model_name": kwargs.get("model_name"),
            "model_type": kwargs.get("model_type"),
            "framework": kwargs.get("framework"),
            "version": kwargs.get("version"),
            "status": kwargs.get("status"),
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso()
        }
        models.append(row)
        return json.dumps({"model_id": new_id, "model_name": row["model_name"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_model",
            "description":"Register a model in the model registry.",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},
                "model_type":{"type":"string"},
                "framework":{"type":"string"},
                "version":{"type":"string"},
                "status":{"type":"string"}
            },"required":["model_name","model_type","framework","version","status"]}
        }}
