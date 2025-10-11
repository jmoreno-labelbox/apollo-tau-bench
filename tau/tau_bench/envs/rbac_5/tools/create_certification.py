# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCertification(Tool):
    """
    Create a new certification entry with deterministic ID and default due date.

    kwargs:
      reviewer_id: str (required) - Reviewer responsible for certification
      resource_id: str (required) - Resource to be certified
      status: str (optional; default "PENDING") - PENDING, IN_PROGRESS, COMPLETED
      due_date: str (optional) - ISO-like timestamp ("YYYY-MM-DD HH:MM:SS+00:00"); defaults to +90 days
      completed_on: str (optional) - If status=COMPLETED, explicit completion time; defaults to now
    """
    @staticmethod
    def invoke(data: Dict[str, Any], completed_on, due_date, resource_id = "", reviewer_id = "", status = "PENDING") -> str:
        status = status.upper()
        completed_on_kw = completed_on

        if not reviewer_id or not resource_id:
            return json.dumps({"error": "reviewer_id and resource_id are required"})

        # Verify the existence of the reviewer and resource.
        if not _find_by_id(list(data.get("users", {}).values()), "user_id", reviewer_id):
            return json.dumps({"error": f"reviewer_id {reviewer_id} not found"})
        if not _find_by_id(data.get("resources", []), "resource_id", resource_id):
            return json.dumps({"error": f"resource_id {resource_id} not found"})

        valid_status = ["PENDING", "IN_PROGRESS", "COMPLETED"]
        if status not in valid_status:
            return json.dumps({"error": f"status must be one of: {valid_status}"})

        # Calculate due_date if unspecified: 90 days from the current date.
        if not due_date:
            base = _parse_iso(get_current_timestamp()) or datetime.now(tz=timezone.utc)
            due_dt = base + timedelta(days=90)
            # Align dataset format to include +00:00 suffix.
            due_date = due_dt.strftime("%Y-%m-%d %H:%M:%S+00:00")

        # set completed_on only when status is COMPLETED
        completed_on: Optional[str]
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
        return json.dumps({"ok": True, "certification": new_cert})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_certification",
                "description": "Create a new certification entry with deterministic ID and default due date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id responsible."},
                        "resource_id": {"type": "string", "description": "Target resource_id."},
                        "status": {"type": "string", "description": "Initial status (PENDING, IN_PROGRESS, COMPLETED).", "default": "PENDING"},
                        "due_date": {"type": "string", "description": "Due date (YYYY-MM-DD HH:MM:SS+00:00)."},
                        "completed_on": {"type": "string", "description": "Completion timestamp if status=COMPLETED."}
                    },
                    "required": ["reviewer_id", "resource_id"],
                    "additionalProperties": False
                }
            }
        }
