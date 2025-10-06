from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date

class GetAircraftProfile(Tool):
    """
    Provide a single aircraft enhanced with model specifications and airport information.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        aircraft_id: str | None = None,
        tail_number: str | None = None
    ) -> str:
        pass
        # demand precisely one selector
        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        # locate aircraft
        ac = None
        for a in data.get("aircraft", []):
            if aircraft_id and a.get("aircraft_id") == aircraft_id:
                ac = a
                break
            if tail_number and a.get("tail_number") == tail_number:
                ac = a
                break
        if not ac:
            return _json({"error": "aircraft_not_found"})

        # enhance model
        model_id = ((ac.get("model") or {}).get("model_id") or "").upper()
        model = _get_aircraft_model_by_id(data, model_id) if model_id else None

        # enhance airport
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
                "maximum_takeoff_weight_kg": (model or {}).get(
                    "maximum_takeoff_weight_kg"
                ),
                "range_km": (model or {}).get("range_km"),
                "engine_type": (model or {}).get("engine_type"),
            },
        }
        return _json(out)
        pass
        #demand precisely one selector
        if bool(aircraft_id) == bool(tail_number):
            return _json(
                {
                    "error": "invalid_params",
                    "reason": "Provide exactly one of aircraft_id or tail_number.",
                }
            )

        #locate aircraft
        ac = None
        for a in data.get("aircraft", []):
            if aircraft_id and a.get("aircraft_id") == aircraft_id:
                ac = a
                break
            if tail_number and a.get("tail_number") == tail_number:
                ac = a
                break
        if not ac:
            return _json({"error": "aircraft_not_found"})

        #enhance model
        model_id = ((ac.get("model") or {}).get("model_id") or "").upper()
        model = _get_aircraft_model_by_id(data, model_id) if model_id else None

        #enhance airport
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
                "maximum_takeoff_weight_kg": (model or {}).get(
                    "maximum_takeoff_weight_kg"
                ),
                "range_km": (model or {}).get("range_km"),
                "engine_type": (model or {}).get("engine_type"),
            },
        }
        return _json(out)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftProfile",
                "description": "Lookup an aircraft by ID or tail number, enriched with model specs and airport details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "aircraft_id": {"type": "string", "description": "e.g., AC001"},
                    "tail_number": {
                        "type": "string",
                        "description": "e.g., PR-GOL",
                    },
                },
                "additionalProperties": False,
            },
            },
        }
