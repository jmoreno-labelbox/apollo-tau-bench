from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterFigmaArtifactsByTags(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], tags: list[str]) -> str:
        pass
        #Check the input for validity
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            payload = {"error": "tags must be a list of strings"}
            out = json.dumps(payload)
            return out
        artifacts = data.get("figma_artifacts", [])
        #Gather all distinct tags from artifacts
        all_tags = set()
        for artifact in artifacts:
            all_tags.update(artifact.get("current_tags", []))
        #Verify that all provided tags are plausible
        unrealistic = [tag for tag in tags if tag not in all_tags]
        if unrealistic:
            payload = {
                    "error": f"Unrealistic tags: {unrealistic}. These tags do not appear in any artifact."
                }
            out = json.dumps(
                payload)
            return out
        matching_ids = []
        for artifact in artifacts:
            artifact_tags = artifact.get("current_tags", [])
            if all(tag in artifact_tags for tag in tags):
                matching_ids.append(artifact.get("artifact_id"))
        if not matching_ids:
            payload = {"artifact_ids": "No matching artifacts found."}
            out = json.dumps(payload)
            return out
        payload = {"artifact_ids": matching_ids}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterFigmaArtifactsByTags",
                "description": "Filter Figma artifacts by tags and return matching artifact IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of tags to filter artifacts by. All tags must be present in the artifact.",
                        }
                    },
                    "required": ["tags"],
                },
            },
        }
