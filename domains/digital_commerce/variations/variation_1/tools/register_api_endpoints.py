from tau_bench.envs.tool import Tool
import json
from typing import Any

class RegisterApiEndpoints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], spec_id: str, gateway_id: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        # Simple mapping (to ensure consistency, we only provide a single GET endpoint)
        endpoint_id = _stable_id("ep", spec_id, gateway_id)
        route_map = {"GET /v3/offers": endpoint_id}
        key = f"Endpoints:{spec_id}:{gateway_id}"
        row = _find_one(settings, name=key)
        val = json.dumps({"endpoint_ids": [endpoint_id], "route_map": route_map})
        if row:
            row["value"] = val
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", key),
                    "name": key,
                    "value": val,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"endpoint_ids": [endpoint_id], "route_map": route_map})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterApiEndpoints",
                "description": "Register endpoints from an OpenAPI spec into a gateway.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spec_id": {"type": "string"},
                        "gateway_id": {"type": "string"},
                    },
                    "required": ["spec_id", "gateway_id"],
                },
            },
        }
