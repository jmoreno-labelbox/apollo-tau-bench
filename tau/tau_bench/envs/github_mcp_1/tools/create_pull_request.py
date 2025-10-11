# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequest(Tool):
    """
    Creates a new pull request entry.
    Inputs: owner, repo_name, pr_title, pr_body, head_branch_name, base_branch_name, head_sha, pr_files
    Behavior:
      - Creates/locates the repo record in the PR DB.
      - Appends aligned fields (titles, bodies, states, branches, shas, flags, files, comments, reviewers, timestamps).
      - PR number = max(all pr_numbers) + 1 (global uniqueness).
      - created_ts/updated_ts = deterministic next timestamp.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], base_branch=None, base_branch_name=None, head_branch=None, head_branch_name=None, head_sha=None, head_sha_value=None, owner=None, pr_body=None, pr_files=None, pr_titile=None, pr_title=None, repo_name=None) -> str:
        owner = (owner if owner is not None else "").strip()
        repo_name = (repo_name or repo_name or "").strip()
        pr_title = (pr_title or pr_titile or "").strip()
        pr_body = (pr_body or "").strip()
        head_branch_name = (head_branch_name or head_branch or "").strip()
        base_branch_name = (base_branch_name or base_branch or "").strip()
        head_sha = (head_sha or head_sha_value or "").strip()
        pr_files_input = (pr_files if pr_files is not None else [])

        if not owner or not repo_name or not pr_title or not head_branch_name or not base_branch_name or not head_sha:
            return json.dumps({
                "error": "Required: owner, repo_name, pr_title, head_branch_name, base_branch_name, head_sha."
            }, indent=2)

        if not isinstance(pr_files_input, list) or not all(isinstance(x, str) for x in pr_files_input):
            return json.dumps({"error": "pr_files must be a list of filenames (strings)."}, indent=2)

        # Load the PR database (accepts a dictionary with 'pull_requests' or a top-level list).
        pr_db = list(data.get("pull_requests", {}).values())


        # Locate or establish a repository bucket.
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            rec = {
                "owner": owner,
                "repo_name": repo_name,
                "pr_numbers": [],
                "pr_titles": [],
                "pr_bodies": [],
                "pr_states": [],
                "head_branches": [],
                "base_branches": [],
                "head_shas": [],
                "mergeable_flags": [],
                "merged_flags": [],
                "pr_files": [],
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
                "created_ts": [],
                "updated_ts": []
            }
            pr_db.append(rec)

        # Fixed numbers and time indicators
        new_pr_number = get_next_pr_number(data)
        new_ts = get_current_timestamp()

        # Verify the presence of arrays.
        rec.setdefault("pr_numbers", [])
        rec.setdefault("pr_titles", [])
        rec.setdefault("pr_bodies", [])
        rec.setdefault("pr_states", [])
        rec.setdefault("head_branches", [])
        rec.setdefault("base_branches", [])
        rec.setdefault("head_shas", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("merged_flags", [])
        rec.setdefault("pr_files", [])
        rec.setdefault("pr_comments", [])
        rec.setdefault("pr_comment_users", [])
        rec.setdefault("reviewers", [])
        rec.setdefault("review_states", [])
        rec.setdefault("review_events", [])
        rec.setdefault("created_ts", [])
        rec.setdefault("updated_ts", [])

        # Add aligned fields.
        rec["pr_numbers"].append(new_pr_number)
        rec["pr_titles"].append(pr_title)
        rec["pr_bodies"].append(pr_body)
        rec["pr_states"].append("open")
        rec["head_branches"].append(head_branch_name)
        rec["base_branches"].append(base_branch_name)
        rec["head_shas"].append(head_sha)
        rec["mergeable_flags"].append(True)
        rec["merged_flags"].append(False)

        # The database structure requires a nested list format for each PR: [ [ "fileA", "fileB" ] ].
        rec["pr_files"].append([list(pr_files_input)])

        # Blank placeholders for feedback/reviews (align nested structures)
        rec["pr_comments"].append([[]])
        rec["pr_comment_users"].append([[]])
        rec["reviewers"].append([[]])
        rec["review_states"].append([[]])
        rec["review_events"].append([[]])

        rec["created_ts"].append(new_ts)
        rec["updated_ts"].append(new_ts)

        add_terminal_message(data, f"Pull request # A new pull request number {new_pr_number} has been generated for {owner}/{repo_name}.", get_current_timestamp())

        return json.dumps({
"success": f"Pull request # A new pull request number {new_pr_number} has been generated for the repository {owner}/{repo_name}.",
            "pull_request": {
                "number": new_pr_number,
                "title": pr_title,
                "body": pr_body,
                "state": "open",
                "base": base_branch_name,
                "head": head_branch_name,
                "head_sha": head_sha,
                "files": pr_files_input,
                "created_ts": new_ts,
                "updated_ts": new_ts
            }
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request",
                "description": "Create a new pull request entry with deterministic PR number and timestamps; creates repo bucket if needed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_title": {"type": "string", "description": "Pull request title."},
                        "pr_body": {"type": "string", "description": "Pull request description/body."},
                        "head_branch_name": {"type": "string", "description": "Source (head) branch name."},
                        "base_branch_name": {"type": "string", "description": "Target (base) branch name."},
                        "head_sha": {"type": "string", "description": "Head commit SHA for the PR."},
                        "pr_files": {"type": "array", "items": {"type": "string"}, "description": "List of file paths included in the PR."}
                    },
                    "required": ["owner", "repo_name", "pr_title", "pr_body", "head_branch_name", "base_branch_name", "head_sha", "pr_files"]
                }
            }
        }