from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any

class GetArtifactsWithFileId(Tool):
    def invoke(
        data: dict[str, Any],
        artifact_type: str = None,
        figma_file_id: str = None,
        frame_id: str = None,
        page_id: str = None
    ) -> str:
        if not figma_file_id:
            payload = {"error": "Missing required field: figma_file_id"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", [])
        results = []
        for row in artifacts:
            if row.get("figma_file_id") != figma_file_id:
                continue
            if artifact_type and row.get("artifact_type") != artifact_type:
                continue
            if frame_id is not None and row.get("frame_id_nullable") != frame_id:
                continue
            if (
                frame_id is None
                and page_id is not None
                and row.get("page_id") != page_id
            ):
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("artifact_id")))
        if not results:
            payload = {"error": "No artifacts matched"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"count": len(results), "artifacts": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getArtifactsWithFileId",
                "description": "Return artifacts for a figma_file_id. Optional filters: artifact_type, page_id, frame_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figma_file_id": {"type": "string"},
                        "artifact_type": {
                            "type": "string",
                            "enum": ["FILE", "PAGE", "FRAME"],
                        },
                        "page_id": {"type": "string"},
                        "frame_id": {"type": "string"},
                    },
                    "required": ["figma_file_id"],
                },
            },
        }
