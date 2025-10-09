from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCourier(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str) -> str:
        """
        Get courier ID based on tracking ID

        Data Sources: couriers.json (courier tracking pools)
        """
        if not tracking_id or not tracking_id.strip():
            payload = {"error": "Tracking ID is required", "status": "failed"}
            out = json.dumps(payload)
            return out

        tracking_id = tracking_id.strip()

        # Find which courier has this tracking ID
        couriers = data.get("couriers", [])

        for courier in couriers:
            courier_tracking_ids = courier.get("tracking_ids", [])
            if tracking_id in courier_tracking_ids:
                result = {
                    "status": "success",
                    "tracking_id": tracking_id,
                    "courier_id": courier.get("courier_id"),
                }
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": f"Tracking ID {tracking_id} not found", "status": "not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourier",
                "description": "Get courier ID based on tracking ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "Package tracking identifier",
                        }
                    },
                    "required": ["tracking_id"],
                },
            },
        }
