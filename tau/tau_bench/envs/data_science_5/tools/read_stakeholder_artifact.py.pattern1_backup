# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadStakeholderArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outs = data.get("stakeholder_outputs", []) or []
        oid = kwargs.get("output_id")
        label = kwargs.get("output_label")
        row = None
        if oid is not None:
            row = next((o for o in outs if str(o.get("output_id")) == str(oid)), None)
        elif label:
            row = next((o for o in outs if o.get("output_label") == label), None)
        return json.dumps(row or {"error": "Stakeholder output not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_stakeholder_artifact",
            "description": "Fetch a stakeholder artifact row by id or label.",
            "parameters": {"type": "object", "properties": {
                "output_id": {"type": "string"},
                "output_label": {"type": "string"}
            }, "required": []}
        }}
