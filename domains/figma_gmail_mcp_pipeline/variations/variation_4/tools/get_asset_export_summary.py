from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetAssetExportSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str = None,
        artifact_id: str = None,
        export_profile: str = None,
        dlp_scan_status: str = None,
        created_after: str = None,
        created_before: str = None
    ) -> str:
        """
        Obtains detailed asset export information and metrics.
        """
        assets = data.get("assets", [])
        figma_artifacts = data.get("figma_artifacts", [])

        # Return the specific asset if asset_id is given
        if asset_id:
            asset_info = None
            for asset in assets:
                if asset.get("asset_id") == asset_id:
                    asset_info = asset
                    break

            if not asset_info:
                payload = {"error": f"Asset with ID '{asset_id}' not found."}
                out = json.dumps(payload)
                return out

            # Enhance with details from the artifact
            artifact_id_ref = asset_info.get("artifact_id_nullable")
            artifact_info = None
            if artifact_id_ref:
                for artifact in figma_artifacts:
                    if artifact.get("artifact_id") == artifact_id_ref:
                        artifact_info = artifact
                        break

            summary = {"asset_info": asset_info, "artifact_info": artifact_info}
            payload = summary
            out = json.dumps(payload, indent=2)
            return out

        # Provide a summary for all assets
        all_assets = assets

        # Implement filters
        if artifact_id:
            all_assets = [
                a for a in all_assets if a.get("artifact_id_nullable") == artifact_id
            ]

        if export_profile:
            all_assets = [
                a for a in all_assets if a.get("export_profile") == export_profile
            ]

        if dlp_scan_status:
            all_assets = [
                a for a in all_assets if a.get("dlp_scan_status") == dlp_scan_status
            ]

        # Enforce date filters
        if created_after:
            all_assets = [
                a for a in all_assets if a.get("created_ts", "") >= created_after
            ]

        if created_before:
            all_assets = [
                a for a in all_assets if a.get("created_ts", "") <= created_before
            ]

        summary = {
            "total_assets": len(all_assets),
            "by_profile": {},
            "by_artifact": {},
            "by_dlp_status": {},
            "total_file_size_bytes": sum(
                a.get("file_size_bytes", 0) for a in all_assets
            ),
            "assets": all_assets,
        }

        # Categorize assets based on profile
        for asset in all_assets:
            profile = asset.get("export_profile")
            if profile not in summary["by_profile"]:
                summary["by_profile"][profile] = 0
            summary["by_profile"][profile] += 1

            # Classify by artifact
            artifact_ref = asset.get("artifact_id_nullable")
            if artifact_ref not in summary["by_artifact"]:
                summary["by_artifact"][artifact_ref] = 0
            summary["by_artifact"][artifact_ref] += 1

            # Categorize by DLP status
            dlp_status = asset.get("dlp_scan_status", "UNKNOWN")
            if dlp_status not in summary["by_dlp_status"]:
                summary["by_dlp_status"][dlp_status] = 0
            summary["by_dlp_status"][dlp_status] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAssetExportSummary",
                "description": "Retrieves comprehensive asset export information and metrics including profile distribution, artifact associations, and DLP scan status breakdowns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {
                            "type": "string",
                            "description": "The ID of a specific asset to retrieve details for.",
                        },
                        "artifact_id": {
                            "type": "string",
                            "description": "Filter assets by associated artifact ID.",
                        },
                        "export_profile": {
                            "type": "string",
                            "description": "Filter assets by export profile (e.g., 'PNG 2x', 'SVG', 'PDF').",
                        },
                        "dlp_scan_status": {
                            "type": "string",
                            "description": "Filter assets by DLP scan status (e.g., 'CLEAN', 'FLAGGED', 'PENDING').",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter assets created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter assets created before this ISO timestamp.",
                        },
                    },
                },
            },
        }
