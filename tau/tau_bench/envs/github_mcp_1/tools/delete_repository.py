# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteRepository(Tool):
    """Deletes a repository identified by owner and repo name."""

    @staticmethod
    def invoke(data: Dict[str, Any], owner = "", repo_name = "") -> str:
        owner = owner.strip()
        # Allow the use of 'repo_name' or 'repo_name' for ease of use.
        repo_name = repo_name.strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Both 'owner' and 'repo_name' are required."},
                indent=2
            )

        # Accept either {"repositories": [...]} format or a direct array.
        repos = None
        if isinstance(data, dict) and "repositories" in data:
            repos = list(data.get("repositories", {}).values())
        elif isinstance(data, list):
            repos = data
        else:
            return json.dumps(
                {"error": "Invalid database format: expected a list or a dict with 'repositories'."},
                indent=2
            )

        # Identify the repository index in a deterministic manner (first precise match).
        idx = next(
            (i for i, r in enumerate(repos)
             if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )

        if idx is None:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        # Eliminate the repository directly (predictable modification).
        removed = repos.pop(idx)

        add_terminal_message(data, f"Repository '{owner}/{repo_name}' deleted.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Repository '{owner}/{repo_name}' deleted.",
                "deleted": {
                    "owner": removed.get("owner"),
                    "repo_name": removed.get("repo_name"),
                    "deleted_ts": get_current_timestamp()
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_repository",
                "description": "Deletes a repository for the given owner and repository name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name."
                        }
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }
