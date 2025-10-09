from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MarkPRasMerged(Tool):
    """
    Marks a pull request as merged, but only if it is currently mergeable.
    NOTE: This tool does NOT copy files or perform any branch/content merge. It only:
      - verifies the PR is mergeable,
      - sets merged flags/states,
      - bumps the PR's updated_ts deterministically,
      - logs a terminal message.
    Inputs: owner, repo_name, pr_number
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None, reponame: str = None, pr_number: int = None, prnumber: int = None) -> str:
        owner = (owner or "").strip()
        repo_name = (repo_name or reponame or "").strip()
        pr_number_raw = pr_number if pr_number is not None else prnumber

        if not owner or not repo_name or pr_number_raw is None:
            payload = {"error": "Required: owner, repo_name, pr_number."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            payload = {"error": "pr_number must be an integer."}
            out = json.dumps(payload, indent=2)
            return out

        #Load PR DB
        pr_db = _convert_db_to_list(data.get("pull_requests", {}).values()
        if not isinstance(pr_db, list):
            payload = {"error": "Invalid pull requests DB: expected a list."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Find PR bucket for repo
        rec = next(
            (
                r
                for r in pr_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {"error": f"No pull requests found for '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        pr_numbers: list[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            payload = {"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        idx = pr_numbers.index(pr_number)

        #Ensure arrays exist/padded
        rec.setdefault("pr_states", [])
        rec.setdefault("merged_flags", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("updated_ts", [])
        rec.setdefault("pr_status", [])

        while len(rec["pr_states"]) <= idx:
            rec["pr_states"].append("open")
        while len(rec["merged_flags"]) <= idx:
            rec["merged_flags"].append(False)
        while len(rec["mergeable_flags"]) <= idx:
            rec["mergeable_flags"].append(False)
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)
        while len(rec["pr_status"]) <= idx:
            rec["pr_status"].append("open")

        #Must be mergeable
        if not bool(rec["mergeable_flags"][idx]):
            payload = {
                    "error": f"PR #{pr_number} is not mergeable for '{owner}/{repo_name}'.",
                    "mergeable": False,
                    "current_state": rec["pr_states"][idx],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Idempotent path: already merged
        if bool(rec["merged_flags"][idx]) and rec["pr_states"][idx] == "merged":
            payload = {
                    "success": f"PR #{pr_number} is already merged for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "pr_number": pr_number,
                    "state": "merged",
                    "merged": True,
                    "mergeable": True,
                    "updated_ts": rec["updated_ts"][idx],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Mark as merged and update timestamp (no file operations)
        rec["pr_states"][idx] = "merged"
        rec["pr_status"][idx] = "merged"
        rec["merged_flags"][idx] = True

        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        #Terminal log
        add_terminal_message(
            data, f"PR #{pr_number} merged for {owner}/{repo_name}.", new_updated_ts
        )
        payload = {
                "success": f"PR #{pr_number} merged for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "state": "merged",
                "merged": True,
                "mergeable": True,
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
                "name": "MarkPrAsMerged",
                "description": "Mark a PR as merged if mergeable; sets merged flags/states and updates PR updated_ts (no file merges).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias: reponame).",
                        },
                        "pr_number": {
                            "type": "integer",
                            "description": "Pull request number.",
                        },
                    },
                    "required": ["owner", "repo_name", "pr_number"],
                },
            },
        }
