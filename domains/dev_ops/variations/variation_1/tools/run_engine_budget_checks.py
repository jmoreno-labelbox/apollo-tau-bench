from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunEngineBudgetChecks(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], files: list[str], scene: str) -> str:
        report = {"scene": scene, "files": files, "violations": []}
        payload = {"engine_report": report}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunEngineBudgetChecks",
                "description": "Runs deterministic engine commandlet budget checks (simulated).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files": {"type": "array", "items": {"type": "string"}},
                        "scene": {"type": "string"},
                    },
                    "required": ["files", "scene"],
                },
            },
        }
