# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetWaterLevels(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], end_ts, start_ts, station_id) -> str:

        if not station_id or not start_ts or not end_ts:
            return json.dumps({"error": "Missing required parameters: station_id, start_ts, end_ts"})

        start_dt = GetWaterLevels._parse_iso(start_ts)
        end_dt = GetWaterLevels._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            return json.dumps({"error": "Invalid time range. Use ISO 8601 and ensure start < end."})

        items = data.get("water_levels", [])
        for rec in items:
            if rec.get("station_id") != station_id:
                continue
            rec_start = GetWaterLevels._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWaterLevels._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                vals = rec.get("water_level_m") or []
                idxs = [i for i, t in enumerate(ts_list)
                        if (GetWaterLevels._parse_iso(t) or start_dt) and (start_dt <= GetWaterLevels._parse_iso(t) <= end_dt)]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                return json.dumps({
                    "station_id": station_id,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "water_level_m": out_vals,
                    "units": rec.get("units", "meters"),
                    "datum": rec.get("datum_nullable")
                })

        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_water_levels",
                "description": "Returns observed water levels for a NOAA station within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string", "description": "NOAA station id (e.g., '9414290')."},
                        "start_ts": {"type": "string", "description": "Start timestamp (ISO 8601)."},
                        "end_ts": {"type": "string", "description": "End timestamp (ISO 8601)."}
                    },
                    "required": ["station_id", "start_ts", "end_ts"]
                }
            }
        }
