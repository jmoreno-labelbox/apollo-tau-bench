# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchProjectCard(Tool):
    """Fetch project by project_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("project_id")
        row = next((p for p in list(data.get("projects", {}).values()) if p.get("project_id") == pid), None)
        if not row:
            return json.dumps({"error": f"project_id '{pid}' not found"}, indent=2)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_project_card",
            "description": "Fetch a project by id.",
            "parameters": {"type": "object", "properties": {"project_id": {"type": "string"}}, "required": ["project_id"]}
        }}
