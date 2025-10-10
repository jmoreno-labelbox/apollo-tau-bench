# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOperationalEvent(Tool):
    """
    A tool to create a new operational event.
    """
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        airport_id: str,
        event_type: str,
        details: str,
        flight_number: Optional[str] = None,
        date: Optional[str] = None
    ) -> str:
        events = data.get("operational_events", [])

        last_id_numeric = 0
        if events:
            numeric_ids = []
            for e in events:
                event_id = e.get("event_id", "")
                if event_id.startswith("OE"):
                    try:
                        num_part = int(event_id[2:])
                        numeric_ids.append(num_part)
                    except ValueError:
                        continue

            if numeric_ids:
                last_id_numeric = max(numeric_ids)

        new_event_id = f"OE{last_id_numeric + 1:03d}"

        new_event = {
            "event_id": new_event_id,
            "event_type": event_type,
            "details": details,
            "status": "LOGGED",
            "airport_id": airport_id
        }

        if flight_number and date:
            new_event["flight"] = {
                "flight_number": flight_number,
                "date": date
            }

        events.append(new_event)
        return json.dumps(new_event)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_operational_event",
                "description": "Creates a new operational event log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "airport_id": {
                            "type": "string",
                            "description": "The unique airport ID where the event occurred."
                        },
                        "event_type": {
                            "type": "string",
                            "description": "The type of event (e.g., 'WEATHER_ALERT', 'MAINTENANCE')."
                        },
                        "details": {
                            "type": "string",
                            "description": "A detailed description of the event."
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Optional: The flight number this event is related to."
                        },
                        "date": {
                            "type": "string",
                            "description": "Optional: The date of the related flight in YYYY-MM-DD format."
                        }
                    },
                    "required": ["airport_id", "event_type", "details"]
                }
            }
        }
