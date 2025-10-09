from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSystemConfigByCategory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        config_key: str = None, 
        config_category: str = None,
        category: str = None,
        key_pattern: str = None, 
        include_history: bool = False
    ) -> str:
        # Support 'category' as an alternative to 'config_category'
        if category is not None:
            config_category = category
        """
        Obtains system configuration entries filtered by category and key patterns.
        """
        system_config = data.get("system_config", {}).values()

        # Return the specific configuration if config_key is supplied
        if config_key:
            for config in system_config.values():
                if config.get("config_key") == config_key:
                    config_copy = config.copy()
                    if not include_history and "change_history" in config_copy:
                        del config_copy["change_history"]
                    payload = config_copy
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Config with key '{config_key}' not found."}
            out = json.dumps(payload)
            return out

        # Sort configurations based on specified criteria
        results = []
        for config in system_config.values():
            # Implement filters
            if config_category:
                if config.get("category") != config_category:
                    continue

            if key_pattern:
                if key_pattern.lower() not in config.get("config_key", "").lower():
                    continue

            config_copy = config.copy()
            if not include_history and "change_history" in config_copy:
                del config_copy["change_history"]

            results.append(config_copy)

        # Categorize results for summary
        summary = {"total_configs": len(results), "by_category": {}, "configs": results}

        for config in results:
            category = config.get("category", "uncategorized")
            if category not in summary["by_category"]:
                summary["by_category"][category] = 0
            summary["by_category"][category] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSystemConfigByCategory",
                "description": "Retrieves system configuration entries filtered by category, key patterns, and optionally includes change history for workflow management.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "config_key": {
                            "type": "string",
                            "description": "The specific configuration key to retrieve.",
                        },
                        "config_category": {
                            "type": "string",
                            "description": "Filter configurations by category (e.g., 'workflow', 'email', 'system').",
                        },
                        "key_pattern": {
                            "type": "string",
                            "description": "Filter configurations by key pattern (e.g., 'email' to find email-related configs).",
                        },
                        "include_history": {
                            "type": "boolean",
                            "description": "Include change history in the results (default: false).",
                        },
                    },
                },
            },
        }
