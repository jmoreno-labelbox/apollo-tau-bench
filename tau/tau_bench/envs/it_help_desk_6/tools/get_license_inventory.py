# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLicenseInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_id: Optional[str] = None) -> str:
        if license_id:
            row = _find_one(data["license_inventory"], license_id=license_id)
            return json.dumps({"status": "ok", "inventory": row})
        return json.dumps({"status": "ok", "inventory": data["license_inventory"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_license_inventory",
                "description": "Read license inventory optionally filtered by license_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
