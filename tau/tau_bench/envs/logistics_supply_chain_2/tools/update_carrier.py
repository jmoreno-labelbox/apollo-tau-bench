from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCarrier(Tool):
    """Utility for modifying carrier details."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_scac: str = None, updates: dict[str, Any] = None) -> str:
        carriers = data.get("carriers", {}).values()

        for carrier in carriers.values():
            if carrier["scac"] == carrier_scac:
                carrier.update(updates)
                payload = {"success": f"carrier {carrier_scac} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"carrier_id {carrier_scac} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCarrier",
                "description": "Update carrier information by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {
                            "type": "string",
                            "description": "The carrier ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["carrier_scac", "updates"],
                },
            },
        }
