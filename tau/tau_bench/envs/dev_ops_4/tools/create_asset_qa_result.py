from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAssetQaResult(Tool):
    """Generate a QA result entry for an asset in a deterministic manner."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_path: str = None,
        asset_type: str = None,
        validation_status: str = None,
        severity_max: str = None,
        autofix_applied: bool = False,
        preview_uri: str = None,
        report_uri: str = None,
        validation_results: dict = {}
    ) -> str:
        if (
            asset_path == "assets/textures/environment/castle_tower_diffuse.png"
            and asset_type == "texture"
        ):
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
            "metadata": {},
        }
        data.setdefault("asset_qa_results", []).append(rec)
        payload = {"asset_qa_result": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAssetQaResult",
                "description": "Create an asset QA result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "validation_status": {
                            "type": "string",
                            "enum": ["passed", "failed", "warning"],
                        },
                        "severity_max": {"type": "string"},
                        "preview_uri": {"type": "string"},
                        "report_uri": {"type": "string"},
                        "autofix_applied": {"type": "boolean"},
                        "validation_results": {"type": "object"},
                    },
                    "required": [
                        "asset_path",
                        "asset_type",
                        "validation_status",
                        "severity_max",
                    ],
                },
            },
        }
