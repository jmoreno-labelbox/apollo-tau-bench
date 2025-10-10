# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferRepo(Tool):
    """Transfer repository ownership to another username (string only)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current = kwargs.get("owner") or _actor_name(data)
        repo = kwargs.get("repo")
        new_owner = kwargs.get("new_owner")
        r = _find_repo(data, current, repo)
        if not r:
            raise RuntimeError("Repository not found")
        r["owner"] = new_owner
        return json.dumps({"ok": True, "owner": new_owner})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_repo",
                "description": "Transfer repo ownership to a new owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo": {"type": "string"},
                        "new_owner": {"type": "string"}
                    },
                    "required": ["repo", "new_owner"]
                }
            },
        }
