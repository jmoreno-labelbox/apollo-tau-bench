from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetInventoryAssetFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str, fields: dict[str, Any] = {}) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            payload = {"asset_tag": asset_tag, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"asset_tag": asset_tag, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setInventoryAssetFields",
                "description": "Update fields on an inventory asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["asset_tag", "fields"],
                },
            },
        }
