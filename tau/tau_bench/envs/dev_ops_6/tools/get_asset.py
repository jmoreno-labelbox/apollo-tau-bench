from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAsset(Tool):
    """Retrieve an asset using asset_path or id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, asset_path: str = None) -> str:
        rows = _table(data, "asset_catalog")
        row = next(
            (
                r
                for r in rows
                if id
                and r.get("id") == id
                or (asset_path and r.get("asset_path") == asset_path)
            ),
            None,
        )
        return _ok({"asset": row}) if row else _err("asset not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAsset",
                "description": "Fetch an asset by asset_path (or id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "asset_path": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
