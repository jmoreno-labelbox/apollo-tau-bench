from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReadModelProfiles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, config_name: str = None) -> str:
        cfgs = data.get("model_config", []) or []
        rows = [
            c
            for c in cfgs
            if (not model_name or c.get("model_name") == model_name)
            and (not config_name or c.get("config_name") == config_name)
        ]
        payload = {"configs": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadModelProfiles",
                "description": "List model configs (filtered by model and/or config name).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "config_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
