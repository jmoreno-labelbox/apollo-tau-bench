# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class StoreWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], city, end_ts, fetched_ts, horizon_days, latitude, longitude, precipitation_mm_hr_nullable, raw_json_path_nullable, start_ts, temperature_2m_c_nullable, timestamps, timezone, variables, wind_speed_10m_ms_nullable) -> str:
        req = ["city", "latitude", "longitude"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "city": city, "latitude": latitude, "longitude": longitude,
            "variables": variables, "timezone": timezone,
            "horizon_days": horizon_days,
            "start_ts": start_ts, "end_ts": end_ts,
            "timestamps": timestamps,
            "precipitation_mm_hr_nullable": precipitation_mm_hr_nullable,
            "temperature_2m_c_nullable": temperature_2m_c_nullable,
            "wind_speed_10m_ms_nullable": wind_speed_10m_ms_nullable,
            "provider": "open-meteo",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts
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