# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCourier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], tracking_id: str) -> str:
        """
        Get courier ID based on tracking ID

        Data Sources: couriers.json (courier tracking pools)
        """
        if not tracking_id or not tracking_id.strip():
            return json.dumps({
                "error": "Tracking ID is required",
                "status": "failed"
            })

        tracking_id = tracking_id.strip()

        # Find which courier has this tracking ID
        couriers = data.get("couriers", [])

        for courier in couriers:
            courier_tracking_ids = courier.get("tracking_ids", [])
            if tracking_id in courier_tracking_ids:
                result = {
                    "status": "success",
                    "tracking_id": tracking_id,
                    "courier_id": courier.get("courier_id")
                }
                return json.dumps(result)

        # Tracking ID not found
        return json.dumps({
            "error": f"Tracking ID {tracking_id} not found",
            "status": "not_found"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_courier",
                "description": "Get courier ID based on tracking ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string", "description": "Package tracking identifier"}
                    },
                    "required": ["tracking_id"]
                }
            }
        }
