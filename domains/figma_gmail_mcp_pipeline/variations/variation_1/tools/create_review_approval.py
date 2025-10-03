from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateReviewApproval(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str,
        approval_comment_id: str = None,
        approver_email: str = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(cycle_id, str) or not cycle_id:
            payload = {"error": "cycle_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not approval_comment_id and not approver_email:
            payload = {"error": "Must provide either approval_comment_id or approver_email"}
            out = json.dumps(
                payload)
            return out
        review_approvals = data.get("review_approvals", [])
        next_num = len(review_approvals) + 1
        approval_id = f"approval_{next_num:03d}"
        approved_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
        #If a comment is given, attempt to retrieve approver_email from figma_comments
        if approval_comment_id:
            figma_comments = data.get("figma_comments", [])
            comment = next(
                (
                    c
                    for c in figma_comments
                    if c.get("comment_id") == approval_comment_id
                ),
                None,
            )
            if comment:
                approver_email = comment.get("commenter_email")
        new_approval = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts": approved_ts,
            "approval_comment_ref_nullable": approval_comment_id,
        }
        review_approvals.append(new_approval)
        payload = {"new_approval": new_approval}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewApproval",
                "description": "Create a new review approval for a cycle, using either a figma comment id or approver email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {
                            "type": "string",
                            "description": "The review cycle ID.",
                        },
                        "approval_comment_ref_nullable": {
                            "type": "string",
                            "description": "Optional figma comment ID for the approval.",
                        },
                        "approver_email": {
                            "type": "string",
                            "description": "Optional approver email if no comment is provided.",
                        },
                        "approved_ts": {
                            "type": "string",
                            "description": "Timestamp of approval (optional).",
                        },
                    },
                    "required": ["cycle_id"],
                },
            },
        }
