# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAssetsByArtifactId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id) -> str:
        if not artifact_id:
            return json.dumps({"error": "Missing required field: artifact_id"}, indent=2)
        assets = data.get("assets", [])

        results = [row for row in assets if row.get("artifact_id_nullable") == artifact_id]

        if not results:
            return json.dumps({"error": f"No assets found for artifact_id '{artifact_id}'"}, indent=2)

        results.sort(key=lambda r: str(r.get("asset_id")))
        return json.dumps({"count": len(results), "assets": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_assets_by_artifact_id",
                "description": "Return all asset objects belonging to the given artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"}
                    },
                    "required": ["artifact_id"]
                }
            }
        }
