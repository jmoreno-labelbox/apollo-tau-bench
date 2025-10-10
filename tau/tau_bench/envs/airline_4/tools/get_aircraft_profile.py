# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAircraftProfile(Tool):
    """
    Return a single aircraft enriched with model specs and airport details.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any], *,
        aircraft_id: Optional[str] = None,
        tail_number: Optional[str] = None,
    ) -> str:
        # require exactly one selector
        if bool(aircraft_id) == bool(tail_number):
            return _json({"error": "invalid_params",
                          "reason": "Provide exactly one of aircraft_id or tail_number."})

        # find aircraft
        ac = None
        for a in list(data.get("aircraft", {}).values()):
            if aircraft_id and a.get("aircraft_id") == aircraft_id:
                ac = a; break
            if tail_number and a.get("tail_number") == tail_number:
                ac = a; break
        if not ac:
            return _json({"error": "aircraft_not_found"})

        # enrich model
        model_id = ((ac.get("model") or {}).get("model_id") or "").upper()
        model = _get_aircraft_model_by_id(data, model_id) if model_id else None

        # enrich airport
        iata = ((ac.get("location") or {}).get("iata_code") or "").upper()
        apt = _get_airport_by_iata(data, iata) if iata else None

        out = {
            "aircraft_id": ac.get("aircraft_id"),
            "tail_number": ac.get("tail_number"),
            "status": _norm_status(ac.get("status")),
            "location": {
                "iata_code": iata or None,
                "airport_name": (apt or {}).get("airport_name"),
                "icao_code": (apt or {}).get("icao_code"),
                "timezone": (apt or {}).get("timezone"),
            },
            "model": {
                "model_id": model_id or None,
                "model_name": (ac.get("model") or {}).get("model_name"),
                "manufacturer": (model or {}).get("manufacturer"),
                "passenger_capacity": (model or {}).get("passenger_capacity"),
                "cargo_capacity_kg": (model or {}).get("cargo_capacity_kg"),
                "maximum_takeoff_weight_kg": (model or {}).get("maximum_takeoff_weight_kg"),
                "range_km": (model or {}).get("range_km"),
                "engine_type": (model or {}).get("engine_type"),
            }
        }
        return _json(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_aircraft_profile",
                "description": "Lookup an aircraft by ID or tail number, enriched with model specs and airport details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                        "tail_number": {"type": "string", "description": "e.g., PR-GOL"}
                    },
                    "oneOf": [
                        {"required": ["aircraft_id"]},
                        {"required": ["tail_number"]}
                    ],
                    "additionalProperties": False
                }
            }
        }
