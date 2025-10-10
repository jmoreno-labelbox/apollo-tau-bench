# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAircraftStatus(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        aircraft_id: Optional[str] = None,
        tail_number: Optional[str] = None,
        status: str,
        reason: Optional[str] = None,
    ) -> str:
        new_status = _norm_status(status) if isinstance(status, str) else ""
        if not new_status:
            return _json({"error": "missing_params", "reason": "status is required"})
        if new_status not in AIRCRAFT_STATUS:
            return _json({
                "error": "invalid_status",
                "entity": "aircraft",
                "provided": status,
                "allowed": sorted(list(AIRCRAFT_STATUS))
            })

        if bool(aircraft_id) == bool(tail_number):
            return _json({
                "error": "invalid_params",
                "reason": "Provide exactly one of aircraft_id or tail_number."
            })

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        old_status = _norm_status(ac.get("status"))
        if old_status == new_status:
            return _json({
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "old_status": old_status,
                "new_status": new_status,
                "no_change": True,
                "after": {
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "status": new_status,
                    "location": (ac.get("location") or {}),
                }
            })

        ac["status"] = new_status

        audit_id = _next_change_id(data, prefix="AS")
        (data.setdefault("aircraft_status_changes", [])).append({
            "id": audit_id,
            "type": "update_aircraft_status",
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "old_status": old_status,
            "new_status": new_status,
            "reason": reason
        })

        after = {
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "status": new_status,
            "location": (ac.get("location") or {}),
        }

        return _json({
            "success": True,
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "old_status": old_status,
            "new_status": new_status,
            "no_change": False,
            "audit_id": audit_id,
            "after": after
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_aircraft_status",
                "description": "Update an aircraft's status with a deterministic audit record; returns a post-update snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {"type": "string", "description": "e.g., N123AB"},
                        "status": {"type": "string", "description": "New status, e.g., active"},
                        "reason": {"type": "string", "description": "Audit text (optional)"}
                    },
                    "oneOf": [
                        {"required": ["aircraft_id", "status"]},
                        {"required": ["tail_number", "status"]}
                    ]
                }
            }
        }
