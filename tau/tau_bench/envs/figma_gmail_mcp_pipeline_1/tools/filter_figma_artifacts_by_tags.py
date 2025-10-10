# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterFigmaArtifactsByTags(Tool):  # READ
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        tags: List[str]
    ) -> str:
        # Validate input
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            return json.dumps({"error": "tags must be a list of strings"})
        artifacts = data.get("figma_artifacts", [])
        # Collect all unique tags from artifacts
        all_tags = set()
        for artifact in artifacts:
            all_tags.update(artifact.get("current_tags", []))
        # Check if all input tags are realistic
        unrealistic = [tag for tag in tags if tag not in all_tags]
        if unrealistic:
            return json.dumps({"error": f"Unrealistic tags: {unrealistic}. These tags do not appear in any artifact."})
        matching_ids = []
        for artifact in artifacts:
            artifact_tags = artifact.get("current_tags", [])
            if all(tag in artifact_tags for tag in tags):
                matching_ids.append(artifact.get("artifact_id"))
        if not matching_ids:
            return json.dumps({"artifact_ids": "No matching artifacts found."})
        return json.dumps({"artifact_ids": matching_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_figma_artifacts_by_tags",
                "description": "Filter Figma artifacts by tags and return matching artifact IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of tags to filter artifacts by. All tags must be present in the artifact."
                        }
                    },
                    "required": ["tags"]
                }
            }
        }
