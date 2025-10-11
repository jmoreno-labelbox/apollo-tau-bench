# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class GetAssetFiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str) -> str:
        catalog = _get_table(data, "asset_catalog")
        rec = next((a for a in catalog if a.get("id") == asset_id), None)
        files = [rec.get("asset_path")] if rec and rec.get("asset_path") else []
        return json.dumps({"files": files}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_asset_files", "description": "Retrieves asset file paths from asset_catalog by asset_id.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}}, "required": ["asset_id"]}}}