from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateUserCertification(Tool):
    """Revise a user's certification."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, certification: str = None) -> str:
        uid = user_id
        cert = certification
        certs = data.setdefault("user_certifications", [])
        certs[:] = [
            c for c in certs if not (c["user_id"] == uid and c["certification"] == cert)
        ]
        certs.append(
            {
                "user_id": uid,
                "certification": cert,
                "date_earned": datetime.utcnow().date().isoformat(),
            }
        )
        payload = {"success": f"{uid} earned {cert}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateUserCertification",
                "description": "Update user certification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "certification": {"type": "string"},
                    },
                    "required": ["user_id", "certification"],
                },
            },
        }
