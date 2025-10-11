# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordStakeholderArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_path, audience, output_label) -> str:
        outs = list(data.get("stakeholder_outputs", {}).values())
        max_id = 0
        for o in outs:
            try:
                oid = int(o.get("output_id", 0))
                if oid > max_id:
                    max_id = oid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "output_id": new_id,
            "output_label": output_label,
            "audience": audience,
            "artifact_path": artifact_path,
            "created_at": _fixed_now_iso(),
        }
        outs.append(row)
        return json.dumps({"output_id": new_id, "output_label": row["output_label"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "record_stakeholder_artifact",
            "description": "Insert a stakeholder-visible artifact row.",
            "parameters": {"type": "object", "properties": {
                "output_label": {"type": "string"},
                "audience": {"type": "string"},
                "artifact_path": {"type": "string"}
            }, "required": ["output_label", "audience", "artifact_path"]}
        }}
