# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        # This is a simulation; in a real environment, this would fetch data from NOAA.

        water_level_data = {
            "station_id": station_id,
            "data_points": [
                {"timestamp": "2023-10-01T00:00:00Z", "water_level_meters": 1.2},
                {"timestamp": "2023-10-01T01:00:00Z", "water_level_meters": 1.3},
            ],
            "raw_json_path_nullable": f"/data/raw/water_levels_{station_id}.json",
        }
        list(data.get("water_level_data", {}).values()).append(water_level_data)
        return json.dumps(water_level_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetWaterLevels",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "The ID of the NOAA station.",
                        }
                    },
                    "required": ["station_id"],
                },
            },
        }
