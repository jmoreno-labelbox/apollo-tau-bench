from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetReviewApprovalsSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        approval_id: str = None,
        cycle_id: str = None,
        approver_id: str = None,
        approval_status: str = None,
        approved_after: str = None,
        approved_before: str = None
    ) -> str:
        """
        Obtains review approvals with filtering and summarization features.
        """
        review_approvals = data.get("review_approvals", {}).values()
        review_cycles = data.get("review_cycles", {}).values()

        # Return the specific approval if approval_id is given
        if approval_id:
            for approval in review_approvals.values():
                if approval.get("approval_id") == approval_id:
                    # Enhance with details from the cycle
                    approval_copy = approval.copy()
                    cycle_id_ref = approval.get("cycle_id")
                    if cycle_id_ref:
                        for cycle in review_cycles.values():
                            if cycle.get("cycle_id") == cycle_id_ref:
                                approval_copy["review_cycle"] = cycle
                                break
                    payload = approval_copy
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Approval with ID '{approval_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort approvals based on specified criteria
        results = []
        for approval in review_approvals.values():
            # Implement filters
            if cycle_id:
                if approval.get("cycle_id") != cycle_id:
                    continue

            if approver_id:
                if approval.get("approver_id") != approver_id:
                    continue

            if approval_status:
                if approval.get("status") != approval_status:
                    continue

            # Enforce date filters
            if approved_after:
                approval_date = approval.get("approval_date", "")
                if approval_date < approved_after:
                    continue

            if approved_before:
                approval_date = approval.get("approval_date", "")
                if approval_date > approved_before:
                    continue

            # Enhance with details from the cycle
            approval_copy = approval.copy()
            cycle_id_ref = approval.get("cycle_id")
            if cycle_id_ref:
                for cycle in review_cycles.values():
                    if cycle.get("cycle_id") == cycle_id_ref:
                        approval_copy["review_cycle"] = cycle
                        break

            results.append(approval_copy)

        # Generate a summary
        summary = {
            "total_approvals": len(results),
            "by_status": {},
            "by_approver": {},
            "approvals": results,
        }

        # Categorize by status and approver
        for approval in results:
            status = approval.get("status", "UNKNOWN")
            if status not in summary["by_status"]:
                summary["by_status"][status] = 0
            summary["by_status"][status] += 1

            approver = approval.get("approver_id", "unknown")
            if approver not in summary["by_approver"]:
                summary["by_approver"][approver] = 0
            summary["by_approver"][approver] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewApprovalsSummary",
                "description": "Retrieves review approvals with filtering and summary capabilities including status distribution and approver breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "approval_id": {
                            "type": "string",
                            "description": "The ID of a specific approval to retrieve.",
                        },
                        "cycle_id": {
                            "type": "string",
                            "description": "Filter approvals by review cycle ID.",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Filter approvals by approver ID.",
                        },
                        "approval_status": {
                            "type": "string",
                            "description": "Filter approvals by status (e.g., 'APPROVED', 'REJECTED').",
                        },
                        "approved_after": {
                            "type": "string",
                            "description": "Filter approvals made after this ISO timestamp.",
                        },
                        "approved_before": {
                            "type": "string",
                            "description": "Filter approvals made before this ISO timestamp.",
                        },
                    },
                },
            },
        }
