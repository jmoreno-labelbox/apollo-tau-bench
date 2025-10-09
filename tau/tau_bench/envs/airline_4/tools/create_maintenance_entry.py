from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateMaintenanceEntry(Tool):
    """API tool for recording new maintenance activities for aircraft."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str,
        maintenance_type: str,
        description: str,
        work_order_id: str,
        ata_chapter: str,
        corrective_action: str,
        event_timestamp_utc: str,
        technician_id: str | None = None,
        status: str = "Scheduled",
        mel_cdl_reference: str | None = None,
        next_due: str | None = None,
    ) -> str:
        pass
        from datetime import datetime

        #Check that necessary parameters are valid
        required_params = [
            "aircraft_id",
            "maintenance_type",
            "description",
            "work_order_id",
            "ata_chapter",
            "corrective_action",
            "event_timestamp_utc",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        for param in required_params:
            if not params_dict.get(param):
                payload = {"error": "Missing required parameter", "required": param}
                out = json.dumps(
                    payload)
                return out

        #Create technician_id if not supplied (deterministic based on aircraft and timestamp)
        if not technician_id:
            #Establish a deterministic technician assignment based on the aircraft and work order
            import hashlib

            seed = f"{aircraft_id}_{work_order_id}"
            hash_value = int(hashlib.md5(seed.encode()).hexdigest()[:4], 16)
            technician_number = (hash_value % 50) + 1  #Create identifiers from TECH001 to TECH050
            technician_id = f"TECH{technician_number:03d}"

        #Confirm the aircraft is present
        aircraft_data = data.get("aircraft", [])
        target_aircraft = None

        for aircraft in aircraft_data:
            if aircraft.get("aircraft_id") == aircraft_id:
                target_aircraft = aircraft
                break

        if not target_aircraft:
            payload = {"error": "Aircraft not found", "aircraft_id": aircraft_id}
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

        #Confirm the maintenance_type is valid
        valid_maintenance_types = [
            "A-Check",
            "B-Check",
            "C-Check",
            "D-Check",
            "Line Maintenance",
            "Engine Repair",
            "Avionics Repair",
            "Structural Repair",
            "Avionics Update",
            "Emergency Repair",
            "Unscheduled",
        ]
        if maintenance_type not in valid_maintenance_types:
            payload = {
                    "error": "Invalid maintenance type",
                    "valid_maintenance_types": valid_maintenance_types,
                    "received": maintenance_type,
                }
            out = json.dumps(
                payload)
            return out

        #Check the format of event_timestamp_utc (now required)
        try:
            datetime.fromisoformat(event_timestamp_utc.replace("Z", "+00:00"))
        except ValueError:
            payload = {
                    "error": "Invalid event_timestamp_utc format. Expected ISO format with Z suffix (e.g., '2024-07-28T10:00:00Z')",
                    "received": event_timestamp_utc,
                }
            out = json.dumps(
                payload)
            return out

        #Check the format of next_due if supplied
        if next_due:
            try:
                datetime.strptime(next_due, "%Y-%m-%d")
            except ValueError:
                payload = {
                        "error": "Invalid next_due format. Expected YYYY-MM-DD",
                        "received": next_due,
                    }
                out = json.dumps(
                    payload)
                return out

        #Create a unique identifier for the maintenance log
        maintenance_logs = data.get("maintenance_logs", [])
        existing_numbers = []

        #Obtain existing log numbers
        for log in maintenance_logs:
            log_id = log.get("log_id", "")
            if log_id.startswith("ML") and len(log_id) == 5:
                try:
                    number = int(log_id[2:])  #Retrieve the number portion following "ML"
                    existing_numbers.append(number)
                except ValueError:
                    continue

        #Determine the next available number (highest + 1)
        next_number = max(existing_numbers) + 1 if existing_numbers else 1
        log_id = f"ML{next_number:03d}"

        #Confirm that the work_order_id is unique
        existing_work_orders = [log.get("work_order_id") for log in maintenance_logs]
        if work_order_id in existing_work_orders:
            payload = {
                    "error": "Work order ID already exists",
                    "work_order_id": work_order_id,
                    "existing_work_orders": existing_work_orders,
                }
            out = json.dumps(
                payload)
            return out

        #Establish a maintenance entry
        maintenance_entry = {
            "log_id": log_id,
            "aircraft": {
                "aircraft_id": target_aircraft.get("aircraft_id"),
                "tail_number": target_aircraft.get("tail_number"),
            },
            "event_timestamp_utc": event_timestamp_utc,
            "maintenance_type": maintenance_type,
            "description": description,
            "status": status,
            "technician_id": technician_id,
            "work_order_id": work_order_id,
            "ata_chapter": ata_chapter,
            "corrective_action": corrective_action,
            "mel_cdl_reference": mel_cdl_reference,
            "next_due": next_due,
        }

        #Include in the maintenance logs
        if "maintenance_logs" not in data:
            data["maintenance_logs"] = []
        data["maintenance_logs"].append(maintenance_entry)

        #Formulate response
        response = {
            "success": True,
            "message": "Maintenance entry created successfully",
            "maintenance_entry": maintenance_entry,
            "aircraft": {
                "aircraft_id": target_aircraft.get("aircraft_id"),
                "tail_number": target_aircraft.get("tail_number"),
                "model": target_aircraft.get("model"),
                "status": target_aircraft.get("status"),
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMaintenanceEntry",
                "description": "Log new maintenance activity for aircraft. Creates a maintenance record with all required details including work orders, technician assignments, and scheduling information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Unique aircraft identifier (e.g., 'AC001', 'AC004')",
                        },
                        "maintenance_type": {
                            "type": "string",
                            "description": "Type of maintenance: 'A-Check', 'B-Check', 'C-Check', 'D-Check', 'Line Maintenance', 'Engine Repair', 'Avionics Repair', 'Structural Repair', 'Avionics Update', 'Emergency Repair'",
                        },
                        "description": {
                            "type": "string",
                            "description": "Detailed description of the maintenance activity",
                        },
                        "technician_id": {
                            "type": "string",
                            "description": "ID of the assigned technician (e.g., 'TECH012'). If not provided, will be auto-assigned deterministically.",
                        },
                        "work_order_id": {
                            "type": "string",
                            "description": "Unique work order reference (e.g., 'WO-2024-07-28-001')",
                        },
                        "ata_chapter": {
                            "type": "string",
                            "description": "ATA chapter reference (e.g., '05', '72', '34')",
                        },
                        "corrective_action": {
                            "type": "string",
                            "description": "Detailed description of corrective action to be taken or performed",
                        },
                        "event_timestamp_utc": {
                            "type": "string",
                            "description": "Maintenance event timestamp in UTC (ISO format with Z suffix, e.g., '2024-07-28T10:00:00Z'). Required for deterministic behavior.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Initial maintenance status: 'Scheduled', 'In Progress', 'Completed', or 'Deferred'. Defaults to 'Scheduled'.",
                        },
                        "mel_cdl_reference": {
                            "type": "string",
                            "description": "MEL/CDL reference if applicable (e.g., 'MEL-72-001')",
                        },
                        "next_due": {
                            "type": "string",
                            "description": "Next maintenance due date in YYYY-MM-DD format (optional)",
                        },
                    },
                    "required": [
                        "aircraft_id",
                        "maintenance_type",
                        "description",
                        "work_order_id",
                        "ata_chapter",
                        "corrective_action",
                        "event_timestamp_utc",
                    ],
                },
            },
        }
