# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetArtifactWithId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id) -> str:
        if not artifact_id:
            return json.dumps({"error": "Missing required field: artifact_id"}, indent=2)
        artifacts = list(data.get("figma_artifacts", {}).values())
        for row in artifacts:
            if row.get("artifact_id") == artifact_id:
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No artifact with id '{artifact_id}'."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_artifact_with_id",
                "description": "Fetch a single Figma artifact by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"}
                    },
                    "required": ["artifact_id"]
                }
            }
        }
