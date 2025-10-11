# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetCoastalMeteorology(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], station_id) -> str:
        # This is a simulated scenario; in a real-world setting, data would be retrieved from NOAA.

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
        list(data.get("coastal_meteorology_data", {}).values()).append(coastal_meteorology_data)
        return json.dumps(coastal_meteorology_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCoastalMeteorology",
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
