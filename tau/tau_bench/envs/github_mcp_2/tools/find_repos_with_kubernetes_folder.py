# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
