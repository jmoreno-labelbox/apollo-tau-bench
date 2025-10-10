# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class StoreCoastalMeteorology(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["station_id", "timestamps"]
        err = _require(kwargs, req)
        if err: return err
        row = {"station_id": kwargs["station_id"], "start_ts": kwargs.get("start_ts"),
               "end_ts": kwargs.get("end_ts"), "timestamps": kwargs["timestamps"],
               "wind_speed_ms_nullable": kwargs.get("wind_speed_ms_nullable"),
               "pressure_hpa_nullable": kwargs.get("pressure_hpa_nullable"),
               "temperature_c_nullable": kwargs.get("temperature_c_nullable"),
               "provider": "noaa-tides-currents", "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
               "fetched_ts": kwargs.get("fetched_ts")}
        return json.dumps(_append(data.setdefault("coastal_meteorology", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_coastal_meteorology",
            "description": "Stores coastal meteorology (wind/pressure/temperature) by station.",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"}, "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "wind_speed_ms_nullable": {"type": "array", "items": {"type": "number"}},
                "pressure_hpa_nullable": {"type": "array", "items": {"type": "number"}},
                "temperature_c_nullable": {"type": "array", "items": {"type": "number"}},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["station_id", "timestamps"]}}}
