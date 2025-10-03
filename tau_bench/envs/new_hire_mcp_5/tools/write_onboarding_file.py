from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class WriteOnboardingFile(Tool):
    """Add or update an entry in onboarding_files for candidate_id and file_path."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str,
        file_path: str,
        content_text: str = "",
        mime_type: str = "text/markdown",
        created_ts: Any = None,
        updated_ts: Any = None
,
    payload: Any = None,
    ) -> str:
        cand_id = candidate_id
        created_ts = _fixed_ts(created_ts)
        updated_ts = _fixed_ts(updated_ts)

        files = data.setdefault("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path and f.get("candidate_id") == cand_id:
                f["content_text"] = content_text
                f["mime_type"] = mime_type
                f["updated_ts"] = updated_ts
                payload = {"file_path": file_path, "status": "updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        files.append(
            {
                "file_path": file_path,
                "content_text": content_text,
                "mime_type": mime_type,
                "created_ts": created_ts,
                "updated_ts": updated_ts,
                "candidate_id": cand_id,
            }
        )
        payload = {"file_path": file_path, "status": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteOnboardingFile",
                "description": "Create or update an onboarding file record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "file_path"],
                },
            },
        }
