# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddIssueComment(Tool):
    """Adds a comment to an issue. Supports both aggregated blocks and flat issue rows."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        issue_number = kwargs.get("issue_number")
        comment = kwargs.get("comment", "")

        if not all([repo_name, issue_number is not None, comment is not None]):
            return json.dumps({"error": "repo_name, issue_number, and comment are required."}, indent=2)

        target = int(issue_number)
        me = _auth(data)["username"]  # keep parity with CreateIssue

        # 1) Aggregated blocks (original dataset shape)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue

            nums = block.get("issue_numbers")
            if isinstance(nums, list) and target in nums:
                idx = nums.index(target)

                # Ensure parallel lists exist and are long enough
                if "issue_comments" not in block or not isinstance(block["issue_comments"], list):
                    block["issue_comments"] = [[] for _ in nums]
                while len(block["issue_comments"]) < len(nums):
                    block["issue_comments"].append([])

                block["issue_comments"][idx].append(comment)

                # Optionally track comment user if the structure exists
                if "issue_comment_users" in block and isinstance(block["issue_comment_users"], list):
                    while len(block["issue_comment_users"]) < len(nums):
                        block["issue_comment_users"].append([])
                    block["issue_comment_users"][idx].append(me)

                # Update updated_ts if present (keeps dataset consistent)
                if "updated_ts" in block and isinstance(block["updated_ts"], list):
                    from datetime import datetime, timezone
                    iso = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
                    if len(block["updated_ts"]) < len(nums):
                        block["updated_ts"] += [iso] * (len(nums) - len(block["updated_ts"]))
                    block["updated_ts"][idx] = iso

                return json.dumps({"message": "Comment added."}, indent=2)

        # 2) Flat issue rows (created by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                comments = row.get("comments")
                if not isinstance(comments, list):
                    comments = []
                comments.append(comment)
                row["comments"] = comments
                # keep a lightweight timestamp here too, if you want
                return json.dumps({"message": "Comment added."}, indent=2)

        return json.dumps({"error": "Issue not found."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "add_issue_comment",
                "description": "Adds a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "comment"]
                }
            }
        }
