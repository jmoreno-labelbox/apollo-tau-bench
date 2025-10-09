from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetWeatherForecastByCity(Tool):
    """Fetches a weather_forecasts record using city and horizon_days."""

    @staticmethod
    def invoke(data: dict[str, Any], city: str, horizon_days: int) -> str:
        rows = data.get("weather_forecasts", [])
        for row in rows:
            if row.get("city") == city and row.get("horizon_days") == horizon_days:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {
            "error": "weather forecast not found",
            "city": city,
            "horizon_days": horizon_days,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeatherForecastByCity",
                "description": "Retrieves weather_forecasts by city and exact horizon_days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "horizon_days": {"type": "integer"},
                    },
                    "required": ["city", "horizon_days"],
                },
            },
        }
