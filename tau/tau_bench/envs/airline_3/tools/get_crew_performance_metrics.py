# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewPerformanceMetrics(Tool):
    """
    API tool to get crew member performance metrics and statistics.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str = None) -> str:
        if not crew_id:
            return json.dumps({
                "status": "missing_parameter",
                "message": "The crew_id parameter is required to retrieve crew performance metrics.",
                "required": "crew_id"
            })

        crew_members = data.get("crew_members", [])
        target_crew = None

        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                target_crew = crew
                break

        if not target_crew:
            return json.dumps({
                "status": "not_found",
                "message": f"No crew member found with ID '{crew_id}'. Please check the crew ID and try again.",
                "crew_id": crew_id
            })

        # Create performance indicators from crew information.
        flight_hours = target_crew.get("flight_hours", 0)
        flights_completed = target_crew.get("flights_completed", 0)
        on_time_performance = target_crew.get("on_time_performance", 95.0)
        customer_satisfaction = target_crew.get("customer_satisfaction", 4.5)
        safety_incidents = target_crew.get("safety_incidents", 0)

        performance_metrics = {
            "crew_id": crew_id,
            "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "role": target_crew.get("role", ""),
            "metrics": {
                "flight_hours": flight_hours,
                "flights_completed": flights_completed,
                "on_time_performance": f"{on_time_performance}%",
                "customer_satisfaction": f"{customer_satisfaction}/5.0",
                "safety_incidents": safety_incidents,
                "performance_rating": "Excellent" if on_time_performance >= 98 and customer_satisfaction >= 4.7 else "Good" if on_time_performance >= 95 and customer_satisfaction >= 4.3 else "Average"
            }
        }

        return json.dumps({
            "status": "success",
            "performance_metrics": performance_metrics
        })

    def get_info(self):
        return {
            "type": "function",
            "function": {
                "name": "get_crew_performance_metrics",
                "description": "Get crew member performance metrics and statistics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew member ID."}
                    },
                    "required": ["crew_id"]
                }
            }
        }
