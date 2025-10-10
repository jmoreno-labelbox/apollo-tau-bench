# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BulkOperator(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], operation, target_type, filters = {}, updates = {}) -> str:

        if not operation or not target_type:
            return json.dumps({"error": "operation and target_type required"}, indent=2)

        targets = data.get(target_type, [])
        affected = []

        if operation == 'bulk_update':
            for item in targets:
                match = True
                for key, value in filters.items():
                    if item.get(key) != value:
                        match = False
                        break
                if match:
                    item.update(updates)
                    affected.append(item.get('id', item.get('name', 'unnamed')))

        elif operation == 'bulk_state_update' and target_type == 'devices':
            for device in targets:
                match = True
                for key, value in filters.items():
                    if device.get(key) != value:
                        match = False
                        break
                if match:
                    existing_updates = {
                       k: v for k, v in updates.items()
                        if k in device['state']
                    }
                    device['state'].update(existing_updates)
                    device['state']['last_updated'] = _now_iso()
                    affected.append(device['id'])

        return json.dumps({"success": f"Updated {len(affected)} items"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_operator",
                "description": "Perform bulk operations across multiple entities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {"type": "string", "enum": ["bulk_update", "bulk_state_update"]},
                        "target_type": {"type": "string", "enum": ["devices", "scenes", "custom_lists", "reminders", "members"]},
                        "filters": {"type": "object", "description": "Criteria to match items"},
                        "updates": {"type": "object", "description": "Updates to apply"}
                    },
                    "required": ["operation", "target_type"],
                    "additionalProperties": False
                }
            }
        }
