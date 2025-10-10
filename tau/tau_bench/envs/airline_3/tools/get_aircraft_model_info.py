# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAircraftModelInfo(Tool):
    """
    API tool to get detailed specifications for aircraft models including performance metrics, capacity, and technical specifications.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], model_id: str = None) -> str:
        if not model_id:
            return json.dumps({
                "status": "Missing required parameter",
                "required": "model_id"
            })

        aircraft_models = data.get("aircraft_models", [])
        target_model = None

        for model in aircraft_models:
            if model.get("model_id") == model_id:
                target_model = model
                break

        if not target_model:
            # Aircraft model not found - return helpful information instead of error
            available_models = [model.get("model_id") for model in aircraft_models]
            response = {
                "status": "aircraft_model_not_available",
                "requested_model_id": model_id,
                "message": f"Aircraft model '{model_id}' is not available in the current system",
                "available_aircraft_models": available_models,
                "suggestions": {
                    "message": f"Available aircraft models: {', '.join(available_models)}",
                    "note": "Common aircraft models include B737-800, A320neo, B787-9, A350-900"
                }
            }
            return json.dumps(response, indent=2)

        # Get aircraft instances using this model
        aircraft = list(data.get("aircraft", {}).values())
        model_aircraft = []
        for ac in aircraft:
            if ac.get("model_id") == model_id:
                model_aircraft.append({
                    "aircraft_id": ac.get("aircraft_id"),
                    "tail_number": ac.get("tail_number"),
                    "status": ac.get("status"),
                    "current_location": ac.get("current_location", {}).get("iata_code")
                })

        # Calculate fleet statistics
        total_fleet_size = len(model_aircraft)
        operational_count = len([ac for ac in model_aircraft if ac.get("status") == "operational"])
        maintenance_count = len([ac for ac in model_aircraft if ac.get("status") == "maintenance"])
        grounded_count = len([ac for ac in model_aircraft if ac.get("status") == "grounded"])

        response = {
            "model_id": target_model.get("model_id"),
            "manufacturer": target_model.get("manufacturer"),
            "model_name": target_model.get("model_name"),
            "specifications": {
                "passenger_capacity": target_model.get("passenger_capacity"),
                "cargo_capacity_kg": target_model.get("cargo_capacity_kg"),
                "maximum_takeoff_weight_kg": target_model.get("maximum_takeoff_weight_kg"),
                "range_km": target_model.get("range_km"),
                "engine_type": target_model.get("engine_type")
            },
            "fleet_status": {
                "total_fleet_size": total_fleet_size,
                "operational": operational_count,
                "maintenance": maintenance_count,
                "grounded": grounded_count
            },
            "aircraft_instances": model_aircraft
        }

        # Add performance metrics if available
        if target_model.get("range_km"):
            response["performance_metrics"] = {
                "range_miles": round(target_model.get("range_km") * 0.621371, 1),
                "range_nautical_miles": round(target_model.get("range_km") * 0.539957, 1),
                "max_takeoff_weight_lbs": round(target_model.get("maximum_takeoff_weight_kg") * 2.20462, 1),
                "cargo_capacity_lbs": round(target_model.get("cargo_capacity_kg") * 2.20462, 1)
            }

        return json.dumps(response, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_aircraft_model_info",
                "description": "Get detailed specifications for aircraft models including performance metrics, capacity, technical specifications, and fleet status. Returns comprehensive data about aircraft capabilities, operational parameters, and fleet management information. If the requested aircraft model is not available, provides helpful information about available models.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_id": {
                            "type": "string",
                            "description": "Aircraft model identifier"
                        }
                    },
                    "required": ["model_id"]
                }
            }
        }
