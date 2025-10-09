from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class SendCertificate(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], user_email: str, amount: float) -> str:
        users = data.get("users", [])
        user = next(
            (u for u in users if u.get("email", "").startswith(user_email)), None
        )
        if not user:
            payload = {"error": "User not found", "user_email": user_email}
            out = json.dumps(payload)
            return out

        payment_methods = user.get("payment_methods", {})
        cert_ids = [
            int(k.split("_")[-1])
            for k in payment_methods
            if k.startswith("certificate_")
        ]
        next_id_num = max(cert_ids) + 1 if cert_ids else 1000001
        new_cert_id = f"certificate_{next_id_num}"

        payment_methods[new_cert_id] = {
            "source": "certificate",
            "amount": amount,
            "id": new_cert_id,
        }
        user["payment_methods"] = payment_methods
        payload = {
                "status": "success",
                "user_email": user_email,
                "certificate_id": new_cert_id,
                "amount": amount,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendCertificate",
                "description": "Issues a new travel certificate of a specific value to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_email": {
                            "type": "string",
                            "description": "The user's email address to receive the certificate.",
                        },
                        "amount": {
                            "type": "number",
                            "description": "The value of the certificate to be issued.",
                        },
                    },
                    "required": ["user_email", "amount"],
                },
            },
        }
