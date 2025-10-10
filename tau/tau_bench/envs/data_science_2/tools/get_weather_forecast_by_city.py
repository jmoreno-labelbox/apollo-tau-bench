# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWeatherForecastByCity(Tool):
    """
    Retrieves a weather_forecasts record by city and horizon_days.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], city: str, horizon_days: int) -> str:
        rows = list(data.get("weather_forecasts", {}).values())
        for row in rows:
            if row.get("city") == city and row.get("horizon_days") == horizon_days:
                return json.dumps(row)
        return json.dumps({"error": "weather forecast not found", "city": city, "horizon_days": horizon_days})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_weather_forecast_by_city",
                "description": "Retrieves weather_forecasts by city and exact horizon_days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "horizon_days": {"type": "integer"}
                    },
                    "required": ["city", "horizon_days"]
                }
            }
        }
