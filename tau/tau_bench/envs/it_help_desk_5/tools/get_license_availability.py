from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None) -> str:
        inventory = data.get("license_inventory")

        if license_id is None:
            payload = {"status": "error", "reason": "The license_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        for license in inventory.values():
            if license["license_id"] == license_id:
                if (
                    license["total_seats"]
                    - license["reserved_seats"]
                    - license["used_seats"]
                    > 0
                ):
                    payload = {"available": True}
                    out = json.dumps(payload, indent=2)
                    return out
                else:
                    payload = {"available": False}
                    out = json.dumps(payload, indent=2)
                    return out
        payload = {"status": "error", "reason": f"License {license_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLicenseAvailability",
                "description": "Checks if a license with a designated id is available.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The id of the license to search for.",
                        }
                    },
                },
            },
        }
