# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRepositories(Tool):
    """Lists all repositories owned by the current user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        owned = [r for r in _repos(data) if r["owner"] == me]
        return json.dumps({"repositories": owned}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_repositories",
                "description": "Returns all repositories owned by the current user.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
