# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCarrier(Tool):
    """Tool to update carrier information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_scac = kwargs.get("carrier_scac")
        updates = kwargs.get("updates")
        carriers = list(data.get("carriers", {}).values())

        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                carrier.update(updates)
                return json.dumps({"success": f"carrier {carrier_scac} updated"}, indent=2)
        return json.dumps({"error": f"carrier_id {carrier_scac} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_carrier",
                "description": "Update carrier information by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {"type": "string", "description": "The carrier ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["carrier_scac", "updates"]
                }
            }
        }
