# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordLifecycleAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lifecycle_id: str, event: str, timestamp: str, actor: str) -> str:
        row = {
            "audit_id": f"lcaud_{lifecycle_id}_{event}",
            "lifecycle_id": lifecycle_id,
            "event": event,
            "timestamp": timestamp,
            "actor": actor,
        }
        _append_row(data["lifecycle_audit"], row)
        return json.dumps({"status": "ok", "audit": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_lifecycle_audit",
                "description": "Append a lifecycle_audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "event": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "actor": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "event", "timestamp", "actor"],
                },
            },
        }
