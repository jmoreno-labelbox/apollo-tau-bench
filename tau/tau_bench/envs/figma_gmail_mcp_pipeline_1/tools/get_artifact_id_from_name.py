from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetArtifactIdFromName(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], artifact_name: str) -> str:
        _artifact_nameL = artifact_name or ''.lower()
        pass
        #Check the input for validity
        if not isinstance(artifact_name, str) or not artifact_name:
            payload = {"error": "artifact_name must be a non-empty string"}
            out = json.dumps(payload)
            return out

        artifacts = data.get("figma_artifacts", {}).values()

        #Look for an exact match initially
        exact_match = None
        for artifact in artifacts.values():
            if artifact.get("artifact_name") == artifact_name:
                exact_match = artifact
                break

        if exact_match:
            payload = {
                    "artifact_id": exact_match.get("artifact_id"),
                    "artifact_name": exact_match.get("artifact_name"),
                    "artifact_type": exact_match.get("artifact_type"),
                    "owner_email": exact_match.get("owner_email"),
                }
            out = json.dumps(
                payload)
            return out

        #If an exact match is not found, search for partial matches (case-insensitive)
        partial_matches = []
        artifact_name_lower = artifact_name.lower()
        for artifact in artifacts.values():
            artifact_artifact_name = artifact.get("artifact_name", "").lower()
            if (
                artifact_name_lower in artifact_artifact_name
                or artifact_artifact_name in artifact_name_lower
            ):
                partial_matches.append(
                    {
                        "artifact_id": artifact.get("artifact_id"),
                        "artifact_name": artifact.get("artifact_name"),
                        "artifact_type": artifact.get("artifact_type"),
                        "owner_email": artifact.get("owner_email"),
                    }
                )

        if partial_matches:
            payload = {
                    "exact_match": False,
                    "partial_matches": partial_matches,
                    "message": f"No exact match found for '{artifact_name}'. Found {len(partial_matches)} partial matches.",
                }
            out = json.dumps(
                payload)
            return out
        payload = {"error": f"No artifact found with name '{artifact_name}'"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArtifactIdFromName",
                "description": "Get artifact ID and details by searching for artifact name. Returns exact match if found, otherwise returns partial matches.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_name": {
                            "type": "string",
                            "description": "The name of the artifact to search for.",
                        }
                    },
                    "required": ["artifact_name"],
                },
            },
        }
