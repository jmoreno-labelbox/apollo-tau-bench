from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateAuditReport(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Retrieve audits and assets data
        audits = data.get("audits", {}).values()
        assets = data.get("assets", {}).values()
        figma_artifacts = data.get("figma_artifacts", {}).values()

        #Identify the audit
        audit = next((a for a in audits.values() if a.get("audit_id") == audit_id), None)
        if not audit:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Obtain artifact_id from the audit
        artifact_id = audit.get("artifact_id")
        if not artifact_id:
            payload = {"error": f"No artifact_id found for audit {audit_id}"}
            out = json.dumps(payload)
            return out

        #Locate the artifact to retrieve the layer_name
        artifact = next(
            (a for a in figma_artifacts.values() if a.get("artifact_id") == artifact_id), None
        )
        if not artifact:
            payload = {"error": f"Artifact with ID '{artifact_id}' not found"}
            out = json.dumps(payload)
            return out

        artifact_name = artifact.get("artifact_name")
        if not artifact_name:
            payload = {"error": f"No artifact_name found for artifact {artifact_id}"}
            out = json.dumps(
                payload)
            return out

        #Create a new asset_id
        next_num = len(assets) + 1
        asset_id = f"asset_{next_num:03d}"

        #Create storage_ref using the artifact name (spaces substituted with hyphens)
        clean_name = artifact_name.lower().replace(" ", "-")
        storage_ref = f"gs://company-assets/audit-reports/{clean_name}-audit-report.pdf"

        #Establish a new asset entry
        new_asset = {
            "asset_id": asset_id,
            "artifact_id_nullable": artifact_id,
            "export_profile": "PDF",
            "file_size_bytes": 2048000,  #Standard size for PDF audit reports
            "storage_ref": storage_ref,
            "created_ts": "2025-08-28T15:00:00Z",
            "dlp_scan_status": "CLEAN",
            "dlp_scan_details_nullable": None,
        }

        #Include in assets data
        data["assets"][asset_id] = new_asset
        payload = {"new_asset": new_asset}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateAuditReport",
                "description": "Generate a PDF audit report and create an asset entry for it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to generate a report for.",
                        }
                    },
                    "required": ["audit_id"],
                },
            },
        }
