# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

class UpdateReservationDetails(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        reservation_id: str,
        flights: Optional[List[Dict[str, str]]] = None,
        passengers: Optional[List[Dict[str, str]]] = None,
        cabin: Optional[str]=None,
        seat: Optional[str]=None,
        contact_email: Optional[str]=None,
        contact_phone: Optional[str]=None,
        insurance: Optional[str] = None,
        total_baggages :Optional[int] = None,
        nonfree_baggages : Optional[int] = None,
    ) -> str:
        reservations = list(data.get("reservations", {}).values())
        for r in reservations:
            if r.get("reservation_id") == reservation_id:
                if cabin is not None:
                    r["cabin"] = cabin
                if seat is not None:
                    r["seat"] = seat
                if insurance is not None:
                    r["insurance"] = insurance
                if total_baggages is not None:
                    r["total_baggages"] = total_baggages
                if nonfree_baggages is not None:
                    r["nonfree_baggages"] = nonfree_baggages

                if flights is not None:
                    r["flights"] = flights
                if passengers is not None:
                    r["passengers"] = passengers
                if contact_email is not None:
                    r.setdefault("contact", {})["email"] = contact_email
                if contact_phone is not None:
                    r.setdefault("contact", {})["phone"] = contact_phone
                return _j(r)
        return _j({"error":"reservation_not_found","reservation_id":reservation_id})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"update_reservation_details",
            "description":"Update editable reservation fields (cabin, seat, contact email/phone).",
            "parameters":{"type":"object","properties":{
                "reservation_id":{"type":"string"},
                "cabin":{"type":"string"},
                "seat":{"type":"string"},
                "contact_email":{"type":"string"},
                "contact_phone":{"type":"string"},
                "insurance": {"type": "string"},
                "total_baggages": {"type": "integer"},
                "nonfree_baggages": {"type": "integer"},
                "flights": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "flight_number": {"type": "string"},
                            "date": {"type": "string", "description": "Date in YYYY-MM-DD format."},
                            "origin": {"type": "string"},
                            "destination": {"type": "string"}
                        },
                        "required": ["flight_number", "date", "origin", "destination"]
                    }
                },
                "passengers": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "first_name": {"type": "string"},
                            "last_name": {"type": "string"},
                            "dob": {"type": "string", "description": "Date of birth in YYYY-MM-DD format."}
                        },
                        "required": ["first_name", "last_name", "dob"]
                    }
                },
            },"required":["reservation_id"]}
        }}