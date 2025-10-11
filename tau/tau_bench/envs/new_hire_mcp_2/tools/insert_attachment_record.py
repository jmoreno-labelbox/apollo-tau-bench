# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class InsertAttachmentRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachment_id, file_path, filename, message_id, mime_type, size_bytes = 0, stored_ts = NOW_TS) -> str:
        rows = _ensure_list(data, "attachments")
        payload = {"attachment_id": attachment_id, "message_id": message_id,
                   "filename": filename, "mime_type": mime_type,
                   "file_path": file_path, "size_bytes": size_bytes,
                   "stored_ts": stored_ts}
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