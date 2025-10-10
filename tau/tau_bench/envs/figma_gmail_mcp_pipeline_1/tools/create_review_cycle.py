# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateReviewCycle(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        artifact_id: str,
        status: str,
        thread_id_nullable: str = None
    ) -> str:
        # Validate input
        if not isinstance(artifact_id, str) or not artifact_id:
            return json.dumps({"error": "artifact_id must be a non-empty string"})
        allowed_status = ["NEEDS_REVIEW", "APPROVED", "CHANGES_REQUESTED", "ESCALATED", "IN_FLIGHT"]
        if status not in allowed_status:
            return json.dumps({"error": f"Invalid status. Allowed: {allowed_status}"})
        review_cycles = data.get("review_cycles", [])
        # Generate new cycle_id
        next_num = len(review_cycles) + 1
        cycle_id = f"cycle_{next_num:03d}"
        now = "2025-08-21T16:00:00Z"
        created_ts = now
        # Default SLA: 3 days from now
        sla_deadline_ts = "2025-08-24T16:00:00Z"
        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "thread_id_nullable": thread_id_nullable,
            "status": status,
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }
        review_cycles.append(new_cycle)
        return json.dumps({"new_cycle": new_cycle})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_review_cycle",
                "description": "Create a new review cycle for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string", "description": "The artifact ID for the review cycle."},
                        "status": {"type": "string", "description": "Review cycle status (NEEDS_REVIEW, APPROVED, CHANGES_REQUESTED, ESCALATED, IN_FLIGHT)."},
                        "thread_id_nullable": {"type": "string", "description": "Optional thread ID for the review cycle."}
                    },
                    "required": ["artifact_id", "status"]
                }
            }
        }
