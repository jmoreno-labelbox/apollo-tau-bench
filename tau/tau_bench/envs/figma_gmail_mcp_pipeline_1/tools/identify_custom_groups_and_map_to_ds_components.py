from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class IdentifyCustomGroupsAndMapToDsComponents(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        audits = data.get("audits", {}).values()
        artifacts = data.get("figma_artifacts", {}).values()

        #Identify the audit
        audit = next((a for a in audits.values() if a.get("audit_id") == audit_id), None)
        if not audit:
            payload = {"error": f"Audit {audit_id} not found"}
            out = json.dumps(payload)
            return out

        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            payload = {"error": f"No artifact_id found for audit {audit_id}"}
            out = json.dumps(payload)
            return out

        #Locate the artifact
        artifact = next(
            (a for a in artifacts.values() if a.get("artifact_id") == artifact_id), None
        )
        if not artifact:
            payload = {"error": f"Artifact {artifact_id} not found"}
            out = json.dumps(payload)
            return out

        #Utilize page_id as layer_id and artifact_name as layer_name
        layer_id = artifact.get("page_id")
        layer_name = artifact.get("artifact_name")

        if not layer_id or not layer_name:
            payload = {
                    "error": f"Missing page_id or artifact_name for artifact {artifact_id}"
                }
            out = json.dumps(
                payload)
            return out

        #Create consistent yet "random" values by hashing audit_id + artifact_id
        seed_string = f"{audit_id}_{artifact_id}"
        hash_value = custom_hash(seed_string)

        #Choose finding_type in a consistent manner
        finding_types = ["SUBSTITUTE_RECOMMENDED", "UNMAPPED", "AMBIGUOUS"]
        finding_type = finding_types[abs(hash_value) % len(finding_types)]

        #Create recommended_component_id based on layer_name
        #Extract the first word from layer_name and append the version
        words = layer_name.split()
        if words:
            component_word = words[0]
            version_major = (abs(hash_value) % 2) + 1  #1 or 2
            version_minor = abs(hash_value) % 10  #0-9
            recommended_component_id_nullable = (
                f"{component_word}-v{version_major}.{version_minor}"
            )
        else:
            recommended_component_id_nullable = None

        #Create severity in a consistent manner
        severities = ["LOW", "MEDIUM", "HIGH"]
        severity = severities[
            abs(hash_value // 7) % len(severities)
        ]  #Apply various hash divisions for diversity
        payload = {
                "audit_id": audit_id,
                "layer_id": layer_id,
                "layer_name": layer_name,
                "finding_type": finding_type,
                "recommended_component_id_nullable": recommended_component_id_nullable,
                "code_connect_link_nullable": None,
                "severity": severity,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IdentifyCustomGroupsAndMapToDsComponents",
                "description": "Identify custom groups in a Figma artifact and map them to design system components.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to process.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }
