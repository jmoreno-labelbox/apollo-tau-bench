from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWeatherForecast(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> datetime | None:
        pass
        try:
            #accepts "YYYY-MM-DDTHH:MM:SSZ" and "YYYY-MM-DDTHH:MM:SS"
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: dict[str, Any], city: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not city or not start_ts or not end_ts:
            payload = {"error": "Missing required parameters: city, start_ts, end_ts"}
            out = json.dumps(payload)
            return out

        start_dt = GetWeatherForecast._parse_iso(start_ts)
        end_dt = GetWeatherForecast._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            payload = {"error": "Invalid time range. Use ISO 8601 and ensure start < end."}
            out = json.dumps(payload)
            return out

        items = data.get("weather_forecasts", {}).values()
        for rec in items.values():
            if rec.get("city") != city:
                continue
            rec_start = GetWeatherForecast._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWeatherForecast._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            # we require complete coverage of the requested range
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []

                # sub-selects the range
                def in_range(ts):
                    dt = GetWeatherForecast._parse_iso(ts)
                    return dt is not None and (start_dt <= dt <= end_dt)

                out_ts = [t for t in ts_list.values() if in_range(t)]
                # align series (nullable may exist)
                precip = rec.get("precipitation_mm_hr_nullable") or []
                temp = rec.get("temperature_2m_c_nullable") or []
                wind = rec.get("wind_speed_10m_ms_nullable") or []

                # cut by the same selected indices
                # (assumes position alignment with timestamps)
                idxs = [i for i, t in enumerate(ts_list) if t in out_ts]

                def sel(arr):
                    return [arr[i] for i in idxs if i < len(arr)]

                result = {
                    "city": city,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "temperature_c": sel(temp),
                    "precipitation_mm_hr": sel(precip),
                    "wind_speed_10m_ms": sel(wind),
                }
                payload = result
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeatherForecast",
                "description": "Returns hourly weather forecast series for a city within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City name exactly as stored in the database.",
                        },
                        "start_ts": {
                            "type": "string",
                            "description": "Start timestamp (ISO 8601).",
                        },
                        "end_ts": {
                            "type": "string",
                            "description": "End timestamp (ISO 8601).",
                        },
                    },
                    "required": ["city", "start_ts", "end_ts"],
                },
            },
        }
