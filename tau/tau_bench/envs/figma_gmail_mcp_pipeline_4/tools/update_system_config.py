# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSystemConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], config_category, config_key, config_value_json, description = '') -> str:
        """
        Updates system configuration values for workflow management.
        """

        if not all([config_key, config_value_json]):
            return json.dumps({"error": "config_key and config_value_json are required."})

        system_config = data.get('system_config', [])

        # Locate the current configuration or generate a new one.
        config_found = False
        for config in system_config:
            if config.get('config_key') == config_key:
                config_found = True
                old_value = config.get('config_value_json')

                # Revise configuration
                config['config_value_json'] = config_value_json
                config['last_updated'] = datetime.now().isoformat()

                # Include optional parameters
                if description:
                    config['description'] = description
                if config_category:
                    config['category'] = config_category

                # Record the modification.
                if 'change_history' not in config:
                    config['change_history'] = []
                config['change_history'].append({
                    "timestamp": datetime.now().isoformat(),
                    "old_value": old_value,
                    "new_value": config_value_json,
                    "change_description": description
                })

                break

        # Generate a new configuration if it does not exist.
        if not config_found:
            new_config = {
                "config_key": config_key,
                "config_value_json": config_value_json,
                "created_at": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat()
            }

            if description:
                new_config['description'] = description
            if config_category:
                new_config['category'] = config_category

            new_config['change_history'] = [{
                "timestamp": datetime.now().isoformat(),
                "old_value": None,
                "new_value": config_value_json,
                "change_description": f"Created new config: {description}"
            }]

            system_config.append(new_config)

        return json.dumps({
            "success": True,
            "config_key": config_key,
            "updated_at": datetime.now().isoformat(),
            "action": "updated" if config_found else "created"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_system_config",
                "description": "Updates system configuration values for workflow management including design system mappings, email templates, and SLA settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {"type": "string", "description": "The configuration key to update (e.g., 'design_system_aliases', 'email_templates')."},
                        "config_value_json": {"type": "string", "description": "The JSON string value for the configuration."},
                        "description": {"type": "string", "description": "Optional description of the configuration change."},
                        "config_category": {"type": "string", "description": "Optional category for the configuration (e.g., 'workflow', 'email', 'system')."}
                    },
                    "required": ["config_key", "config_value_json"]
                }
            }
        }
