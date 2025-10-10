# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllArtifactsOfTypeWithTagsAndEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("artifact_type"):
            return json.dumps({"error": "Missing required field: artifact_type"}, indent=2)

        artifact_type = kwargs.get("artifact_type")
        tags = kwargs.get("tags")
        owner_email = kwargs.get("owner_email")

        artifacts = list(data.get("figma_artifacts", {}).values())
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
        return json.dumps({"count": len(results), "artifacts": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_artifacts_of_type_with_tags_and_email",
                "description": "Return artifacts of the given type, optionally filtered to include all specified tags and a specific owner_email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "owner_email": {"type": "string"}
                    },
                    "required": ["artifact_type"]
                }
            }
        }
