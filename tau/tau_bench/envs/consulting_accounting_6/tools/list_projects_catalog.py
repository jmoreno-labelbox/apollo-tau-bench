# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListProjectsCatalog(Tool):
    """List all projects."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"projects": list(data.get("projects", {}).values())}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_projects_catalog",
            "description": "List projects.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}
