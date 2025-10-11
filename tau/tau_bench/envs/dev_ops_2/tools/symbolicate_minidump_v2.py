# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class SymbolicateMinidumpV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], run_id: str) -> str:
        artifacts = _get_table(data, "artifacts")
        art = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not art:
            art = {"run_id": run_id}
            artifacts.append(art)
        symbolicated_stack_uri = f"artifact://symbolicated_stack/{run_id}"
        art["symbolicated_stack_uri"] = symbolicated_stack_uri
        return json.dumps({"symbolicated_stack_uri": symbolicated_stack_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "symbolicate_minidump_v2", "description": "Writes a deterministic symbolicated stack URI for the run.", "parameters": {"type": "object", "properties": {"run_id": {"type": "string"}}, "required": ["run_id"]}}}