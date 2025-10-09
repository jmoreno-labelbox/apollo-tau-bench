from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetWeatherForecast(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        city: str = None,
        city_name: str = None,
        latitude: Any = None
    ) -> str:
        # Accept either city or city_name
        if city_name is not None:
            city = city_name
        id = "WEATHER_FORECAST_001"
        weather_forecast_json = {
            "forecast_id": id,
            "raw_json_path_nullable": f"/data/raw/weather_forecast_{id}.json",
        }
        data.get("weather_forecasts", []).append(weather_forecast_json)
        payload = weather_forecast_json
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setWeatherForecast",
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
