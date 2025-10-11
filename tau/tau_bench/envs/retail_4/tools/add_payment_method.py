# Sierra Copyright

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddPaymentMethod(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, payment_type: str, payment_details: Dict[str, Any]) -> str:
        """
        Add a new payment method to customer account

        Writes to: users.json (adds new payment method to user)
        """
        # Requirement: Confirm the existence of user identity prior to handling any user requests.
        users = list(data.get("users", {}).values())
        user_to_update = None
        user_index = None

        for i, user in enumerate(users):
            if user.get("user_id") == user_id:
                user_to_update = user
                user_index = i
                break

        if not user_to_update:
            return json.dumps({"error": f"User {user_id} not found", "status": "failed"})

        # Constraint: Accepted payment methods include credit_card, paypal, or gift_card.
        if payment_type not in ["credit_card", "paypal", "gift_card"]:
            return json.dumps({
                "error": f"Invalid payment type '{payment_type}'. Valid types: credit_card, paypal, gift_card",
                "status": "failed"
            })

        # Create a distinct identifier for the payment method.
        existing_payment_methods = user_to_update.get("payment_methods", {})
        method_count = len(existing_payment_methods) + 1
        new_payment_id = f"{payment_type}_{method_count}{user_id.split('_')[-1]}"

        # Verify payment information according to its type.
        new_payment_method = {
            "source": payment_type,
            "id": new_payment_id,
        }

        if payment_type == "credit_card":
            # Requirement: Credit card transactions should verify the last four digits and card brand.
            required_fields = ["brand", "last_four"]
            for field in required_fields:
                if field not in payment_details:
                    return json.dumps({
                        "error": f"Missing required field '{field}' for credit card",
                        "status": "failed"
                    })

            if payment_details["brand"] not in ["visa", "mastercard", "amex"]:
                return json.dumps({
                    "error": f"Invalid card brand '{payment_details['brand']}'",
                    "status": "failed"
                })

            new_payment_method["brand"] = payment_details["brand"]
            new_payment_method["last_four"] = payment_details["last_four"]

        elif payment_type == "gift_card":
            # Condition: Payments made with gift cards must not surpass the available balance.
            balance = payment_details.get("balance", 0)
            if balance < 0:
                return json.dumps({"error": "Gift card balance cannot be negative", "status": "failed"})
            new_payment_method["balance"] = balance

        # ADD OPERATION: Insert a new payment method into users.json
        if "payment_methods" not in user_to_update:
            user_to_update["payment_methods"] = {}

        user_to_update["payment_methods"][new_payment_id] = new_payment_method
        user_to_update["last_updated"] = datetime.now().isoformat()

        # Modify the user information in the data structure.
        data["users"][user_index] = user_to_update

        result = {
            "status": "success",
            "user_id": user_id,
            "payment_method_added": {
                "payment_method_id": new_payment_id,
                "payment_type": payment_type,
                "details": new_payment_method
            },
            "total_payment_methods": len(user_to_update["payment_methods"]),
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_payment_method",
                "description": "Add a new payment method to customer account",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "Customer identifier"},
                        "payment_type": {"type": "string", "description": "Payment method type (credit_card, paypal, gift_card)"},
                        "payment_details": {
                            "type": "object",
                            "description": "Payment method details (brand/last_four for credit_card, balance for gift_card)"
                        }
                    },
                    "required": ["user_id", "payment_type", "payment_details"]
                }
            }
        }
