from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetUserProfile(Tool):
    """
    API tool for retrieving customer profiles
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_email: str = None) -> str:
        if not user_email:
            payload = {
                "status": "missing_parameter",
                "message": "The user_email parameter is required to retrieve the user profile.",
                "required": "user_email",
            }
            out = json.dumps(payload)
            return out

        users = data.get("users", {}).values()
        target_user = None

        for user in users.values():
            if user.get("email") == user_email:
                target_user = user
                break

        if not target_user:
            payload = {
                "status": "not_found",
                "message": f"No user found with the email address '{user_email}'. Please check the email address and try again.",
                "email": user_email,
            }
            out = json.dumps(payload)
            return out

        payment_methods = target_user.get("payment_methods", {}).values()
        processed_payment_methods = []
        total_available_balance = 0

        for method_id, method_info in payment_methods.items():
            method_data = {
                "id": method_info.get("id", method_id),
                "source": method_info.get("source"),
                "primary_info": {},
            }

            if method_info.get("source") == "credit_card":
                method_data["primary_info"] = {
                    "brand": method_info.get("brand"),
                    "last_four": method_info.get("last_four"),
                }
            elif method_info.get("source") in ["gift_card", "certificate"]:
                amount = method_info.get("amount", 0)
                method_data["primary_info"] = {
                    "balance": amount,
                    "status": "active" if amount > 0 else "depleted",
                }
                total_available_balance += amount

            processed_payment_methods.append(method_data)

        saved_passengers = target_user.get("saved_passengers", [])
        passenger_count = len(saved_passengers)

        dob_str = target_user.get("dob")
        age = None
        if dob_str:
            try:
                dob = datetime.strptime(dob_str, "%Y-%m-%d")
                today = datetime.now()
                age = (
                    today.year
                    - dob.year
                    - ((today.month, today.day) < (dob.month, dob.day))
                )
            except ValueError:
                age = None

        reservations = target_user.get("reservations", [])
        reservation_count = len(reservations)

        membership_level = target_user.get("membership", "basic")
        membership_benefits = {
            "basic": ["Standard check-in", "Basic customer service"],
            "silver": [
                "Priority check-in",
                "1 free bag",
                "Preferred seating",
                "Silver customer service",
            ],
            "gold": [
                "Priority check-in",
                "2 free bags",
                "Preferred seating",
                "Lounge access",
                "Gold customer service",
                "Priority boarding",
            ],
            "platinum": [
                "Priority check-in",
                "3 free bags",
                "Premium seating",
                "Lounge access",
                "Platinum customer service",
                "Priority boarding",
                "Upgrade eligibility",
            ],
        }

        response = {
            "profile": {
                "personal_info": {
                    "name": target_user.get("name"),
                    "email": target_user.get("email"),
                    "date_of_birth": target_user.get("dob"),
                    "age": age,
                },
                "contact_info": {"address": target_user.get("address")},
                "membership": {
                    "level": membership_level,
                    "benefits": membership_benefits.get(membership_level, []),
                },
            },
            "preferences": {
                "saved_passengers": {
                    "count": passenger_count,
                    "passengers": saved_passengers,
                },
                "payment_methods": {
                    "total_methods": len(processed_payment_methods),
                    "total_available_balance": total_available_balance,
                    "methods": processed_payment_methods,
                },
            },
            "account_summary": {
                "total_reservations": reservation_count,
                "reservation_ids": reservations,
                "account_status": "active",
                "profile_completeness": {
                    "has_address": bool(target_user.get("address")),
                    "has_payment_methods": len(payment_methods) > 0,
                    "has_saved_passengers": passenger_count > 0,
                    "completion_percentage": round(
                        (
                            sum(
                                [
                                    bool(target_user.get("name")),
                                    bool(target_user.get("email")),
                                    bool(target_user.get("address")),
                                    bool(target_user.get("dob")),
                                    len(payment_methods) > 0,
                                    len(saved_passengers) > 0,
                                ]
                            )
                            / 6
                        )
                        * 100
                    ),
                },
            },
        }
        payload = response
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserProfile",
                "description": "Get customer profile and preferences by email address, including personal information, membership details, payment methods, saved passengers, and account summary. Supports membership levels: basic, silver, gold, platinum with corresponding benefits.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "Customer email address to retrieve profile information for",
                        }
                    },
                    "required": ["user_email"],
                },
            },
        }
