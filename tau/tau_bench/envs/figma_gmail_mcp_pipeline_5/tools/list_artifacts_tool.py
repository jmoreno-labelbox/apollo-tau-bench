from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListArtifactsTool(Tool):
    """Enumerate Figma artifacts filtered by owner, tags, type, or modified since."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner_email: str = None,
        tag: str = None,
        artifact_type: str = None,
        modified_since: str = None
    ) -> str:
        rows = data.get("figma_artifacts", [])
        out: list[dict[str, Any]] = []
        for r in rows:
            if owner_email and r.get("owner_email") != owner_email:
                continue
            if artifact_type and r.get("artifact_type") != artifact_type:
                continue
            if tag:
                tags = r.get("current_tags", [])
                if tag not in tags:
                    continue
            if modified_since and r.get("modified_ts", "") < modified_since:
                continue
            out.append(
                _small_fields(
                    r,
                    [
                        "artifact_id",
                        "artifact_name",
                        "artifact_type",
                        "owner_email",
                        "modified_ts",
                    ],
                )
            )

        out.sort(key=lambda x: (x.get("artifact_type", ""), x.get("artifact_name", "")))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListArtifacts",
                "description": "List Figma artifacts filtered by owner, tag, type, or modified_since (ISO).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {"type": "string"},
                        "tag": {"type": "string"},
                        "artifact_type": {"type": "string"},
                        "modified_since": {
                            "type": "string",
                            "description": "ISO timestamp; include rows with modified_ts >= this.",
                        },
                    },
                },
            },
        }
