from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LinkAuditReportAsset(Tool):  #WRITE
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str, report_asset_id: str) -> str:
        pass
        #Check the input for validity
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        if not isinstance(report_asset_id, str) or not report_asset_id:
            payload = {"error": "report_asset_id must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Retrieve audits and assets data
        audits = data.get("audits", [])
        assets = data.get("assets", [])

        #Check for the existence of the asset
        asset_exists = any(asset.get("asset_id") == report_asset_id for asset in assets)
        if not asset_exists:
            payload = {"error": f"Asset with ID '{report_asset_id}' not found"}
            out = json.dumps(payload)
            return out

        #Identify the audit that needs updating
        audit_to_update = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_to_update = audit
                break

        if not audit_to_update:
            payload = {"error": f"Audit with ID '{audit_id}' not found"}
            out = json.dumps(payload)
            return out

        #Modify the report_asset_id_nullable
        old_asset_id = audit_to_update.get("report_asset_id_nullable")
        audit_to_update["report_asset_id_nullable"] = report_asset_id
        payload = {
                "updated_audit": audit_to_update,
                "old_report_asset_id": old_asset_id,
                "new_report_asset_id": report_asset_id,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkAuditReportAsset",
                "description": "Link an asset to an audit as its report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID to update.",
                        },
                        "report_asset_id": {
                            "type": "string",
                            "description": "The asset ID to link as the audit report.",
                        },
                    },
                    "required": ["audit_id", "report_asset_id"],
                },
            },
        }
