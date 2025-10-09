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

class GetAircraftByTailNumber(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tail_number: str) -> str:
        aircraft_list = data.get("aircraft", [])
        for aircraft in aircraft_list:
            if aircraft.get("tail_number") == tail_number:
                #standardize status casing prior to returning
                out = dict(aircraft)
                if "status" in out:
                    out["status"] = _norm_status(out.get("status"))
                return _json(out)
        return _json({"error": "Aircraft not found", "tail_number": tail_number})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByTailNumber",
                "description": "Retrieves the full details of an aircraft using its unique tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tail_number": {
                            "type": "string",
                            "description": "The unique tail number of the aircraft (e.g., 'G-ZNKH').",
                        }
                    },
                    "required": ["tail_number"],
                },
            },
        }
