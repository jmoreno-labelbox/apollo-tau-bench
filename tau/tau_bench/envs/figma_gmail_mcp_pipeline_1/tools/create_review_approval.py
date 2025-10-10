# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateReviewApproval(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cycle_id: str,
        approval_comment_id: str = None,
        approver_email: str = None,
    ) -> str:
        # Validate input
        if not isinstance(cycle_id, str) or not cycle_id:
            return json.dumps({"error": "cycle_id must be a non-empty string"})
        if not approval_comment_id and not approver_email:
            return json.dumps({"error": "Must provide either approval_comment_id or approver_email"})
        review_approvals = data.get("review_approvals", [])
        next_num = len(review_approvals) + 1
        approval_id = f"approval_{next_num:03d}"
        approved_ts = "2025-08-26T12:00:00Z"  # Use current date/time in production
        # If comment is provided, try to get approver_email from figma_comments
        if approval_comment_id:
            figma_comments = data.get("figma_comments", [])
            comment = next((c for c in figma_comments if c.get("comment_id") == approval_comment_id), None)
            if comment:
                approver_email = comment.get("commenter_email")
        new_approval = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts": approved_ts,
            "approval_comment_ref_nullable": approval_comment_id
        }
        review_approvals.append(new_approval)
        return json.dumps({"new_approval": new_approval})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_review_approval",
                "description": "Create a new review approval for a cycle, using either a figma comment id or approver email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string", "description": "The review cycle ID."},
                        "approval_comment_ref_nullable": {"type": "string", "description": "Optional figma comment ID for the approval."},
                        "approver_email": {"type": "string", "description": "Optional approver email if no comment is provided."},
                        "approved_ts": {"type": "string", "description": "Timestamp of approval (optional)."}
                    },
                    "required": ["cycle_id"]
                }
            }
        }
