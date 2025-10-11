# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class RenameRepository(Tool):
    """Renames a repository owned by the acting user."""

    @staticmethod
    def invoke(data: Dict[str, Any], new_name, old_name) -> str:
        me = _auth(data)["username"]

        if not all([old_name, new_name]):
            return json.dumps({"error": "old_name and new_name are required."}, indent=2)

        repos = _repos(data)
        for r in repos:
            if r.get("owner") == me and r.get("repo_name") == old_name:
                r["repo_name"] = new_name
                return json.dumps({"message": "Repository renamed", "new_name": new_name}, indent=2)

        return json.dumps({"error": f"Repository '{old_name}' not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "rename_repository",
                "description": "Renames an existing repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "old_name": {"type": "string"},
                        "new_name": {"type": "string"}
                    },
                    "required": ["old_name", "new_name"]
                }
            }
        }