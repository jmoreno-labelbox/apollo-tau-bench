from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMaintenanceLogs(Tool):
    """
    API tool for retrieving maintenance logs for aircraft and equipment.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        aircraft_id: str = None,
        maintenance_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> str:
        from datetime import datetime
        import json

        # First, check the validity of date parameters
        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            except ValueError:
                payload = {
                    "status": "invalid_date",
                    "message": "Invalid start_date format. Expected YYYY-MM-DD",
                    "received": start_date,
                }
                out = json.dumps(payload)
                return out

        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                payload = {
                    "status": "invalid_date",
                    "message": "Invalid end_date format. Expected YYYY-MM-DD",
                    "received": end_date,
                }
                out = json.dumps(payload)
                return out

            # Check the validity of the date range
            if start_date and end_date_obj < start_date_obj:
                payload = {
                    "status": "invalid_date_range",
                    "message": "end_date cannot be before start_date",
                    "start_date": start_date,
                    "end_date": end_date,
                }
                out = json.dumps(payload)
                return out

        maintenance_logs = data.get("maintenance_logs", {}).values()
        filtered_logs = []

        for log in maintenance_logs.values():
            # Implement aircraft filtering
            if aircraft_id and log.get("aircraft_id") != aircraft_id:
                continue

            # Implement maintenance type filtering
            if maintenance_type and log.get("type") != maintenance_type:
                continue

            # Implement date filtering
            if start_date:
                try:
                    log_date = datetime.strptime(log.get("date", ""), "%Y-%m-%d").date()
                    if log_date < start_date_obj:
                        continue
                except ValueError:
                    continue

            if end_date:
                try:
                    log_date = datetime.strptime(log.get("date", ""), "%Y-%m-%d").date()
                    if log_date > end_date_obj:
                        continue
                except ValueError:
                    continue

            filtered_logs.append(log)

        # Arrange by date (most recent first)
        filtered_logs.sort(key=lambda x: x.get("date", ""), reverse=True)

        response = {
            "filters_applied": {
                "aircraft_id": aircraft_id,
                "maintenance_type": maintenance_type,
                "start_date": start_date,
                "end_date": end_date,
            },
            "total_logs_found": len(filtered_logs),
            "maintenance_logs": filtered_logs,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMaintenanceLogs",
                "description": "Get maintenance logs for aircraft and equipment with optional filtering by aircraft, type, and date range. Returns detailed maintenance records including aircraft status, maintenance schedules, and compliance tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Optional aircraft identifier to filter logs. Format: AC followed by 3-digit number.",
                        },
                        "maintenance_type": {
                            "type": "string",
                            "description": "Optional maintenance type filter. Different types have different compliance requirements.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Optional start date filter in YYYY-MM-DD format",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Optional end date filter in YYYY-MM-DD format",
                        },
                    },
                    "required": [],
                },
            },
        }
