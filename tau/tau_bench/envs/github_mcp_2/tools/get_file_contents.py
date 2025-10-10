# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFileContents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        path = kwargs.get("path")
        branch = kwargs.get("branch")

        if not all([repo_name, path]):
            return json.dumps({"error": "repo_name and path are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        # print("files:", files)
        contents = repo["branch_contents"][idx]
        # output("contents:", contents)

        if path not in files:
            return json.dumps({"error": f"File '{path}' not found."}, indent=2)

        i = files.index(path)
        return json.dumps({"path": path, "content": contents[i]}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_file_contents",
                "description": "Gets the contents of a file in a repository branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"}
                    },
                    "required": ["repo_name", "path"]
                }
            }
        }
