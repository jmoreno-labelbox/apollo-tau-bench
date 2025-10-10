# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateMaintenanceLog(Tool):
    """
    A tool to create a new maintenance log entry.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], aircraft_id: str, maintenance_type: str, description: str, technician_id: str, event_date: str, status: str, work_order_id: str) -> str:
        logs = data.get("maintenance_logs", [])
        aircraft_list = list(data.get("aircraft", {}).values())

        target_aircraft = next((a for a in aircraft_list if a.get("aircraft_id") == aircraft_id), None)
        if not target_aircraft:
            return json.dumps({"error": "Aircraft not found", "aircraft_id": aircraft_id})

        last_id_numeric = 0
        if logs:
            numeric_ids = []
            for log in logs:
                log_id = log.get("log_id", "")
                if log_id.startswith("ML"):
                    try:
                        num_part = int(log_id[2:])
                        numeric_ids.append(num_part)
                    except ValueError:
                        continue

            if numeric_ids:
                last_id_numeric = max(numeric_ids)

        new_log_id = f"ML{last_id_numeric + 1:03d}"


        new_log = {
            "log_id": new_log_id,
            "aircraft": {
                "aircraft_id": target_aircraft["aircraft_id"],
                "tail_number": target_aircraft["tail_number"]
            },
            "event_timestamp_utc": event_date+"T00:00:00Z",
            "maintenance_type": maintenance_type,
            "description": description,
            "status": status,
            "technician_id": technician_id,
            "work_order_id": work_order_id
        }
        logs.append(new_log)
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_maintenance_log",
                "description": "Creates a new log entry for aircraft maintenance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {"type": "string", "description": "The unique ID of the aircraft."},
                        "maintenance_type": {"type": "string", "description": "Type of maintenance (e.g., 'UNSCHEDULED', 'A_CHECK')."},
                        "description": {"type": "string", "description": "A detailed description of the maintenance task."},
                        "technician_id": {"type": "string", "description": "The ID of the technician assigned."},
                        "event_date": {"type": "string", "description": "The date of the maintenance event in YYYY-MM-DD format."},
                        "status": {"type": "string", "description": "The current status of the maintenance (e.g., 'Scheduled', 'Completed')."},
                        "work_order_id": {"type": "string", "description": "The associated work order ID."}
                    },
                    "required": [
                        "aircraft_id", "maintenance_type", "description", "technician_id",
                        "event_date", "status", "work_order_id"
                    ]
                }
            }
        }
