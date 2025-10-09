from tau_bench.envs.tool import Tool
import json
from typing import Any

class RenderTurntableV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], files: list[str]) -> str:
        pass
        previews = {
            "turntable_uri": f"artifact://turntable/{len(files)}",
            "stills_uris": [
                f"artifact://still/{i}" for i, _ in enumerate(files, start=1)
            ],
        }
        payload = previews
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RenderTurntableV2",
                "description": "Creates deterministic preview URIs for assets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["files"],
                },
            },
        }
