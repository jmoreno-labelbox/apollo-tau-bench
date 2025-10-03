from tau_bench.envs.tool import Tool
import json
from typing import Any

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
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        pr_number: str = None,
        comment: str = "",
        comment_user: str = "",
        review_state: str = ""
    ) -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        pr_number_raw = pr_number
        comment = comment.strip()
        comment_user = comment_user.strip()
        review_state = review_state.strip()

        if (
            not owner
            or not repo_name
            or pr_number_raw is None
            or not comment
            or not comment_user
            or not review_state
        ):
            payload = {
                    "error": "Required: owner, repo_name, pr_number, comment, comment_user, review_state."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            payload = {"error": "pr_number must be an integer."}
            out = json.dumps(payload, indent=2)
            return out

        #Load PR DB (expects list at data['pull_requests'])
        pr_db = data.get("pull_requests", [])
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

        pr_numbers = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            payload = {"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        idx = pr_numbers.index(pr_number)

        #---- Ensure comments/users structures exist (thread 0) ----
        rec.setdefault("pr_comments", [])
        rec.setdefault("pr_comment_users", [])
        while len(rec["pr_comments"]) <= idx:
            rec["pr_comments"].append([])
        while len(rec["pr_comment_users"]) <= idx:
            rec["pr_comment_users"].append([])

        if not isinstance(rec["pr_comments"][idx], list):
            rec["pr_comments"][idx] = []
        if not isinstance(rec["pr_comment_users"][idx], list):
            rec["pr_comment_users"][idx] = []

        if len(rec["pr_comments"][idx]) == 0:
            rec["pr_comments"][idx].append([])
        if len(rec["pr_comment_users"][idx]) == 0:
            rec["pr_comment_users"][idx].append([])

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

        #---- Ensure reviewers/state/event structures exist (group 0) ----
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        while len(rec["reviewers"]) <= idx:
            rec["reviewers"].append([])
        while len(rec["review_states"]) <= idx:
            rec["review_states"].append([])
        while len(rec["review_events"]) <= idx:
            rec["review_events"].append([])

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

        reviewers_list = rec["reviewers"][idx][0]
        states_container = rec["review_states"][idx][0]
        events_container = rec["review_events"][idx][0]

        #---- Normalize to per-reviewer histories (lists of lists) ----
        #reviewers_list: List[str]
        #states_hist: List[List[str]], events_hist: List[List[str]]
        if not isinstance(reviewers_list, list):
            reviewers_list = []
        #States
        if isinstance(states_container, list) and all(
            isinstance(x, list) for x in states_container
        ):
            states_hist = states_container
        elif isinstance(states_container, list):
            #old shape: per-reviewer single strings
            states_hist = [
                [x] if isinstance(x, str) and x != "" else [] for x in states_container
            ]
        else:
            states_hist = []
        #Events
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

        #Align lengths with reviewers
        while len(states_hist) < len(reviewers_list):
            states_hist.append([])
        while len(events_hist) < len(reviewers_list):
            events_hist.append([])
        if len(states_hist) > len(reviewers_list):
            states_hist = states_hist[: len(reviewers_list)]
        if len(events_hist) > len(reviewers_list):
            events_hist = events_hist[: len(reviewers_list)]

        #Ensure reviewer exists; then APPEND review_state/event
        if comment_user in reviewers_list:
            ridx = reviewers_list.index(comment_user)
        else:
            reviewers_list.append(comment_user)
            states_hist.append([])
            events_hist.append([])
            ridx = len(reviewers_list) - 1

        states_hist[ridx].append(review_state)
        events_hist[ridx].append(review_state)  #event mirrors state

        #Persist back
        rec["reviewers"][idx][0] = reviewers_list
        rec["review_states"][idx][0] = states_hist
        rec["review_events"][idx][0] = events_hist

        #---- Bump updated_ts deterministically via env helper ----
        rec.setdefault("updated_ts", [])
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(
            data,
            f"Comment added to PR #{pr_number} for {owner}/{repo_name}; review state/event appended.",
            get_current_updated_timestamp(),
        )
        payload = {
                "success": f"Comment added to PR #{pr_number} for {owner}/{repo_name}; review state/event appended.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "thread_index": thread_idx,
                "comment_index": comment_index,
                "comment": comment,
                "comment_user": comment_user,
                "appended_review_state": review_state,
                "appended_review_event": review_state,
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
                "name": "AddPullRequestComment",
                "description": "Add a PR comment and set the comment_user's review_state and review_event (event mirrors state); bumps updated_ts.",
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
                        "comment": {
                            "type": "string",
                            "description": "Comment text to add.",
                        },
                        "comment_user": {
                            "type": "string",
                            "description": "Username of the commenter (reviewer).",
                        },
                        "review_state": {
                            "type": "string",
                            "description": "New review state; review_event will match this value.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "pr_number",
                        "comment",
                        "comment_user",
                        "review_state",
                    ],
                },
            },
        }
