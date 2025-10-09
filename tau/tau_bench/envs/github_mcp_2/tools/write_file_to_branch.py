from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class WriteFileToBranch(Tool):
    """Inserts or modifies a file in a branch (without committing)."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None, path: str = None, content: str = None,
    commit_message: Any = None,
    ) -> str:
        if not all([repo_name, branch, path, content]):
            payload = {"error": "repo_name, branch, path, and content are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

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
            payload = {
                    "message": "File added or updated",
                    "repo": repo_name,
                    "branch": branch,
                    "path": path,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteFileToBranch",
                "description": "Adds or updates a file in the given branch (without committing).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                    },
                    "required": ["repo_name", "branch", "path", "content"],
                },
            },
        }
