# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")
        rows = list(data.get("weather_forecasts", {}).values()) or []
        if city:
            rows = [r for r in rows if r.get("city") == city]
        return json.dumps({"rows": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_weather_forecast",
            "description": "Fetch Open-Meteo style forecast rows (optional city filter).",
            "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": []}
        }}
