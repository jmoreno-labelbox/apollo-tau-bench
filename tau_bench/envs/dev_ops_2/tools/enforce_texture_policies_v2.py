from tau_bench.envs.tool import Tool
import json
from typing import Any

class EnforceTexturePoliciesV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], files: list[str]) -> str:
        pass
        report = [{"file": f, "ok": True} for f in files]
        payload = {"tex_report": report}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnforceTexturePoliciesV2",
                "description": "Deterministic texture checks (simulated).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["files"],
                },
            },
        }
