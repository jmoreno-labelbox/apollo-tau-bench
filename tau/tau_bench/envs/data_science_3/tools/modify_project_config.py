# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class ModifyProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        
        # Ensure project_config exists in data
        if "project_config" not in data or data["project_config"] is None or isinstance(data["project_config"], list):
            data["project_config"] = {}
        
        # Now update the config that's actually in data
        data["project_config"].update(updates)
        data["project_config"]["updated_at"] = _fixed_now_iso()
        
        return json.dumps({"updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_project_config",
            "description":"Update project configuration with provided key/value pairs.",
            "parameters":{"type":"object","properties":{"updates":{"type":"object"}},"required":["updates"]}
        }}
