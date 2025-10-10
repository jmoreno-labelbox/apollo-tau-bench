# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFigmaArtifactsByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves Figma artifacts filtered by various criteria including status, tags, and review state.
        """
        artifact_id = kwargs.get('artifact_id')
        status = kwargs.get('status')
        tags = kwargs.get('tags', [])
        review_status = kwargs.get('review_status')
        artifact_type = kwargs.get('artifact_type')

        figma_artifacts = data.get('figma_artifacts', [])
        review_cycles = data.get('review_cycles', [])

        # If artifact_id is provided, return specific artifact
        if artifact_id:
            for artifact in figma_artifacts:
                if artifact.get('artifact_id') == artifact_id:
                    # Enrich with review cycle information
                    artifact_copy = artifact.copy()
                    for cycle in review_cycles:
                        if cycle.get('artifact_id') == artifact_id:
                            artifact_copy['review_cycle'] = cycle
                            break
                    return json.dumps(artifact_copy, indent=2)
            return json.dumps({"error": f"Artifact with ID '{artifact_id}' not found."})

        # Filter artifacts by criteria
        results = []
        for artifact in figma_artifacts:
            # Apply filters
            if status and artifact.get('status') != status:
                continue

            if artifact_type and artifact.get('artifact_type') != artifact_type:
                continue

            if tags:
                artifact_tags = artifact.get('current_tags', [])
                if not any(tag in artifact_tags for tag in tags):
                    continue

            # Enrich with review cycle information
            artifact_copy = artifact.copy()
            for cycle in review_cycles:
                if cycle.get('artifact_id') == artifact.get('artifact_id'):
                    artifact_copy['review_cycle'] = cycle
                    break

            # Apply review status filter
            if review_status:
                if 'review_cycle' not in artifact_copy:
                    continue
                if artifact_copy['review_cycle'].get('status') != review_status:
                    continue

            results.append(artifact_copy)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_figma_artifacts_by_status",
                "description": "Retrieves Figma artifacts filtered by various criteria including status, tags, review state, and artifact type. Enriches results with review cycle information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string", "description": "The ID of a specific artifact to retrieve."},
                        "status": {"type": "string", "description": "Filter by artifact status (e.g., 'active', 'archived')."},
                        "tags": {"type": "array", "items": {"type": "string"}, "description": "Filter by tags (e.g., ['needs-review', 'design-system'])."},
                        "review_status": {"type": "string", "description": "Filter by review cycle status (e.g., 'NEEDS_REVIEW', 'APPROVED')."},
                        "artifact_type": {"type": "string", "description": "Filter by artifact type (e.g., 'frame', 'component', 'page')."}
                    }
                }
            }
        }
