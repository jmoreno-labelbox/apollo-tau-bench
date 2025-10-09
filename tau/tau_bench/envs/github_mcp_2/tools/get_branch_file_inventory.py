from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetBranchFileInventory(Tool):
    """Delivers the list of files and the latest SHA for a specified branch in a repository owned by the user."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not all([repo_name, branch]):
            payload = {"error": "repo_name and branch are required."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo.get("branch_files", [])[idx]
            sha = repo.get("branch_shas", [])[idx]
            payload = {
                    "repo_name": repo_name,
                    "branch": branch,
                    "commit_sha": sha,
                    "files": files,
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
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getBranchFileInventory",
                "description": "Returns latest SHA and file list for a given repo and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }
