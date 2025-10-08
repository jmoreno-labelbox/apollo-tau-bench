from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreTidePredictions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        end_ts: str = None,
        fetched_ts: str = None,
        method_nullable: str = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        station_id: str = None,
        station_name_nullable: str = None,
        tide_pred_m: float = None,
        timestamps: list = None,
        units: str = None
    ) -> str:
        req = ["station_id", "timestamps", "tide_pred_m", "units"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "station_id": station_id,
            "station_name_nullable": station_name_nullable,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "tide_pred_m": tide_pred_m,
            "units": units,
            "method_nullable": method_nullable,
            "provider": "noaa-tides-currents",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("tide_predictions", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreTidePredictions",
                "description": "Stores tide predictions for a station and window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "station_name_nullable": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "tide_pred_m": {"type": "array", "items": {"type": "number"}},
                        "units": {"type": "string"},
                        "method_nullable": {"type": "string"},
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["station_id", "timestamps", "tide_pred_m", "units"],
                },
            },
        }
