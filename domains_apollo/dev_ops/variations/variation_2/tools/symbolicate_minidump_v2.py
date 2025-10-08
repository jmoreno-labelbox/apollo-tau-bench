from tau_bench.envs.tool import Tool
import json
from typing import Any

class SymbolicateMinidumpV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str) -> str:
        pass
        artifacts = _get_table(data, "artifacts")
        art = next((a for a in artifacts if a.get("run_id") == run_id), None)
        if not art:
            art = {"run_id": run_id}
            artifacts.append(art)
        symbolicated_stack_uri = f"artifact://symbolicated_stack/{run_id}"
        art["symbolicated_stack_uri"] = symbolicated_stack_uri
        payload = {"symbolicated_stack_uri": symbolicated_stack_uri}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SymbolicateMinidumpV2",
                "description": "Writes a deterministic symbolicated stack URI for the run.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_id": {"type": "string"}},
                    "required": ["run_id"],
                },
            },
        }
