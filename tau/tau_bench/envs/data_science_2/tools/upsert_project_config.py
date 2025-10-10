# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertProjectConfig(Tool):
    """
    Inserts or updates a project_config record by target_city.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        if "target_city" not in record:
            return json.dumps({"error": "missing target_city"})
        rows = data.setdefault("project_config", [])
        for row in rows:
            if row.get("target_city") == record["target_city"]:
                row.update(record)
                return json.dumps({"status": "updated", "record": row})
        rows.append(record)
        return json.dumps({"status": "inserted", "record": record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_project_config",
                "description": "Inserts or updates a project_config record by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object", "description": "Full project_config record with target_city as key."}
                    },
                    "required": ["record"]
                }
            }
        }
