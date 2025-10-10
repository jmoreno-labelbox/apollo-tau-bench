# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildBearerForConnectedApp(Tool):
    """Deterministically build an Authorization: Bearer header for an org/client pair (compute-only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, client_id: Any) -> str:
        if not org_id or not client_id:
            return json.dumps(
                {"error": "Missing required fields: org_id and/or client_id"}, indent=2
            )
        token = f"{org_id}:{client_id}"
        digest = hex(sum(ord(c) for c in token))[2:].rjust(16, "0")[-16:]
        header = f"Bearer {digest}"
        return json.dumps({"authorization_header": header}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "build_bearer_for_connected_app",
                "description": "Return a deterministic Authorization header (Bearer ...) for org_id + client_id (compute-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "client_id": {"type": "string"},
                    },
                    "required": ["org_id", "client_id"],
                },
            },
        }
