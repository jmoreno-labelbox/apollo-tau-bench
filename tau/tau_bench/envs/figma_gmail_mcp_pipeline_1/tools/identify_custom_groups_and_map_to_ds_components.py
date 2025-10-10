# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class IdentifyCustomGroupsAndMapToDsComponents(Tool):  # READ
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str
    ) -> str:
        # Validate input
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        audits = data.get("audits", [])
        artifacts = data.get("figma_artifacts", [])

        # Find the audit
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)
        if not audit:
            return json.dumps({"error": f"Audit {audit_id} not found"})

        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            return json.dumps({"error": f"No artifact_id found for audit {audit_id}"})

        # Find the artifact
        artifact = next((a for a in artifacts if a.get("artifact_id") == artifact_id), None)
        if not artifact:
            return json.dumps({"error": f"Artifact {artifact_id} not found"})

        # Use page_id as layer_id and artifact_name as layer_name
        layer_id = artifact.get("page_id")
        layer_name = artifact.get("artifact_name")

        if not layer_id or not layer_name:
            return json.dumps({"error": f"Missing page_id or artifact_name for artifact {artifact_id}"})

        # Generate deterministic but "random" values using hash of audit_id + artifact_id
        seed_string = f"{audit_id}_{artifact_id}"
        hash_value = custom_hash(seed_string)

        # Select finding_type deterministically
        finding_types = ["SUBSTITUTE_RECOMMENDED", "UNMAPPED", "AMBIGUOUS"]
        finding_type = finding_types[abs(hash_value) % len(finding_types)]

        # Generate recommended_component_id from layer_name
        # Take first word from layer_name, add version
        words = layer_name.split()
        if words:
            component_word = words[0]
            version_major = (abs(hash_value) % 2) + 1  # 1 or 2
            version_minor = abs(hash_value) % 10  # 0-9
            recommended_component_id_nullable = f"{component_word}-v{version_major}.{version_minor}"
        else:
            recommended_component_id_nullable = None

        # Generate severity deterministically
        severities = ["LOW", "MEDIUM", "HIGH"]
        severity = severities[abs(hash_value // 7) % len(severities)]  # Use different hash division for variety

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
