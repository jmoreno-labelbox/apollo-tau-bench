from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class AddArtifactTagTool(Tool):
    """Attach a tag to an artifact (idempotent). Requires a specific timestamp for audit purposes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        changed_ts: str = None,
        tag: str = None
    ) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        tag = _require_str(tag, "tag")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (artifact_id and tag and changed_ts):
            payload = {"error": "artifact_id, tag, changed_ts are required"}
            out = json.dumps(payload)
            return out

        artifacts = _safe_table(data, "figma_artifacts")
        idx = _index_by(artifacts, "artifact_id")
        if artifact_id not in idx:
            payload = {"error": f"artifact_id {artifact_id} not found"}
            out = json.dumps(payload)
            return out

        row = artifacts[idx[artifact_id]]
        tags = row.setdefault("current_tags", [])
        if tag not in tags:
            tags.append(tag)
        row["modified_ts"] = max(changed_ts, row.get("modified_ts", ""))

        logs = _safe_table(data, "terminal_logs")
        logs.append(
            {
                "log_ts": changed_ts,
                "message": f"INFO: Tag '{tag}' added to {artifact_id}",
            }
        )
        payload = {"success": True, "artifact_id": artifact_id, "tag": tag}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddArtifactTag",
                "description": "Add a tag to artifact (idempotent). Requires 'changed_ts' (ISO).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "tag": {"type": "string"},
                        "changed_ts": {
                            "type": "string",
                            "description": "Explicit ISO timestamp",
                        },
                    },
                    "required": ["artifact_id", "tag", "changed_ts"],
                },
            },
        }
