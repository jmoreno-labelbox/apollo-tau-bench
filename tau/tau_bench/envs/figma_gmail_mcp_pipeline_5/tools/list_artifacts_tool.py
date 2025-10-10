# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListArtifactsTool(Tool):
    """List Figma artifacts filtered by owner, tags, type, or modified since."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_type, modified_since, owner_email, tag) -> str:

        rows = data.get("figma_artifacts", [])
        out: List[Dict[str, Any]] = []
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
            out.append(_small_fields(r, ["artifact_id", "artifact_name", "artifact_type", "owner_email", "modified_ts"]))

        out.sort(key=lambda x: (x.get("artifact_type",""), x.get("artifact_name","")))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_artifacts",
                "description": "List Figma artifacts filtered by owner, tag, type, or modified_since (ISO).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_email": {"type": "string"},
                        "tag": {"type": "string"},
                        "artifact_type": {"type": "string"},
                        "modified_since": {"type": "string", "description": "ISO timestamp; include rows with modified_ts >= this."}
                    }
                }
            }
        }
