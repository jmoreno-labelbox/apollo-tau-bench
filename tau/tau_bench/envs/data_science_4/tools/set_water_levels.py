from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetWaterLevels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        pass
        # This is a mockup; in an actual setting, this would retrieve data from NOAA.

        water_level_data = {
            "station_id": station_id,
            "data_points": [
                {"timestamp": "2023-10-01T00:00:00Z", "water_level_meters": 1.2},
                {"timestamp": "2023-10-01T01:00:00Z", "water_level_meters": 1.3},
            ],
            "raw_json_path_nullable": f"/data/raw/water_levels_{station_id}.json",
        }
        data.get("water_level_data", []).append(water_level_data)
        payload = water_level_data
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setWaterLevels",
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
