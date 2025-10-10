# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddArtifactTagTool(Tool):
    """Add a tag to an artifact (idempotent). Requires explicit timestamp for auditability."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, changed_ts, tag) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        tag = _require_str(tag, "tag")
        changed_ts = _require_str(changed_ts, "changed_ts")  # is required
        if not (artifact_id and tag and changed_ts):
            return json.dumps({"error":"artifact_id, tag, changed_ts are required"})

        artifacts = _safe_table(data, "figma_artifacts")
        idx = _index_by(artifacts, "artifact_id")
        if artifact_id not in idx:
            return json.dumps({"error": f"artifact_id {artifact_id} not found"})

        row = artifacts[idx[artifact_id]]
        tags = row.setdefault("current_tags", [])
        if tag not in tags:
            tags.append(tag)
        row["modified_ts"] = max(changed_ts, row.get("modified_ts",""))

        # Record
        logs = _safe_table(data, "terminal_logs")
        logs.append({"log_ts": changed_ts, "message": f"INFO: Tag '{tag}' added to {artifact_id}"})
        return json.dumps({"success": True, "artifact_id": artifact_id, "tag": tag}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_artifact_tag",
            "description":"Add a tag to artifact (idempotent). Requires 'changed_ts' (ISO).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "tag":{"type":"string"},
                "changed_ts":{"type":"string","description":"Explicit ISO timestamp"}
            },"required":["artifact_id","tag","changed_ts"]}
        }}
