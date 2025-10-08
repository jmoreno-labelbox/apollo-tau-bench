from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateReviewCycleStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, new_status: str = None, approver_id: str = None, comments: str = "", reviewer_email: str = None, status_notes: str = None, completion_notes: str = None, updated_by: str = None) -> str:
        # Support reviewer_email as alternative to approver_id
        if reviewer_email is not None:
            approver_id = reviewer_email
        # Support status_notes or completion_notes as alternative to comments
        if status_notes is not None:
            comments = status_notes
        if completion_notes is not None:
            comments = completion_notes
        # Support updated_by as alternative to approver_id
        if updated_by is not None:
            approver_id = updated_by
        """
        Modifies the status of a review cycle and manages status transitions.
        """
        if not all([cycle_id, new_status]):
            payload = {"error": "cycle_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = [
            "IN_FLIGHT",
            "NEEDS_REVIEW",
            "APPROVED",
            "CHANGES_REQUESTED",
            "ESCALATED",
        ]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        review_cycles = data.get("review_cycles", [])
        review_approvals = data.get("review_approvals", [])

        # Locate the review cycle
        cycle_found = False
        for cycle in review_cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle_found = True
                old_status = cycle.get("status")

                # Modify the status of the cycle
                cycle["status"] = new_status
                cycle["last_updated"] = datetime.now().isoformat()

                # Manage logic based on status
                if new_status == "APPROVED" and approver_id:
                    # Generate an approval record
                    approval_id = f"approval_{uuid.uuid4().hex[:8]}"
                    new_approval = {
                        "approval_id": approval_id,
                        "cycle_id": cycle_id,
                        "approver_id": approver_id,
                        "approval_date": datetime.now().isoformat(),
                        "comments": comments,
                        "status": "APPROVED",
                    }
                    review_approvals.append(new_approval)

                elif new_status == "CHANGES_REQUESTED" and comments:
                    # Include change request in comments
                    if "change_requests" not in cycle:
                        cycle["change_requests"] = []
                    cycle["change_requests"].append(
                        {
                            "request_id": f"req_{uuid.uuid4().hex[:8]}",
                            "requester_id": approver_id,
                            "request_date": datetime.now().isoformat(),
                            "comments": comments,
                        }
                    )

                # Record the change in status
                if "status_history" not in cycle:
                    cycle["status_history"] = []
                cycle["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_by": approver_id,
                        "changed_at": datetime.now().isoformat(),
                        "comments": comments,
                    }
                )

                break

        if not cycle_found:
            payload = {"error": f"Review cycle with ID '{cycle_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "cycle_id": cycle_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Updates the status of a design review cycle and handles status transitions including approvals and change requests.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {
                            "type": "string",
                            "description": "The ID of the review cycle to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the review cycle. Must be one of: IN_FLIGHT, NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED.",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "The ID of the person making the status change.",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Optional comments about the status change or change request.",
                        },
                    },
                    "required": ["cycle_id", "new_status"],
                },
            },
        }
