# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddPullRequestComment(Tool):
    """
    Adds a comment to a pull request for (owner, repo_name, pr_number).
    - Appends the comment to the first thread of the PR (creates it if missing).
    - Mirrors the comment author in pr_comment_users with the same indices.
    - Updates reviewer state/event for the comment_user:
        * Sets review_state to input value
        * Sets review_event to the same value
        * Adds the reviewer if not already present
    - Updates the PR's updated_ts (via get_current_updated_timestamp()).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))
        comment = (kwargs.get("comment") or kwargs.get("comment_body") or "").strip()
        comment_user = (kwargs.get("comment_user") or kwargs.get("user") or "").strip()
        review_state = (kwargs.get("review_state") or "").strip()

        if not owner or not repo_name or pr_number_raw is None or not comment or not comment_user or not review_state:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number, comment, comment_user, review_state."},
                indent=2
            )

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Load the PR database (anticipates a list in data['pull_requests']).
        pr_db = list(data.get("pull_requests", {}).values())
        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Locate repository bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers = rec.get("pr_numbers", [])
if pr_number not in pr_numbers:
return json.dumps({"error": f"PR # {pr_number} does not exist for '{owner}/{repo_name}'."}, indent=2)
        idx = pr_numbers.index(pr_number)

        # ---- Verify the existence of comments/users structures (thread 0) ----
        rec.setdefault("pr_comments", [])
        rec.setdefault("pr_comment_users", [])
        while len(rec["pr_comments"]) <= idx: rec["pr_comments"].append([])
        while len(rec["pr_comment_users"]) <= idx: rec["pr_comment_users"].append([])

        if not isinstance(rec["pr_comments"][idx], list): rec["pr_comments"][idx] = []
        if not isinstance(rec["pr_comment_users"][idx], list): rec["pr_comment_users"][idx] = []

        if len(rec["pr_comments"][idx]) == 0: rec["pr_comments"][idx].append([])
        if len(rec["pr_comment_users"][idx]) == 0: rec["pr_comment_users"][idx].append([])

        thread_idx = 0
        comments_thread = rec["pr_comments"][idx][thread_idx]
        users_thread = rec["pr_comment_users"][idx][thread_idx]
        if not isinstance(comments_thread, list):
            comments_thread = []
            rec["pr_comments"][idx][thread_idx] = comments_thread
        if not isinstance(users_thread, list):
            users_thread = []
            rec["pr_comment_users"][idx][thread_idx] = users_thread

        comments_thread.append(comment)
        users_thread.append(comment_user)
        comment_index = len(comments_thread) - 1

        # ---- Verify the existence of reviewers/state/event structures (group 0) ----
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        while len(rec["reviewers"]) <= idx: rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx: rec["review_states"].append([])
        while len(rec["review_events"]) <= idx: rec["review_events"].append([])

        if not isinstance(rec["reviewers"][idx], list): rec["reviewers"][idx] = []
        if not isinstance(rec["review_states"][idx], list): rec["review_states"][idx] = []
        if not isinstance(rec["review_events"][idx], list): rec["review_events"][idx] = []

        if len(rec["reviewers"][idx]) == 0: rec["reviewers"][idx].append([])
        if len(rec["review_states"][idx]) == 0: rec["review_states"][idx].append([])
        if len(rec["review_events"][idx]) == 0: rec["review_events"][idx].append([])

        reviewers_list = rec["reviewers"][idx][0]
        states_container = rec["review_states"][idx][0]
        events_container = rec["review_events"][idx][0]

        # ---- Standardize to individual reviewer histories (arrays of arrays) ----
        # list_of_reviewers: List[str]
        # states_hist: List of List of strings, events_hist: List of List of strings
        if not isinstance(reviewers_list, list):
            reviewers_list = []
        # Statuses
        if isinstance(states_container, list) and all(isinstance(x, list) for x in states_container):
            states_hist = states_container
        elif isinstance(states_container, list):
            # previous format: individual strings per reviewer
            states_hist = [[x] if isinstance(x, str) and x != "" else [] for x in states_container]
        else:
            states_hist = []
        # Event handling
        if isinstance(events_container, list) and all(isinstance(x, list) for x in events_container):
            events_hist = events_container
        elif isinstance(events_container, list):
            events_hist = [[x] if isinstance(x, str) and x != "" else [] for x in events_container]
        else:
            events_hist = []

        # Coordinate lengths with reviewers.
        while len(states_hist) < len(reviewers_list): states_hist.append([])
        while len(events_hist) < len(reviewers_list): events_hist.append([])
        if len(states_hist) > len(reviewers_list): states_hist = states_hist[:len(reviewers_list)]
        if len(events_hist) > len(reviewers_list): events_hist = events_hist[:len(reviewers_list)]

        # Verify the existence of the reviewer; then ADD review_state/event.
        if comment_user in reviewers_list:
            ridx = reviewers_list.index(comment_user)
        else:
            reviewers_list.append(comment_user)
            states_hist.append([])
            events_hist.append([])
            ridx = len(reviewers_list) - 1

        states_hist[ridx].append(review_state)
        events_hist[ridx].append(review_state)  # event reflects state

        # Save changes.
        rec["reviewers"][idx][0] = reviewers_list
        rec["review_states"][idx][0] = states_hist
        rec["review_events"][idx][0] = events_hist

        # ---- Update updated_ts in a deterministic manner using the environment helper ----
        rec.setdefault("updated_ts", [])
        while len(rec["updated_ts"]) <= idx: rec["updated_ts"].append(None)
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"Comment added to PR # Appending review state/event for {owner}/{repo_name} with {pr_number}; current timestamp updated.

        return json.dumps(
            {
                "success": f"Comment added to PR # Added review state/event for {owner}/{repo_name} in {pr_number}.
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "thread_index": thread_idx,
                "comment_index": comment_index,
                "comment": comment,
                "comment_user": comment_user,
                "appended_review_state": review_state,
                "appended_review_event": review_state,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_pull_request_comment",
                "description": "Add a PR comment and set the comment_user's review_state and review_event (event mirrors state); bumps updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."},
                        "comment": {"type": "string", "description": "Comment text to add."},
                        "comment_user": {"type": "string", "description": "Username of the commenter (reviewer)."},
                        "review_state": {"type": "string", "description": "New review state; review_event will match this value."}
                    },
                    "required": ["owner", "repo_name", "pr_number", "comment", "comment_user", "review_state"]
                }
            }
        }