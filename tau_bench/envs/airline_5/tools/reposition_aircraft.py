from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class RepositionAircraft(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        to_iata: str = "",
        reason: str | None = None
    ) -> str:
        to_iata = (to_iata or "").upper()

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )
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
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "from_iata": cur_iata or None,
                    "to_iata": to_iata,
                    "no_change": True,
                }
            )

        ac.setdefault("location", {})
        ac["location"]["iata_code"] = to_iata

        audit_id = _next_change_id(data, prefix="AM")
        (data.setdefault("aircraft_movements", [])).append(
            {
                "id": audit_id,
                "type": "RepositionAircraft",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "no_change": False,
                "audit_id": audit_id,
            }
        )
        pass
        to_iata = (to_iata or "").upper()

        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )
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
            return _json(
                {
                    "success": True,
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "from_iata": cur_iata or None,
                    "to_iata": to_iata,
                    "no_change": True,
                }
            )

        ac.setdefault("location", {})
        ac["location"]["iata_code"] = to_iata

        audit_id = _next_change_id(data, prefix="AM")
        (data.setdefault("aircraft_movements", [])).append(
            {
                "id": audit_id,
                "type": "RepositionAircraft",
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "reason": reason,
            }
        )

        return _json(
            {
                "success": True,
                "aircraft_id": ac.get("aircraft_id"),
                "tail_number": ac.get("tail_number"),
                "from_iata": cur_iata or None,
                "to_iata": to_iata,
                "no_change": False,
                "audit_id": audit_id,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RepositionAircraft",
                "description": "Move an aircraft to a new IATA airport with validation and deterministic audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {
                            "type": "string",
                            "description": "e.g., N123AB",
                        },
                        "to_iata": {
                            "type": "string",
                            "description": "Target IATA, e.g., ATL",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Audit text (optional)",
                        },
                    },
},
            },
        }
