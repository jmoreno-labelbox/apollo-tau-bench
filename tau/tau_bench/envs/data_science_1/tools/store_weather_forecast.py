# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StoreWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["city", "latitude", "longitude"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "city": kwargs["city"], "latitude": kwargs["latitude"], "longitude": kwargs["longitude"],
            "variables": kwargs.get("variables"), "timezone": kwargs.get("timezone"),
            "horizon_days": kwargs.get("horizon_days"),
            "start_ts": kwargs.get("start_ts"), "end_ts": kwargs.get("end_ts"),
            "timestamps": kwargs.get("timestamps"),
            "precipitation_mm_hr_nullable": kwargs.get("precipitation_mm_hr_nullable"),
            "temperature_2m_c_nullable": kwargs.get("temperature_2m_c_nullable"),
            "wind_speed_10m_ms_nullable": kwargs.get("wind_speed_10m_ms_nullable"),
            "provider": "open-meteo",
            "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
            "fetched_ts": kwargs.get("fetched_ts")
        }
        return json.dumps(_append(data.setdefault("weather_forecasts", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_weather_forecast",
            "description": "Adds an hourly weather forecast record.",
            "parameters": {"type": "object", "properties": {
                "city": {"type": "string"}, "latitude": {"type": "number"}, "longitude": {"type": "number"},
                "variables": {"type": "array", "items": {"type": "string"}}, "timezone": {"type": "string"},
                "horizon_days": {"type": "integer"}, "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "precipitation_mm_hr_nullable": {"type": "array", "items": {"type": "number"}},
                "temperature_2m_c_nullable": {"type": "array", "items": {"type": "number"}},
                "wind_speed_10m_ms_nullable": {"type": "array", "items": {"type": "number"}},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["city", "latitude", "longitude"]}}}
