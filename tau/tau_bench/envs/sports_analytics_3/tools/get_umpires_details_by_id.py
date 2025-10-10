# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUmpiresDetailsById(Tool):
    """Fetch an umpire record by umpire_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        umpire_id = kwargs.get("umpire_id")

        # 1) Validate
        if umpire_id is None:
            return json.dumps({"error": "Missing required field: umpire_id"}, indent=2)

        # 2) Get DB
        umpires: List[Dict[str, Any]] = list(data.get("umpires", {}).values())

        # 3) Exact match
        for ump in umpires:
            if ump.get("umpire_id") == umpire_id:
                return json.dumps(ump, indent=2)

        return json.dumps({"error": f"No umpire found with ID {umpire_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_umpires_details_by_id",
                "description": "Fetch a single umpire's full details by umpire_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "umpire_id": {
                            "type": "integer",
                            "description": "Exact umpire ID to retrieve."
                        }
                    },
                    "required": ["umpire_id"]
                }
            }
        }
