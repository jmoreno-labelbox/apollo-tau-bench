# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertAttachmentRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "attachments")
        payload = {"attachment_id": kwargs.get("attachment_id"), "message_id": kwargs.get("message_id"),
                   "filename": kwargs.get("filename"), "mime_type": kwargs.get("mime_type"),
                   "file_path": kwargs.get("file_path"), "size_bytes": kwargs.get("size_bytes", 0),
                   "stored_ts": kwargs.get("stored_ts", NOW_TS)}
        rows.append(payload)
        return json.dumps({"attachment_id": payload["attachment_id"], "created": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "insert_attachment_record",
                                                 "description": "Insert a new attachment row bound to a message_id.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"attachment_id": {"type": "string"},
                                                                               "message_id": {"type": "string"},
                                                                               "filename": {"type": "string"},
                                                                               "mime_type": {"type": "string"},
                                                                               "file_path": {"type": "string"},
                                                                               "size_bytes": {"type": "integer"}},
                                                                "required": ["attachment_id", "message_id", "filename",
                                                                             "mime_type", "file_path"]}}}
