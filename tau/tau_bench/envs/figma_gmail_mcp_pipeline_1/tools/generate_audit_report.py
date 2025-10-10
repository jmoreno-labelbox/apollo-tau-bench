# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateAuditReport(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str
    ) -> str:
        # Verify input correctness.
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        # Retrieve audit and asset information.
        audits = data.get("audits", [])
        assets = data.get("assets", [])
        figma_artifacts = data.get("figma_artifacts", [])

        # Locate the audit.
        audit = next((a for a in audits if a.get("audit_id") == audit_id), None)
        if not audit:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Retrieve artifact_id from the audit.
        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            return json.dumps({"error": f"No artifact_id found for audit {audit_id}"})

        # Retrieve the artifact to obtain the layer_name.
        artifact = next((a for a in figma_artifacts if a.get("artifact_id") == artifact_id), None)
        if not artifact:
            return json.dumps({"error": f"Artifact with ID '{artifact_id}' not found"})

        artifact_name = artifact.get("artifact_name")
        if not artifact_name:
            return json.dumps({"error": f"No artifact_name found for artifact {artifact_id}"})

        # Create a new asset identifier.
        next_num = len(assets) + 1
        asset_id = f"asset_{next_num:03d}"

        # Create storage_ref using the artifact name with spaces replaced by hyphens.
        clean_name = artifact_name.lower().replace(" ", "-")
        storage_ref = f"gs://company-assets/audit-reports/{clean_name}-audit-report.pdf"

        # Generate a new asset record.
        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": "PDF",
            "file_size_bytes": 2048000,  # Standard size for a PDF audit report.
            "storage_ref": storage_ref,
            "created_ts": "2025-08-28T15:00:00Z",
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None
        }

        # Incorporate into assets information.
        assets.append(new_asset)

        return json.dumps({"new_asset": new_asset})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_audit_report",
                "description": "Generate a PDF audit report and create an asset entry for it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to generate a report for."}
                    },
                    "required": ["audit_id"]
                }
            }
        }
