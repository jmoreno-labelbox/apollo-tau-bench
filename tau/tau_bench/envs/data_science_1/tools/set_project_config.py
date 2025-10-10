# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class SetProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_ts, forecast_horizon_days, max_station_distance_km_nullable, primary_station_id_nullable, target_city, timezone_default, top_n_results, updated_ts) -> str:
        err = _require(kwargs, ["target_city", "timezone_default"])
        if err: return err
        cfg = {
            "target_city": target_city,
            "forecast_horizon_days": forecast_horizon_days,
            "top_n_results": top_n_results,
            "timezone_default": timezone_default,
            "max_station_distance_km_nullable": max_station_distance_km_nullable,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
            "primary_station_id_nullable": primary_station_id_nullable,
        }
        data["project_config"] = [cfg]  
        return json.dumps(cfg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "set_project_config",
            "description": "Create/replace the single project config row deterministically.",
            "parameters": {"type": "object", "properties": {
                "target_city": {"type": "string"},
                "forecast_horizon_days": {"type": "integer"},
                "top_n_results": {"type": "integer"},
                "timezone_default": {"type": "string"},
                "max_station_distance_km_nullable": {"type": "number"},
                "created_ts": {"type": "string"},
                "updated_ts": {"type": "string"},
                "primary_station_id_nullable": {"type": "string"},
            }, "required": ["target_city", "timezone_default"]}}}
