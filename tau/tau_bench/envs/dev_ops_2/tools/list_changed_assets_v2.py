from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListChangedAssetsV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], commit_sha: str) -> str:
        pass
        catalog = _get_table(data, "asset_catalog")
        #Consistent: return assets with an existing updated_at (simulated dataset), disregard commit.
        files = [row.get("asset_path") for row in catalog if row.get("asset_path")]
        payload = {"files": files}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListChangedAssetsV2",
                "description": "Returns deterministic list of asset paths (simulated changed set).",
                "parameters": {
                    "type": "object",
                    "properties": {"commit_sha": {"type": "string"}},
                    "required": ["commit_sha"],
                },
            },
        }
