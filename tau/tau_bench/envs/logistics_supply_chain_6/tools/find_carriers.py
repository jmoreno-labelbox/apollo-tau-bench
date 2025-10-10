# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCarriers(Tool):
    """Tool to find carriers based on supported transport modes."""

    @staticmethod
    def invoke(data: Dict[str, Any], transport_mode: str) -> str:
        """Execute the tool with given parameters."""
        carriers = data.get("carriers", [])
        results = [
            carrier for carrier in carriers
            if transport_mode in carrier.get("supported_modes", []) and carrier.get("active_status")
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_carriers",
                "description": "Finds active shipping carriers that support a specific mode of transport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transport_mode": {"type": "string", "description": "The mode of transport (e.g., 'Air', 'Sea', 'Truck', 'Rail')."}
                    },
                    "required": ["transport_mode"],
                },
            },
        }
