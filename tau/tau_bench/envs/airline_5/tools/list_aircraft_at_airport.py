from tau_bench.envs.tool import Tool
from __future__ import annotations
import json
from datetime import date, datetime, timedelta  #required for fallback window enlargement
from decimal import ROUND_HALF_UP, Decimal
from typing import Any
import re
from datetime import date as _date



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListAircraftAtAirport(Tool):
    """
    Enumerate aircraft currently stationed at a specified IATA airport, with optional filters.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        iata_code: str,
        status: str | None = None,
        model_id: str | None = None
    ) -> str:
        iata = (iata_code or "").upper()
        if not iata:
            return _json({"error": "missing_params", "reason": "iata_code is required"})

        status = status.strip() if isinstance(status, str) else None
        model_id = (model_id or "").upper() if model_id else None

        airport = _get_airport_by_iata(data, iata)

        rows: list[dict[str, Any]] = []
        for a in data.get("aircraft", []):
            loc = (a.get("location") or {}).get("iata_code")
            if (loc or "").upper() != iata:
                continue

            if status and _norm_status(a.get("status")) != status:
                continue

            ac_model_id = ((a.get("model") or {}).get("model_id") or "").upper()
            if model_id and ac_model_id != model_id:
                continue

            rows.append(
                {
                    "aircraft_id": a.get("aircraft_id"),
                    "tail_number": a.get("tail_number"),
                    "status": _norm_status(a.get("status")),
                    "model_id": ac_model_id or None,
                    "model_name": (a.get("model") or {}).get("model_name"),
                }
            )

        rows.sort(key=lambda r: (r.get("tail_number") or ""))

        return _json(
            {
                "airport": {
                    "iata_code": iata,
                    "airport_name": (airport or {}).get("airport_name"),
                    "icao_code": (airport or {}).get("icao_code"),
                    "timezone": (airport or {}).get("timezone"),
                },
                "total": len(rows),
                "aircraft": rows,
            }
        )
        pass
        iata = (iata_code or "").upper()
        if not iata:
            return _json({"error": "missing_params", "reason": "iata_code is required"})

        status = status.strip() if isinstance(status, str) else None
        model_id = (model_id or "").upper() if model_id else None

        airport = _get_airport_by_iata(data, iata)

        rows: list[dict[str, Any]] = []
        for a in data.get("aircraft", []):
            loc = (a.get("location") or {}).get("iata_code")
            if (loc or "").upper() != iata:
                continue

            if status and _norm_status(a.get("status")) != status:
                continue

            ac_model_id = ((a.get("model") or {}).get("model_id") or "").upper()
            if model_id and ac_model_id != model_id:
                continue

            rows.append(
                {
                    "aircraft_id": a.get("aircraft_id"),
                    "tail_number": a.get("tail_number"),
                    "status": _norm_status(a.get("status")),
                    "model_id": ac_model_id or None,
                    "model_name": (a.get("model") or {}).get("model_name"),
                }
            )

        rows.sort(key=lambda r: (r.get("tail_number") or ""))

        return _json(
            {
                "airport": {
                    "iata_code": iata,
                    "airport_name": (airport or {}).get("airport_name"),
                    "icao_code": (airport or {}).get("icao_code"),
                    "timezone": (airport or {}).get("timezone"),
                },
                "total": len(rows),
                "aircraft": rows,
            }
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAircraftAtAirport",
                "description": "List aircraft currently located at a given IATA airport with optional status/model filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "iata_code": {
                            "type": "string",
                            "description": "Airport IATA code, e.g., ATL",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by aircraft status, e.g., Active",
                        },
                        "model_id": {
                            "type": "string",
                            "description": "Filter by model_id, e.g., B737-800",
                        },
                    },
                    "required": ["iata_code"],
                    "additionalProperties": False,
                },
            },
        }
