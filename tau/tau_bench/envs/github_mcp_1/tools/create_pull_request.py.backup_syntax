from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        pr_title: str = "",
        pr_body: str = "",
        head_branch_name: str = "",
        base_branch_name: str = "",
        head_sha: str = "",
        pr_files: list[str] = None,
    ) -> str:
        if pr_files is None:
            pr_files = []

        owner = owner.strip()
        repo_name = repo_name.strip()
        pr_title = pr_title.strip()
        pr_body = pr_body.strip()
        head_branch_name = head_branch_name.strip()
        base_branch_name = base_branch_name.strip()
        head_sha = head_sha.strip()

        if (
            not owner
            or not repo_name
            or not pr_title
            or not head_branch_name
            or not base_branch_name
            or not head_sha
        ):
            payload = {
                "error": "Required: owner, repo_name, pr_title, head_branch_name, base_branch_name, head_sha."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if not isinstance(pr_files, list) or not all(
            isinstance(x, str) for x in pr_files
        ):
            payload = {"error": "pr_files must be a list of filenames (strings)."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Load PR DB (supports dict with 'pull_requests' or top-level list)
        pr_db = _convert_db_to_list(data.get("pull_requests", {}).values()

        # Find or create repo bucket
        rec = next(
            (
                r
                for r in pr_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
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
                "updated_ts": [],
            }
            pr_db.append(rec)

        # Deterministic number & timestamps
        new_pr_number = get_next_pr_number(data)
        new_ts = get_current_timestamp()

        # Ensure arrays exist
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

        # Append aligned fields
        rec["pr_numbers"].append(new_pr_number)
        rec["pr_titles"].append(pr_title)
        rec["pr_bodies"].append(pr_body)
        rec["pr_states"].append("open")
        rec["head_branches"].append(head_branch_name)
        rec["base_branches"].append(base_branch_name)
        rec["head_shas"].append(head_sha)
        rec["mergeable_flags"].append(True)
        rec["merged_flags"].append(False)

        # DB shape expects a nested list per PR: [ [ "fileA", "fileB" ] ]
        rec["pr_files"].append([list(pr_files)])

        # Empty placeholders for comments/reviews (match nested shapes)
        rec["pr_comments"].append([[]])
        rec["pr_comment_users"].append([[]])
        rec["reviewers"].append([[]])
        rec["review_states"].append([[]])
        rec["review_events"].append([[]])

        rec["created_ts"].append(new_ts)
        rec["updated_ts"].append(new_ts)

        add_terminal_message(
            data,
            f"Pull request #{new_pr_number} created for {owner}/{repo_name}.",
            get_current_timestamp(),
        )
        payload = {
            "success": f"Pull request #{new_pr_number} created for {owner}/{repo_name}.",
            "pull_request": {
                "number": new_pr_number,
                "title": pr_title,
                "body": pr_body,
                "state": "open",
                "base": base_branch_name,
                "head": head_branch_name,
                "head_sha": head_sha,
                "files": pr_files,
                "created_ts": new_ts,
                "updated_ts": new_ts,
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
                "name": "CreatePullRequest",
                "description": "Create a new pull request entry with deterministic PR number and timestamps; creates repo bucket if needed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name.",
                        },
                        "pr_title": {
                            "type": "string",
                            "description": "Pull request title.",
                        },
                        "pr_body": {
                            "type": "string",
                            "description": "Pull request description/body.",
                        },
                        "head_branch_name": {
                            "type": "string",
                            "description": "Source (head) branch name.",
                        },
                        "base_branch_name": {
                            "type": "string",
                            "description": "Target (base) branch name.",
                        },
                        "head_sha": {
                            "type": "string",
                            "description": "Head commit SHA for the PR.",
                        },
                        "pr_files": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of file paths included in the PR.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "pr_title",
                        "pr_body",
                        "head_branch_name",
                        "base_branch_name",
                        "head_sha",
                        "pr_files",
                    ],
                },
            },
        }
