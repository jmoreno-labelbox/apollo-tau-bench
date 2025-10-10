# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SaveStakeholderOutput(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outs = data.get("stakeholder_outputs", [])
        max_id = 0
        for o in outs:
            try:
                oid = int(o.get("output_id", 0))
                if oid > max_id: max_id = oid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "output_id": new_id,
            "output_label": kwargs.get("output_label"),
            "audience": kwargs.get("audience"),
            "artifact_path": kwargs.get("artifact_path"),
            "created_at": _fixed_now_iso()
        }
        outs.append(row)
        return json.dumps({"output_id": new_id, "output_label": row["output_label"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_stakeholder_output",
            "description":"Insert a stakeholder output record pointing to an artifact path.",
            "parameters":{"type":"object","properties":{
                "output_label":{"type":"string"},
                "audience":{"type":"string"},
                "artifact_path":{"type":"string"}
            },"required":["output_label","audience","artifact_path"]}
        }}
