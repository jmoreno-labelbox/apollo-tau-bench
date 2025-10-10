# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RefundReservation(Tool):
    """Tool to Refund a passenger's reservation by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str) -> str:
        """Refund a reservation if it exists; return success or error message."""
        # Reconstruct kwargs from explicit params to keep body unchanged
        kwargs = {__k: __v for __k, __v in [('reservation_id', reservation_id)] if __v is not None}

        reservation_id = kwargs.get("reservation_id")
        reservations = list(data.get("reservations", {}).values())

        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                reservation["status"] = "refunded"
                return json.dumps(
                    {"success": f"Reservation {reservation_id} has been refunded."}
                )

        return json.dumps(
            {"error": f"Reservation with ID {reservation_id} not found."},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return metadata for the tool's function signature."""
        return {
            "type": "function",
            "function": {
                "name": "refund_reservation",
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
