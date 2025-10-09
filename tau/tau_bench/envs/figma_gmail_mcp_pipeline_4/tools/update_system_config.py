from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateSystemConfig(Tool):
    def invoke(
        data: dict[str, Any],
        config_key: str,
        config_category: str = None,
        config_value_json: str = None,
        description: str = ""
    ) -> str:
        """
        Modifies system configuration values for managing workflows.
        """
        if not all([config_key, config_value_json]):
            payload = {"error": "config_key and config_value_json are required."}
            out = json.dumps(
                payload)
            return out

        system_config = data.get("system_config", [])

        # Locate existing configuration or generate a new one
        config_found = False
        for config in system_config:
            if config.get("config_key") == config_key:
                config_found = True
                old_value = config.get("config_value_json")

                # Revise configuration
                config["config_value_json"] = config_value_json
                config["last_updated"] = datetime.now().isoformat()

                # Include optional fields
                if description:
                    config["description"] = description
                if config_category:
                    config["category"] = config_category

                # Document the change
                if "change_history" not in config:
                    config["change_history"] = []
                config["change_history"].append(
                    {
                        "timestamp": datetime.now().isoformat(),
                        "old_value": old_value,
                        "new_value": config_value_json,
                        "change_description": description,
                    }
                )

                break

        # Generate a new configuration if none exists
        if not config_found:
            new_config = {
                "config_key": config_key,
                "config_value_json": config_value_json,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
            }

            if description:
                new_config["description"] = description
            if config_category:
                new_config["category"] = config_category

            new_config["change_history"] = [
                {
                    "timestamp": datetime.now().isoformat(),
                    "old_value": None,
                    "new_value": config_value_json,
                    "change_description": f"Created new config: {description}",
                }
            ]

            system_config.append(new_config)
        payload = {
                "success": True,
                "config_key": config_key,
                "updated_at": datetime.now().isoformat(),
                "action": "updated" if config_found else "created",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSystemConfig",
                "description": "Updates system configuration values for workflow management including design system mappings, email templates, and SLA settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {
                            "type": "string",
                            "description": "The configuration key to update (e.g., 'design_system_aliases', 'email_templates').",
                        },
                        "config_value_json": {
                            "type": "string",
                            "description": "The JSON string value for the configuration.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Optional description of the configuration change.",
                        },
                        "config_category": {
                            "type": "string",
                            "description": "Optional category for the configuration (e.g., 'workflow', 'email', 'system').",
                        },
                    },
                    "required": ["config_key", "config_value_json"],
                },
            },
        }
