from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertProjectConfig(Tool):
    """Adds or modifies a project_config record based on target_city."""

    @staticmethod
    def invoke(data: dict[str, Any], record: dict[str, Any]) -> str:
        if "target_city" not in record:
            payload = {"error": "missing target_city"}
            out = json.dumps(payload)
            return out
        rows = data.setdefault("project_config", [])
        for row in rows:
            if row.get("target_city") == record["target_city"]:
                row.update(record)
                payload = {"status": "updated", "record": row}
                out = json.dumps(payload)
                return out
        rows.append(record)
        payload = {"status": "inserted", "record": record}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertProjectConfig",
                "description": "Inserts or updates a project_config record by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {
                            "type": "object",
                            "description": "Full project_config record with target_city as key.",
                        }
                    },
                    "required": ["record"],
                },
            },
        }
