from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetProjectConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], target_city: str = None, forecast_horizon_days: int = None, max_station_distance_km_nullable: float = None) -> str:
        target_city = target_city
        horizon = forecast_horizon_days
        max_radius = max_station_distance_km_nullable
        configs = data.get("project_config", [])

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
        data.get("project_config", []).append(config)
        payload = {"config_id": "CONFIG_001", **config}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setProjectConfig",
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
