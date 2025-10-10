# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_user_certification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, cert: dict) -> str:
        cert["user_id"] = user_id
        data.setdefault("user_certification", []).append(cert)
        return json.dumps(
            {"success": f"Certification {cert['cert_name']} added for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_user_certification",
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
