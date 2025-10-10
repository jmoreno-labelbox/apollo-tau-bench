# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendCertificate(Tool):
    """
    A tool to issue a new travel certificate to a user.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], user_email: str, amount: float) -> str:
        users = list(data.get("users", {}).values())
        user = next((u for u in users if u.get("email", "").startswith(user_email)), None)
        if not user:
            return json.dumps({"error": "User not found", "user_email": user_email})

        payment_methods = user.get("payment_methods", {})
        cert_ids = [int(k.split('_')[-1]) for k in payment_methods if k.startswith('certificate_')]
        next_id_num = max(cert_ids) + 1 if cert_ids else 1000001
        new_cert_id = f"certificate_{next_id_num}"

        payment_methods[new_cert_id] = {
            "source": "certificate",
            "amount": amount,
            "id": new_cert_id
        }
        user["payment_methods"] = payment_methods
        return json.dumps({"status": "success", "user_email": user_email, "certificate_id": new_cert_id, "amount": amount})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_certificate",
                "description": "Issues a new travel certificate of a specific value to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "The user's email address to receive the certificate."
                        },
                        "amount": {
                            "type": "number",
                            "description": "The value of the certificate to be issued."
                        }
                    },
                    "required": ["user_email", "amount"]
                }
            }
        }
