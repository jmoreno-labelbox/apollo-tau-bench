from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DataPorter(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = None, data_types: list[str] = ["all"], import_data: dict[str, Any] = {}) -> str:
        if action == "export":
            export_result = {}
            if "all" in data_types or "devices" in data_types:
                export_result["devices"] = data.get("devices", {}).values()
            if "all" in data_types or "scenes" in data_types:
                export_result["scenes"] = data.get("scenes", {}).values()
            if "all" in data_types or "lists" in data_types:
                export_result["custom_lists"] = data.get("custom_lists", {}).values()
            if "all" in data_types or "reminders" in data_types:
                export_result["reminders"] = data.get("reminders", {}).values()
            if "all" in data_types or "members" in data_types:
                export_result["members"] = data.get("members", {}).values()
            if "all" in data_types or "rooms" in data_types:
                export_result["rooms"] = data.get("rooms", {}).values()
            payload = export_result
            out = json.dumps(payload, indent=2)
            return out

        elif action == "import":
            if not import_data:
                payload = {"error": "import_data required"}
                out = json.dumps(payload, indent=2)
                return out

            imported = []
            for key, value in import_data.items():
                if key in [
                    "devices",
                    "scenes",
                    "custom_lists",
                    "reminders",
                    "members",
                    "rooms",
                ]:
                    data[key] = value
                    imported.append(key)
            payload = {"success": f"Imported data types: {imported}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DataPorter",
                "description": "Import/export system data for backup and restore",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["export", "import"]},
                        "data_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Data types to export/import",
                        },
                        "import_data": {
                            "type": "object",
                            "description": "Data to import",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
