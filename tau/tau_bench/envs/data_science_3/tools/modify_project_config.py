# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso




def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

class ModifyProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], updates) -> str:
        updates = updates or {}
        
        # Verify that project_config is present in the data.
        if "project_config" not in data or data["project_config"] is None or isinstance(data["project_config"], list):
            data["project_config"] = {}
        
        # Update the configuration present in the data.
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