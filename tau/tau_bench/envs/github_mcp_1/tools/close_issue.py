from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CloseIssue(Tool):
    """
    Close an issue in the issues DB.
    - Inputs: owner, repo_name (alias: repo_name), issue_number (aliases supported)
    - Sets issue_states[idx] = "closed" and bumps updated_ts via get_current_updated_timestamp().
    - Idempotent: if already closed, returns current state without changing anything.
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None, issue_number: int = None) -> str:
        owner = owner.strip() if owner else None
        repo_name = repo_name.strip() if repo_name else None
        issue_number_raw = issue_number

        if not owner or not repo_name or issue_number_raw is None:
            payload = {"error": "Required: owner, repo_name (or repo_name), issue_number."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Normalize issue_number
        try:
            issue_number = int(issue_number_raw)
        except Exception:
            payload = {"error": "issue_number must be an integer."}
            out = json.dumps(payload, indent=2)
            return out

        # Load issues DB
        issues_db = _convert_db_to_list(data.get("issues", {}).values())
        if not isinstance(issues_db, list):
            payload = {"error": "Invalid issues DB: expected a list at data['issues']."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find repo bucket
        rec = next(
            (
                r
                for r in issues_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {"error": f"No issues found for repository '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        issue_numbers: list[int] = rec.get("issue_numbers", [])
        if issue_number not in issue_numbers:
            payload = {
                    "error": f"Issue #{issue_number} not found for '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        idx = issue_numbers.index(issue_number)

        # Ensure arrays exist and are padded
        rec.setdefault("issue_states", [])
        rec.setdefault("updated_ts", [])
        while len(rec["issue_states"]) <= idx:
            rec["issue_states"].append("open")
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)

        current_state = rec["issue_states"][idx]
        if current_state == "closed":
            payload = {
                    "success": f"Issue #{issue_number} is already closed for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "issue_number": issue_number,
                    "state": "closed",
                    "updated_ts": rec["updated_ts"][idx],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Close the issue
        rec["issue_states"][idx] = "closed"

        # Bump updated_ts using environment-provided deterministic helper
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(
            data,
            f"Issue #{issue_number} closed for {owner}/{repo_name}.",
            get_current_updated_timestamp(),
        )
        payload = {
                "success": f"Issue #{issue_number} closed for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "issue_number": issue_number,
                "state": "closed",
                "updated_ts": new_updated_ts,
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
                "name": "CloseIssue",
                "description": "Close an issue (sets state to 'closed') and update its updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias: repo_name).",
                        },
                        "issue_number": {
                            "type": "integer",
                            "description": "Issue number to close.",
                        },
                    },
                    "required": ["owner", "repo_name", "issue_number"],
                },
            },
        }
