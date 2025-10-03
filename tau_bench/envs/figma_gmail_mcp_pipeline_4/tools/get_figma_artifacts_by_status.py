from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetFigmaArtifactsByStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        status: str = None,
        tags: list[str] = None,
        review_status: str = None,
        artifact_type: str = None
    ) -> str:
        """
        Obtains Figma artifacts filtered by different criteria such as status, tags, and review state.
        """
        if tags is None:
            tags = []

        figma_artifacts = data.get("figma_artifacts", [])
        review_cycles = data.get("review_cycles", [])

        # Return the specific artifact if artifact_id is given
        if artifact_id:
            for artifact in figma_artifacts:
                if artifact.get("artifact_id") == artifact_id:
                    # Enhance with details from the review cycle
                    artifact_copy = artifact.copy()
                    for cycle in review_cycles:
                        if cycle.get("artifact_id") == artifact_id:
                            artifact_copy["review_cycle"] = cycle
                            break
                    payload = artifact_copy
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Artifact with ID '{artifact_id}' not found."}
            out = json.dumps(payload)
            return out

        # Sort artifacts based on specified criteria
        results = []
        for artifact in figma_artifacts:
            # Implement filters
            if status and artifact.get("status") != status:
                continue

            if artifact_type and artifact.get("artifact_type") != artifact_type:
                continue

            if tags:
                artifact_tags = artifact.get("current_tags", [])
                if not any(tag in artifact_tags for tag in tags):
                    continue

            # Augment with review cycle details
            artifact_copy = artifact.copy()
            for cycle in review_cycles:
                if cycle.get("artifact_id") == artifact.get("artifact_id"):
                    artifact_copy["review_cycle"] = cycle
                    break

            # Implement filter for review status
            if review_status:
                if "review_cycle" not in artifact_copy:
                    continue
                if artifact_copy["review_cycle"].get("status") != review_status:
                    continue

            results.append(artifact_copy)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFigmaArtifactsByStatus",
                "description": "Retrieves Figma artifacts filtered by various criteria including status, tags, review state, and artifact type. Enriches results with review cycle information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {
                            "type": "string",
                            "description": "The ID of a specific artifact to retrieve.",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by artifact status (e.g., 'active', 'archived').",
                        },
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by tags (e.g., ['needs-review', 'design-system']).",
                        },
                        "review_status": {
                            "type": "string",
                            "description": "Filter by review cycle status (e.g., 'NEEDS_REVIEW', 'APPROVED').",
                        },
                        "artifact_type": {
                            "type": "string",
                            "description": "Filter by artifact type (e.g., 'frame', 'component', 'page').",
                        },
                    },
                },
            },
        }
