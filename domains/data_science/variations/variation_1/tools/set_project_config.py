from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetProjectConfig(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        created_ts: str = None,
        forecast_horizon_days: int = None,
        max_station_distance_km_nullable: float = None,
        primary_station_id_nullable: str = None,
        target_city: str = None,
        timezone_default: str = None,
        top_n_results: int = None,
        updated_ts: str = None
    ) -> str:
        err = _require({"target_city": target_city, "timezone_default": timezone_default}, ["target_city", "timezone_default"])
        if err:
            return err
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
        payload = cfg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetProjectConfig",
                "description": "Create/replace the single project config row deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {"type": "string"},
                        "forecast_horizon_days": {"type": "integer"},
                        "top_n_results": {"type": "integer"},
                        "timezone_default": {"type": "string"},
                        "max_station_distance_km_nullable": {"type": "number"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                        "primary_station_id_nullable": {"type": "string"},
                    },
                    "required": ["target_city", "timezone_default"],
                },
            },
        }
