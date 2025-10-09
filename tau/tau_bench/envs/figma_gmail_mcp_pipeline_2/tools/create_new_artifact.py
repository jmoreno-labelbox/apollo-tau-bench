from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any

class CreateNewArtifact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_type: str,
        artifact_name: str,
        figma_file_id: str,
        page_id: str,
        owner_email: str,
        deep_link: str,
        frame_id_nullable: str = None,
        current_tags: list = None
    ) -> str:
        required = [
            "artifact_type",
            "artifact_name",
            "figma_file_id",
            "page_id",
            "owner_email",
            "deep_link",
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if artifact_type == "FRAME" and not frame_id_nullable:
            payload = {"error": "frame_id_nullable is required for FRAME artifacts"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        artifacts = data.get("figma_artifacts", [])
        artifact_id = get_next_art_id(data)
        created_ts = get_now_timestamp()
        current_tags = current_tags or []

        new_row = {
            "artifact_id": artifact_id,
            "figma_file_id": figma_file_id,
            "page_id": page_id,
            "frame_id_nullable": (
                frame_id_nullable if artifact_type == "FRAME" else None
            ),
            "artifact_type": artifact_type,
            "artifact_name": artifact_name,
            "owner_email": owner_email,
            "modified_ts": created_ts,
            "deep_link": deep_link,
            "current_tags": current_tags,
        }

        artifacts.append(new_row)
        data["figma_artifacts"] = artifacts
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewArtifact",
                "description": "Create a new figma_artifacts row. If artifact_type=FRAME, frame_id_nullable is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {
                            "type": "string",
                            "enum": ["FILE", "PAGE", "FRAME"],
                        },
                        "artifact_name": {"type": "string"},
                        "figma_file_id": {"type": "string"},
                        "page_id": {"type": "string"},
                        "frame_id_nullable": {"type": ["string", "null"]},
                        "owner_email": {"type": "string"},
                        "deep_link": {"type": "string"},
                        "current_tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "default": [],
                        },
                    },
                    "required": [
                        "artifact_type",
                        "artifact_name",
                        "figma_file_id",
                        "page_id",
                        "owner_email",
                        "deep_link",
                    ],
                },
            },
        }
