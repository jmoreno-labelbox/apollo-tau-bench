# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RepositionAircraft(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        aircraft_id: Optional[str] = None,
        tail_number: Optional[str] = None,
        to_iata: str = "",
        reason: Optional[str] = None,
    ) -> str:
        to_iata = (to_iata or "").upper()

        if bool(aircraft_id) == bool(tail_number):
            return _json({"error": "invalid_params", "reason": "Provide exactly one of aircraft_id or tail_number."})
        if not to_iata:
            return _json({"error": "missing_params", "reason": "to_iata is required"})

        apt = _get_airport_by_iata(data, to_iata)
        if not apt:
            return _json({"error": "airport_not_found", "iata_code": to_iata})

        ac = _find_aircraft(data, aircraft_id, tail_number)
        if not ac:
            return _json({"error": "aircraft_not_found"})

        cur_iata = ((ac.get("location") or {}).get("iata_code") or "").upper()
        if cur_iata == to_iata:
            # No operation performed, but provide a verification snapshot ("after").
            return _json({
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "no_change": True,
                "after": {
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "location": {"iata_code": cur_iata or None},
                    "status": _norm_status(ac.get("status")),
                }
            })

        ac.setdefault("location", {})
        ac["location"]["iata_code"] = to_iata

        audit_id = _next_change_id(data, prefix="AM")
        (data.setdefault("aircraft_movements", [])).append({
            "id": audit_id,
            "type": "reposition_aircraft",
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "from_iata": cur_iata or None,
            "to_iata": to_iata,
            "reason": reason
        })

        after = {
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "location": {"iata_code": to_iata},
            "status": _norm_status(ac.get("status")),
        }

        return _json({
            "success": True,
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "from_iata": cur_iata or None,
            "to_iata": to_iata,
            "no_change": False,
            "audit_id": audit_id,
            "after": after
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reposition_aircraft",
                "description": "Move an aircraft to a new IATA airport with validation and deterministic audit; returns a post-move snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {"type": "string", "description": "e.g., N123AB"},
                        "to_iata": {"type": "string", "description": "Target IATA, e.g., ATL"},
                        "reason": {"type": "string", "description": "Audit text (optional)"}
                    },
                    "oneOf": [
                        {"required": ["aircraft_id", "to_iata"]},
                        {"required": ["tail_number", "to_iata"]}
                    ]
                }
            }
        }
