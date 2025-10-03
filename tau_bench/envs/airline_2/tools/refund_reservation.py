from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class RefundReservation(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], reservation_id: str) -> str:
        """If a reservation is present, refund it and return a success or error message."""
        reservations = data.get("reservations", [])

        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                reservation["status"] = "refunded"
                payload = {"success": f"Reservation {reservation_id} has been refunded."}
                out = json.dumps(
                    payload)
                return out
        payload = {"error": f"Reservation with ID {reservation_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide metadata for the function signature of the tool."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "RefundReservation",
                "description": "refunds a reservation by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string",
                            "description": "The ID of the reservation to refund.",
                        }
                    },
                    "required": ["reservation_id"],
                },
            },
        }
