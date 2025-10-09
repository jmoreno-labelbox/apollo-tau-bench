from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DecideAccessRequest(Tool):
    """
    Approve or deny an access request with validations and consistent timestamps.

    kwargs:
      request_id: str (mandatory)
      reviewer_id: str (mandatory)
      decision: str = "APPROVED" | "REJECTED" (mandatory)
      decision_notes: str (mandatory)
      decision_at: str ISO-8601 (optional; defaults to request.submitted_at or now)
      enforce_admin: bool = True  (require the reviewer to have 'Administrator' role)
      enforce_pending: bool = True (require the current status to be 'PENDING')
      enforce_sla: bool = False   (deny approvals if older than sla_days without exemption)
      sla_days: int = 5
      waive_sla: bool = False
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = "",
        reviewer_id: str = "",
        decision: str = "",
        decision_at: str = None,
        enforce_admin: bool = True,
        enforce_pending: bool = True,
        enforce_sla: bool = False,
        sla_days: int = 5,
        waive_sla: bool = False
    ) -> str:
        decision = decision.upper()
        decision_at_kw = decision_at or get_current_timestamp()

        if decision not in ("APPROVED", "REJECTED"):
            payload = {"error": "decision must be APPROVED or REJECTED"}
            out = json.dumps(payload)
            return out

        # Retrieve the request
        requests = data.get("access_requests", {}).values()
        req = _find_by_id(requests, "request_id", request_id)
        if not req:
            payload = {"error": f"request_id {request_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the reviewer's admin role if necessary
        if enforce_admin:
            # Locate the role_id for Administrator
            admin_roles = []
            for r in data.get("roles", {}).values():
                role_name = str(r.get("role_name", "")).strip().lower()
                if role_name.endswith("admin") or role_name.endswith("lead"):
                    admin_data["roles"][role_id] = r
            if not admin_roles:
                payload = {"error": "Administrator role not defined in roles.json"}
                out = json.dumps(payload)
                return out
            # Verify assignments
            has_admin = any(
                ur.get("user_id") == reviewer_id
                and ur.get("role_id") in [r.get("role_id") for r in admin_roles]
                for ur in data.get("user_roles", {}).values()
            )
            if not has_admin:
                payload = {"error": f"reviewer_id {reviewer_id} lacks Administrator role"}
                out = json.dumps(payload)
                return out

        # Confirm the pending status
        if enforce_pending and req.get("status") != "PENDING":
            payload = {"error": f"request {request_id} is not PENDING"}
            out = json.dumps(payload)
            return out

        # Ensure the target user and role are present
        user = _find_by_id(data.get("users", {}).values()), "user_id", req.get("user_id") or "")
        role = _find_by_id(
            data.get("roles", {}).values()), "role_id", req.get("requested_role_id") or ""
        )
        if not user or not role:
            payload = {"error": "target user or requested role does not exist"}
            out = json.dumps(payload)
            return out

        # SLA enforcement (only prevent approvals unless exempted)
        if enforce_sla and decision == "APPROVED" and not waive_sla:
            sub_dt = _parse_iso(req.get("submitted_at"))
            now_dt = _parse_iso(get_current_timestamp()) or datetime.now(
                tz=timezone.utc
            )
            if sub_dt:
                age_days = (now_dt - sub_dt).days
                if age_days > int(sla_days):
                    payload = {
                        "error": f"request {request_id} exceeds SLA ({age_days}d) — approval blocked without waiver"
                    }
                    out = json.dumps(payload)
                    return out

        # Consistent decision_at
        decision_at = (
            decision_at_kw or req.get("submitted_at") or get_current_timestamp()
        )

        updated = dict(req)
        updated.update(
            {
                "status": decision,
                "reviewed_by": reviewer_id,
                "decision_at": decision_at,
            }
        )

        # Save the update
        for i, r in enumerate(requests.values():
            if r.get("request_id") == request_id:
                data["access_requests"][i] = updated
                break
        payload = {"ok": True, "request": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DecideAccessRequest",
                "description": "Approve or reject an access request with validation, deterministic timestamps, and notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request id (AR-###).",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer user_id (must be Administrator if enforce_admin).",
                        },
                        "decision": {
                            "type": "string",
                            "enum": ["APPROVED", "REJECTED"],
                            "description": "Decision outcome.",
                        },
                        "decision_at": {
                            "type": "string",
                            "description": "ISO timestamp; defaults to submitted_at or now.",
                        },
                        "enforce_admin": {
                            "type": "boolean",
                            "description": "Require reviewer to have Administrator role.",
                            "default": True,
                        },
                        "enforce_pending": {
                            "type": "boolean",
                            "description": "Require request to be PENDING.",
                            "default": True,
                        },
                        "enforce_sla": {
                            "type": "boolean",
                            "description": "Block approvals older than sla_days without waiver.",
                            "default": False,
                        },
                        "sla_days": {
                            "type": "integer",
                            "description": "SLA day threshold for approvals.",
                            "default": 5,
                        },
                        "waive_sla": {
                            "type": "boolean",
                            "description": "Allow approval despite SLA breach.",
                        },
                    },
                    "required": ["request_id", "reviewer_id", "decision"],
                    "additionalProperties": False,
                },
            },
        }
