from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class FindReposWithDocsFolder(Tool):
    """Delivers repositories that have files located in the 'docs/' directory."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        me = _auth(data)["username"]
        matches = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("docs/") for f in file_list):
                    matches.append(r["repo_name"])
                    break
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "findReposWithDocsFolder",
                "description": "Finds repositories with files under 'docs/' folder.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
