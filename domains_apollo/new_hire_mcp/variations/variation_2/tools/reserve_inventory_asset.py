from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReserveInventoryAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None, candidate_id: str = None) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Reserved"
            row.setdefault("updated_ts", NOW_TS)
            payload = {
                "asset_tag": asset_tag,
                "reserved": True,
                "candidate_id": candidate_id,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"asset_tag": asset_tag, "reserved": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reserveInventoryAsset",
                "description": "Reserve an inventory asset for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["asset_tag", "candidate_id"],
                },
            },
        }
