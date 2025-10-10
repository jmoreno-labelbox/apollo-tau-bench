# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs["repo_name"]
        title = kwargs["title"]
        body = kwargs.get("body", "")
        head = kwargs["head"]
        base = kwargs["base"]

        me = _auth(data)["username"]
        repo = _find_repo_record(data, repo_name)
        # print("repooo:", repo)

        # Ensure pull request record exists
        pr_block = next(
            (b for b in _prs(data) if b.get("owner") == me and b.get("repo_name") == repo_name),
            None,
        )
        if not pr_block:
            # ✅ Create PR block if it doesn't exist
            pr_block = {
                "owner": me,
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
                "created_ts": [],
                "updated_ts": [],
                "pr_files": [],
                "pr_comments": [],
                "pr_comment_users": [],
                "reviewers": [],
                "review_states": [],
                "review_events": [],
            }
            _prs(data).append(pr_block)

        # Append PR metadata
        pr_number = 1
        pr_block["pr_numbers"].append(pr_number)
        pr_block["pr_titles"].append(title)
        pr_block["pr_bodies"].append(body)
        pr_block["pr_states"].append("open")
        pr_block["head_branches"].append(head)
        pr_block["base_branches"].append(base)
        pr_block["head_shas"].append("sha_0000000000000000000000000000000000000000")
        pr_block["mergeable_flags"].append(True)
        pr_block["merged_flags"].append(False)
        pr_block["created_ts"].append("2025-08-23T12:00:00Z")
        pr_block["updated_ts"].append("2025-08-23T12:00:00Z")

        # Detect changed files based on filenames and content
        try:
            head_idx = repo["branches"].index(head)
            base_idx = repo["branches"].index(base)
        except ValueError:
            return json.dumps({"error": "Invalid head or base branch."}, indent=2)

        head_files = set(repo["branch_files"][head_idx])
        base_files = set(repo["branch_files"][base_idx])
        file_diff = head_files.symmetric_difference(base_files)

        # Also check for content changes if filenames are same
        if not file_diff:
            file_diff = set()
            for path in repo["branch_files"][head_idx]:
                if path in repo["branch_files"][base_idx]:
                    head_i = next((i for i, p in enumerate(repo["branch_files"][head_idx]) if p == path), None)
                    base_i = next((i for i, p in enumerate(repo["branch_files"][base_idx]) if p == path), None)

                    if head_i is not None and base_i is not None:
                        if repo["branch_contents"][head_idx][head_i] != repo["branch_contents"][base_idx][base_i]:
                            file_diff.add(path)

                    if repo["branch_contents"][head_idx][head_i] != repo["branch_contents"][base_idx][base_i]:
                        file_diff.add(path)

        changed_files = sorted(list(file_diff))

        # Append changed file list as nested list (List[List[str]])
        if "pr_files" not in pr_block:
            pr_block["pr_files"] = []
        pr_block["pr_files"].append([changed_files])

        # Initialize empty nested structures for comments/reviews if needed
        pr_block.setdefault("pr_comments", []).append([[]])
        pr_block.setdefault("pr_comment_users", []).append([[]])
        pr_block.setdefault("reviewers", []).append([[]])
        pr_block.setdefault("review_states", []).append([[]])
        pr_block.setdefault("review_events", []).append([[]])

        return json.dumps({
            "message": "Pull request opened",
            "title": title,
            "base": base,
            "head": head,
            "pr_number": pr_number
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_pull_request",
                "description": "Creates a pull request from head to base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "base": {"type": "string"},
                        "head": {"type": "string"},
                    },
                    "required": ["repo_name", "title", "base", "head"]
                }
            }
        }
