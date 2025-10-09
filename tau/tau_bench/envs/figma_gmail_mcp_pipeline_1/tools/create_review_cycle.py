from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateReviewCycle(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str,
        status: str,
        thread_id_nullable: str = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_id, str) or not artifact_id:
            payload = {"error": "artifact_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        allowed_status = [
            "NEEDS_REVIEW",
            "APPROVED",
            "CHANGES_REQUESTED",
            "ESCALATED",
            "IN_FLIGHT",
        ]
        if status not in allowed_status:
            payload = {"error": f"Invalid status. Allowed: {allowed_status}"}
            out = json.dumps(payload)
            return out
        review_cycles = data.get("review_cycles", {}).values()
        #Create a new cycle_id
        next_num = len(review_cycles) + 1
        cycle_id = f"cycle_{next_num:03d}"
        now = "2025-08-21T16:00:00Z"
        created_ts = now
        #Standard SLA: 3 days ahead
        sla_deadline_ts = "2025-08-24T16:00:00Z"
        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "thread_id_nullable": thread_id_nullable,
            "status": status,
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None,
        }
        data["review_cycles"][new_cycle["review_cycle_id"]] = new_cycle
        payload = {"new_cycle": new_cycle}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewCycle",
                "description": "Create a new review cycle for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The artifact ID for the review cycle.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Review cycle status (NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED, IN_FLIGHT).",
                        },
                        "thread_id_nullable": {
                            "type": "string",
                            "description": "Optional thread ID for the review cycle.",
                        },
                    },
                    "required": ["artifact_id", "status"],
                },
            },
        }
