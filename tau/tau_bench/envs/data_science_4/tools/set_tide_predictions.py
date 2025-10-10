# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetTidePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        # This is a simulation; in a real environment, this would fetch data from NOAA.

        tide_prediction_data = {
            "station_id": station_id,
            "predictions": [
                {"timestamp": "2023-10-01T00:00:00Z", "predicted_tide_meters": 1.5},
                {"timestamp": "2023-10-01T01:00:00Z", "predicted_tide_meters": 1.6},
            ],
            "raw_json_path_nullable": f"/data/raw/tide_predictions_{station_id}.json",
        }
        list(data.get("tide_predictions", {}).values()).append(tide_prediction_data)
        return json.dumps(tide_prediction_data)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetTidePredictions",
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
