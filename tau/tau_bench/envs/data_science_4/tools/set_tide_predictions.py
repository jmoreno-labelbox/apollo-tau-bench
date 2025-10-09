from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetTidePredictions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        # This is a mockup; in an actual setting, this would retrieve data from NOAA.

        tide_prediction_data = {
            "station_id": station_id,
            "predictions": [
                {"timestamp": "2023-10-01T00:00:00Z", "predicted_tide_meters": 1.5},
                {"timestamp": "2023-10-01T01:00:00Z", "predicted_tide_meters": 1.6},
            ],
            "raw_json_path_nullable": f"/data/raw/tide_predictions_{station_id}.json",
        }
        data["tide_predictions"][tide_prediction_data["tide_prediction_id"]] = tide_prediction_data
        payload = tide_prediction_data
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setTidePredictions",
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
