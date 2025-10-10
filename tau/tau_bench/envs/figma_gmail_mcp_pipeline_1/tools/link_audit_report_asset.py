# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkAuditReportAsset(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        report_asset_id: str
    ) -> str:
        # Validate input
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})

        if not isinstance(report_asset_id, str) or not report_asset_id:
            return json.dumps({"error": "report_asset_id must be a non-empty string"})

        # Get audits and assets data
        audits = data.get("audits", [])
        assets = data.get("assets", [])

        # Validate that the asset exists
        asset_exists = any(asset.get("asset_id") == report_asset_id for asset in assets)
        if not asset_exists:
            return json.dumps({"error": f"Asset with ID '{report_asset_id}' not found"})

        # Find the audit to update
        audit_to_update = None
        for audit in audits:
            if audit.get("audit_id") == audit_id:
                audit_to_update = audit
                break

        if not audit_to_update:
            return json.dumps({"error": f"Audit with ID '{audit_id}' not found"})

        # Update the report_asset_id_nullable
        old_asset_id = audit_to_update.get("report_asset_id_nullable")
        audit_to_update["report_asset_id_nullable"] = report_asset_id

        return json.dumps({
            "updated_audit": audit_to_update,
            "old_report_asset_id": old_asset_id,
            "new_report_asset_id": report_asset_id
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_audit_report_asset",
                "description": "Link an asset to an audit as its report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string", "description": "The audit ID to update."},
                        "report_asset_id": {"type": "string", "description": "The asset ID to link as the audit report."}
                    },
                    "required": ["audit_id", "report_asset_id"]
                }
            }
        }
