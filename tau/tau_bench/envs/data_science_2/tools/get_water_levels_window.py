from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetWaterLevelsWindow(Tool):
    """Provides a portion of water_levels for a station during [window_start_ts, window_end_ts]."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        station_id: str,
        window_start_ts: str,
        window_end_ts: str
    ) -> str:
        rows = data.get("water_levels", [])
        for row in rows:
            if (
                row.get("station_id") == station_id
                and row.get("start_ts") <= window_start_ts
                and row.get("end_ts") >= window_end_ts
            ):
                ts = row.get("timestamps", [])
                wl = row.get("water_level_m", [])
                out_ts = []
                out_wl = []
                for t, v in zip(ts, wl):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_wl.append(v)
                payload = {
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "water_level_m": out_wl,
                    "units": row.get("units"),
                    "datum_nullable": row.get("datum_nullable"),
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
                "name": "GetWaterLevelsWindow",
                "description": "Returns subset of water_levels for a station and time window.",
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
