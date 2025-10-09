from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class MergePullRequest(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str,
        repo: str,
        pullNumber: int,
        merge_method: str,
        commit_message: str = None,
    ) -> str:
        """Merge a PR using the specified method with optional commit message."""
        pass
        pull_requests = data.get("pull_requests", [])

        for pr_entry in pull_requests:
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                try:
                    pr_idx = pr_entry["pr_numbers"].index(pullNumber)
                    pr_entry["pr_states"][pr_idx] = "merged"
                    pr_entry["merged_flags"][pr_idx] = True

                    #Utilize commit_message if available, else create a default
                    if commit_message:
                        merge_sha = f"merge_{pullNumber}_{merge_method}_{hash(commit_message) % 10000}"
                    else:
                        merge_sha = f"merge_{pullNumber}_{merge_method}"

                    result = {"merged": True, "sha": merge_sha}
                    if commit_message:
                        result["commit_message"] = commit_message
                    payload = result
                    out = json.dumps(payload, indent=2)
                    return out
                except ValueError:
                    pass
        payload = {"error": f"Pull request #{pullNumber} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mergePullRequest",
                "description": "Merge a PR using the specified method with optional commit message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "pullNumber": {"type": "integer", "description": "PR number"},
                        "merge_method": {
                            "type": "string",
                            "description": "Merge method",
                        },
                        "commit_message": {
                            "type": "string",
                            "description": "Optional commit message for the merge",
                        },
                    },
                    "required": ["owner", "repo", "pullNumber", "merge_method"],
                },
            },
        }
