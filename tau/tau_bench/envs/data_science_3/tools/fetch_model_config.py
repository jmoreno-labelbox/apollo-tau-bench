# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], config_name, model_name) -> str:
        cfgs = data.get("model_config", []) or []
        rows = [c for c in cfgs if (not model_name or c.get("model_name")==model_name) and (not config_name or c.get("config_name")==config_name)]
        return json.dumps({"configs": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_model_config",
            "description":"List model configs (optionally filtered by model_name and/or config_name).",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},"config_name":{"type":"string"}
            },"required":[]}
        }}
