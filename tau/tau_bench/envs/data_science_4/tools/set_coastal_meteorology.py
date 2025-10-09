from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetCoastalMeteorology(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        # This is a mockup; in an actual setting, this would retrieve data from NOAA.

        coastal_meteorology_data = {
            "station_id": station_id,
            "data_points": [
                {
                    "timestamp": "2023-10-01T00:00:00Z",
                    "wind_speed_m_s": 5.0,
                    "pressure_hPa": 1013,
                },
                {
                    "timestamp": "2023-10-01T01:00:00Z",
                    "wind_speed_m_s": 5.5,
                    "pressure_hPa": 1012,
                },
            ],
            "raw_json_path_nullable": f"/data/raw/coastal_meteorology_{station_id}.json",
        }
        data["coastal_meteorology_data"][coastal_meteorology_data["coastal_meteorology_data_id"]] = coastal_meteorology_data
        payload = coastal_meteorology_data
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setCoastalMeteorology",
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
