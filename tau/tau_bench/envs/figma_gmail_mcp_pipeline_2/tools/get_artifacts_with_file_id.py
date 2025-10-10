# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetArtifactsWithFileId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_type, figma_file_id, frame_id, page_id) -> str:
        if not figma_file_id:
            return json.dumps({"error": "Missing required field: figma_file_id"}, indent=2)

        artifacts = list(data.get("figma_artifacts", {}).values())
        results = []
        for row in artifacts:
            if row.get("figma_file_id") != figma_file_id:
                continue
            if artifact_type and row.get("artifact_type") != artifact_type:
                continue
            if frame_id is not None and row.get("frame_id_nullable") != frame_id:
                continue
            if frame_id is None and page_id is not None and row.get("page_id") != page_id:
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("artifact_id")))
        if not results:
            return json.dumps({"error": "No artifacts matched"}, indent=2)
        return json.dumps({"count": len(results), "artifacts": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_artifacts_with_file_id",
                "description": "Return artifacts for a figma_file_id. Optional filters: artifact_type, page_id, frame_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "artifact_type": {"type": "string", "enum": ["FILE", "PAGE", "FRAME"]},
                        "page_id": {"type": "string"},
                        "frame_id": {"type": "string"}
                    },
                    "required": ["figma_file_id"]
                }
            }
        }
