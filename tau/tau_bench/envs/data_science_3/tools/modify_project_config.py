# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class ModifyProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        cfg = data.get("project_config", {})
        if cfg is None or isinstance(cfg, list):
            cfg = {}
            data["project_config"] = cfg
        cfg.update(updates)
        cfg["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_project_config",
            "description":"Update project configuration with provided key/value pairs.",
            "parameters":{"type":"object","properties":{"updates":{"type":"object"}},"required":["updates"]}
        }}
