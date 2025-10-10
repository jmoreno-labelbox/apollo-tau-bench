# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteAuditLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = data.get('audit_logs', [])
        new_id_num = max((int(l['log_id'][2:]) for l in logs), default=0) + 1
        new_log_id = f"L-{new_id_num:03d}"
        new_log = {
                "log_id": new_log_id,
                "actor_id": kwargs.get("actor_id"),
                "action_type": kwargs.get("action_type"),
                "target_id": kwargs.get("target_id"),
                "timestamp": kwargs.get("timestamp"),
                "details": kwargs.get("details"),
        }
        logs.append(new_log)
        data['audit_logs'] = logs
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "write_audit_log",
                        "description": "Writes an entry to the audit log.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "actor_id": {"type": "string"},
                                        "action_type": {"type": "string"},
                                        "target_id": {"type": "string"},
                                        "timestamp": {"type": "string"},
                                        "details": {"type": "string"}
                                },
                                "required": ["actor_id", "action_type", "target_id", "timestamp", "details"]
                        }
                }
        }
