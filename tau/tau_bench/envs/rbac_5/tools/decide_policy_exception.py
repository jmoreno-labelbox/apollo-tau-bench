# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DecidePolicyException(Tool):
    """
    Approve or deny a policy exception with deterministic timestamps.

    kwargs:
      exception_id: str (required)
      reviewer_id: str (required)
      decision: str = "APPROVED" | "DENIED" (required)
      reviewed_on: str ISO (optional; defaults to current timestamp)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id", "")
        reviewer_id = kwargs.get("reviewer_id", "")
        decision = (kwargs.get("decision") or "").upper()
        reviewed_on = kwargs.get("reviewed_on") or get_current_timestamp()

        if decision not in ("APPROVED", "DENIED"):
            return json.dumps({"error": "decision must be APPROVED or DENIED"})

        # Obtain exception
        exceptions = data.get("policy_exceptions", [])
        exception = _find_by_id(exceptions, "exception_id", exception_id)
        if not exception:
            return json.dumps({"error": f"exception_id {exception_id} not found"})

        # Verify reviewer correspondence.
        if exception.get("reviewed_by") != reviewer_id:
            return json.dumps({"error": f"reviewer_id {reviewer_id} does not match assigned reviewer {exception.get('reviewed_by')}"})

        # Check status validity.
        if exception.get("status") != "PENDING_REVIEW":
            return json.dumps({"error": f"exception {exception_id} is not PENDING_REVIEW"})

        # Refresh status
        updated = dict(exception)
        updated.update({
            "status": "ACTIVE" if decision == "APPROVED" else "DENIED",
            "reviewed_on": reviewed_on,
        })

        # If rejected, reset expires_on.
        if decision == "DENIED":
            updated["expires_on"] = None

        # Save changes
        for i, exc in enumerate(exceptions):
            if exc.get("exception_id") == exception_id:
                data["policy_exceptions"][i] = updated
                break

        return json.dumps({"ok": True, "policy_exception": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "decide_policy_exception",
                "description": "Approve or deny a policy exception with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string", "description": "Policy exception id (PE-###)."},
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id."},
                        "decision": {"type": "string", "enum": ["APPROVED", "DENIED"], "description": "Decision outcome."},
                        "reviewed_on": {"type": "string", "description": "ISO timestamp; defaults to now."}
                    },
                    "required": ["exception_id", "reviewer_id", "decision"],
                    "additionalProperties": False
                }
            }
        }
