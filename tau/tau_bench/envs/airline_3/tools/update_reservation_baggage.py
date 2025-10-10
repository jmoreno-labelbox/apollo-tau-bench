# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReservationBaggage(Tool):
    """
    Simple API tool to update reservation baggage information.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], reservation_id: str = None, total_baggages: int = None, nonfree_baggages: int = None) -> str:
        if not reservation_id:
            return json.dumps({
                "status": "missing_parameter",
                "message": "The reservation_id parameter is required to update baggage information.",
                "required": "reservation_id"
            })

        reservations = list(data.get("reservations", {}).values())
        target_reservation = None

        for reservation in reservations:
            if reservation.get("reservation_id") == reservation_id:
                target_reservation = reservation
                break

        if not target_reservation:
            return json.dumps({
                "status": "not_found",
                "message": f"No reservation found with ID '{reservation_id}'. Please check the reservation ID and try again.",
                "reservation_id": reservation_id
            })

        # Revise luggage details
        old_total = target_reservation.get("total_baggages", 0)
        old_nonfree = target_reservation.get("nonfree_baggages", 0)
        
        if total_baggages is not None:
            target_reservation["total_baggages"] = total_baggages
        
        if nonfree_baggages is not None:
            target_reservation["nonfree_baggages"] = nonfree_baggages
        
        # Verify that nonfree_baggages is not greater than total_baggages.
        if target_reservation.get("nonfree_baggages", 0) > target_reservation.get("total_baggages", 0):
            target_reservation["nonfree_baggages"] = target_reservation["total_baggages"]

        return json.dumps({
            "status": "success",
            "message": f"Reservation {reservation_id} baggage information updated successfully.",
            "reservation_id": reservation_id,
            "old_values": {
                "total_baggages": old_total,
                "nonfree_baggages": old_nonfree
            },
            "new_values": {
                "total_baggages": target_reservation.get("total_baggages"),
                "nonfree_baggages": target_reservation.get("nonfree_baggages")
            }
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reservation_baggage",
                "description": "Simple API tool to update reservation baggage information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reservation_id": {
                            "type": "string", 
                            "description": "The reservation ID to update. Format: 6-character alphanumeric code."
                        },
                        "total_baggages": {
                            "type": "integer",
                            "description": "Optional total number of baggage items for the reservation"
                        },
                        "nonfree_baggages": {
                            "type": "integer",
                            "description": "Optional number of non-free baggage items for the reservation"
                        }
                    },
                    "required": ["reservation_id"]
                }
            }
        }
