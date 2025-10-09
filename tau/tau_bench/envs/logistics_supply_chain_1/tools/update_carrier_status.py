from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateCarrierStatus(Tool):
    """Modifies the status of a carrier."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None, status: str = None) -> str:
        if not all([carrier_name, status]):
            payload = {"error": "carrier_name and status are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        carrier_to_update = next(
            (
                c
                for c in data.get("carriers", [])
                if c.get("carrier_name") == carrier_name
            ),
            None,
        )
        if not carrier_to_update:
            payload = {"error": f"Carrier '{carrier_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        carrier_to_update["active_status"] = status
        payload = {
                "carrier_id": carrier_to_update.get("carrier_id"),
                "carrier_name": carrier_name,
                "new_status": status,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCarrierStatus",
                "description": "Updates the operational status of a carrier (e.g., True, False, 'Under Review').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {"type": "string"},
                        "status": {
                            "type": "string",
                            "description": "The new status to set for the carrier.",
                        },
                    },
                    "required": ["carrier_name", "status"],
                },
            },
        }
