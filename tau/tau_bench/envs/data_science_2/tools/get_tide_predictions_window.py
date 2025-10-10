# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTidePredictionsWindow(Tool):
    """
    Returns a subset of tide_predictions for a station within [window_start_ts, window_end_ts].
    """
    @staticmethod
    def invoke(data: Dict[str, Any], station_id: str, window_start_ts: str, window_end_ts: str) -> str:
        rows = list(data.get("tide_predictions", {}).values())
        for row in rows:
            if row.get("station_id") == station_id and row.get("start_ts") <= window_start_ts and row.get("end_ts") >= window_end_ts:
                ts = row.get("timestamps", [])
                tp = row.get("tide_pred_m", [])
                out_ts = []
                out_tp = []
                for t, v in zip(ts, tp):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_tp.append(v)
                return json.dumps({
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "tide_pred_m": out_tp,
                    "units": row.get("units"),
                    "method_nullable": row.get("method_nullable")
                })
        return json.dumps({"error": "window not covered", "station_id": station_id, "window_start_ts": window_start_ts, "window_end_ts": window_end_ts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tide_predictions_window",
                "description": "Returns subset of tide_predictions for a station and time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "window_start_ts": {"type": "string"},
                        "window_end_ts": {"type": "string"}
                    },
                    "required": ["station_id", "window_start_ts", "window_end_ts"]
                }
            }
        }
