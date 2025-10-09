from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ApprovePR(Tool):
    """
    Appends an 'APPROVE' entry to review_states and review_events for all assigned reviewers
    on a pull request, and sets the PR's mergeable flag to True.
    Inputs: owner, repo_name, pr_number
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "", pr_number: Any = None) -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        pr_number_raw = pr_number

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

        #Load PR DB (expects list at data['pull_requests'])
        pr_db = _convert_db_to_list(data.get("pull_requests", {}))
        if not isinstance(pr_db, list):
            payload = {"error": "Invalid pull requests DB: expected a list."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Find repo bucket
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

        #Ensure structures exist
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("updated_ts", [])

        while len(rec["reviewers"]) <= idx:
            rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx:
            rec["review_states"].append([])
        while len(rec["review_events"]) <= idx:
            rec["review_events"].append([])
        while len(rec["mergeable_flags"]) <= idx:
            rec["mergeable_flags"].append(False)
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)

        #Ensure first group exists
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
        states_container = rec["review_states"][idx][0]
        events_container = rec["review_events"][idx][0]

        #Normalize states/events to per-reviewer histories (lists of lists)
        if isinstance(states_container, list) and all(
            isinstance(x, list) for x in states_container
        ):
            states_hist = states_container
        elif isinstance(states_container, list):
            states_hist = [
                [x] if isinstance(x, str) and x != "" else [] for x in states_container
            ]
        else:
            states_hist = []

        if isinstance(events_container, list) and all(
            isinstance(x, list) for x in events_container
        ):
            events_hist = events_container
        elif isinstance(events_container, list):
            events_hist = [
                [x] if isinstance(x, str) and x != "" else [] for x in events_container
            ]
        else:
            events_hist = []

        #Align with reviewers
        while len(states_hist) < len(reviewers_list):
            states_hist.append([])
        while len(events_hist) < len(reviewers_list):
            events_hist.append([])
        if len(states_hist) > len(reviewers_list):
            states_hist = states_hist[: len(reviewers_list)]
        if len(events_hist) > len(reviewers_list):
            events_hist = events_hist[: len(reviewers_list)]

        #Append "APPROVE" for all assigned reviewers (if any)
        appended_for: list[str] = []
        for i, reviewer in enumerate(reviewers_list):
            states_hist[i].append("APPROVE")
            events_hist[i].append("APPROVE")
            appended_for.append(reviewer)

        #Persist back
        rec["review_states"][idx][0] = states_hist
        rec["review_events"][idx][0] = events_hist

        #Set mergeable flag to True
        rec["mergeable_flags"][idx] = True

        #Bump updated_ts deterministically (env-provided helper)
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(
            data,
            f"PR #{pr_number} marked APPROVE for {owner}/{repo_name}.",
            get_current_updated_timestamp(),
        )
        payload = {
                "success": f"PR #{pr_number} marked APPROVE for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "mergeable": True,
                "appended_review_event": "APPROVE",
                "appended_for_reviewers": appended_for,
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
                "name": "ApprovePr",
                "description": "Append 'APPROVE' to review_states and review_events for all assigned reviewers and set mergeable flag to true.",
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
                    },
                    "required": ["owner", "repo_name", "pr_number"],
                },
            },
        }
