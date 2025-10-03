from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreCoastalMeteorology(Tool):
    def invoke(
        data: dict[str, Any],
        end_ts: str = None,
        fetched_ts: str = None,
        pressure_hpa_nullable: float = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        station_id: str = None,
        temperature_c_nullable: float = None,
        timestamps: list = None,
        wind_speed_ms_nullable: float = None
    ) -> str:
        req = ["station_id", "timestamps"]
        err = _require({"station_id": station_id, "timestamps": timestamps}, req)
        if err:
            return err
        row = {
            "station_id": station_id,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "wind_speed_ms_nullable": wind_speed_ms_nullable,
            "pressure_hpa_nullable": pressure_hpa_nullable,
            "temperature_c_nullable": temperature_c_nullable,
            "provider": "noaa-tides-currents",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("coastal_meteorology", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "storeCoastalMeteorology",
                "description": "Stores coastal meteorology (wind/pressure/temperature) by station.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "wind_speed_ms_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "pressure_hpa_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "temperature_c_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["station_id", "timestamps"],
                },
            },
        }
