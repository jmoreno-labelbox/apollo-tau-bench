# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadSystemConfigTool(Tool):
    """Read a config by key and return limited fields (avoid large blobs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        config_key = _require_str(kwargs.get("config_key"), "config_key")
        if not config_key:
            return json.dumps({"error":"config_key is required"})

        rows = data.get("system_config", [])
        for r in rows:
            if r.get("config_key") == config_key:
                return json.dumps({
                    "config_key": r.get("config_key"),
                    "sample": (r.get("config_value_json") or "")[:200]  # preview only
                }, indent=2)
        return json.dumps({"error": f"config_key {config_key} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"read_system_config",
            "description":"Return a preview of the config value by key (first 200 chars).",
            "parameters":{"type":"object","properties":{
                "config_key":{"type":"string"}
            },"required":["config_key"]}
        }}
