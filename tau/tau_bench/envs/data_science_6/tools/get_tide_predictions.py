# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTidePredictions(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")

        if not station_id or not start_ts or not end_ts:
            return json.dumps({"error": "Missing required parameters: station_id, start_ts, end_ts"})

        start_dt = GetTidePredictions._parse_iso(start_ts)
        end_dt = GetTidePredictions._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            return json.dumps({"error": "Invalid time range. Use ISO 8601 and ensure start < end."})

        items = data.get("tide_predictions", [])
        for rec in items:
            if rec.get("station_id") != station_id:
                continue
            rec_start = GetTidePredictions._parse_iso(rec.get("start_ts", ""))
            rec_end = GetTidePredictions._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                vals = rec.get("tide_pred_m") or []
                idxs = [i for i, t in enumerate(ts_list)
                        if (GetTidePredictions._parse_iso(t) or start_dt) and (start_dt <= GetTidePredictions._parse_iso(t) <= end_dt)]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                return json.dumps({
                    "station_id": station_id,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "tide_pred_m": out_vals,
                    "units": rec.get("units", "meters")
                })

        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tide_predictions",
                "description": "Returns tide prediction series for a NOAA station within a given ISO-8601 time window.",
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
