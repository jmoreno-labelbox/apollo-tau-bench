from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ExportFigmaArtifactsToAssets(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_ids: list[str],
        export_profile: dict[str, Any] = None,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(artifact_ids, list) or not all(
            isinstance(aid, str) for aid in artifact_ids
        ):
            payload = {"error": "artifact_ids must be a list of strings"}
            out = json.dumps(payload)
            return out
        artifacts = data.get("figma_artifacts", [])
        assets = data.get("assets", [])
        #Standard export profile
        default_profile = {"format": "PNG", "scale": "2x"}
        profile = export_profile if export_profile else default_profile
        #Check the profile for validity
        allowed_formats = ["PNG", "JPG", "SVG", "PDF"]
        allowed_scales = ["1x", "2x", "4x"]
        if export_profile is not None and (
            "format" not in export_profile.keys()
            or "scale" not in export_profile.keys()
        ):
            payload = {"error": "Invalid export profile. Must include 'format' and 'scale'."}
            out = json.dumps(
                payload)
            return out
        fmt = profile.get("format", "PNG")
        scale = profile.get("scale", "2x")
        if fmt not in allowed_formats or scale not in allowed_scales:
            payload = {
                    "error": f"Invalid export profile. Allowed formats: {allowed_formats}, scales: {allowed_scales}"
                }
            out = json.dumps(
                payload)
            return out
        exported = []
        for aid in artifact_ids:
            artifact = next((a for a in artifacts if a.get("artifact_id") == aid), None)
            if not artifact:
                continue
            #Construct the export_profile string similar to assets.json
            if fmt == "SVG" or fmt == "PDF":
                export_profile_str = fmt
            else:
                export_profile_str = f"{fmt} {scale}"
            asset = {
                "asset_id": f"asset_{aid}_{fmt.lower()}_{scale}",
                "artifact_id_nullable": aid,
                "export_profile": export_profile_str,
                #Default values for additional fields
                "file_size_bytes": 205500,
                "storage_ref": f"gs://company-assets/figma-exports/{artifact.get('artifact_name').replace(' ', '-').lower()}-{scale}.{fmt.lower()}",
                "created_ts": "2025-08-26T00:00:00Z",
                "dlp_scan_status": "CLEAN",
                "dlp_scan_details_nullable": None,
            }
            assets.append(asset)
            exported.append(asset["asset_id"])
        payload = {"exported_asset_ids": exported, "profile": profile}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportFigmaArtifactsToAssets",
                "description": "Export Figma artifacts to assets with a customizable profile (default PNG 2x).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of Figma artifact IDs to export.",
                        },
                        "export_profile": {
                            "type": "object",
                            "properties": {
                                "format": {
                                    "type": "string",
                                    "description": "Export format (PNG, JPG, SVG, PDF).",
                                },
                                "scale": {
                                    "type": "string",
                                    "description": "Export scale (1x, 2x, 4x).",
                                },
                            },
                            "description": "Custom export profile. Defaults to PNG 2x.",
                            "default": {"format": "PNG", "scale": "2x"},
                        },
                    },
                    "required": ["artifact_ids"],
                },
            },
        }
