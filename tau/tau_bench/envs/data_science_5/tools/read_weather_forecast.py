from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadWeatherForecast(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city: str = None) -> str:
        rows = data.get("weather_forecasts", []) or []
        if city:
            rows = [r for r in rows if r.get("city") == city]
        payload = {"rows": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "readWeatherForecast",
                "description": "Fetch Open-Meteo style forecast rows (optional city filter).",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": [],
                },
            },
        }
