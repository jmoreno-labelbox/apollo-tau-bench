# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListChangedAssetsV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], commit_sha: str) -> str:
        catalog = _get_table(data, "asset_catalog")
        # Deterministic: return assets whose updated_at exists (dataset simulated), ignore commit.
        files = [row.get("asset_path") for row in catalog if row.get("asset_path")]
        return json.dumps({"files": files}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_changed_assets_v2", "description": "Returns deterministic list of asset paths (simulated changed set).", "parameters": {"type": "object", "properties": {"commit_sha": {"type": "string"}}, "required": ["commit_sha"]}}}
