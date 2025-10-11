# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], forecast_horizon_days, max_station_distance_km_nullable, target_city) -> str:
        horizon = forecast_horizon_days
        max_radius = max_station_distance_km_nullable
        configs = list(data.get("project_config", {}).values())

        timezone = "America/New_York"
        for config in configs:
            if config.get("target_city") == target_city:
                timezone = config.get("timezone_default")
                break
        config = {
            "config_id": "CONFIG_001",
            "target_city": target_city,
            "timezone_default": timezone,
            "forecast_horizon_days": horizon,
            "max_station_distance_km_nullable": max_radius,
        }
        list(data.get("project_config", {}).values()).append(config)
        return json.dumps({"config_id": "CONFIG_001", **config})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetProjectConfig",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {
                            "type": "string",
                            "description": "The name of the city to look up.",
                        }
                    },
                    "required": ["target_city"],
                },
            },
        }
