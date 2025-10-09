from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DecidePolicyException(Tool):
    """
    Approve or reject a policy exception with consistent timestamps.

    kwargs:
      exception_id: str (mandatory)
      reviewer_id: str (mandatory)
      decision: str = "APPROVED" | "DENIED" (mandatory)
      reviewed_on: str ISO (optional; defaults to the current timestamp)
    """

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = "", reviewer_id: str = "", decision: str = None, reviewed_on: str = None) -> str:
        decision = (decision or "").upper()
        reviewed_on = reviewed_on or get_current_timestamp()

        if decision not in ("APPROVED", "DENIED"):
            payload = {"error": "decision must be APPROVED or DENIED"}
            out = json.dumps(payload)
            return out

        # Retrieve the exception
        exceptions = data.get("policy_exceptions", [])
        exception = _find_by_id(exceptions, "exception_id", exception_id)
        if not exception:
            payload = {"error": f"exception_id {exception_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the reviewer matches
        if exception.get("reviewed_by") != reviewer_id:
            payload = {
                "error": f"reviewer_id {reviewer_id} does not match assigned reviewer {exception.get('reviewed_by')}"
            }
            out = json.dumps(payload)
            return out

        # Confirm the status
        if exception.get("status") != "PENDING_REVIEW":
            payload = {"error": f"exception {exception_id} is not PENDING_REVIEW"}
            out = json.dumps(payload)
            return out

        # Modify the status
        updated = dict(exception)
        updated.update(
            {
                "status": "ACTIVE" if decision == "APPROVED" else "DENIED",
                "reviewed_on": reviewed_on,
            }
        )

        # If denied, remove expires_on
        if decision == "DENIED":
            updated["expires_on"] = None

        # Save the update
        for i, exc in enumerate(exceptions):
            if exc.get("exception_id") == exception_id:
                data["policy_exceptions"][i] = updated
                break
        payload = {"ok": True, "policy_exception": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DecidePolicyException",
                "description": "Approve or deny a policy exception with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "Policy exception id (PE-###).",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id.",
                        },
                        "decision": {
                            "type": "string",
                            "enum": ["APPROVED", "DENIED"],
                            "description": "Decision outcome.",
                        },
                        "reviewed_on": {
                            "type": "string",
                            "description": "ISO timestamp; defaults to now.",
                        },
                    },
                    "required": ["exception_id", "reviewer_id", "decision"],
                    "additionalProperties": False,
                },
            },
        }
