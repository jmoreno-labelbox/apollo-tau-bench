from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class FindReposWithKubernetesFolder(Tool):
    """Delivers repositories that have files within the 'kubernetes/' directory."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        matched = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("kubernetes/") for f in file_list):
                    matched.append(r["repo_name"])
                    break
        payload = matched
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findReposWithKubernetesFolder",
                "description": "Finds repositories with files under 'kubernetes/' folder.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
