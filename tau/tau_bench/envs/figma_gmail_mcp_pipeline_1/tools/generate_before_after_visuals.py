# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateBeforeAfterVisuals(Tool):  # GENERATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        release_id: str,
        hero_artifact_ids: List[str]
    ) -> str:
        # Verify the input.
        if not isinstance(release_id, str) or not release_id:
            return json.dumps({"error": "release_id must be a non-empty string"})

        if not isinstance(hero_artifact_ids, list) or not all(isinstance(aid, str) for aid in hero_artifact_ids):
            return json.dumps({"error": "hero_artifact_ids must be a list of strings"})

        # Create a consistent visual identifier derived from release_id.
        visual_name = f"before_after_visual_{release_id}"

        # Generate a consistent hash-style suffix derived from hero_artifact_ids.
        artifacts_string = "".join(sorted(hero_artifact_ids))
        artifacts_hash = custom_hash(artifacts_string) % 10000
        visual_name_with_hash = f"{visual_name}_{artifacts_hash:04d}"

        return json.dumps({
            "visual_name": visual_name_with_hash,
            "success": True,
            "message": f"Before/after visual successfully created for release {release_id}",
            "hero_artifacts_processed": len(hero_artifact_ids),
            "artifacts_included": hero_artifact_ids
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_before_after_visuals",
                "description": "Generate before/after visuals for a release using hero artifacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "release_id": {"type": "string", "description": "The release ID to generate visuals for."},
                        "hero_artifact_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of hero artifact IDs to include in the visual."
                        }
                    },
                    "required": ["release_id", "hero_artifact_ids"]
                }
            }
        }
