# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindWarehouses(Tool):
    """Tool to find warehouses based on location or capabilities."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        city: Optional[str] = None,
        country: Optional[str] = None,
        special_capability: Optional[str] = None,
        special_capabilities: Optional[List] = None,
    ) -> str:
        """Execute the tool with given parameters."""
        warehouses = list(data.get("warehouses", {}).values())
        results = []
        for warehouse in warehouses:
            has_capability = False
            if special_capability:
                if special_capability in warehouse.get("special_capabilities", []) or warehouse.get("warehouse_type") == special_capability:
                    has_capability = True

            if special_capabilities:
                if bool(set(special_capabilities)) and set(special_capabilities).issubset(warehouse.get("special_capabilities", [])):
                    has_capability = True

            if (not city or warehouse.get("city") == city) and \
               (not country or warehouse.get("country") == country) and \
               (not special_capability or has_capability) and \
               (not special_capabilities or has_capability):
                results.append(warehouse)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_warehouses",
                "description": "Finds warehouses based on location or special capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "Filter by city."},
                        "country": {"type": "string", "description": "Filter by country."},
                        "special_capability": {"type": "string", "description": "Filter by a special capability (e.g., 'Cold Storage', 'Hazmat Certified')."},
                        "special_capabilities": {"type": "array", "items": {"type": "string"}, "description": "Filter by multiple special capabilities (e.g., 'Cold Storage', 'Hazmat Certified')."},
                    },
                },
            },
        }
