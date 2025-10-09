from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetWaterLevels(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        pass
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not station_id or not start_ts or not end_ts:
            payload = {"error": "Missing required parameters: station_id, start_ts, end_ts"}
            out = json.dumps(
                payload)
            return out

        start_dt = GetWaterLevels._parse_iso(start_ts)
        end_dt = GetWaterLevels._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            payload = {"error": "Invalid time range. Use ISO 8601 and ensure start < end."}
            out = json.dumps(
                payload)
            return out

        items = data.get("water_levels", {}).values()
        for rec in items.values():
            if rec.get("station_id") != station_id:
                continue
            rec_start = GetWaterLevels._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWaterLevels._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                vals = rec.get("water_level_m") or []
                idxs = [
                    i
                    for i, t in enumerate(ts_list)
                    if (GetWaterLevels._parse_iso(t) or start_dt)
                    and (start_dt <= GetWaterLevels._parse_iso(t) <= end_dt)
                ]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                payload = {
                        "station_id": station_id,
                        "start_ts": start_ts,
                        "end_ts": end_ts,
                        "timestamps": out_ts,
                        "water_level_m": out_vals,
                        "units": rec.get("units", "meters"),
                        "datum": rec.get("datum_nullable"),
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWaterLevels",
                "description": "Returns observed water levels for a NOAA station within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "NOAA station id (e.g., '9414290').",
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
                    "required": ["station_id", "start_ts", "end_ts"],
                },
            },
        }
