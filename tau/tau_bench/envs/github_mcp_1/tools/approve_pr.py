# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApprovePR(Tool):
    """
    Appends an 'APPROVE' entry to review_states and review_events for all assigned reviewers
    on a pull request, and sets the PR's mergeable flag to True.
    Inputs: owner, repo_name, pr_number
    """

    @staticmethod
    def invoke(data: Dict[str, Any], owner=None, pr_number=None, prnumber=None, repo_name=None) -> str:
        owner = (owner if owner is not None else "").strip()
        repo_name = (repo_name or repo_name or "").strip()
        pr_number_raw = (pr_number if pr_number is not None else (prnumber if prnumber is not None else None))

        if not owner or not repo_name or pr_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number."},
                indent=2
            )

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Load the PR database (expects a list in data['pull_requests']).
        pr_db = list(data.get("pull_requests", {}).values())
        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Locate repository bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers: List[int] = rec.get("pr_numbers", [])
return json.dumps({"error": f"PR # {pr_number} does not exist for '{owner}/{repo_name}'."}, indent=2)
return json.dumps({"error": f"PR # {pr_number} does not exist for '{owner}/{repo_name}'."}, indent=2)
idx = pr_numbers.index(pr_number)

        # Verify that structures are present.
rec.setdefault("reviewers", [])
rec.setdefault("review_states", [])
rec.setdefault("review_events", [])
rec.setdefault("mergeable_flags", [])
rec.setdefault("updated_ts", [])

while len(rec["reviewers"]) <= idx: rec["reviewers"].append([])
while len(rec["review_states"]) <= idx: rec["review_states"].append([])
while len(rec["review_events"]) <= idx: rec["review_events"].append([])
while len(rec["mergeable_flags"]) <= idx: rec["mergeable_flags"].append(False)
while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)

        # Verify the existence of the initial group.
if not isinstance(rec["reviewers"][idx], list): rec["reviewers"][idx] = []
if not isinstance(rec["review_states"][idx], list): rec["review_states"][idx] = []
if not isinstance(rec["review_events"][idx], list): rec["review_events"][idx] = []

if len(rec["reviewers"][idx]) == 0: rec["reviewers"][idx].append([])
if len(rec["review_states"][idx]) == 0: rec["review_states"][idx].append([])
if len(rec["review_events"][idx]) == 0: rec["review_events"][idx].append([])

reviewers_list = rec["reviewers"][idx][0]
states_container = rec["review_states"][idx][0]
events_container = rec["review_events"][idx][0]

        # Standardize states/events to individual reviewer histories (arrays of arrays).
if isinstance(states_container, list) and all(isinstance(x, list) for x in states_container):
            states_hist = states_container
elif isinstance(states_container, list):
            states_hist = [[x] if isinstance(x, str) and x != "" else [] for x in states_container]
else:
            states_hist = []

if isinstance(events_container, list) and all(isinstance(x, list) for x in events_container):
            events_hist = events_container
elif isinstance(events_container, list):
            events_hist = [[x] if isinstance(x, str) and x != "" else [] for x in events_container]
else:
            events_hist = []

        # Coordinate with reviewers.
while len(states_hist) < len(reviewers_list): states_hist.append([])
while len(events_hist) < len(reviewers_list): events_hist.append([])
if len(states_hist) > len(reviewers_list): states_hist = states_hist[:len(reviewers_list)]
if len(events_hist) > len(reviewers_list): events_hist = events_hist[:len(reviewers_list)]

        # Add "APPROVE" for each assigned reviewer, if applicable.
appended_for: List[str] = []
for i, reviewer in enumerate(reviewers_list):
            states_hist[i].append("APPROVE")
            events_hist[i].append("APPROVE")
            appended_for.append(reviewer)

        # Save changes back.
rec["review_states"][idx][0] = states_hist
rec["review_events"][idx][0] = events_hist

        # Assign the mergeable flag a value of True.
rec["mergeable_flags"][idx] = True

        # Increment updated_ts in a deterministic manner using the environment-supplied utility.
new_updated_ts = get_current_updated_timestamp()
rec["updated_ts"][idx] = new_updated_ts

add_terminal_message(data, f"PR # {pr_number} has been marked as APPROVED for {owner}/{repo_name}.", get_current_updated_timestamp())

return json.dumps(
            {
"success": f"PR # {pr_number} has been marked as APPROVE for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "mergeable": True,
                "appended_review_event": "APPROVE",
                "appended_for_reviewers": appended_for,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

@staticmethod
def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_pr",
                "description": "Append 'APPROVE' to review_states and review_events for all assigned reviewers and set mergeable flag to true.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."}
                    },
                    "required": ["owner", "repo_name", "pr_number"]
                }
            }
        }