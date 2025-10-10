# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectKey(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: Optional[str] = None) -> str:
        projects = _get_table(data, "projects")
        proj = None
        if project_id:
            proj = next((p for p in projects if p.get("id") == project_id), None)
        if not proj:
            # Fallback deterministically to the lexicographically smallest id
            proj = sorted(projects, key=lambda x: x.get("id", ""))[0] if projects else None
        key = (proj or {}).get("project_key")
        return json.dumps({"project_key": key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_project_key", "description": "Returns a deterministic project_key from projects.json (by id if provided, else first by id).", "parameters": {"type": "object", "properties": {"project_id": {"type": "string"}}, "required": []}}}
