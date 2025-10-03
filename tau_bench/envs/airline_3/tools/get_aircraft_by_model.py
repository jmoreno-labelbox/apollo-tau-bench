from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetAircraftByModel(Tool):
    """
    A tool for retrieving all aircraft of a particular model.
    """

    @staticmethod
    def invoke(data: dict[str, Any], model_id: str) -> str:
        aircraft_list = data.get("aircraft", [])
        aircraft_models = data.get("aircraft_models", [])

        # Locate the model details
        model_info = None
        for model in aircraft_models:
            if model.get("model_id") == model_id:
                model_info = model
                break

        if not model_info:
            available_models = [model.get("model_id") for model in aircraft_models]
            payload = {
                "status": "Model not found",
                "model_id": model_id,
                "available_models": available_models,
            }
            out = json.dumps(payload)
            return out

        # Retrieve all aircraft corresponding to this model
        model_aircraft = []
        for aircraft in aircraft_list:
            if aircraft.get("model", {}).get("model_id") == model_id:
                model_aircraft.append(
                    {
                        "aircraft_id": aircraft.get("aircraft_id"),
                        "tail_number": aircraft.get("tail_number"),
                        "status": aircraft.get("status"),
                        "manufacture_date": aircraft.get("manufacture_date"),
                        "location": aircraft.get("location", {}).get("iata_code"),
                    }
                )

        # Determine statistics
        total_count = len(model_aircraft)
        active_count = len(
            [ac for ac in model_aircraft if ac.get("status") == "Active"]
        )

        response = {
            "model_info": {
                "model_id": model_info.get("model_id"),
                "manufacturer": model_info.get("manufacturer"),
                "model_name": model_info.get("model_name"),
                "passenger_capacity": model_info.get("passenger_capacity"),
            },
            "fleet_statistics": {
                "total_aircraft": total_count,
                "active_aircraft": active_count,
                "inactive_aircraft": total_count - active_count,
            },
            "aircraft": model_aircraft,
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAircraftByModel",
                "description": "Get all aircraft of a specific model with fleet statistics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_id": {
                            "type": "string",
                            "description": "The aircraft model ID (e.g., B737-800, A320neo).",
                        }
                    },
                    "required": ["model_id"],
                },
            },
        }
