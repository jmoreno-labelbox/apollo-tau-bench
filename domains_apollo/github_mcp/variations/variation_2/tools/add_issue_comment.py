from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class AddIssueComment(Tool):
    """Inserts a comment into an issue. Supports both aggregated blocks and flat issue rows."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, issue_number: int = None, comment: str = "") -> str:
        if not all([repo_name, issue_number is not None, comment is not None]):
            payload = {"error": "repo_name, issue_number, and comment are required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        target = int(issue_number)
        me = _auth(data)["username"]  #maintain consistency with CreateIssue

        #1) Aggregated blocks (original dataset structure)
        for block in _issues(data):
            if block.get("repo_name") != repo_name:
                continue

            nums = block.get("issue_numbers")
            if isinstance(nums, list) and target in nums:
                idx = nums.index(target)

                #Confirm that parallel lists are present and sufficiently lengthy
                if "issue_comments" not in block or not isinstance(
                    block["issue_comments"], list
                ):
                    block["issue_comments"] = [[] for _ in nums]
                while len(block["issue_comments"]) < len(nums):
                    block["issue_comments"].append([])

                block["issue_comments"][idx].append(comment)

                #Optionally monitor the comment user if the structure is available
                if "issue_comment_users" in block and isinstance(
                    block["issue_comment_users"], list
                ):
                    while len(block["issue_comment_users"]) < len(nums):
                        block["issue_comment_users"].append([])
                    block["issue_comment_users"][idx].append(me)

                #Refresh updated_ts if it exists (maintains dataset consistency)
                if "updated_ts" in block and isinstance(block["updated_ts"], list):
                    from datetime import datetime, timezone

                    iso = (
                        datetime.now(timezone.utc)
                        .isoformat(timespec="seconds")
                        .replace("+00:00", "Z")
                    )
                    if len(block["updated_ts"]) < len(nums):
                        block["updated_ts"] += [iso] * (
                            len(nums) - len(block["updated_ts"])
                        )
                    block["updated_ts"][idx] = iso
                payload = {"message": "Comment added."}
                out = json.dumps(payload, indent=2)
                return out

        #2) Flat issue rows (produced by CreateIssue)
        for row in _issues(data):
            if row.get("repo_name") == repo_name and row.get("number") == target:
                comments = row.get("comments")
                if not isinstance(comments, list):
                    comments = []
                comments.append(comment)
                row["comments"] = comments
                payload = {"message": "Comment added."}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Issue not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AddIssueComment",
                "description": "Adds a comment to an issue.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "issue_number": {"type": "integer"},
                        "comment": {"type": "string"},
                    },
                    "required": ["repo_name", "issue_number", "comment"],
                },
            },
        }
