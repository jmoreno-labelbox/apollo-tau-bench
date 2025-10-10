# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertWeatherForecast(Tool):
    """
    Appends a weather_forecasts record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"city", "latitude", "longitude", "variables", "timezone", "horizon_days", "start_ts", "end_ts", "timestamps", "provider", "fetched_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        ts = record.get("timestamps", [])
        for k in ["precipitation_mm_hr_nullable", "temperature_2m_c_nullable", "wind_speed_10m_ms_nullable"]:
            if k in record and isinstance(record[k], list) and len(record[k]) != len(ts):
                return json.dumps({"error": "array length mismatch", "field": k})
        data.setdefault("weather_forecasts", []).append(record)
        return json.dumps({"status": "inserted", "record": {"city": record.get("city"), "horizon_days": record.get("horizon_days")}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insert_weather_forecast",
                "description": "Appends a weather_forecasts record with required fields and aligned arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
