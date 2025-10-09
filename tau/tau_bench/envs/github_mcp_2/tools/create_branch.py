from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class CreateBranch(Tool):
    """Establishes a new branch based on an existing branch within the repository."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, source_branch: str = None, new_branch: str = None) -> str:
        if not all([repo_name, source_branch, new_branch]):
            payload = {"error": "repo_name, source_branch, and new_branch are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        try:
            repo = _find_repo_record(data, repo_name)
            if new_branch in repo.get("branches", []):
                payload = {"error": f"Branch '{new_branch}' already exists."}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            idx = _branch_index(repo, source_branch)
            repo.setdefault("branches", []).append(new_branch)
            repo.setdefault("branch_files", []).append(list(repo["branch_files"][idx]))
            repo.setdefault("branch_contents", []).append(
                list(repo["branch_contents"][idx])
            )
            repo.setdefault("branch_shas", []).append(get_next_commit_sha())
            payload = {
                    "message": "Branch created",
                    "new_branch": new_branch,
                    "from": source_branch,
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
                "name": "CreateBranch",
                "description": "Creates a new branch from an existing one in the repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "source_branch": {"type": "string"},
                        "new_branch": {"type": "string"},
                    },
                    "required": ["repo_name", "source_branch", "new_branch"],
                },
            },
        }
