# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class StoreTidePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["station_id", "timestamps", "tide_pred_m", "units"]
        err = _require(kwargs, req)
        if err: return err
        row = {"station_id": kwargs["station_id"], "station_name_nullable": kwargs.get("station_name_nullable"),
               "start_ts": kwargs.get("start_ts"), "end_ts": kwargs.get("end_ts"),
               "timestamps": kwargs["timestamps"], "tide_pred_m": kwargs["tide_pred_m"], "units": kwargs["units"],
               "method_nullable": kwargs.get("method_nullable"), "provider": "noaa-tides-currents",
               "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"), "fetched_ts": kwargs.get("fetched_ts")}
        return json.dumps(_append(data.setdefault("tide_predictions", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_tide_predictions",
            "description": "Stores tide predictions for a station and window.",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"}, "station_name_nullable": {"type": "string"},
                "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "tide_pred_m": {"type": "array", "items": {"type": "number"}},
                "units": {"type": "string"}, "method_nullable": {"type": "string"},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["station_id", "timestamps", "tide_pred_m", "units"]}}}
