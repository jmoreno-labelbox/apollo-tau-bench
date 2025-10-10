# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")
        id = "WEATHER_FORECAST_001"
        weather_forecast_json = {
            "forecast_id": id,
            "raw_json_path_nullable": f"/data/raw/weather_forecast_{id}.json",
        }
        list(data.get("weather_forecasts", {}).values()).append(weather_forecast_json)
        return json.dumps(weather_forecast_json)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetWeatherForecast",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "number",
                            "description": "The latitude of the forecast location.",
                        },
                        "longitude": {
                            "type": "number",
                            "description": "The longitude of the forecast location.",
                        },
                        "horizon_days": {
                            "type": "integer",
                            "description": "The number of days to forecast.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                },
            },
        }
