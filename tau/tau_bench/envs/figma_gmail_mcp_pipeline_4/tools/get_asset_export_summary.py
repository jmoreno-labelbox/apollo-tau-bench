# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAssetExportSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves comprehensive asset export information and metrics.
        """
        asset_id = kwargs.get('asset_id')
        artifact_id = kwargs.get('artifact_id')
        export_profile = kwargs.get('export_profile')
        dlp_scan_status = kwargs.get('dlp_scan_status')
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')

        assets = data.get('assets', [])
        figma_artifacts = data.get('figma_artifacts', [])

        # If asset_id is provided, return specific asset
        if asset_id:
            asset_info = None
            for asset in assets:
                if asset.get('asset_id') == asset_id:
                    asset_info = asset
                    break

            if not asset_info:
                return json.dumps({"error": f"Asset with ID '{asset_id}' not found."})

            # Enrich with artifact information
            artifact_id_ref = asset_info.get('artifact_id_nullable')
            artifact_info = None
            if artifact_id_ref:
                for artifact in figma_artifacts:
                    if artifact.get('artifact_id') == artifact_id_ref:
                        artifact_info = artifact
                        break

            summary = {
                "asset_info": asset_info,
                "artifact_info": artifact_info
            }

            return json.dumps(summary, indent=2)

        # Return summary across all assets
        all_assets = assets

        # Apply filters
        if artifact_id:
            all_assets = [a for a in all_assets if a.get('artifact_id_nullable') == artifact_id]

        if export_profile:
            all_assets = [a for a in all_assets if a.get('export_profile') == export_profile]

        if dlp_scan_status:
            all_assets = [a for a in all_assets if a.get('dlp_scan_status') == dlp_scan_status]

        # Apply date filters
        if created_after:
            all_assets = [a for a in all_assets if a.get('created_ts', '') >= created_after]

        if created_before:
            all_assets = [a for a in all_assets if a.get('created_ts', '') <= created_before]

        summary = {
            "total_assets": len(all_assets),
            "by_profile": {},
            "by_artifact": {},
            "by_dlp_status": {},
            "total_file_size_bytes": sum(a.get('file_size_bytes', 0) for a in all_assets),
            "assets": all_assets
        }

        # Group assets by profile
        for asset in all_assets:
            profile = asset.get('export_profile')
            if profile not in summary["by_profile"]:
                summary["by_profile"][profile] = 0
            summary["by_profile"][profile] += 1

            # Group by artifact
            artifact_ref = asset.get('artifact_id_nullable')
            if artifact_ref not in summary["by_artifact"]:
                summary["by_artifact"][artifact_ref] = 0
            summary["by_artifact"][artifact_ref] += 1

            # Group by DLP status
            dlp_status = asset.get('dlp_scan_status', 'UNKNOWN')
            if dlp_status not in summary["by_dlp_status"]:
                summary["by_dlp_status"][dlp_status] = 0
            summary["by_dlp_status"][dlp_status] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_asset_export_summary",
                "description": "Retrieves comprehensive asset export information and metrics including profile distribution, artifact associations, and DLP scan status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string", "description": "The ID of a specific asset to retrieve details for."},
                        "artifact_id": {"type": "string", "description": "Filter assets by associated artifact ID."},
                        "export_profile": {"type": "string", "description": "Filter assets by export profile (e.g., 'PNG 2x', 'SVG', 'PDF')."},
                        "dlp_scan_status": {"type": "string", "description": "Filter assets by DLP scan status (e.g., 'CLEAN', 'FLAGGED', 'PENDING')."},
                        "created_after": {"type": "string", "description": "Filter assets created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter assets created before this ISO timestamp."}
                    }
                }
            }
        }
