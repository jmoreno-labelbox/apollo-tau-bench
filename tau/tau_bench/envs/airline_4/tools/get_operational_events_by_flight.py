from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetOperationalEventsByFlight(Tool):
    """API tool for retrieving all operational events related to a specific flight."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        flight_id: str | None = None,
        flight_number: str | None = None,
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not flight_id and not flight_number:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either flight_id or flight_number must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve operational events
        operational_events = data.get("operational_events", [])
        flight_events = []

        #Apply filters to events based on flight
        for event in operational_events:
            flight_info = event.get("flight", {})
            event_flight_id = flight_info.get("flight_id")
            event_flight_number = flight_info.get("flight_number")

            #Verify if this event aligns with the search criteria
            match_found = False
            if flight_id and event_flight_id == flight_id:
                match_found = True
            elif flight_number and event_flight_number == flight_number:
                match_found = True
            elif (
                flight_id
                and flight_number
                and event_flight_id == flight_id
                and event_flight_number == flight_number
            ):
                match_found = True

            if match_found:
                flight_events.append(event)

        #Organize events by timestamp (latest first)
        flight_events.sort(key=lambda x: x.get("event_timestamp_utc", ""), reverse=True)

        #Retrieve flight details if events are located
        flight_info = None
        if flight_events and flight_events[0].get("flight"):
            flight_info = flight_events[0]["flight"]
        elif flight_id or flight_number:
            #Attempt to locate flight information from flight data
            flights = data.get("flights", [])
            for flight in flights:
                if (flight_id and flight.get("flight_id") == flight_id) or (
                    flight_number and flight.get("flight_number") == flight_number
                ):
                    flight_info = {
                        "flight_id": flight.get("flight_id"),
                        "flight_number": flight.get("flight_number"),
                        "origin": flight.get("origin"),
                        "destination": flight.get("destination"),
                    }
                    break

        #Compute statistics for events
        total_events = len(flight_events)
        active_events = len([e for e in flight_events if e.get("status") == "Active"])
        resolved_events = len(
            [e for e in flight_events if e.get("status") == "Resolved"]
        )
        monitoring_events = len(
            [e for e in flight_events if e.get("status") == "Monitoring"]
        )

        #Categorize events based on type
        events_by_type = {}
        for event in flight_events:
            event_type = event.get("event_type", "Unknown")
            if event_type not in events_by_type:
                events_by_type[event_type] = 0
            events_by_type[event_type] += 1

        #Locate the most recent active event
        most_recent_active = None
        for event in flight_events:
            if event.get("status") == "Active":
                most_recent_active = {
                    "event_id": event.get("event_id"),
                    "event_type": event.get("event_type"),
                    "event_timestamp_utc": event.get("event_timestamp_utc"),
                    "details": event.get("details"),
                }
                break

        #Formulate response
        response = {
            "flight": flight_info,
            "search_criteria": {"flight_id": flight_id, "flight_number": flight_number},
            "summary": {
                "total_events": total_events,
                "active_events": active_events,
                "resolved_events": resolved_events,
                "monitoring_events": monitoring_events,
                "events_by_type": events_by_type,
                "most_recent_active": most_recent_active,
            },
            "events": flight_events,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOperationalEventsByFlight",
                "description": "Get all operational events for a specific flight. Returns comprehensive event history with statistics and filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "flight_id": {
                            "type": "string",
                            "description": "Flight ID to search for (e.g., 'FL001'). Either this or flight_number must be provided.",
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Flight number to search for (e.g., 'HAT004'). Either this or flight_id must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
