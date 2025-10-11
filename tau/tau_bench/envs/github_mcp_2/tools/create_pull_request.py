# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePullRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], base, head, repo_name, title, body = "") -> str:

        me = _auth(data)["username"]
        repo = _find_repo_record(data, repo_name)
        # print("repository:", repo)

        # Verify that a pull request entry is present.
        pr_block = next(
            (b for b in _prs(data) if b.get("owner") == me and b.get("repo_name") == repo_name),
            None,
        )
        if not pr_block:
            # ✅ Generate PR block if absent
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

        # Add pull request metadata
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

        # Identify modified files by analyzing both their names and content.
        try:
            head_idx = repo["branches"].index(head)
            base_idx = repo["branches"].index(base)
        except ValueError:
            return json.dumps({"error": "Invalid head or base branch."}, indent=2)

        head_files = set(repo["branch_files"][head_idx])
        base_files = set(repo["branch_files"][base_idx])
        file_diff = head_files.symmetric_difference(base_files)

        # Additionally, verify for content modifications when the filenames match.
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

        # Add modified file list as a nested structure (List[List[str]])
        if "pr_files" not in pr_block:
            pr_block["pr_files"] = []
        pr_block["pr_files"].append([changed_files])

        # Set up empty nested structures for comments/reviews if required.
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
