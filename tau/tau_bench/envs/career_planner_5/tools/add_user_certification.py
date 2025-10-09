from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddUserCertification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, cert: dict) -> str:
        cert["user_id"] = user_id
        data.setdefault("user_certification", []).append(cert)
        payload = {"success": f"Certification {cert['cert_name']} added for user {user_id}"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addUserCertification",
                "description": "Add a certification for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "cert": {"type": "object"},
                    },
                    "required": ["user_id", "cert"],
                },
            },
        }
