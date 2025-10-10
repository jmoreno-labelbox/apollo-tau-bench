# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectConfigByCity(Tool):
    """
    Retrieves a project_config entry by target_city.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], target_city: str) -> str:
        rows = list(data.get("project_config", {}).values())
        for row in rows:
            if row.get("target_city") == target_city:
                return json.dumps(row)
        return json.dumps({"error": "project_config not found", "target_city": target_city})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_config_by_city",
                "description": "Retrieves a project_config entry by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {"type": "string", "description": "City name key in project_config."}
                    },
                    "required": ["target_city"]
                }
            }
        }
