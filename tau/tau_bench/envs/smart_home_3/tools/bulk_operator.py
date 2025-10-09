from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class BulkOperator(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], operation: str = None, target_type: str = None, filters: dict = {}, updates: dict = {}) -> str:
        if not operation or not target_type:
            payload = {"error": "operation and target_type required"}
            out = json.dumps(payload, indent=2)
            return out

        targets = data.get(target_type, {}).values()
        affected = []

        if operation == "bulk_update":
            for item in targets:
                match = True
                for key, value in filters.items():
                    if item.get(key) != value:
                        match = False
                        break
                if match:
                    item.update(updates)
                    affected.append(item.get("id", item.get("name", "unnamed")))

        elif operation == "bulk_state_update" and target_type == "devices":
            for device in targets:
                match = True
                for key, value in filters.items():
                    if device.get(key) != value:
                        match = False
                        break
                if match:
                    existing_updates = {
                        k: v for k, v in updates.items() if k in device["state"]
                    }
                    device["state"].update(existing_updates)
                    device["state"]["last_updated"] = _now_iso()
                    affected.append(device["id"])
        payload = {"success": f"Updated {len(affected)} items"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkOperator",
                "description": "Perform bulk operations across multiple entities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {
                            "type": "string",
                            "enum": ["bulk_update", "bulk_state_update"],
                        },
                        "target_type": {
                            "type": "string",
                            "enum": [
                                "devices",
                                "scenes",
                                "custom_lists",
                                "reminders",
                                "members",
                            ],
                        },
                        "filters": {
                            "type": "object",
                            "description": "Criteria to match items",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Updates to apply",
                        },
                    },
                    "required": ["operation", "target_type"],
                    "additionalProperties": False,
                },
            },
        }
