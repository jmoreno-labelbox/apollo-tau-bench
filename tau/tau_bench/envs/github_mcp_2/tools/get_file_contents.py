from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetFileContents(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, path: str = None, branch: str = None) -> str:
        if not all([repo_name, path]):
            payload = {"error": "repo_name and path are required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        idx = _branch_index(repo, branch)
        files = repo["branch_files"][idx]
        #print("files:", files)
        contents = repo["branch_contents"][idx]
        #print("contents:", contents)

        if path not in files:
            payload = {"error": f"File '{path}' not found."}
            out = json.dumps(payload, indent=2)
            return out

        i = files.index(path)
        payload = {"path": path, "content": contents[i]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFileContents",
                "description": "Gets the contents of a file in a repository branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                    },
                    "required": ["repo_name", "path"],
                },
            },
        }
