from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateBeforeAfterVisuals(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any], release_id: str, hero_artifact_ids: list[str]
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(release_id, str) or not release_id:
            payload = {"error": "release_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(hero_artifact_ids, list) or not all(
            isinstance(aid, str) for aid in hero_artifact_ids
        ):
            payload = {"error": "hero_artifact_ids must be a list of strings"}
            out = json.dumps(payload)
            return out

        #Create a consistent visual name derived from release_id
        visual_name = f"before_after_visual_{release_id}"

        #Generate a consistent hash-like suffix using hero_artifact_ids
        artifacts_string = "".join(sorted(hero_artifact_ids))
        artifacts_hash = custom_hash(artifacts_string) % 10000
        visual_name_with_hash = f"{visual_name}_{artifacts_hash:04d}"
        payload = {
                "visual_name": visual_name_with_hash,
                "success": True,
                "message": f"Before/after visual successfully created for release {release_id}",
                "hero_artifacts_processed": len(hero_artifact_ids),
                "artifacts_included": hero_artifact_ids,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateBeforeAfterVisuals",
                "description": "Generate before/after visuals for a release using hero artifacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {
                            "type": "string",
                            "description": "The release ID to generate visuals for.",
                        },
                        "hero_artifact_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of hero artifact IDs to include in the visual.",
                        },
                    },
                    "required": ["release_id", "hero_artifact_ids"],
                },
            },
        }
