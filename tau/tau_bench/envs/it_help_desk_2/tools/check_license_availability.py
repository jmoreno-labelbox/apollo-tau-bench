from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None) -> str:
        license_id = license_id
        inventory = data.get("license_inventory", [])
        license_info = next(
            (lic for lic in inventory if lic.get("license_id") == license_id), None
        )
        if not license_info:
            payload = {"error": f"License ID {license_id} not found in inventory."}
            out = json.dumps(payload, indent=2)
            return out
        available = license_info.get("total_seats", 0) - license_info.get(
            "used_seats", 0
        )
        payload = {
            "license_id": license_id,
            "seats_available": available > 0,
            "available_count": available,
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckLicenseAvailability",
                "description": "Check if there are available seats for a given license SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}},
                    "required": ["license_id"],
                },
            },
        }
