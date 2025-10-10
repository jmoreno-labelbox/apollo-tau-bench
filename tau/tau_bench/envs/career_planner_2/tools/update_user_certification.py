# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserCertification(Tool):
    """Update user certification."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        cert = kwargs.get("certification")
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
        return json.dumps({"success": f"{uid} earned {cert}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_certification",
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
