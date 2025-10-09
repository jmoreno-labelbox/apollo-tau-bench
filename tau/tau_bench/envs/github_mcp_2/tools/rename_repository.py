from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class RenameRepository(Tool):
    """Changes the name of a repository owned by the acting user."""

    @staticmethod
    def invoke(data: dict[str, Any], old_name: str = None, new_name: str = None) -> str:
        me = _auth(data)["username"]

        if not all([old_name, new_name]):
            payload = {"error": "old_name and new_name are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        repos = _repos(data)
        for r in repos:
            if r.get("owner") == me and r.get("repo_name") == old_name:
                r["repo_name"] = new_name
                payload = {"message": "Repository renamed", "new_name": new_name}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Repository '{old_name}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RenameRepository",
                "description": "Renames an existing repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "old_name": {"type": "string"},
                        "new_name": {"type": "string"},
                    },
                    "required": ["old_name", "new_name"],
                },
            },
        }
