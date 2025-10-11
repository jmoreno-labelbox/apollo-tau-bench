# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPolicyExceptionsTool(Tool):
    """
    list_policy_exceptions

    Lists policy exception records with optional filters:
      - user_id:       filter to a specific user
      - permission_id: filter to a specific permission
      - status:        filter by exception status (e.g., APPROVED, DENIED, EXPIRED, PENDING)
      - requested_on_from / requested_on_to: inclusive ISO-8601 bounds on requested_on
      - active_only:   if True, return only non-denied/non-expired records

    Results are returned sorted by requested_on, then exception_id for determinism.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], date_from, date_to, permission_id, requested_on_from, requested_on_to, status, user_id, active_only = False) -> str:
        active_only = bool(active_only)

        # Enable functionality for both exact and general date filter names (consistent with
        # alternative tools)
        date_from = requested_on_from or date_from
        date_to = requested_on_to or date_to

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        exceptions: List[Dict[str, Any]] = data.get("policy_exceptions", [])
        out: List[Dict[str, Any]] = []

        for rec in exceptions:
            if user_id and not _eq(rec.get("user_id"), user_id):
                continue
            if permission_id and not _eq(rec.get("permission_id"), permission_id):
                continue
            if status and not _eq(rec.get("status"), status):
                continue
            if active_only and (rec.get("status") in ("DENIED", "EXPIRED")):
                continue

            # Date filter applied to requested_on.
            if dt_from or dt_to:
                ts = _parse_iso(rec.get("requested_on"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue

            out.append(rec)

        out.sort(
            key=lambda r: ((r.get("requested_on") or ""), (r.get("exception_id") or ""))
        )
        import json as _json

        return _json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_policy_exceptions",
                "description": (
                    "List policy exceptions with optional filters (user_id, permission_id, status, requested_on bounds, active_only)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Filter by user (e.g., U-026)",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "Filter by permission (e.g., P-014)",
                        },
                        "status": {
                            "type": "string",
                            "description": (
                                "Filter by status (e.g., APPROVED, DENIED, EXPIRED, PENDING)"
                            ),
                        },
                        "requested_on_from": {
                            "type": "string",
                            "description": (
                                "ISO 8601 inclusive lower bound for requested_on"
                            ),
                        },
                        "requested_on_to": {
                            "type": "string",
                            "description": (
                                "ISO 8601 inclusive upper bound for requested_on"
                            ),
                        },
                        "date_from": {
                            "type": "string",
                            "description": (
                                "(alias) inclusive lower bound for requested_on"
                            ),
                        },
                        "date_to": {
                            "type": "string",
                            "description": (
                                "(alias) inclusive upper bound for requested_on"
                            ),
                        },
                        "active_only": {
                            "type": "boolean",
                            "description": (
                                "If true, exclude DENIED and EXPIRED records"
                            ),
                        },
                    },
                    "required": [],
                },
            },
        }
