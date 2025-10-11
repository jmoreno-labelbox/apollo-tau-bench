# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2FindProjectByIsbn(Tool):
    """Find project by ISBN."""

    @staticmethod
    def invoke(data: Dict[str, Any], isbn) -> str:
        if not isbn:
            return _error("isbn is required.")
        projects = list(data.get("projects", {}).values())
        project = _find_one(projects, "isbn", isbn)
        return json.dumps(project) if project else _error(f"Project with ISBN '{isbn}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_find_project_by_isbn",
                "description": "Find a project by its ISBN code.",
                "parameters": {
                    "type": "object",
                    "properties": {"isbn": {"type": "string"}},
                    "required": ["isbn"],
                },
            },
        }