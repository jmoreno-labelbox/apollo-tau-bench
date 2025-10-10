# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReviewCycleStatus(Tool):  # GENERATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cycle_id: str,
        new_status: str
    ) -> str:
        # Verify input correctness.
        if not isinstance(cycle_id, str) or not cycle_id:
            return json.dumps({"error": "cycle_id must be a non-empty string"})

        allowed_status = ["NEEDS_REVIEW", "APPROVED", "CHANGES_REQUESTED", "ESCALATED", "IN_FLIGHT"]
        if new_status not in allowed_status:
            return json.dumps({"error": f"Invalid status. Allowed: {allowed_status}"})

        review_cycles = list(data.get("review_cycles", {}).values())

        # Locate the review cycle for updates.
        cycle_found = False
        for cycle in review_cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle_found = True
                old_status = cycle.get("status")
                cycle["status"] = new_status

                # When the status changes to ESCALATED, update the escalated timestamp.
                if new_status == "ESCALATED" and old_status != "ESCALATED":
                    cycle["escalated_ts_nullable"] = "2025-08-26T12:00:00Z"
                elif new_status != "ESCALATED":
                    cycle["escalated_ts_nullable"] = None

                return json.dumps({
                    "updated_cycle": cycle,
                    "previous_status": old_status,
                    "new_status": new_status
                })

        if not cycle_found:
            return json.dumps({"error": f"Review cycle with cycle_id '{cycle_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_review_cycle_status",
                "description": "Update the status of an existing review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string", "description": "The review cycle ID to update."},
                        "new_status": {"type": "string", "description": "New review cycle status (NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED, IN_FLIGHT)."}
                    },
                    "required": ["cycle_id", "new_status"]
                }
            }
        }
