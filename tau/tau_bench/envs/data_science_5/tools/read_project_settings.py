# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadProjectSettings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfg = data.get("project_config", {}) or {}
        key = kwargs.get("key")
        if key:
            return json.dumps({key: cfg.get(key)}, indent=2)
        return json.dumps(cfg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_project_settings",
            "description": "Return full project settings or a single key.",
            "parameters": {"type": "object", "properties": {"key": {"type": "string"}}, "required": []}
        }}
