# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DecideAccessRequest(Tool):
    """
    Approve or reject an access request with validations and deterministic timestamps.

    kwargs:
      request_id: str (required)
      reviewer_id: str (required)
      decision: str = "APPROVED" | "REJECTED" (required)
      decision_notes: str (required)
      decision_at: str ISO-8601 (optional; defaults to request.submitted_at else now)
      enforce_admin: bool = True  (require reviewer has 'Administrator' role)
      enforce_pending: bool = True (require current status == 'PENDING')
      enforce_sla: bool = False   (reject approvals if older than sla_days without waiver)
      sla_days: int = 5
      waive_sla: bool = False
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id", "")
        reviewer_id = kwargs.get("reviewer_id", "")
        decision = (kwargs.get("decision") or "").upper()
        decision_at_kw = kwargs.get("decision_at", get_current_timestamp())
        enforce_admin = kwargs.get("enforce_admin", True)
        enforce_pending = kwargs.get("enforce_pending", True)
        # SLA enforcement is optional; default to False to avoid blocking decisions in static datasets
        enforce_sla = kwargs.get("enforce_sla", False)
        sla_days = kwargs.get("sla_days", 5)
        waive_sla = kwargs.get("waive_sla", False)

        if decision not in ("APPROVED", "REJECTED"):
            return json.dumps({"error": "decision must be APPROVED or REJECTED"})

        # Get request
        requests = data.get("access_requests", [])
        req = _find_by_id(requests, "request_id", request_id)
        if not req:
            return json.dumps({"error": f"request_id {request_id} not found"})

        # Validate reviewer admin role if required
        if enforce_admin:
            # Find Administrator role_id
            admin_roles = []
            for r in list(data.get("roles", {}).values()):
                role_name = str(r.get("role_name", "")).strip().lower()
                if role_name.endswith("admin") or role_name.endswith("lead"):
                    admin_roles.append(r)
            if not admin_roles:
                return json.dumps({"error": "Administrator role not defined in roles.json"})
            # Check assignments
            has_admin = any(
                ur.get("user_id") == reviewer_id and ur.get("role_id") in [r.get("role_id") for r in admin_roles]
                for ur in data.get("user_roles", [])
            )
            if not has_admin:
                return json.dumps({"error": f"reviewer_id {reviewer_id} lacks Administrator role"})

        # Validate pending status
        if enforce_pending and req.get("status") != "PENDING":
            return json.dumps({"error": f"request {request_id} is not PENDING"})

        # Validate target user and role exist
        user = _find_by_id(list(data.get("users", {}).values()), "user_id", req.get("user_id") or "")
        role = _find_by_id(list(data.get("roles", {}).values()), "role_id", req.get("requested_role_id") or "")
        if not user or not role:
            return json.dumps({"error": "target user or requested role does not exist"})

        # SLA enforcement (only block approvals unless waived)
        if enforce_sla and decision == "APPROVED" and not waive_sla:
            sub_dt = _parse_iso(req.get("submitted_at"))
            now_dt = _parse_iso(get_current_timestamp()) or datetime.now(tz=timezone.utc)
            if sub_dt:
                age_days = (now_dt - sub_dt).days
                if age_days > int(sla_days):
                    return json.dumps({"error": f"request {request_id} exceeds SLA ({age_days}d) — approval blocked without waiver"})

        # Deterministic decision_at
        decision_at = decision_at_kw or req.get("submitted_at") or get_current_timestamp()

        updated = dict(req)
        updated.update({
            "status": decision,
            "reviewed_by": reviewer_id,
            "decision_at": decision_at,
        })

        # Persist update
        for i, r in enumerate(requests):
            if r.get("request_id") == request_id:
                data["access_requests"][i] = updated
                break

        return json.dumps({"ok": True, "request": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "decide_access_request",
                "description": "Approve or reject an access request with validation, deterministic timestamps, and notes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "Access request id (AR-###)."},
                        "reviewer_id": {"type": "string", "description": "Reviewer user_id (must be Administrator if enforce_admin)."},
                        "decision": {"type": "string", "enum": ["APPROVED", "REJECTED"], "description": "Decision outcome."},
                        "decision_at": {"type": "string", "description": "ISO timestamp; defaults to submitted_at or now."},
                        "enforce_admin": {"type": "boolean", "description": "Require reviewer to have Administrator role.", "default": True},
                        "enforce_pending": {"type": "boolean", "description": "Require request to be PENDING.", "default": True},
                        "enforce_sla": {"type": "boolean", "description": "Block approvals older than sla_days without waiver.", "default": False},
                        "sla_days": {"type": "integer", "description": "SLA day threshold for approvals.", "default": 5},
                        "waive_sla": {"type": "boolean", "description": "Allow approval despite SLA breach."},
                    },
                    "required": ["request_id", "reviewer_id", "decision"],
                    "additionalProperties": False
                }
            }
        }
