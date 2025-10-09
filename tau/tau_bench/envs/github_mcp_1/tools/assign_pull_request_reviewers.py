from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AssignPullRequestReviewers(Tool):
    """
    Assign reviewers to a pull request.
    - Inputs: owner, repo_name, pr_number, reviewers (list[str])
    - Adds new reviewers (no duplicates) and aligns review_states/review_events.
    - Bumps PR updated_ts deterministically (max existing + 1 minute).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        pr_number: Any = None,
        reviewers: list[str] = None
    ) -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        pr_number_raw = pr_number
        reviewers_input = reviewers

        if (
            not owner
            or not repo_name
            or pr_number_raw is None
            or reviewers_input is None
        ):
            payload = {"error": "Required: owner, repo_name, pr_number, reviewers."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Normalize pr_number
        try:
            pr_number = int(pr_number_raw)
        except Exception:
            payload = {"error": "pr_number must be an integer."}
            out = json.dumps(payload, indent=2)
            return out

        # Validate reviewers list
        if not isinstance(reviewers_input, list) or any(
            (not isinstance(u, str) or not u.strip()) for u in reviewers_input
        ):
            payload = {"error": "reviewers must be a non-empty list of non-empty strings."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        reviewers_input = [
            u.strip() for u in reviewers_input if isinstance(u, str) and u.strip()
        ]
        if not reviewers_input:
            payload = {"error": "reviewers cannot be empty."}
            out = json.dumps(payload, indent=2)
            return out

        # Load PR DB (supports dict with 'pull_requests' or top-level list)
        pr_db = _convert_db_to_list(data.get("pull_requests", {}).values())

        if not isinstance(pr_db, list):
            payload = {"error": "Invalid pull requests DB: expected a list."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Find repo bucket
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

        # Ensure nested arrays exist and are properly shaped
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        rec.setdefault("updated_ts", [])
        rec.setdefault("created_ts", [])

        while len(rec["reviewers"]) <= idx:
            rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx:
            rec["review_states"].append([])
        while len(rec["review_events"]) <= idx:
            rec["review_events"].append([])
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)

        # Each PR keeps reviewers/states/events as a list of groups; ensure first group exists
        if not isinstance(rec["reviewers"][idx], list):
            rec["reviewers"][idx] = []
        if not isinstance(rec["review_states"][idx], list):
            rec["review_states"][idx] = []
        if not isinstance(rec["review_events"][idx], list):
            rec["review_events"][idx] = []

        if len(rec["reviewers"][idx]) == 0:
            rec["reviewers"][idx].append([])
        if len(rec["review_states"][idx]) == 0:
            rec["review_states"][idx].append([])
        if len(rec["review_events"][idx]) == 0:
            rec["review_events"][idx].append([])

        reviewers_list: list[str] = rec["reviewers"][idx][0]
        states_list: list[str] = rec["review_states"][idx][0]
        events_list: list[str] = rec["review_events"][idx][0]

        if not isinstance(reviewers_list, list):
            reviewers_list = []
            rec["reviewers"][idx][0] = reviewers_list
        if not isinstance(states_list, list):
            states_list = []
            rec["review_states"][idx][0] = states_list
        if not isinstance(events_list, list):
            events_list = []
            rec["review_events"][idx][0] = events_list

        added: list[str] = []
        skipped_existing: list[str] = []

        for user in reviewers_input:
            if user in reviewers_list:
                skipped_existing.append(user)
            else:
                reviewers_list.append(user)
                states_list.append("REQUESTED")  # initial state for new reviewer
                events_list.append("REQUESTED")
                added.append(user)

        # Deterministic updated_ts bump
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(
            data,
            f"Assigned reviewers to PR #{pr_number} for {owner}/{repo_name}.",
            get_current_updated_timestamp(),
        )
        payload = {
            "success": f"Assigned reviewers to PR #{pr_number} for {owner}/{repo_name}.",
            "repo": f"{owner}/{repo_name}",
            "pr_number": pr_number,
            "added_reviewers": added,
            "skipped_existing": skipped_existing,
            "total_reviewers": len(reviewers_list),
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
                "name": "AssignPullRequestReviewers",
                "description": "Assign reviewers to a pull request; aligns reviewers/states/events and bumps updated_ts deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name.",
                        },
                        "pr_number": {
                            "type": "integer",
                            "description": "Pull request number.",
                        },
                        "reviewers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of usernames to assign as reviewers.",
                        },
                    },
                    "required": ["owner", "repo_name", "pr_number", "reviewers"],
                },
            },
        }
