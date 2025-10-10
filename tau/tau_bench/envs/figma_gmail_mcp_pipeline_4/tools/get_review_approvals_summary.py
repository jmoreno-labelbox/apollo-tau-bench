# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReviewApprovalsSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves review approvals with filtering and summary capabilities.
        """
        approval_id = kwargs.get('approval_id')
        cycle_id = kwargs.get('cycle_id')
        approver_id = kwargs.get('approver_id')
        approval_status = kwargs.get('approval_status')
        approved_after = kwargs.get('approved_after')
        approved_before = kwargs.get('approved_before')

        review_approvals = data.get('review_approvals', [])
        review_cycles = data.get('review_cycles', [])

        # Return the specific approval if an approval_id is given.
        if approval_id:
            for approval in review_approvals:
                if approval.get('approval_id') == approval_id:
                    # Add cycle-related data.
                    approval_copy = approval.copy()
                    cycle_id_ref = approval.get('cycle_id')
                    if cycle_id_ref:
                        for cycle in review_cycles:
                            if cycle.get('cycle_id') == cycle_id_ref:
                                approval_copy['review_cycle'] = cycle
                                break
                    return json.dumps(approval_copy, indent=2)
            return json.dumps({"error": f"Approval with ID '{approval_id}' not found."})

        # Apply criteria to filter approvals.
        results = []
        for approval in review_approvals:
            # Implement filters
            if cycle_id:
                if approval.get('cycle_id') != cycle_id:
                    continue

            if approver_id:
                if approval.get('approver_id') != approver_id:
                    continue

            if approval_status:
                if approval.get('status') != approval_status:
                    continue

            # Implement date constraints.
            if approved_after:
                approval_date = approval.get('approval_date', '')
                if approval_date < approved_after:
                    continue

            if approved_before:
                approval_date = approval.get('approval_date', '')
                if approval_date > approved_before:
                    continue

            # Augment with cycle details
            approval_copy = approval.copy()
            cycle_id_ref = approval.get('cycle_id')
            if cycle_id_ref:
                for cycle in review_cycles:
                    if cycle.get('cycle_id') == cycle_id_ref:
                        approval_copy['review_cycle'] = cycle
                        break

            results.append(approval_copy)

        # Generate a summary.
        summary = {
            "total_approvals": len(results),
            "by_status": {},
            "by_approver": {},
            "approvals": results
        }

        # Aggregate by status and approver.
        for approval in results:
            status = approval.get('status', 'UNKNOWN')
            if status not in summary["by_status"]:
                summary["by_status"][status] = 0
            summary["by_status"][status] += 1

            approver = approval.get('approver_id', 'unknown')
            if approver not in summary["by_approver"]:
                summary["by_approver"][approver] = 0
            summary["by_approver"][approver] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_review_approvals_summary",
                "description": "Retrieves review approvals with filtering and summary capabilities including status distribution and approver breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "approval_id": {"type": "string", "description": "The ID of a specific approval to retrieve."},
                        "cycle_id": {"type": "string", "description": "Filter approvals by review cycle ID."},
                        "approver_id": {"type": "string", "description": "Filter approvals by approver ID."},
                        "approval_status": {"type": "string", "description": "Filter approvals by status (e.g., 'APPROVED', 'REJECTED')."},
                        "approved_after": {"type": "string", "description": "Filter approvals made after this ISO timestamp."},
                        "approved_before": {"type": "string", "description": "Filter approvals made before this ISO timestamp."}
                    }
                }
            }
        }
