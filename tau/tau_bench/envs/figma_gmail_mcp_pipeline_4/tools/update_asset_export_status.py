from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAssetExportStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        new_status: str,
        export_notes: str = "",
        notes: str = None,
        dlp_scan_status: str = None,
        storage_ref: str = None
    ) -> str:
        # Support 'notes' as an alternative to 'export_notes'
        if notes is not None:
            export_notes = notes
        """
        Modifies asset export status and oversees export workflow metadata.
        """
        if not all([asset_id, new_status]):
            payload = {"error": "asset_id and new_status are required."}
            out = json.dumps(payload)
            return out

        # Check the validity of status values
        valid_statuses = ["PENDING", "EXPORTING", "COMPLETED", "FAILED", "ARCHIVED"]
        if new_status not in valid_statuses:
            payload = {
                "error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"
            }
            out = json.dumps(payload)
            return out

        assets = data.get("assets", {}).values()

        # Locate the asset
        asset_found = False
        for asset in assets.values():
            if asset.get("asset_id") == asset_id:
                asset_found = True
                old_status = asset.get("export_status", "PENDING")

                # Change the status of the asset
                asset["export_status"] = new_status
                asset["last_updated"] = datetime.now().isoformat()

                # Modify DLP scan status if specified
                if dlp_scan_status:
                    asset["dlp_scan_status"] = dlp_scan_status
                    asset["dlp_scan_timestamp"] = datetime.now().isoformat()

                # Revise storage reference if supplied
                if storage_ref:
                    asset["storage_ref"] = storage_ref

                # Include notes regarding the export
                if export_notes:
                    if "export_history" not in asset:
                        asset["export_history"] = []
                    asset["export_history"].append(
                        {
                            "timestamp": datetime.now().isoformat(),
                            "status": new_status,
                            "notes": export_notes,
                        }
                    )

                # Document the change in status
                if "status_history" not in asset:
                    asset["status_history"] = []
                asset["status_history"].append(
                    {
                        "from_status": old_status,
                        "to_status": new_status,
                        "changed_at": datetime.now().isoformat(),
                        "notes": export_notes,
                    }
                )

                break

        if not asset_found:
            payload = {"error": f"Asset with ID '{asset_id}' not found."}
            out = json.dumps(payload)
            return out
        payload = {
            "success": True,
            "asset_id": asset_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetExportStatus",
                "description": "Updates asset export status and manages export workflow metadata including DLP scan status and storage references.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {
                            "type": "string",
                            "description": "The ID of the asset to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new export status. Must be one of: PENDING, EXPORTING, COMPLETED, FAILED, ARCHIVED.",
                        },
                        "export_notes": {
                            "type": "string",
                            "description": "Optional notes about the export process or status change.",
                        },
                        "dlp_scan_status": {
                            "type": "string",
                            "description": "Optional DLP scan status update (e.g., 'CLEAN', 'FLAGGED', 'PENDING').",
                        },
                        "storage_ref": {
                            "type": "string",
                            "description": "Optional new storage reference for the asset.",
                        },
                    },
                    "required": ["asset_id", "new_status"],
                },
            },
        }
