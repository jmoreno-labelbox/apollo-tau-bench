from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteRepository(Tool):
    """Deletes a repository identified by owner and repo name."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "") -> str:
        owner = owner.strip()
        # Accept either 'repo_name' or 'repo_name' for convenience
        repo_name = repo_name.strip()

        if not owner or not repo_name:
            payload = {"error": "Both 'owner' and 'repo_name' are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Support either {"repositories": [...]} or a direct list
        repos = None
        if isinstance(data, dict) and "repositories" in data:
            repos = data.get("repositories", {}).values()
        elif isinstance(data, list):
            repos = data
        else:
            payload = {
                    "error": "Invalid database format: expected a list or a dict with 'repositories'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find the repository index deterministically (first exact match)
        idx = next(
            (
                i
                for i, r in enumerate(repos)
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )

        if idx is None:
            payload = {"error": f"Repository '{owner}/{repo_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Remove the repo in place (deterministic mutation)
        removed = repos.pop(idx)

        add_terminal_message(
            data, f"Repository '{owner}/{repo_name}' deleted.", get_current_timestamp()
        )
        payload = {
                "success": f"Repository '{owner}/{repo_name}' deleted.",
                "deleted": {
                    "owner": removed.get("owner"),
                    "repo_name": removed.get("repo_name"),
                    "deleted_ts": get_current_timestamp(),
                },
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteRepository",
                "description": "Deletes a repository for the given owner and repository name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team).",
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name.",
                        },
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }
