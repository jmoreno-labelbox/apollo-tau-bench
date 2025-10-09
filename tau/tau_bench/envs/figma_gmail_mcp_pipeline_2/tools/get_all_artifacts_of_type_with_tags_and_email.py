from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any

class GetAllArtifactsOfTypeWithTagsAndEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_type: str = None, tags: list = None, owner_email: str = None) -> str:
        if not artifact_type:
            payload = {"error": "Missing required field: artifact_type"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", [])
        results = []
        for row in artifacts:
            if row.get("artifact_type") != artifact_type:
                continue
            if tags:
                row_tags = row.get("current_tags") or []
                if not set(tags).issubset(set(row_tags)):
                    continue
            if owner_email and row.get("owner_email") != owner_email:
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("artifact_id")))
        payload = {"count": len(results), "artifacts": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllArtifactsOfTypeWithTagsAndEmail",
                "description": "Return artifacts of the given type, optionally filtered to include all specified tags and a specific owner_email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "owner_email": {"type": "string"},
                    },
                    "required": ["artifact_type"],
                },
            },
        }
