from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreWeatherForecast(Tool):
    def invoke(
        data: dict[str, Any],
        city: str = None,
        end_ts: str = None,
        fetched_ts: str = None,
        horizon_days: int = None,
        latitude: float = None,
        longitude: float = None,
        precipitation_mm_hr_nullable: float = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        temperature_2m_c_nullable: float = None,
        timestamps: list = None,
        timezone: str = None,
        variables: Any = None,
        wind_speed_10m_ms_nullable: float = None
    ) -> str:
        req = ["city", "latitude", "longitude"]
        err = _require({"city": city, "latitude": latitude, "longitude": longitude}, req)
        if err:
            return err
        row = {
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "variables": variables,
            "timezone": timezone,
            "horizon_days": horizon_days,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "precipitation_mm_hr_nullable": precipitation_mm_hr_nullable,
            "temperature_2m_c_nullable": temperature_2m_c_nullable,
            "wind_speed_10m_ms_nullable": wind_speed_10m_ms_nullable,
            "provider": "open-meteo",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("weather_forecasts", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "storeWeatherForecast",
                "description": "Adds an hourly weather forecast record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "latitude": {"type": "number"},
                        "longitude": {"type": "number"},
                        "variables": {"type": "array", "items": {"type": "string"}},
                        "timezone": {"type": "string"},
                        "horizon_days": {"type": "integer"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "precipitation_mm_hr_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "temperature_2m_c_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "wind_speed_10m_ms_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["city", "latitude", "longitude"],
                },
            },
        }
