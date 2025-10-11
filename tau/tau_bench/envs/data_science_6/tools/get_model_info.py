# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetModelInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], model_name) -> str:
        if not model_name:
            return json.dumps({"error":"Missing model_name"})
        for rec in list(data.get("models", {}).values()):
            if rec.get("model_name") == model_name:
                return json.dumps({"model_name": model_name, "model_path": rec.get("model_path")})
        return json.dumps({})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_model_info","description":"Returns model artifact info such as model_path for a model_name.","parameters":{"type":"object","properties":{"model_name":{"type":"string"}},"required":["model_name"]}}}
