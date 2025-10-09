from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAssetFiles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str) -> str:
        catalog = _get_table(data, "asset_catalog")
        rec = next((a for a in catalog if a.get("id") == asset_id), None)
        files = [rec.get("asset_path")] if rec and rec.get("asset_path") else []
        payload = {"files": files}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAssetFiles",
                "description": "Retrieves asset file paths from asset_catalog by asset_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }
