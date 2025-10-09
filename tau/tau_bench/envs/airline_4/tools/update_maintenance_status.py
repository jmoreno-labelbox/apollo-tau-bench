from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateMaintenanceStatus(Tool):
    """API tool for revising maintenance status and completion details."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_id: str,
        status: str,
        corrective_action: str | None = None,
        next_due: str | None = None,
        mel_cdl_reference: str | None = None,
        technician_id: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that necessary parameters are valid
        if not log_id or not status:
            payload = {
                    "error": "Missing required parameters",
                    "required": ["log_id", "status"],
                }
            out = json.dumps(
                payload)
            return out

        #Check the status for validity
        valid_statuses = ["Scheduled", "In Progress", "Completed", "Deferred"]
        if status not in valid_statuses:
            payload = {
                    "error": "Invalid status",
                    "valid_statuses": valid_statuses,
                    "received": status,
                }
            out = json.dumps(
                payload)
            return out

        #Locate the maintenance entry
        maintenance_logs = data.get("maintenance_logs", [])
        target_entry = None
        entry_index = None

        for i, entry in enumerate(maintenance_logs):
            if entry.get("log_id") == log_id:
                target_entry = entry
                entry_index = i
                break

        if not target_entry:
            payload = {"error": "Maintenance entry not found", "log_id": log_id}
            out = json.dumps(
                payload)
            return out

        #Retain the original status for comparison
        original_status = target_entry.get("status")
        updates_made = []

        #Revise the status
        target_entry["status"] = status
        updates_made.append("status")

        #Revise the corrective action if supplied
        if corrective_action is not None:
            target_entry["corrective_action"] = corrective_action
            updates_made.append("corrective_action")

        #Revise the technician if supplied
        if technician_id is not None:
            target_entry["technician_id"] = technician_id
            updates_made.append("technician_id")

        #Revise the MEL/CDL reference if supplied
        if mel_cdl_reference is not None:
            target_entry["mel_cdl_reference"] = mel_cdl_reference
            updates_made.append("mel_cdl_reference")

        #Note: completion_timestamp_utc is excluded from the database schema, thus not processed

        #Revise the next due date if supplied
        if next_due is not None:
            if next_due:  #String that is not empty
                try:
                    datetime.strptime(next_due, "%Y-%m-%d")
                    target_entry["next_due"] = next_due
                except ValueError:
                    payload = {
                            "error": "Invalid next_due format. Expected YYYY-MM-DD",
                            "received": next_due,
                        }
                    out = json.dumps(
                        payload)
                    return out
            else:  #String that is empty or None
                target_entry["next_due"] = None
            updates_made.append("next_due")

        #Revise the entry within the database
        data["maintenance_logs"][entry_index] = target_entry

        #Retrieve information about the aircraft
        aircraft_info = target_entry.get("aircraft", {})
        aircraft_data = data.get("aircraft", [])
        full_aircraft_info = None

        for aircraft in aircraft_data:
            if aircraft.get("aircraft_id") == aircraft_info.get("aircraft_id"):
                full_aircraft_info = aircraft
                break

        #Formulate response
        response = {
            "success": True,
            "message": "Maintenance status updated successfully",
            "log_id": log_id,
            "status_change": {"from": original_status, "to": status},
            "updates_made": updates_made,
            "updated_entry": target_entry,
        }

        if full_aircraft_info:
            response["aircraft"] = {
                "aircraft_id": full_aircraft_info.get("aircraft_id"),
                "tail_number": full_aircraft_info.get("tail_number"),
                "model": full_aircraft_info.get("model"),
                "status": full_aircraft_info.get("status"),
            }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMaintenanceStatus",
                "description": "Update maintenance status and details. Allows updating status, corrective actions, and scheduling information for existing maintenance entries.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {
                            "type": "string",
                            "description": "Unique maintenance log identifier (e.g., 'ML001', 'ML005')",
                        },
                        "status": {
                            "type": "string",
                            "description": "Updated maintenance status: 'Scheduled', 'In Progress', 'Completed', or 'Deferred'",
                        },
                        "corrective_action": {
                            "type": "string",
                            "description": "Updated description of corrective action taken or to be taken",
                        },
                        "next_due": {
                            "type": "string",
                            "description": "Next maintenance due date in YYYY-MM-DD format. Set to empty string or null to clear.",
                        },
                        "mel_cdl_reference": {
                            "type": "string",
                            "description": "MEL/CDL reference if applicable (e.g., 'MEL-72-001'). Set to empty string or null to clear.",
                        },
                        "technician_id": {
                            "type": "string",
                            "description": "Updated technician ID if reassignment is needed (e.g., 'TECH025')",
                        },
                    },
                    "required": ["log_id", "status"],
                },
            },
        }
