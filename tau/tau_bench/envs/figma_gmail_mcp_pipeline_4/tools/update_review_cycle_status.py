# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReviewCycleStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], approver_id, cycle_id, new_status, comments = '') -> str:
        """
        Updates the status of a review cycle and handles status transitions.
        """

        if not all([cycle_id, new_status]):
            return json.dumps({"error": "cycle_id and new_status are required."})

        # Check the validity of status values.
        valid_statuses = ['IN_FLIGHT', 'NEEDS_REVIEW', 'APPROVED', 'CHANGES_REQUESTED', 'ESCALATED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        review_cycles = data.get('review_cycles', [])
        review_approvals = data.get('review_approvals', [])

        # Identify the review process.
        cycle_found = False
        for cycle in review_cycles:
            if cycle.get('cycle_id') == cycle_id:
                cycle_found = True
                old_status = cycle.get('status')

                # Revise the status of the cycle.
                cycle['status'] = new_status
                cycle['last_updated'] = datetime.now().isoformat()

                # Manage logic based on status conditions.
                if new_status == 'APPROVED' and approver_id:
                    # Generate approval entry
                    approval_id = f"approval_{uuid.uuid4().hex[:8]}"
                    new_approval = {
                        "approval_id": approval_id,
                        "cycle_id": cycle_id,
                        "approver_id": approver_id,
                        "approval_date": datetime.now().isoformat(),
                        "comments": comments,
                        "status": "APPROVED"
                    }
                    review_approvals.append(new_approval)

                elif new_status == 'CHANGES_REQUESTED' and comments:
                    # Incorporate modification request into comments.
                    if 'change_requests' not in cycle:
                        cycle['change_requests'] = []
                    cycle['change_requests'].append({
                        "request_id": f"req_{uuid.uuid4().hex[:8]}",
                        "requester_id": approver_id,
                        "request_date": datetime.now().isoformat(),
                        "comments": comments
                    })

                # Record the change in status.
                if 'status_history' not in cycle:
                    cycle['status_history'] = []
                cycle['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_by": approver_id,
                    "changed_at": datetime.now().isoformat(),
                    "comments": comments
                })

                break

        if not cycle_found:
            return json.dumps({"error": f"Review cycle with ID '{cycle_id}' not found."})

        return json.dumps({
            "success": True,
            "cycle_id": cycle_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_review_cycle_status",
                "description": "Updates the status of a design review cycle and handles status transitions including approvals and change requests.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string", "description": "The ID of the review cycle to update."},
                        "new_status": {"type": "string", "description": "The new status for the review cycle. Must be one of: IN_FLIGHT, NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED."},
                        "approver_id": {"type": "string", "description": "The ID of the person making the status change."},
                        "comments": {"type": "string", "description": "Optional comments about the status change or change request."}
                    },
                    "required": ["cycle_id", "new_status"]
                }
            }
        }
