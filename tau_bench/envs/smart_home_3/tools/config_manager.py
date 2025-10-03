from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigManager(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = "get", config_key: str = None, config_value: Any = None) -> str:
        if "config" not in data:
            data["config"] = {
                "timezone": "America/Los_Angeles",
                "default_schedule_format": "RRULE",
                "notification_channels": ["mobile_push", "email", "speaker"],
                "auto_backup": True,
                "data_retention_days": 365,
            }

        config = data["config"]

        if action == "get":
            if config_key:
                payload = {config_key: config.get(config_key)}
                out = json.dumps(payload, indent=2)
                return out
            payload = config
            out = json.dumps(payload, indent=2)
            return out
        elif action == "set":
            if not config_key:
                payload = {"error": "config_key required"}
                out = json.dumps(payload, indent=2)
                return out
            config[config_key] = config_value
            payload = {"success": f"Set {config_key} to {config_value}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        elif action == "reset":
            data["config"] = {
                "timezone": "America/Los_Angeles",
                "default_schedule_format": "RRULE",
                "notification_channels": ["mobile_push", "email", "speaker"],
                "auto_backup": True,
                "data_retention_days": 365,
            }
            payload = {"success": "Configuration reset to defaults"}
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
                "name": "configManager",
                "description": "Manage system configuration and settings",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "set", "reset"]},
                        "config_key": {
                            "type": "string",
                            "description": "Configuration key",
                        },
                        "config_value": {
                            "type": "string",
                            "description": "Configuration value to set",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
