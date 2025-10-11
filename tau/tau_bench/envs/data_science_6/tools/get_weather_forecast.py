# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWeatherForecast(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> Optional[datetime]:
        try:
            # aceita os formatos "YYYY-MM-DDTHH:MM:SSZ" e "YYYY-MM-DDTHH:MM:SS"
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], city, end_ts, start_ts) -> str:

        if not city or not start_ts or not end_ts:
            return json.dumps({"error": "Missing required parameters: city, start_ts, end_ts"})

        start_dt = GetWeatherForecast._parse_iso(start_ts)
        end_dt = GetWeatherForecast._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            return json.dumps({"error": "Invalid time range. Use ISO 8601 and ensure start < end."})

        items = data.get("weather_forecasts", [])
        for rec in items:
            if rec.get("city") != city:
                continue
            rec_start = GetWeatherForecast._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWeatherForecast._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            # requeremos a cobertura completa do intervalo especificado
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                # sub-selects the range
                def in_range(ts):
                    dt = GetWeatherForecast._parse_iso(ts)
                    return dt is not None and (start_dt <= dt <= end_dt)

                out_ts = [t for t in ts_list if in_range(t)]
                # alinhar séries (pode conter _nullable)
                precip = rec.get("precipitation_mm_hr_nullable") or []
                temp = rec.get("temperature_2m_c_nullable") or []
                wind = rec.get("wind_speed_10m_ms_nullable") or []

                # remover elementos nos mesmos índices escolhidos
                # (assume alignment by position with timestamps)
                idxs = [i for i, t in enumerate(ts_list) if t in out_ts]
                def sel(arr): return [arr[i] for i in idxs if i < len(arr)]
                result = {
                    "city": city,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "temperature_c": sel(temp),
                    "precipitation_mm_hr": sel(precip),
                    "wind_speed_10m_ms": sel(wind)
                }
                return json.dumps(result)

        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_weather_forecast",
                "description": "Returns hourly weather forecast series for a city within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name exactly as stored in the database."},
                        "start_ts": {"type": "string", "description": "Start timestamp (ISO 8601)."},
                        "end_ts": {"type": "string", "description": "End timestamp (ISO 8601)."}
                    },
                    "required": ["city", "start_ts", "end_ts"]
                }
            }
        }
