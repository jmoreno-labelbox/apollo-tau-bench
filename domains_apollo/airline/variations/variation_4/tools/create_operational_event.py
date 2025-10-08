from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CreateOperationalEvent(Tool):
    """API tool for recording new operational events that impact flights, aircraft, or airports."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        event_type: str,
        event_timestamp_utc: str,
        details: str,
        status: str = "Active",
        flight_id: str | None = None,
        flight_number: str | None = None,
        aircraft_id: str | None = None,
        tail_number: str | None = None,
        airport_id: str | None = None,
        iata_code: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that necessary parameters are valid
        if not all([event_type, event_timestamp_utc, details]):
            payload = {
                    "error": "Missing required parameters",
                    "required": ["event_type", "event_timestamp_utc", "details"],
                }
            out = json.dumps(
                payload)
            return out

        #Check the event_type for validity
        valid_event_types = [
            "Gate Change",
            "Minor Delay",
            "Technical Issue",
            "Weather Delay",
            "Crew Replacement",
            "Diversion Landing",
            "Aircraft AOG",
        ]
        if event_type not in valid_event_types:
            payload = {
                    "error": "Invalid event type",
                    "valid_event_types": valid_event_types,
                    "received": event_type,
                }
            out = json.dumps(
                payload)
            return out

        #Check the status for validity
        valid_statuses = ["Active", "Resolved", "Monitoring"]
        if status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status,
                }
            out = json.dumps(
                payload)
            return out

        #Check the format of event_timestamp_utc for validity
        try:
            datetime.fromisoformat(event_timestamp_utc.replace("Z", "+00:00"))
        except ValueError:
            payload = {
                    "error": "Invalid event_timestamp_utc format. Expected ISO format with Z suffix (e.g., '2024-05-01T14:30:00Z')",
                    "received": event_timestamp_utc,
                }
            out = json.dumps(
                payload)
            return out

        #Ensure that at least one association is supplied
        if not any(
            [
                flight_id and flight_number,
                aircraft_id and tail_number,
                airport_id and iata_code,
            ]
        ):
            payload = {
                    "error": "At least one association must be provided",
                    "required": "Either (flight_id AND flight_number) OR (aircraft_id AND tail_number) OR (airport_id AND iata_code)",
                }
            out = json.dumps(
                payload)
            return out

        #Check the aircraft association if supplied
        if aircraft_id or tail_number:
            if not (aircraft_id and tail_number):
                payload = {
                        "error": "Both aircraft_id and tail_number must be provided together",
                        "received": {
                            "aircraft_id": aircraft_id,
                            "tail_number": tail_number,
                        },
                    }
                out = json.dumps(
                    payload)
                return out

            #Confirm the aircraft is present
            aircraft_data = data.get("aircraft", [])
            aircraft_exists = any(
                aircraft.get("aircraft_id") == aircraft_id
                and aircraft.get("tail_number") == tail_number
                for aircraft in aircraft_data
            )
            if not aircraft_exists:
                payload = {
                        "error": "Aircraft not found",
                        "aircraft_id": aircraft_id,
                        "tail_number": tail_number,
                    }
                out = json.dumps(
                    payload)
                return out

        #Check the airport association if supplied
        if airport_id or iata_code:
            if not (airport_id and iata_code):
                payload = {
                        "error": "Both airport_id and iata_code must be provided together",
                        "received": {"airport_id": airport_id, "iata_code": iata_code},
                    }
                out = json.dumps(
                    payload)
                return out

            #Confirm the airport is present
            airports = data.get("airports", [])
            airport_exists = any(
                airport.get("airport_id") == airport_id
                and airport.get("iata_code") == iata_code
                for airport in airports
            )
            if not airport_exists:
                payload = {
                        "error": "Airport not found",
                        "airport_id": airport_id,
                        "iata_code": iata_code,
                    }
                out = json.dumps(
                    payload)
                return out

        #Create a unique event ID (sequential format: OE001, OE002, etc.)
        operational_events = data.get("operational_events", [])
        existing_numbers = []

        for event in operational_events:
            event_id = event.get("event_id", "")
            if event_id.startswith("OE") and len(event_id) == 5:
                try:
                    number = int(event_id[2:])  #Retrieve the number portion following "OE"
                    existing_numbers.append(number)
                except ValueError:
                    continue

        #Determine the next available number (highest + 1)
        next_number = max(existing_numbers) + 1 if existing_numbers else 1
        event_id = f"OE{next_number:03d}"

        #Establish a new operational event
        new_event = {
            "event_id": event_id,
            "event_type": event_type,
            "event_timestamp_utc": event_timestamp_utc,
            "status": status,
            "details": details,
        }

        #Include associations if supplied
        if flight_id and flight_number:
            new_event["flight"] = {
                "flight_id": flight_id,
                "flight_number": flight_number,
            }

        if aircraft_id and tail_number:
            new_event["aircraft"] = {
                "aircraft_id": aircraft_id,
                "tail_number": tail_number,
            }

        if airport_id and iata_code:
            new_event["airport"] = {"airport_id": airport_id, "iata_code": iata_code}

        #Include in the operational events
        operational_events.append(new_event)
        data["operational_events"] = operational_events

        #Formulate response
        response = {
            "success": True,
            "message": "Operational event created successfully",
            "event": new_event,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOperationalEvent",
                "description": "Log new operational events affecting flights, aircraft, or airports. Creates comprehensive event records with proper associations and validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {
                            "type": "string",
                            "description": "Type of operational event: 'Gate Change', 'Minor Delay', 'Technical Issue', 'Weather Delay', 'Crew Replacement', 'Diversion Landing', 'Aircraft AOG'",
                        },
                        "event_timestamp_utc": {
                            "type": "string",
                            "description": "Event timestamp in UTC (ISO format with Z suffix, e.g., '2024-05-01T14:30:00Z'). Required for deterministic behavior.",
                        },
                        "details": {
                            "type": "string",
                            "description": "Detailed description of the operational event",
                        },
                        "status": {
                            "type": "string",
                            "description": "Event status: 'Active', 'Resolved', or 'Monitoring'. Defaults to 'Active'.",
                        },
                        "flight_id": {
                            "type": "string",
                            "description": "Associated flight ID (e.g., 'FL001'). Must be provided with flight_number if flight association is needed.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Associated flight number (e.g., 'HAT004'). Must be provided with flight_id if flight association is needed.",
                        },
                        "aircraft_id": {
                            "type": "string",
                            "description": "Associated aircraft ID (e.g., 'AC001'). Must be provided with tail_number if aircraft association is needed.",
                        },
                        "tail_number": {
                            "type": "string",
                            "description": "Associated aircraft tail number (e.g., 'PR-GOL'). Must be provided with aircraft_id if aircraft association is needed.",
                        },
                        "airport_id": {
                            "type": "string",
                            "description": "Associated airport ID (e.g., 'ARP_ATL'). Must be provided with iata_code if airport association is needed.",
                        },
                        "iata_code": {
                            "type": "string",
                            "description": "Associated airport IATA code (e.g., 'ATL'). Must be provided with airport_id if airport association is needed.",
                        },
                    },
                    "required": ["event_type", "event_timestamp_utc", "details"],
                },
            },
        }
