from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListPolicyExceptionsTool(Tool):
    """
    list_policy_exceptions

    Enumerates policy exception records with optional filters:
      - user_id:       filter for a specific user
      - permission_id: filter for a specific permission
      - status:        filter by exception status (e.g., APPROVED, DENIED, EXPIRED, PENDING)
      - requested_on_from / requested_on_to: inclusive ISO-8601 bounds on requested_on
      - active_only:   if True, return solely non-denied/non-expired records

    Results are sorted by requested_on, then exception_id for consistency.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        permission_id: str = None,
        status: str = None,
        active_only: bool = False,
        requested_on_from: str = None,
        requested_on_to: str = None,
        date_from: str = None,
        date_to: str = None
    ) -> str:
        pass
        # Accommodate both specific and general names for date filters (matching with
        # other utilities)
        date_from = requested_on_from or date_from
        date_to = requested_on_to or date_to

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        exceptions: list[dict[str, Any]] = data.get("policy_exceptions", {}).values()
        out: list[dict[str, Any]] = []

        for rec in exceptions:
            if user_id and not _eq(rec.get("user_id"), user_id):
                continue
            if permission_id and not _eq(rec.get("permission_id"), permission_id):
                continue
            if status and not _eq(rec.get("status"), status):
                continue
            if active_only and (rec.get("status") in ("DENIED", "EXPIRED")):
                continue

            # Date filter based on requested_on
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPolicyExceptions",
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
