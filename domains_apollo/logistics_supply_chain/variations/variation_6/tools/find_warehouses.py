from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindWarehouses(Tool):
    """Utility for locating warehouses according to their location or features."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        city: str | None = None,
        country: str | None = None,
        special_capability: str | None = None,
        special_capabilities: list | None = None
    ) -> str:
        """Run the tool using the specified parameters."""
        warehouses = data.get("warehouses", [])
        results = []
        for warehouse in warehouses:
            has_capability = False
            if special_capability:
                if (
                    special_capability in warehouse.get("special_capabilities", [])
                    or warehouse.get("warehouse_type") == special_capability
                ):
                    has_capability = True

            if special_capabilities:
                if bool(set(special_capabilities)) and set(
                    special_capabilities
                ).issubset(warehouse.get("special_capabilities", [])):
                    has_capability = True

            if (
                (not city or warehouse.get("city") == city)
                and (not country or warehouse.get("country") == country)
                and (not special_capability or has_capability)
                and (not special_capabilities or has_capability)
            ):
                results.append(warehouse)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool using the specified parameters."""
        pass
        warehouses = data.get("warehouses", [])
        results = []
        for warehouse in warehouses:
            has_capability = False
            if special_capability:
                if (
                    special_capability in warehouse.get("special_capabilities", [])
                    or warehouse.get("warehouse_type") == special_capability
                ):
                    has_capability = True

            if special_capabilities:
                if bool(set(special_capabilities)) and set(
                    special_capabilities
                ).issubset(warehouse.get("special_capabilities", [])):
                    has_capability = True

            if (
                (not city or warehouse.get("city") == city)
                and (not country or warehouse.get("country") == country)
                and (not special_capability or has_capability)
                and (not special_capabilities or has_capability)
            ):
                results.append(warehouse)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindWarehouses",
                "description": "Finds warehouses based on location or special capabilities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "Filter by city."},
                        "country": {
                            "type": "string",
                            "description": "Filter by country.",
                        },
                        "special_capability": {
                            "type": "string",
                            "description": "Filter by a special capability (e.g., 'Cold Storage', 'Hazmat Certified').",
                        },
                        "special_capabilities": {
                            "type": "list",
                            "description": "Filter by multiple special capabilities (e.g., 'Cold Storage', 'Hazmat Certified').",
                        },
                    },
                },
            },
        }
