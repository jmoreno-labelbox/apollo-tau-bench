# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["artifact_type", "artifact_name", "figma_file_id", "page_id", "owner_email", "deep_link"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        if kwargs.get("artifact_type") == "FRAME" and not kwargs.get("frame_id_nullable"):
            return json.dumps({"error": "frame_id_nullable is required for FRAME artifacts"}, indent=2)

        artifacts = data.get("figma_artifacts", [])
        artifact_id = get_next_art_id(data)
        created_ts = get_now_timestamp()
        current_tags = kwargs.get("current_tags") or []

        new_row = {
            "artifact_id": artifact_id,
            "figma_file_id": kwargs["figma_file_id"],
            "page_id": kwargs["page_id"],
            "frame_id_nullable": kwargs.get("frame_id_nullable") if kwargs.get("artifact_type") == "FRAME" else None,
            "artifact_type": kwargs["artifact_type"],
            "artifact_name": kwargs["artifact_name"],
            "owner_email": kwargs["owner_email"],
            "modified_ts": created_ts,
            "deep_link": kwargs["deep_link"],
            "current_tags": current_tags,
        }

        artifacts.append(new_row)
        data["figma_artifacts"] = artifacts
        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_artifact",
                "description": "Create a new figma_artifacts row. If artifact_type=FRAME, frame_id_nullable is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string", "enum": ["FILE", "PAGE", "FRAME"]},
                        "artifact_name": {"type": "string"},
                        "figma_file_id": {"type": "string"},
                        "page_id": {"type": "string"},
                        "frame_id_nullable": {"type": ["string", "null"]},
                        "owner_email": {"type": "string"},
                        "deep_link": {"type": "string"},
                        "current_tags": {"type": "array", "items": {"type": "string"}, "default": []}
                    },
                    "required": ["artifact_type", "artifact_name", "figma_file_id", "page_id", "owner_email", "deep_link"]
                }
            }
        }
