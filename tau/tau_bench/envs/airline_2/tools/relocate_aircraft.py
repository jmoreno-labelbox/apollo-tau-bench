from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RelocateAircraft(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str,
        new_location_airport_id: str,
        new_location_iata: str | None = None,
    ) -> str:
        for a in data.get("aircraft", {}).values():
            if a.get("aircraft_id") == aircraft_id:
                a["location"] = (
                    {
                        "airport_id": new_location_airport_id,
                        "iata_code": new_location_iata,
                    }
                    if new_location_iata
                    else {"airport_id": new_location_airport_id}
                )
                return _j(a)
        return _j({"error": "aircraft_not_found", "aircraft_id": aircraft_id})


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RelocateAircraft",
                "description": "Update aircraft.location to a new airport deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string"},
                        "new_location_airport_id": {"type": "string"},
                        "new_location_iata": {"type": "string"},
                    },
                    "required": ["aircraft_id", "new_location_airport_id"],
                },
            },
        }
