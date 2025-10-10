# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUmpiresDetailsByName(Tool):
    """Fetch an umpire record by full_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], full_name) -> str:

        # 1) Verify
        if not isinstance(full_name, str) or full_name == "":
            return json.dumps({"error": "Missing required field: full_name"}, indent=2)

        # Retrieve database
        umpires: List[Dict[str, Any]] = list(data.get("umpires", {}).values())

        # 3) Precise match (without normalization)
        for ump in umpires:
            if ump.get("full_name") == full_name:
                return json.dumps(ump, indent=2)

        return json.dumps({"error": f"No umpire found with full_name {full_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_umpires_details_by_name",
                "description": "Fetch a single umpire's full details by exact full_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact umpire full name to retrieve."
                        }
                    },
                    "required": ["full_name"]
                }
            }
        }
