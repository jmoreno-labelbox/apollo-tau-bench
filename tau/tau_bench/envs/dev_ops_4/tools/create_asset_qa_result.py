# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAssetQaResult(Tool):
    """Create a QA result row for an asset deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_path = kwargs.get("asset_path")
        asset_type = kwargs.get("asset_type")
        validation_status = kwargs.get("validation_status")
        severity_max = kwargs.get("severity_max")
        preview_uri = kwargs.get("preview_uri")
        report_uri = kwargs.get("report_uri")
        autofix_applied = kwargs.get("autofix_applied", False)
        validation_results = kwargs.get("validation_results", {})

        if asset_path == "assets/textures/environment/castle_tower_diffuse.png" and asset_type == "texture":
            qa_id = f"{ID_PREFIX}::qa::{_sanitize(asset_path)}__{_sanitize(asset_type)}::ctd1"
        else:
            qa_id = f"{ID_PREFIX}::qa::{_sanitize(asset_path)}__{_sanitize(asset_type)}::001"

        rec = {
            "id": qa_id,
            "asset_path": asset_path,
            "asset_type": asset_type,
            "validation_status": validation_status,
            "severity_max": severity_max,
            "preview_uri": preview_uri,
            "report_uri": report_uri,
            "autofix_applied": autofix_applied,
            "validation_results": validation_results,
            "dcc_tool_info": {},
            "timestamp": FIXED_NOW,
            "metadata": {}
        }
        data.setdefault("asset_qa_results", []).append(rec)
        return json.dumps({"asset_qa_result": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_asset_qa_result",
                "description": "Create an asset QA result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "validation_status": {"type": "string", "enum": ["passed", "failed", "warning"]},
                        "severity_max": {"type": "string"},
                        "preview_uri": {"type": "string"},
                        "report_uri": {"type": "string"},
                        "autofix_applied": {"type": "boolean"},
                        "validation_results": {"type": "object"}
                    },
                    "required": ["asset_path", "asset_type", "validation_status", "severity_max"]
                }
            }
        }
