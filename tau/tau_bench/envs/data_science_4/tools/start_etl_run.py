from tau_bench.envs.tool import Tool
import json
from typing import Any

class StartEtlRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], weather_raw_path: str = None, tides_raw_path: str = None, water_levels_raw_path: str = None, city_name: str = None) -> str:
        pass
        weather = weather_raw_path
        tides = tides_raw_path
        water = water_levels_raw_path
        city_name  # This line seems to be unused, but kept for consistency

        #consistently generate processed path
        elt_id = "ETL_001"
        processed_path = f"/data/processed/timeseries_{elt_id}.csv"

        etl_entry = {
            "etl_run_id": elt_id,
            "inputs": {"weather": weather, "tides": tides, "water_levels": water},
            "status": "completed",
            "processed_path": processed_path,
        }
        data.setdefault("etl_runs", []).append(etl_entry)
        payload = {"status": "completed", **etl_entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "startEtlRun",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_name": {"type": "string"},
                        "weather_raw_path": {"type": "string"},
                        "tides_raw_path": {"type": "string"},
                        "water_levels_raw_path": {"type": "string"},
                    },
                    "required": [
                        "city_name",
                        "weather_raw_path",
                        "tides_raw_path",
                        "water_levels_raw_path",
                    ],
                },
            },
        }
