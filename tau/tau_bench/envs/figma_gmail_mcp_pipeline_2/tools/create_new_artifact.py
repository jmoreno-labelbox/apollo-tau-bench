# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_name, artifact_type, current_tags, deep_link, figma_file_id, frame_id_nullable, owner_email, page_id) -> str:
        required = ["artifact_type", "artifact_name", "figma_file_id", "page_id", "owner_email", "deep_link"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        if artifact_type == "FRAME" and not frame_id_nullable:
            return json.dumps({"error": "frame_id_nullable is required for FRAME artifacts"}, indent=2)

        artifacts = list(data.get("figma_artifacts", {}).values())
        artifact_id = get_next_art_id(data)
        created_ts = get_now_timestamp()
        current_tags = current_tags or []

        new_row = {
            "artifact_id": artifact_id,
            "figma_file_id": figma_file_id,
            "page_id": page_id,
            "frame_id_nullable": frame_id_nullable if artifact_type == "FRAME" else None,
            "artifact_type": artifact_type,
            "artifact_name": artifact_name,
            "owner_email": owner_email,
            "modified_ts": created_ts,
            "deep_link": deep_link,
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
