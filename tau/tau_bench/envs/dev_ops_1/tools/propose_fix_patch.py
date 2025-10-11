# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class ProposeFixPatch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str, logs_uri: Optional[str] = None, first_bad_commit: Optional[str] = None) -> str:
        fixes = _get_table(data, "fix_proposals")
        existing = next((f for f in fixes if f.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)
        patch_id = f"FP-{run_id}"
        proposal = {"patch_id": patch_id, "run_id": run_id, "logs_uri": logs_uri or f"artifact://logs/{run_id}", "first_bad_commit": first_bad_commit, "status": "proposed"}
        fixes.append(proposal)
        return json.dumps(proposal, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "propose_fix_patch", "description": "Creates a deterministic fix proposal entry for a run.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}, "logs_uri": {"type": "string"}, "first_bad_commit": {"type": "string"}}, "required": ["run_id"]}}}