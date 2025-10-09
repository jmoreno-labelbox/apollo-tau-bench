from tau_bench.envs.tool import Tool
import json
from typing import Any

class InvalidateCacheForCatalog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str, catalog_id: str) -> str:
        org_id, catalog_id = _sid(org_id), _sid(catalog_id)
        _append_audit(data, "INVALIDATE_CACHE", f"{org_id}:{catalog_id}", {})
        _ws_append(data, f"{org_id}:{catalog_id}", "INVALIDATE_CACHE", {})
        payload = {"org_id": org_id, "catalog_id": catalog_id, "scheduled": True}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InvalidateCacheForCatalog",
                "description": "Record a cache invalidation for a catalog scope.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "catalog_id": {"type": "string"},
                    },
                    "required": ["org_id", "catalog_id"],
                },
            },
        }
