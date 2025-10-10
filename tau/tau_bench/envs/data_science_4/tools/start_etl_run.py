# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StartEtlRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        weather = kwargs.get("weather_raw_path")
        tides = kwargs.get("tides_raw_path")
        water = kwargs.get("water_levels_raw_path")
        city = kwargs.get("city_name")

        # deterministically produce processed path
        elt_id = "ETL_001"
        processed_path = f"/data/processed/timeseries_{elt_id}.csv"

        etl_entry = {
            "etl_run_id": elt_id,
            "inputs": {"weather": weather, "tides": tides, "water_levels": water},
            "status": "completed",
            "processed_path": processed_path,
        }
        data.setdefault("etl_runs", []).append(etl_entry)
        return json.dumps({"status": "completed", **etl_entry})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartEtlRun",
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
