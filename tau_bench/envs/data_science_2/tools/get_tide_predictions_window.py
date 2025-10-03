from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTidePredictionsWindow(Tool):
    """Provides a portion of tide_predictions for a station during [window_start_ts, window_end_ts]."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        station_id: str,
        window_start_ts: str,
        window_end_ts: str
    ) -> str:
        rows = data.get("tide_predictions", [])
        for row in rows:
            if (
                row.get("station_id") == station_id
                and row.get("start_ts") <= window_start_ts
                and row.get("end_ts") >= window_end_ts
            ):
                ts = row.get("timestamps", [])
                tp = row.get("tide_pred_m", [])
                out_ts = []
                out_tp = []
                for t, v in zip(ts, tp):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_tp.append(v)
                payload = {
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "tide_pred_m": out_tp,
                    "units": row.get("units"),
                    "method_nullable": row.get("method_nullable"),
                }
                out = json.dumps(payload)
                return out
        payload = {
            "error": "window not covered",
            "station_id": station_id,
            "window_start_ts": window_start_ts,
            "window_end_ts": window_end_ts,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTidePredictionsWindow",
                "description": "Returns subset of tide_predictions for a station and time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "window_start_ts": {"type": "string"},
                        "window_end_ts": {"type": "string"},
                    },
                    "required": ["station_id", "window_start_ts", "window_end_ts"],
                },
            },
        }
