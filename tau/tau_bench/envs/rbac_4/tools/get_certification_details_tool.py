# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCertificationDetailsTool(Tool):
    """Get details of a certification."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("certification_id")
        for c in data.get("certifications", []):
            if c["certification_id"] == cid:
                return json.dumps(c, indent=2)
        return json.dumps({"error": f"Certification {cid} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification_details",
                "description": "Get details of a certification record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {"type": "string"}
                    },
                    "required": ["certification_id"]
                }
            }
        }
