# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ConfigManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action = kwargs.get('action', 'get')
        config_key = kwargs.get('config_key')
        config_value = kwargs.get('config_value')

        if 'config' not in data:
            data['config'] = {
                'timezone': 'America/Los_Angeles',
                'default_schedule_format': 'RRULE',
                'notification_channels': ['mobile_push', 'email', 'speaker'],
                'auto_backup': True,
                'data_retention_days': 365
            }

        config = data['config']

        if action == 'get':
            if config_key:
                return json.dumps({config_key: config.get(config_key)}, indent=2)
            return json.dumps(config, indent=2)
        elif action == 'set':
            if not config_key:
                return json.dumps({"error": "config_key required"}, indent=2)
            config[config_key] = config_value
            return json.dumps({"success": f"Set {config_key} to {config_value}"}, indent=2)
        elif action == 'reset':
            data['config'] = {
                'timezone': 'America/Los_Angeles',
                'default_schedule_format': 'RRULE',
                'notification_channels': ['mobile_push', 'email', 'speaker'],
                'auto_backup': True,
                'data_retention_days': 365
            }
            return json.dumps({"success": "Configuration reset to defaults"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "config_manager",
                "description": "Manage system configuration and settings",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "set", "reset"]},
                        "config_key": {"type": "string", "description": "Configuration key"},
                        "config_value": {"type": "string", "description": "Configuration value to set"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
