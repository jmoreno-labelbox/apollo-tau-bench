# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DataPorter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], action, data_types = ['all'], import_data = {}) -> str:

        if action == 'export':
            export_result = {}
            if 'all' in data_types or 'devices' in data_types:
                export_result['devices'] = list(data.get('devices', {}).values())
            if 'all' in data_types or 'scenes' in data_types:
                export_result['scenes'] = list(data.get('scenes', {}).values())
            if 'all' in data_types or 'lists' in data_types:
                export_result['custom_lists'] = list(data.get('custom_lists', {}).values())
            if 'all' in data_types or 'reminders' in data_types:
                export_result['reminders'] = list(data.get('reminders', {}).values())
            if 'all' in data_types or 'members' in data_types:
                export_result['members'] = list(data.get('members', {}).values())
            if 'all' in data_types or 'rooms' in data_types:
                export_result['rooms'] = list(data.get('rooms', {}).values())

            return json.dumps(export_result, indent=2)

        elif action == 'import':
            if not import_data:
                return json.dumps({"error": "import_data required"}, indent=2)

            imported = []
            for key, value in import_data.items():
                if key in ['devices', 'scenes', 'custom_lists', 'reminders', 'members', 'rooms']:
                    data[key] = value
                    imported.append(key)

            return json.dumps({"success": f"Imported data types: {imported}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "data_porter",
                "description": "Import/export system data for backup and restore",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["export", "import"]},
                        "data_types": {"type": "array", "items": {"type": "string"}, "description": "Data types to export/import"},
                        "import_data": {"type": "object", "description": "Data to import"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
