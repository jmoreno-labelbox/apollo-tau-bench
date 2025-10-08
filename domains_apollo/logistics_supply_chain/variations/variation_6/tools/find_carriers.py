from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindCarriers(Tool):
    """Utility for locating carriers according to their supported transport methods."""

    @staticmethod
    def invoke(data: dict[str, Any], transport_mode: str, carriers: list = None) -> str:
        """Run the tool using the specified parameters."""
        carriers = carriers if carriers is not None else data.get("carriers", [])
        results = [
            carrier
            for carrier in carriers
            if transport_mode in carrier.get("supported_modes", [])
            and carrier.get("active_status")
        ]
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
                "name": "FindCarriers",
                "description": "Finds active shipping carriers that support a specific mode of transport.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transport_mode": {
                            "type": "string",
                            "description": "The mode of transport (e.g., 'Air', 'Sea', 'Truck', 'Rail').",
                        }
                    },
                    "required": ["transport_mode"],
                },
            },
        }
