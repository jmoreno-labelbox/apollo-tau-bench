from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class UpdateAircraftStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        status: str,
        reason: str | None = None
    ) -> str:
        new_status = _norm_status(status) if isinstance(status, str) else ""
        if not new_status:
            return _json({"error": "missing_params", "reason": "status is required"})
        if new_status not in AIRCRAFT_STATUS:
            return _json(
                {
                    "error": "invalid_status",
                    "entity": "aircraft",
                    "provided": status,
                    "allowed": sorted(list(AIRCRAFT_STATUS)),
                }
            )

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        old_status = _norm_status(ac.get("status"))
        if old_status == new_status:
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "old_status": old_status,
                    "new_status": new_status,
                    "no_change": True,
                }
            )

        ac["status"] = new_status

        audit_id = _next_change_id(data, prefix="AS")
        (data.setdefault("aircraft_status_changes", [])).append(
            {
                "id": audit_id,
                "type": "UpdateAircraftStatus",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "no_change": False,
                "audit_id": audit_id,
            }
        )
        pass
        new_status = _norm_status(status) if isinstance(status, str) else ""
        if not new_status:
            return _json({"error": "missing_params", "reason": "status is required"})
        if new_status not in AIRCRAFT_STATUS:
            return _json(
                {
                    "error": "invalid_status",
                    "entity": "aircraft",
                    "provided": status,
                    "allowed": sorted(list(AIRCRAFT_STATUS)),
                }
            )

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        old_status = _norm_status(ac.get("status"))
        if old_status == new_status:
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "old_status": old_status,
                    "new_status": new_status,
                    "no_change": True,
                }
            )

        ac["status"] = new_status

        audit_id = _next_change_id(data, prefix="AS")
        (data.setdefault("aircraft_status_changes", [])).append(
            {
                "id": audit_id,
                "type": "UpdateAircraftStatus",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "no_change": False,
                "audit_id": audit_id,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftStatus",
                "description": "Update an aircraft's status with a deterministic audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {
                            "type": "string",
                            "description": "e.g., N123AB",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status, e.g., active",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Audit text (optional)",
                        },
                    },
                    "oneOf": [
                        {"required": ["aircraft_id", "status"]},
                        {"required": ["tail_number", "status"]},
                    ],
                },
            },
        }
