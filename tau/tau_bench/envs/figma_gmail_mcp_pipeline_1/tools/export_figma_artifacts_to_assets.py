# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportFigmaArtifactsToAssets(Tool):  # CREATE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        artifact_ids: List[str],
        export_profile: Dict[str, Any] = None
    ) -> str:
        # Check the input for correctness.
        if not isinstance(artifact_ids, list) or not all(isinstance(aid, str) for aid in artifact_ids):
            return json.dumps({"error": "artifact_ids must be a list of strings"})
        artifacts = data.get("figma_artifacts", [])
        assets = data.get("assets", [])
        # Export profile by default
        default_profile = {"format": "PNG", "scale": "2x"}
        profile = export_profile if export_profile else default_profile
        # Verify profile integrity.
        allowed_formats = ["PNG", "JPG", "SVG", "PDF"]
        allowed_scales = ["1x", "2x", "4x"]
        if export_profile is not None and ("format" not in export_profile.keys() or "scale" not in export_profile.keys()):
            return json.dumps({"error": "Invalid export profile. Must include 'format' and 'scale'."})
        fmt = profile.get("format", "PNG")
        scale = profile.get("scale", "2x")
        if fmt not in allowed_formats or scale not in allowed_scales:
            return json.dumps({"error": f"Invalid export profile. Allowed formats: {allowed_formats}, scales: {allowed_scales}"})
        exported = []
        for aid in artifact_ids:
            artifact = next((a for a in artifacts if a.get("artifact_id") == aid), None)
            if not artifact:
                continue
            # Generate export_profile string similar to the format in assets.json.
            if fmt == "SVG" or fmt == "PDF":
                export_profile_str = fmt
            else:
                export_profile_str = f"{fmt} {scale}"
            asset = {
                "asset_id": f"asset_{aid}_{fmt.lower()}_{scale}",
                "artifact_id_nullable": aid,
                "export_profile": export_profile_str,
                # Sample values for additional fields
                "file_size_bytes": 205500,
                "storage_ref": f"gs://company-assets/figma-exports/{artifact.get('artifact_name').replace(' ', '-').lower()}-{scale}.{fmt.lower()}",
                "created_ts": "2025-08-26T00:00:00Z",
                "dlp_scan_status": "CLEAN",
                "dlp_scan_details_nullable": None
            }
            assets.append(asset)
            exported.append(asset["asset_id"])
        # Update data['assets'] if necessary.
        return json.dumps({"exported_asset_ids": exported, "profile": profile})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_figma_artifacts_to_assets",
                "description": "Export Figma artifacts to assets with a customizable profile (default PNG 2x).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of Figma artifact IDs to export."
                        },
                        "export_profile": {
                            "type": "object",
                            "properties": {
                                "format": {"type": "string", "description": "Export format (PNG, JPG, SVG, PDF)."},
                                "scale": {"type": "string", "description": "Export scale (1x, 2x, 4x)."}
                            },
                            "description": "Custom export profile. Defaults to PNG 2x.",
                            "default": {"format": "PNG", "scale": "2x"}
                        }
                    },
                    "required": ["artifact_ids"]
                }
            }
        }
