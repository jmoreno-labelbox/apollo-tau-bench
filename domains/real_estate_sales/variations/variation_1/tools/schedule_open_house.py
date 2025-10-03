from tau_bench.envs.tool import Tool
import json
from typing import Any

class ScheduleOpenHouse(Tool):
    """Plan an open house event for a property."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None, date: str = None, start_time: str = None, end_time: str = None) -> str:
        if not all([property_id, date, start_time, end_time]):
            payload = {"error": "property_id, date, start_time, and end_time are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Verify if the property is listed
        listings = data.get("listings", [])
        property_exists = any(l.get("property_id") == property_id for l in listings)

        if not property_exists:
            payload = {"error": f"Property {property_id} not found in listings"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Generate an open house entry (would be stored in database in a real system)
        open_house = {
            "property_id": property_id,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "status": "scheduled",
            "created_at": "2024-08-21T00:00:00Z",
        }
        payload = {
                "success": True,
                "message": f"Open house scheduled for property {property_id}",
                "open_house": open_house,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scheduleOpenHouse",
                "description": "Schedule an open house event for a property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to schedule open house for",
                        },
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format",
                        },
                        "start_time": {
                            "type": "string",
                            "description": "Start time in HH:MM format",
                        },
                        "end_time": {
                            "type": "string",
                            "description": "End time in HH:MM format",
                        },
                    },
                    "required": ["property_id", "date", "start_time", "end_time"],
                },
            },
        }
