# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSystemConfigByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves system configuration entries filtered by category and key patterns.
        """
        config_key = kwargs.get('config_key')
        config_category = kwargs.get('config_category')
        key_pattern = kwargs.get('key_pattern')
        include_history = kwargs.get('include_history', False)

        system_config = data.get('system_config', [])

        # Return the specific configuration if config_key is supplied.
        if config_key:
            for config in system_config:
                if config.get('config_key') == config_key:
                    config_copy = config.copy()
                    if not include_history and 'change_history' in config_copy:
                        del config_copy['change_history']
                    return json.dumps(config_copy, indent=2)
            return json.dumps({"error": f"Config with key '{config_key}' not found."})

        # Refine configurations based on specified criteria.
        results = []
        for config in system_config:
            # Implement filters
            if config_category:
                if config.get('category') != config_category:
                    continue

            if key_pattern:
                if key_pattern.lower() not in config.get('config_key', '').lower():
                    continue

            config_copy = config.copy()
            if not include_history and 'change_history' in config_copy:
                del config_copy['change_history']

            results.append(config_copy)

        # Categorize results for a summary overview.
        summary = {
            "total_configs": len(results),
            "by_category": {},
            "configs": results
        }

        for config in results:
            category = config.get('category', 'uncategorized')
            if category not in summary["by_category"]:
                summary["by_category"][category] = 0
            summary["by_category"][category] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_system_config_by_category",
                "description": "Retrieves system configuration entries filtered by category, key patterns, and optionally includes change history for workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {"type": "string", "description": "The specific configuration key to retrieve."},
                        "config_category": {"type": "string", "description": "Filter configurations by category (e.g., 'workflow', 'email', 'system')."},
                        "key_pattern": {"type": "string", "description": "Filter configurations by key pattern (e.g., 'email' to find email-related configs)."},
                        "include_history": {"type": "boolean", "description": "Include change history in the results (default: false)."}
                    }
                }
            }
        }
