# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMaintenanceLogs(Tool):
    """
    API tool to get maintenance logs for aircraft and equipment.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        aircraft_id: str = None,
        maintenance_type: str = None,
        start_date: str = None,
        end_date: str = None
    ) -> str:
        from datetime import datetime

        # First, verify the date parameters.
        if start_date:
            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
            except ValueError:
                return json.dumps({
                    "status": "invalid_date",
                    "message": "Invalid start_date format. Expected YYYY-MM-DD",
                    "received": start_date
                })

        if end_date:
            try:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return json.dumps({
                    "status": "invalid_date",
                    "message": "Invalid end_date format. Expected YYYY-MM-DD",
                    "received": end_date
                })
            
            # Check the validity of the date range.
            if start_date and end_date_obj < start_date_obj:
                return json.dumps({
                    "status": "invalid_date_range",
                    "message": "end_date cannot be before start_date",
                    "start_date": start_date,
                    "end_date": end_date
                })

        maintenance_logs = data.get("maintenance_logs", [])
        filtered_logs = []

        for log in maintenance_logs:
            # Implement aircraft filtering.
            if aircraft_id and log.get("aircraft_id") != aircraft_id:
                continue

            # Implement filter for maintenance types.
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

        # Order by date with the latest first.
        filtered_logs.sort(key=lambda x: x.get("date", ""), reverse=True)

        response = {
            "filters_applied": {
                "aircraft_id": aircraft_id,
                "maintenance_type": maintenance_type,
                "start_date": start_date,
                "end_date": end_date
            },
            "total_logs_found": len(filtered_logs),
            "maintenance_logs": filtered_logs
        }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_maintenance_logs",
                "description": "Get maintenance logs for aircraft and equipment with optional filtering by aircraft, type, and date range. Returns detailed maintenance records including aircraft status, maintenance schedules, and compliance tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "aircraft_id": {
                            "type": "string",
                            "description": "Optional aircraft identifier to filter logs. Format: AC followed by 3-digit number."
                        },
                        "maintenance_type": {
                            "type": "string",
                            "description": "Optional maintenance type filter. Different types have different compliance requirements."
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Optional start date filter in YYYY-MM-DD format"
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Optional end date filter in YYYY-MM-DD format"
                        }
                    },
                    "required": []
                }
            }
        }
