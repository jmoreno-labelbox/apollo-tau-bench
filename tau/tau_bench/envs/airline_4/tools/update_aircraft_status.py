from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAircraftStatus(Tool):
    """API tool for updating the aircraft status and optionally altering its location."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        new_status: str,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        new_location_iata: str | None = None,
    ) -> str:
        pass
        if not aircraft_id and not tail_number:
            payload = {"error": "Either aircraft_id or tail_number must be provided"}
            out = json.dumps(
                payload)
            return out

        #Acceptable status values derived from real data
        valid_statuses = ["Active", "Maintenance", "In Maintenance", "Stored"]
        if new_status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "provided_status": new_status,
                    "valid_statuses": valid_statuses,
                }
            out = json.dumps(
                payload)
            return out

        aircraft_list = data.get("aircraft", {}).values()
        airports = data.get("airports", {}).values()

        #Locate the aircraft
        target_aircraft = None
        for aircraft in aircraft_list.values():
            if (aircraft_id and aircraft.get("aircraft_id") == aircraft_id) or (
                tail_number and aircraft.get("tail_number") == tail_number
            ):
                target_aircraft = aircraft
                break

        if not target_aircraft:
            search_term = aircraft_id if aircraft_id else tail_number
            search_type = "aircraft_id" if aircraft_id else "tail_number"
            payload = {"error": "Aircraft not found", search_type: search_term}
            out = json.dumps(payload)
            return out

        #Revise status
        target_aircraft["status"] = new_status

        #Revise location if supplied
        if new_location_iata:
            #Locate the airport using the IATA code
            target_airport = None
            for airport in airports.values():
                if airport.get("iata_code") == new_location_iata:
                    target_airport = airport
                    break

            if not target_airport:
                payload = {
                        "error": "Airport not found for location update",
                        "iata_code": new_location_iata,
                    }
                out = json.dumps(
                    payload)
                return out

            #Revise the location of the aircraft
            target_aircraft["location"] = {
                "airport_id": target_airport["airport_id"],
                "iata_code": target_airport["iata_code"],
            }
        payload = {
                "aircraft_id": target_aircraft["aircraft_id"],
                "tail_number": target_aircraft["tail_number"],
                "status": target_aircraft["status"],
                "location": target_aircraft["location"],
                "updated": True,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAircraftStatus",
                "description": "Update aircraft status and optionally change location using either aircraft ID or tail number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Aircraft ID (e.g., 'AC001'). Either this or tail_number must be provided.",
                        },
                        "tail_number": {
                            "type": "string",
                            "description": "Aircraft tail number (e.g., 'PR-GOL'). Either this or aircraft_id must be provided.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New aircraft status. Valid values: 'Active', 'Maintenance', 'In Maintenance', 'Stored'.",
                        },
                        "new_location_iata": {
                            "type": "string",
                            "description": "Optional new location IATA code (e.g., 'ATL'). Updates aircraft location if provided.",
                        },
                    },
                    "required": ["new_status"],
                },
            },
        }
