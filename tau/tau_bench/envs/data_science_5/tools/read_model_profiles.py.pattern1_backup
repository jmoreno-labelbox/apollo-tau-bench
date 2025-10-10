# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadModelProfiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfgs = data.get("model_config", []) or []
        model_name = kwargs.get("model_name")
        config_name = kwargs.get("config_name")
        rows = [
            c for c in cfgs
            if (not model_name or c.get("model_name") == model_name)
               and (not config_name or c.get("config_name") == config_name)
        ]
        return json.dumps({"configs": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_model_profiles",
            "description": "List model configs (filtered by model and/or config name).",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "config_name": {"type": "string"}
            }, "required": []}
        }}
