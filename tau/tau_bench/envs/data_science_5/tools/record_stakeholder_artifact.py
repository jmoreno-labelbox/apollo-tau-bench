from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecordStakeholderArtifact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], output_label: str = None, audience: str = None, artifact_path: str = None) -> str:
        outs = data.get("stakeholder_outputs", {}).values()
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
            "created_at": _now_iso_fixed(),
        }
        data["stakeholder_outputs"][row["stakeholder_output_id"]] = row
        payload = {"output_id": new_id, "output_label": row["output_label"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordStakeholderArtifact",
                "description": "Insert a stakeholder-visible artifact row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "output_label": {"type": "string"},
                        "audience": {"type": "string"},
                        "artifact_path": {"type": "string"},
                    },
                    "required": ["output_label", "audience", "artifact_path"],
                },
            },
        }
