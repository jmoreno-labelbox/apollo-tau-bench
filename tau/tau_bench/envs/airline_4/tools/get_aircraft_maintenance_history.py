from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAircraftMaintenanceHistory(Tool):
    """API tool for retrieving maintenance logs for a specific aircraft using aircraft_id or tail_number."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str | None = None,
        tail_number: str | None = None,
    ) -> str:
        pass
        #Ensure that at least one parameter is supplied
        if not aircraft_id and not tail_number:
            payload = {
                    "error": "Missing required parameter",
                    "required": "Either aircraft_id or tail_number must be provided",
                }
            out = json.dumps(
                payload)
            return out

        #Locate the aircraft initially to confirm its existence and obtain both identifiers
        aircraft_data = data.get("aircraft", [])
        target_aircraft = None

        for aircraft in aircraft_data:
            if (aircraft_id and aircraft.get("aircraft_id") == aircraft_id) or (
                tail_number and aircraft.get("tail_number") == tail_number
            ):
                target_aircraft = aircraft
                break

        if not target_aircraft:
            payload = {
                    "error": "Aircraft not found",
                    "aircraft_id": aircraft_id,
                    "tail_number": tail_number,
                }
            out = json.dumps(
                payload)
            return out

        #Retrieve both identifiers for a thorough search
        target_aircraft_id = target_aircraft.get("aircraft_id")
        target_tail_number = target_aircraft.get("tail_number")

        #Locate all maintenance records for this aircraft
        maintenance_logs = data.get("maintenance_logs", [])
        aircraft_maintenance = []

        for log in maintenance_logs:
            aircraft_info = log.get("aircraft", {})
            log_aircraft_id = aircraft_info.get("aircraft_id")
            log_tail_number = aircraft_info.get("tail_number")

            #Identify using either aircraft_id or tail_number
            if (
                log_aircraft_id == target_aircraft_id
                or log_tail_number == target_tail_number
            ):
                #Establish a detailed maintenance record
                maintenance_record = {
                    "log_id": log.get("log_id"),
                    "event_timestamp_utc": log.get("event_timestamp_utc"),
                    "maintenance_type": log.get("maintenance_type"),
                    "description": log.get("description"),
                    "status": log.get("status"),
                    "technician_id": log.get("technician_id"),
                    "work_order_id": log.get("work_order_id"),
                    "ata_chapter": log.get("ata_chapter"),
                    "corrective_action": log.get("corrective_action"),
                    "mel_cdl_reference": log.get("mel_cdl_reference"),
                    "next_due": log.get("next_due"),
                }

                aircraft_maintenance.append(maintenance_record)

        #Organize maintenance logs by timestamp (latest first)
        aircraft_maintenance.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Compute summary statistics
        total_maintenance_events = len(aircraft_maintenance)
        maintenance_types = {}
        status_counts = {}
        latest_maintenance = aircraft_maintenance[0] if aircraft_maintenance else None

        for record in aircraft_maintenance:
            #Tally by type of maintenance
            mtype = record.get("maintenance_type", "Unknown")
            maintenance_types[mtype] = maintenance_types.get(mtype, 0) + 1

            #Tally by status
            status = record.get("status", "Unknown")
            status_counts[status] = status_counts.get(status, 0) + 1

        #Locate the upcoming scheduled maintenance
        next_scheduled = None
        for record in aircraft_maintenance:
            if record.get("status") == "Scheduled":
                if not next_scheduled or record.get(
                    "event_timestamp_utc", ""
                ) < next_scheduled.get("event_timestamp_utc", ""):
                    next_scheduled = record

        #Identify any overdue maintenance (status is Scheduled but timestamp is past)
        overdue_maintenance = []
        from datetime import datetime

        current_time = datetime(2025, 9, 15, 0, 0, 0).isoformat().replace("+00:00", "Z")

        for record in aircraft_maintenance:
            if (
                record.get("status") == "Scheduled"
                and record.get("event_timestamp_utc", "") < current_time
            ):
                overdue_maintenance.append(record)

        #Formulate a detailed response
        response = {
            "aircraft": {
                "aircraft_id": target_aircraft.get("aircraft_id"),
                "tail_number": target_aircraft.get("tail_number"),
                "model": target_aircraft.get("model"),
                "status": target_aircraft.get("status"),
                "location": target_aircraft.get("location"),
            },
            "maintenance_summary": {
                "total_maintenance_events": total_maintenance_events,
                "maintenance_types": maintenance_types,
                "status_counts": status_counts,
                "latest_maintenance": latest_maintenance,
                "next_scheduled": next_scheduled,
                "overdue_count": len(overdue_maintenance),
            },
            "maintenance_history": aircraft_maintenance,
        }

        if overdue_maintenance:
            response["overdue_maintenance"] = overdue_maintenance
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftMaintenanceHistory",
                "description": "Get comprehensive maintenance logs and history for a specific aircraft by aircraft_id or tail_number. Returns maintenance records, summary statistics, and scheduling information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Unique aircraft identifier (e.g., 'AC001', 'AC004'). Either aircraft_id or tail_number must be provided.",
                        },
                        "tail_number": {
                            "type": "string",
                            "description": "Aircraft registration/tail number (e.g., 'PR-GOL', 'PS-AEF'). Either aircraft_id or tail_number must be provided.",
                        },
                    },
                    "required": [],
                },
            },
        }
