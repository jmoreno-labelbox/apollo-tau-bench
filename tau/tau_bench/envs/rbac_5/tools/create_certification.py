from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateCertification(Tool):
    """
    Establish a new certification entry with consistent ID and a default due date.

    kwargs:
      reviewer_id: str (mandatory) - Reviewer accountable for certification
      resource_id: str (mandatory) - Resource to be certified
      status: str (optional; defaults to "PENDING") - PENDING, IN_PROGRESS, COMPLETED
      due_date: str (optional) - ISO-like timestamp ("YYYY-MM-DD HH:MM:SS+00:00"); defaults to +90 days
      completed_on: str (optional) - If status=COMPLETED, specific completion time; defaults to now
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reviewer_id: str = "",
        resource_id: str = "",
        status: str = "PENDING",
        due_date: str = None,
        completed_on_kw: str = None
    ) -> str:
        status = status.upper()

        if not reviewer_id or not resource_id:
            payload = {"error": "reviewer_id and resource_id are required"}
            out = json.dumps(payload)
            return out

        # Confirm the presence of the reviewer and resource
        if not _find_by_id(data.get("users", {}).values(), "user_id", reviewer_id):
            payload = {"error": f"reviewer_id {reviewer_id} not found"}
            out = json.dumps(payload)
            return out
        if not _find_by_id(data.get("resources", {}).values(), "resource_id", resource_id):
            payload = {"error": f"resource_id {resource_id} not found"}
            out = json.dumps(payload)
            return out

        valid_status = ["PENDING", "IN_PROGRESS", "COMPLETED"]
        if status not in valid_status:
            payload = {"error": f"status must be one of: {valid_status}"}
            out = json.dumps(payload)
            return out

        # Establish due_date deterministically if not supplied: +90 days from the current date
        if not due_date:
            base = _parse_iso(get_current_timestamp()) or datetime.now(tz=timezone.utc)
            due_dt = base + timedelta(days=90)
            # Align dataset format with +00:00 suffix
            due_date = due_dt.strftime("%Y-%m-%d %H:%M:%S+00:00")

        # completed_on is set only if COMPLETED
        completed_on: str | None
        if status == "COMPLETED":
            completed_on = completed_on_kw or get_current_timestamp()
        else:
            completed_on = None

        new_cert = {
            "certification_id": _next_id(data, "certifications", "C"),
            "reviewer_id": reviewer_id,
            "resource_id": resource_id,
            "status": status,
            "due_date": due_date,
            "completed_on": completed_on,
        }

        data.setdefault("certifications", []).append(new_cert)
        payload = {"ok": True, "certification": new_cert}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCertification",
                "description": "Create a new certification entry with deterministic ID and default due date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id responsible.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Target resource_id.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Initial status (PENDING, IN_PROGRESS, COMPLETED).",
                            "default": "PENDING",
                        },
                        "due_date": {
                            "type": "string",
                            "description": "Due date (YYYY-MM-DD HH:MM:SS+00:00).",
                        },
                        "completed_on": {
                            "type": "string",
                            "description": "Completion timestamp if status=COMPLETED.",
                        },
                    },
                    "required": ["reviewer_id", "resource_id"],
                    "additionalProperties": False,
                },
            },
        }
