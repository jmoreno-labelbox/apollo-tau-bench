from tau_bench.envs.tool import Tool
import json
from typing import Any

class VideoCreation(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], insights: Any = None, manifest: Any = None, tool: str = None) -> str:
        payload = {"video_manifest": "manifest_001"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "vidMani",
                "description": "Creates a manifest of clips.",
                "parameters": {
                    "type": "object",
                    "properties": {"insights": {"type": "string"}},
                    "required": ["insights"],
                },
            },
        }
