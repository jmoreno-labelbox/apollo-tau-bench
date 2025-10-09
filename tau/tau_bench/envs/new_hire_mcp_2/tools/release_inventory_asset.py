from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReleaseInventoryAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = None
            row["status"] = "Available"
            row.setdefault("updated_ts", NOW_TS)
            payload = {"asset_tag": asset_tag, "released": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"asset_tag": asset_tag, "released": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReleaseInventoryAsset",
                "description": "Release an inventory asset. No-op if not found.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_tag": {"type": "string"}},
                    "required": ["asset_tag"],
                },
            },
        }
