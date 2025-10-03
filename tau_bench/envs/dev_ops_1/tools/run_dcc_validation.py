from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunDccValidation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], files: list[str]) -> str:
        results = [{"file": f, "issues": []} for f in files]
        payload = {"qa_json": results}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunDccValidation",
                "description": "Returns deterministic headless DCC validation results (simulated).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["files"],
                },
            },
        }
