from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsertAttachmentRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        attachment_id: str,
        message_id: str,
        filename: str,
        mime_type: str,
        file_path: str,
        size_bytes: int = 0,
        stored_ts: str = NOW_TS
    ) -> str:
        pass
        rows = _ensure_list(data, "attachments")
        payload = {
            "attachment_id": attachment_id,
            "message_id": message_id,
            "filename": filename,
            "mime_type": mime_type,
            "file_path": file_path,
            "size_bytes": size_bytes,
            "stored_ts": stored_ts,
        }
        rows.append(payload)
        payload = {"attachment_id": payload["attachment_id"], "created": True}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertAttachmentRecord",
                "description": "Insert a new attachment row bound to a message_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "attachment_id": {"type": "string"},
                        "message_id": {"type": "string"},
                        "filename": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "file_path": {"type": "string"},
                        "size_bytes": {"type": "integer"},
                    },
                    "required": [
                        "attachment_id",
                        "message_id",
                        "filename",
                        "mime_type",
                        "file_path",
                    ],
                },
            },
        }
