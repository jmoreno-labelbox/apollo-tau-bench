# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_all(lst: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [x for x in lst or [] if x.get(key) == value]

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2GetProjectsByPublisher(Tool):
    """Get all projects for a specific publisher."""

    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id, active_only = True) -> str:
        if not publisher_id:
            return _error("publisher_id is required.")

        projects = list(data.get("projects", {}).values())
        publisher_projects = _find_all(projects, "publisher_id", publisher_id)

        if active_only:
            publisher_projects = [p for p in publisher_projects if p.get("is_active", True)]

        return json.dumps(publisher_projects)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_projects_by_publisher",
                "description": "Get all projects for a specific publisher, optionally filtering to active projects only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True}
                    },
                    "required": ["publisher_id"],
                },
            },
        }