# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        archive_id: str,
        mailbox_id: str,
        employee_id: str,
        archive_path: str,
        retention_policy: str,
        created_at: str,
    ) -> str:
        row = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "mailbox_id": mailbox_id,
            "archive_path": archive_path,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["data_archives"], row)
        return json.dumps({"status": "ok", "archive": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archive_mailbox",
                "description": "Archive a mailbox to a storage path with retention policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {"type": "string"},
                        "mailbox_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "archive_path": {"type": "string"},
                        "retention_policy": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["archive_id", "mailbox_id", "employee_id", "archive_path", "retention_policy", "created_at"],
                },
            },
        }
