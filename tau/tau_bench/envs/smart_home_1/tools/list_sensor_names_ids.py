# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListSensorNamesIds(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        return json.dumps([{"name": s["name"], "sensor_id": s["id"]} for s in list(data.get("sensors", {}).values())], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_sensor_names_ids",
                "description": "Return all sensors' names and ids (state is read-only).",
                "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False},
            },
        }
