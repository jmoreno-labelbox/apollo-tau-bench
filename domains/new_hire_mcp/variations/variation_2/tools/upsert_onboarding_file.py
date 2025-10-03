from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertOnboardingFile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        file_path: str,
        content_text: str = "",
        mime_type: str = "text/plain",
        candidate_id: str = None
    ) -> str:
        rows = _ensure_list(data, "onboarding_files")
        row = _find_by_key(rows, "file_path", file_path)
        created = False
        if row is None:
            row = {
                "file_path": file_path,
                "content_text": content_text,
                "mime_type": mime_type,
                "created_ts": NOW_TS,
                "updated_ts": NOW_TS,
                "candidate_id": candidate_id,
            }
            rows.append(row)
            created = True
        else:
            row["content_text"] = content_text
            row["mime_type"] = mime_type
            row["candidate_id"] = candidate_id
            row["updated_ts"] = NOW_TS
        payload = {"file_path": file_path, "created": created}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertOnboardingFile",
                "description": "Create or update an onboarding_files row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": [
                        "file_path",
                        "content_text",
                        "mime_type",
                        "candidate_id",
                    ],
                },
            },
        }
