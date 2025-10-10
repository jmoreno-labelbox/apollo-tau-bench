# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUmpiresDetailsById(Tool):
    """Fetch an umpire record by umpire_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], umpire_id) -> str:

        # 1) Verify
        if umpire_id is None:
            return json.dumps({"error": "Missing required field: umpire_id"}, indent=2)

        # Retrieve database.
        umpires: List[Dict[str, Any]] = list(data.get("umpires", {}).values())

        # 3) Precise match
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
