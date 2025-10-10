# Sierra copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAssetExportStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Updates asset export status and manages export workflow metadata.
        """
        asset_id = kwargs.get('asset_id')
        new_status = kwargs.get('new_status')
        export_notes = kwargs.get('export_notes', '')
        dlp_scan_status = kwargs.get('dlp_scan_status')
        storage_ref = kwargs.get('storage_ref')

        if not all([asset_id, new_status]):
            return json.dumps({"error": "asset_id and new_status are required."})

        # Check the validity of status values.
        valid_statuses = ['PENDING', 'EXPORTING', 'COMPLETED', 'FAILED', 'ARCHIVED']
        if new_status not in valid_statuses:
            return json.dumps({"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"})

        assets = data.get('assets', [])

        # Locate the asset.
        asset_found = False
        for asset in assets:
            if asset.get('asset_id') == asset_id:
                asset_found = True
                old_status = asset.get('export_status', 'PENDING')

                # Revise the status of the asset.
                asset['export_status'] = new_status
                asset['last_updated'] = datetime.now().isoformat()

                # Modify the DLP scan status if available.
                if dlp_scan_status:
                    asset['dlp_scan_status'] = dlp_scan_status
                    asset['dlp_scan_timestamp'] = datetime.now().isoformat()

                # Modify the storage reference if it is given.
                if storage_ref:
                    asset['storage_ref'] = storage_ref

                # Include export documentation.
                if export_notes:
                    if 'export_history' not in asset:
                        asset['export_history'] = []
                    asset['export_history'].append({
                        "timestamp": datetime.now().isoformat(),
                        "status": new_status,
                        "notes": export_notes
                    })

                # Record the status update.
                if 'status_history' not in asset:
                    asset['status_history'] = []
                asset['status_history'].append({
                    "from_status": old_status,
                    "to_status": new_status,
                    "changed_at": datetime.now().isoformat(),
                    "notes": export_notes
                })

                break

        if not asset_found:
            return json.dumps({"error": f"Asset with ID '{asset_id}' not found."})

        return json.dumps({
            "success": True,
            "asset_id": asset_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_export_status",
                "description": "Updates asset export status and manages export workflow metadata including DLP scan status and storage references.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string", "description": "The ID of the asset to update."},
                        "new_status": {"type": "string", "description": "The new export status. Must be one of: PENDING, EXPORTING, COMPLETED, FAILED, ARCHIVED."},
                        "export_notes": {"type": "string", "description": "Optional notes about the export process or status change."},
                        "dlp_scan_status": {"type": "string", "description": "Optional DLP scan status update (e.g., 'CLEAN', 'FLAGGED', 'PENDING')."},
                        "storage_ref": {"type": "string", "description": "Optional new storage reference for the asset."}
                    },
                    "required": ["asset_id", "new_status"]
                }
            }
        }
