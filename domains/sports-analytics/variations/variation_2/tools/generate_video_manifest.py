from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateVideoManifest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"video_manifest": "manifest_001"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateVideoManifest",
                "description": "Generates a manifest of clips.",
                "parameters": {
                    "type": "object",
                    "properties": {"insights": {"type": "string"}},
                    "required": ["insights"],
                },
            },
        }
