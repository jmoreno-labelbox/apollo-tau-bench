from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCertificationDetailsTool(Tool):
    """Retrieve information about a certification."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None,
    user_id: Any = None,
    ) -> str:
        cid = certification_id
        for c in data.get("certifications", []):
            if c["certification_id"] == cid:
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Certification {cid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetails",
                "description": "Get details of a certification record",
                "parameters": {
                    "type": "object",
                    "properties": {"certification_id": {"type": "string"}},
                    "required": ["certification_id"],
                },
            },
        }
