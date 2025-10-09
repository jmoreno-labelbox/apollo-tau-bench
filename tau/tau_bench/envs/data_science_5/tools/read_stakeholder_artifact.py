from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReadStakeholderArtifact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], output_id: str = None, output_label: str = None) -> str:
        outs = data.get("stakeholder_outputs", {}).values() or []
        oid = output_id
        label = output_label
        row = None
        if oid is not None:
            row = next((o for o in outs.values() if str(o.get("output_id")) == str(oid)), None)
        elif label:
            row = next((o for o in outs.values() if o.get("output_label") == label), None)
        payload = row or {"error": "Stakeholder output not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadStakeholderArtifact",
                "description": "Fetch a stakeholder artifact row by id or label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "output_id": {"type": "string"},
                        "output_label": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
