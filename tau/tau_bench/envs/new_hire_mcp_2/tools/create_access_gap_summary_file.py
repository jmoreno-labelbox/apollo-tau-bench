from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAccessGapSummaryFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None, content_lines: list[str] = None, candidate_id: str = None) -> str:
        if content_lines is None:
            content_lines = []
        content_text = "\n".join(content_lines) + ("\n" if content_lines else "")
        res = json.loads(
            UpsertOnboardingFile.invoke(
                data,
                file_path=file_path,
                content_text=content_text,
                mime_type="text/markdown",
                candidate_id=candidate_id,
            )
        )
        payload = {"file_path": file_path, "created": res.get("created", False)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessGapSummaryFile",
                "description": "Create a markdown summary file from lines.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content_lines": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["file_path", "content_lines", "candidate_id"],
                },
            },
        }
