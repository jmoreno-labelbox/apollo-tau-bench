# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CloseIssue(Tool):
    """
    Close an issue in the issues DB.
    - Inputs: owner, repo_name (alias: repo_name), issue_number (aliases supported)
    - Sets issue_states[idx] = "closed" and bumps updated_ts via get_current_updated_timestamp().
    - Idempotent: if already closed, returns current state without changing anything.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo_name, issue_number) -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        issue_number_raw = issue_number
                

        if not owner or not repo_name or issue_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), issue_number."},
                indent=2
            )

        # Standardize issue_number
        try:
            issue_number = int(issue_number_raw)
        except Exception:
            return json.dumps({"error": "issue_number must be an integer."}, indent=2)

        # Initialize issues database
        issues_db = list(data.get("issues", {}).values())
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Locate the repository bucket.
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No issues found for repository '{owner}/{repo_name}'."}, indent=2)

        issue_numbers: List[int] = rec.get("issue_numbers", [])
        if issue_number not in issue_numbers:
            return json.dumps({"error": f"Issue # {issue_number} does not exist for '{owner}/{repo_name}'."}, indent=2)

        idx = issue_numbers.index(issue_number)

        # Verify the existence of arrays and apply padding.
        rec.setdefault("issue_states", [])
        rec.setdefault("updated_ts", [])
        while len(rec["issue_states"]) <= idx: rec["issue_states"].append("open")
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)

        current_state = rec["issue_states"][idx]
        if current_state == "closed":
            # Response is idempotent if it is already closed.
            return json.dumps(
                {
"success": f"Issue # {issue_number} is already resolved for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "issue_number": issue_number,
                    "state": "closed",
                    "updated_ts": rec["updated_ts"][idx]
                },
                indent=2
            )

        # Resolve the issue.
        rec["issue_states"][idx] = "closed"

        # Update updated_ts using the deterministic helper supplied by the environment.
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

add_terminal_message(data, f"Issue # Closed issue {issue_number} for repository {owner}/{repo_name} at {get_current_updated_timestamp()}.")

return json.dumps(
            {
"success": f"Issue # Closed issue number {issue_number} for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "issue_number": issue_number,
                "state": "closed",
                "updated_ts": new_updated_ts
            },
            indent=2
        )

@staticmethod
def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_issue",
                "description": "Close an issue (sets state to 'closed') and update its updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "issue_number": {"type": "integer", "description": "Issue number to close."}
                    },
                    "required": ["owner", "repo_name", "issue_number"]
                }
            }
        }