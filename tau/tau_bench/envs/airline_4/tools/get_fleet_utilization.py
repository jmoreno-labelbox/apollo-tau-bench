from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetFleetUtilization(Tool):
    """API tool for obtaining the status of the aircraft fleet and metrics on utilization."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        model_filter: str | None = None,
        status_filter: list[str] | None = None,
    ) -> str:
        pass
        #Retrieve data about the aircraft
        aircraft_data = data.get("aircraft", [])

        if not aircraft_data:
            payload = {"error": "No aircraft data available"}
            out = json.dumps(payload)
            return out

        #Check the status filter for validity
        valid_statuses = ["Active", "Grounded", "Maintenance"]
        if status_filter:
            for status in status_filter:
                if status not in valid_statuses:
                    payload = {
                            "error": "Invalid status in status_filter",
                            "valid_statuses": valid_statuses,
                            "received": status,
                        }
                    out = json.dumps(
                        payload)
                    return out

        #Apply filters to aircraft
        filtered_aircraft = []
        for aircraft in aircraft_data:
            #Implement the model filter
            if model_filter:
                model_info = aircraft.get("model", {})
                if (
                    model_info.get("model_id") != model_filter
                    and model_info.get("model_name") != model_filter
                ):
                    continue

            #Implement the status filter
            if status_filter and aircraft.get("status") not in status_filter:
                continue

            filtered_aircraft.append(aircraft)

        #Compute statistics for the fleet
        total_aircraft = len(filtered_aircraft)
        status_breakdown = {}
        model_breakdown = {}
        location_breakdown = {}
        age_analysis = {"aircraft_ages": []}

        for aircraft in filtered_aircraft:
            #Analysis of status
            status = aircraft.get("status", "Unknown")
            status_breakdown[status] = status_breakdown.get(status, 0) + 1

            #Analysis of model
            model_info = aircraft.get("model", {})
            model_name = model_info.get("model_name", "Unknown")
            if model_name not in model_breakdown:
                model_breakdown[model_name] = {
                    "count": 0,
                    "model_id": model_info.get("model_id"),
                    "aircraft": [],
                }
            model_breakdown[model_name]["count"] += 1
            model_breakdown[model_name]["aircraft"].append(
                {
                    "aircraft_id": aircraft.get("aircraft_id"),
                    "tail_number": aircraft.get("tail_number"),
                    "status": aircraft.get("status"),
                }
            )

            #Analysis of location
            location = aircraft.get("location", {})
            location_key = location.get("iata_code", "Unknown")
            location_breakdown[location_key] = (
                location_breakdown.get(location_key, 0) + 1
            )

            #Calculation of age
            manufacture_date_str = aircraft.get("manufacture_date")
            if manufacture_date_str:
                try:
                    from datetime import date, datetime

                    manufacture_date = datetime.strptime(
                        manufacture_date_str, "%Y-%m-%d"
                    ).date()
                    today = date.today()
                    age_years = (today - manufacture_date).days / 365.25
                    age_analysis["aircraft_ages"].append(
                        {
                            "aircraft_id": aircraft.get("aircraft_id"),
                            "tail_number": aircraft.get("tail_number"),
                            "age_years": round(age_years, 1),
                            "manufacture_date": manufacture_date_str,
                        }
                    )
                except ValueError:
                    pass

        #Compute statistics related to age
        if age_analysis["aircraft_ages"]:
            ages = [a["age_years"] for a in age_analysis["aircraft_ages"]]
            age_analysis["statistics"] = {
                "average_age": round(sum(ages) / len(ages), 1),
                "oldest_aircraft": max(ages),
                "newest_aircraft": min(ages),
                "total_with_age_data": len(ages),
            }
        else:
            age_analysis["statistics"] = {
                "average_age": None,
                "oldest_aircraft": None,
                "newest_aircraft": None,
                "total_with_age_data": 0,
            }

        #Locate maintenance and operational events associated with the aircraft
        maintenance_logs = data.get("maintenance_logs", [])
        operational_events = data.get("operational_events", [])

        #Latest maintenance activities
        aircraft_ids = [a.get("aircraft_id") for a in filtered_aircraft]
        recent_maintenance = []

        for log in maintenance_logs:
            aircraft_info = log.get("aircraft", {})
            if aircraft_info.get("aircraft_id") in aircraft_ids:
                recent_maintenance.append(
                    {
                        "log_id": log.get("log_id"),
                        "aircraft_id": aircraft_info.get("aircraft_id"),
                        "tail_number": aircraft_info.get("tail_number"),
                        "maintenance_type": log.get("maintenance_type"),
                        "status": log.get("status"),
                        "event_timestamp_utc": log.get("event_timestamp_utc"),
                    }
                )

        #Organize by timestamp (latest first)
        recent_maintenance.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Latest operational events concerning the aircraft
        recent_aircraft_events = []

        for event in operational_events:
            aircraft_info = event.get("aircraft", {})
            if aircraft_info.get("aircraft_id") in aircraft_ids:
                recent_aircraft_events.append(
                    {
                        "event_id": event.get("event_id"),
                        "aircraft_id": aircraft_info.get("aircraft_id"),
                        "tail_number": aircraft_info.get("tail_number"),
                        "event_type": event.get("event_type"),
                        "status": event.get("status"),
                        "event_timestamp_utc": event.get("event_timestamp_utc"),
                    }
                )

        #Organize by timestamp (latest first)
        recent_aircraft_events.sort(
            key=lambda x: x.get("event_timestamp_utc", ""), reverse=True
        )

        #Compute percentages of utilization
        utilization_metrics = {
            "active_percentage": (
                round((status_breakdown.get("Active", 0) / total_aircraft * 100), 1)
                if total_aircraft > 0
                else 0
            ),
            "grounded_percentage": (
                round((status_breakdown.get("Grounded", 0) / total_aircraft * 100), 1)
                if total_aircraft > 0
                else 0
            ),
            "maintenance_percentage": (
                round(
                    (status_breakdown.get("Maintenance", 0) / total_aircraft * 100), 1
                )
                if total_aircraft > 0
                else 0
            ),
        }

        #Identify aircraft with problems (maintenance status or recent occurrences)
        aircraft_with_issues = []

        for aircraft in filtered_aircraft:
            issues = []
            aircraft_id = aircraft.get("aircraft_id")

            #Verify if under maintenance
            if aircraft.get("status") == "Maintenance":
                issues.append("Currently in maintenance")

            #Verify for recent operational occurrences
            aircraft_events = [
                e
                for e in recent_aircraft_events
                if e.get("aircraft_id") == aircraft_id and e.get("status") == "Active"
            ]
            if aircraft_events:
                issues.append(f"{len(aircraft_events)} active operational events")

            if issues:
                aircraft_with_issues.append(
                    {
                        "aircraft_id": aircraft_id,
                        "tail_number": aircraft.get("tail_number"),
                        "model": aircraft.get("model", {}),
                        "status": aircraft.get("status"),
                        "issues": issues,
                    }
                )

        #Formulate response
        response = {
            "search_criteria": {
                "model_filter": model_filter,
                "status_filter": status_filter,
            },
            "fleet_summary": {
                "total_aircraft": total_aircraft,
                "status_breakdown": status_breakdown,
                "utilization_metrics": utilization_metrics,
            },
            "model_analysis": model_breakdown,
            "location_distribution": location_breakdown,
            "age_analysis": age_analysis,
            "recent_activity": {
                "maintenance_logs": recent_maintenance[:10],  #Latest 10
                "operational_events": recent_aircraft_events[:10],  #Latest 10
            },
            "fleet_health": {
                "aircraft_with_issues": aircraft_with_issues,
                "total_with_issues": len(aircraft_with_issues),
            },
            "aircraft_details": filtered_aircraft,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFleetUtilization",
                "description": "Get comprehensive aircraft fleet status and utilization metrics including age analysis, location distribution, and operational health.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_filter": {
                            "type": "string",
                            "description": "Filter by aircraft model ID or model name (e.g., 'B737-800', '737-800'). Optional.",
                        },
                        "status_filter": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by aircraft status: 'Active', 'Grounded', 'Maintenance'. Optional.",
                        },
                    },
                    "required": [],
                },
            },
        }
