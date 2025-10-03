from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsertWeatherForecast(Tool):
    """Adds a weather_forecasts record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        city: str,
        latitude: float,
        longitude: float,
        variables: list[str],
        timezone: str,
        horizon_days: int,
        start_ts: str,
        end_ts: str,
        timestamps: list[str],
        provider: str,
        fetched_ts: str,
        precipitation_mm_hr_nullable: list[float] = None,
        temperature_2m_c_nullable: list[float] = None,
        wind_speed_10m_ms_nullable: list[float] = None,
    ) -> str:
        req = {
            "city",
            "latitude",
            "longitude",
            "variables",
            "timezone",
            "horizon_days",
            "start_ts",
            "end_ts",
            "timestamps",
            "provider",
            "fetched_ts",
        }
        record = {
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "variables": variables,
            "timezone": timezone,
            "horizon_days": horizon_days,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "provider": provider,
            "fetched_ts": fetched_ts,
            "precipitation_mm_hr_nullable": precipitation_mm_hr_nullable,
            "temperature_2m_c_nullable": temperature_2m_c_nullable,
            "wind_speed_10m_ms_nullable": wind_speed_10m_ms_nullable,
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        ts = record.get("timestamps", [])
        for k in [
            "precipitation_mm_hr_nullable",
            "temperature_2m_c_nullable",
            "wind_speed_10m_ms_nullable",
        ]:
            if (
                k in record
                and isinstance(record[k], list)
                and len(record[k]) != len(ts)
            ):
                payload = {"error": "array length mismatch", "field": k}
                out = json.dumps(payload)
                return out
        data.setdefault("weather_forecasts", []).append(record)
        payload = {
            "status": "inserted",
            "record": {
                "city": record.get("city"),
                "horizon_days": record.get("horizon_days"),
            },
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insertWeatherForecast",
                "description": "Appends a weather_forecasts record with required fields and aligned arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
