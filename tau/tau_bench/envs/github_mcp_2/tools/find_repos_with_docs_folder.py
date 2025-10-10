# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindReposWithDocsFolder(Tool):
    """Returns repositories containing files under the 'docs/' folder."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        me = _auth(data)["username"]
        matches = []

        for r in _repos(data):
            if r.get("owner") != me:
                continue
            for file_list in r.get("branch_files", []):
                if any(f.startswith("docs/") for f in file_list):
                    matches.append(r["repo_name"])
                    break

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "find_repos_with_docs_folder",
                "description": "Finds repositories with files under 'docs/' folder.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
