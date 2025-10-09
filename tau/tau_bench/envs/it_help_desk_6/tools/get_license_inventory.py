from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetLicenseInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str | None = None) -> str:
        pass
        if license_id:
            row = _find_one(data["license_inventory"], license_id=license_id)
            payload = {"status": "ok", "inventory": row}
            out = json.dumps(payload)
            return out
        payload = {"status": "ok", "inventory": data["license_inventory"]}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLicenseInventory",
                "description": "Read license inventory optionally filtered by license_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
