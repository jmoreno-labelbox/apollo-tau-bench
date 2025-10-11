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

class FindReposWithKubernetesFolder(Tool):
    """Returns repositories with files inside 'kubernetes/' directory."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        matched = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("kubernetes/") for f in file_list):
                    matched.append(r["repo_name"])
                    break

        return json.dumps(matched, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "find_repos_with_kubernetes_folder",
                "description": "Finds repositories with files under 'kubernetes/' folder.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }