# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetArtifactIdFromName(Tool):  # READ DATA
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        artifact_name: str
    ) -> str:
        # Check the input for correctness.
        if not isinstance(artifact_name, str) or not artifact_name:
            return json.dumps({"error": "artifact_name must be a non-empty string"})

        artifacts = data.get("figma_artifacts", [])

        # Locate the precise match initially.
        exact_match = None
        for artifact in artifacts:
            if artifact.get("artifact_name") == artifact_name:
                exact_match = artifact
                break

        if exact_match:
            return json.dumps({
                "artifact_id": exact_match.get("artifact_id"),
                "artifact_name": exact_match.get("artifact_name"),
                "artifact_type": exact_match.get("artifact_type"),
                "owner_email": exact_match.get("owner_email")
            })

        # If an exact match is not found, look for case-insensitive partial matches.
        partial_matches = []
        artifact_name_lower = artifact_name.lower()
        for artifact in artifacts:
            artifact_artifact_name = artifact.get("artifact_name", "").lower()
            if artifact_name_lower in artifact_artifact_name or artifact_artifact_name in artifact_name_lower:
                partial_matches.append({
                    "artifact_id": artifact.get("artifact_id"),
                    "artifact_name": artifact.get("artifact_name"),
                    "artifact_type": artifact.get("artifact_type"),
                    "owner_email": artifact.get("owner_email")
                })

        if partial_matches:
            return json.dumps({
                "exact_match": False,
                "partial_matches": partial_matches,
                "message": f"No exact match found for '{artifact_name}'. Found {len(partial_matches)} partial matches."
            })

        return json.dumps({"error": f"No artifact found with name '{artifact_name}'"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_artifact_id_from_name",
                "description": "Get artifact ID and details by searching for artifact name. Returns exact match if found, otherwise returns partial matches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_name": {"type": "string", "description": "The name of the artifact to search for."}
                    },
                    "required": ["artifact_name"]
                }
            }
        }
