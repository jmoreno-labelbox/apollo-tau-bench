from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListPullRequests(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str, state: str) -> str:
        """List PRs filtered by state."""
        pass
        pull_requests = data.get("pull_requests", {}).values()

        for pr_entry in pull_requests.values():
            if pr_entry["owner"] == owner and pr_entry["repo_name"] == repo:
                prs = []
                for i, pr_number in enumerate(pr_entry["pr_numbers"]):
                    pr_state = pr_entry["pr_states"][i]
                    if state == "all" or pr_state == state:
                        prs.append(
                            {
                                "number": pr_number,
                                "state": pr_state,
                                "title": pr_entry["pr_titles"][i],
                            }
                        )
                payload = {"prs": prs}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"prs": []}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listPullRequests",
                "description": "List PRs filtered by state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                        "state": {"type": "string", "description": "PR state filter"},
                    },
                    "required": ["owner", "repo", "state"],
                },
            },
        }
