from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateReviewCycleStatus(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str, new_status: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(cycle_id, str) or not cycle_id:
            payload = {"error": "cycle_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        allowed_status = [
            "NEEDS_REVIEW",
            "APPROVED",
            "CHANGES_REQUESTED",
            "ESCALATED",
            "IN_FLIGHT",
        ]
        if new_status not in allowed_status:
            payload = {"error": f"Invalid status. Allowed: {allowed_status}"}
            out = json.dumps(payload)
            return out

        review_cycles = data.get("review_cycles", [])

        #Identify the review cycle that needs updating
        cycle_found = False
        for cycle in review_cycles:
            if cycle.get("cycle_id") == cycle_id:
                cycle_found = True
                old_status = cycle.get("status")
                cycle["status"] = new_status

                #If the status is being updated to ESCALATED, record the escalated timestamp
                if new_status == "ESCALATED" and old_status != "ESCALATED":
                    cycle["escalated_ts_nullable"] = "2025-08-26T12:00:00Z"
                elif new_status != "ESCALATED":
                    cycle["escalated_ts_nullable"] = None
                payload = {
                        "updated_cycle": cycle,
                        "previous_status": old_status,
                        "new_status": new_status,
                    }
                out = json.dumps(
                    payload)
                return out

        if not cycle_found:
            payload = {"error": f"Review cycle with cycle_id '{cycle_id}' not found"}
            out = json.dumps(
                payload)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Update the status of an existing review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {
                            "type": "string",
                            "description": "The review cycle ID to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New review cycle status (NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED, IN_FLIGHT).",
                        },
                    },
                    "required": ["cycle_id", "new_status"],
                },
            },
        }
