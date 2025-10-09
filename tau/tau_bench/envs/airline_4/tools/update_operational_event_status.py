from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateOperationalEventStatus(Tool):
    """API tool for revising the status and details of operational events."""

    @staticmethod
    def invoke(
        data: dict[str, Any], event_id: str, status: str, details: str | None = None
    ) -> str:
        pass
        #Check that necessary parameters are valid
        if not event_id or not status:
            payload = {
                    "error": "Missing required parameters",
                    "required": ["event_id", "status"],
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

        #Locate the operational event
        operational_events = data.get("operational_events", {}).values()
        target_event = None
        event_index = None

        for i, event in enumerate(operational_events.values()):
            if event.get("event_id") == event_id:
                target_event = event
                event_index = i
                break

        if not target_event:
            payload = {"error": "Operational event not found", "event_id": event_id}
            out = json.dumps(
                payload)
            return out

        #Retain original values for the response
        original_status = target_event.get("status")
        target_event.get("details")
        updates_made = []

        #Revise the status
        target_event["status"] = status
        updates_made.append("status")

        #Revise details if supplied
        if details is not None:
            target_event["details"] = details
            updates_made.append("details")

        #Revise the event within the database
        data["operational_events"][event_index] = target_event

        #Retrieve information about associated entities for a more detailed response
        flight_info = target_event.get("flight")
        aircraft_info = target_event.get("aircraft")
        airport_info = target_event.get("airport")

        #Formulate response
        response = {
            "success": True,
            "message": "Operational event updated successfully",
            "event_id": event_id,
            "status_change": {"from": original_status, "to": status},
            "updates_made": updates_made,
            "updated_event": target_event,
        }

        #Include association details if accessible
        if flight_info:
            response["flight"] = flight_info
        if aircraft_info:
            response["aircraft"] = aircraft_info
        if airport_info:
            response["airport"] = airport_info
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateOperationalEventStatus",
                "description": "Update operational event status and details. Allows changing event status between Active, Resolved, and Monitoring states with optional detail updates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {
                            "type": "string",
                            "description": "Unique operational event identifier (e.g., 'OE001', 'OE025')",
                        },
                        "status": {
                            "type": "string",
                            "description": "Updated event status: 'Active', 'Resolved', or 'Monitoring'",
                        },
                        "details": {
                            "type": "string",
                            "description": "Updated event details or description (optional)",
                        },
                    },
                    "required": ["event_id", "status"],
                },
            },
        }
