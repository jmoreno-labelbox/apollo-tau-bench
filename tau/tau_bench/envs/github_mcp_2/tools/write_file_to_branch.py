# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteFileToBranch(Tool):
    """Adds or updates a file in a branch (does not commit)."""

    @staticmethod
    def invoke(data: Dict[str, Any], branch, content, path, repo_name) -> str:

        if not all([repo_name, branch, path, content]):
            return json.dumps({"error": "repo_name, branch, path, and content are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo["branch_files"][idx]
            contents = repo["branch_contents"][idx]

            if path in files:
                i = files.index(path)
                contents[i] = content
            else:
                files.append(path)
                contents.append(content)

            return json.dumps({
                "message": "File added or updated",
                "repo": repo_name,
                "branch": branch,
                "path": path
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_file_to_branch",
                "description": "Adds or updates a file in the given branch (without committing).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["repo_name", "branch", "path", "content"]
                }
            }
        }
