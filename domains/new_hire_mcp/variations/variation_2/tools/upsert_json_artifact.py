from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertJsonArtifact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None, content_obj: dict = None, candidate_id: str = None) -> str:
        if content_obj is None:
            content_obj = {}
        text = json.dumps(content_obj, sort_keys=True)
        res = json.loads(
            UpsertOnboardingFile.invoke(
                data,
                file_path=file_path,
                content_text=text,
                mime_type="application/json",
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
                "name": "UpsertJsonArtifact",
                "description": "Create or update a JSON artifact file under onboarding_files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content_obj": {"type": "object"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["file_path", "content_obj", "candidate_id"],
                },
            },
        }
