# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class IdentifyCustomGroupsAndMapToDsComponents(Tool):  # ACCESS
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str
    ) -> str:
        # Check the validity of the input.
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        audits = list(data.get("audits", {}).values())
        artifacts = list(data.get("figma_artifacts", {}).values())

        # Locate the audit.
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)
        if not audit:
            return json.dumps({"error": f"Audit {audit_id} not found"})

        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            return json.dumps({"error": f"No artifact_id found for audit {audit_id}"})

        # Locate the artifact.
        artifact = next((a for a in artifacts if a.get("artifact_id") == artifact_id), None)
        if not artifact:
            return json.dumps({"error": f"Artifact {artifact_id} not found"})

        # Utilize page_id as layer_id and artifact_name as layer_name.
        layer_id = artifact.get("page_id")
        layer_name = artifact.get("artifact_name")

        if not layer_id or not layer_name:
            return json.dumps({"error": f"Missing page_id or artifact_name for artifact {artifact_id}"})

        # Create consistent "random" values by hashing the combination of audit_id and artifact_id.
        seed_string = f"{audit_id}_{artifact_id}"
        hash_value = custom_hash(seed_string)

        # Choose finding_type in a deterministic manner.
        finding_types = ["SUBSTITUTE_RECOMMENDED", "UNMAPPED", "AMBIGUOUS"]
        finding_type = finding_types[abs(hash_value) % len(finding_types)]

        # Derive recommended_component_id using layer_name.
        # Extract the initial word from layer_name and append the version.
        words = layer_name.split()
        if words:
            component_word = words[0]
            version_major = (abs(hash_value) % 2) + 1  # one or two
            version_minor = abs(hash_value) % 10  # Zero to nine
            recommended_component_id_nullable = f"{component_word}-v{version_major}.{version_minor}"
        else:
            recommended_component_id_nullable = None

        # Produce severity in a deterministic manner.
        severities = ["LOW", "MEDIUM", "HIGH"]
        severity = severities[abs(hash_value // 7) % len(severities)]  # Employ alternative hash divisions for diversity.

        return json.dumps({
            "audit_id": audit_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "finding_type": finding_type,
            "recommended_component_id_nullable": recommended_component_id_nullable,
            "code_connect_link_nullable": None,
            "severity": severity
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "identify_custom_groups_and_map_to_ds_components",
                "description": "Identify custom groups in a Figma artifact and map them to design system components.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to process."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
