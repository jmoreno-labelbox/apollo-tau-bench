# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_one(collection: List[Dict[str, Any]], **filters: Any) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

def _append_row(table: List[Dict[str, Any]], row: Dict[str, Any]) -> None:
    table.append(row)

class UpdateLifecycleStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lifecycle_id: str, status: str, timestamp: str, actor: str) -> str:
        row = _find_one(data["lifecycle_queue"], lifecycle_id=lifecycle_id)
        if not row:
            return json.dumps({"status": "error", "reason": "lifecycle_not_found"})
        row["status"] = status
        _append_row(
            data["lifecycle_audit"],
            {
                "audit_id": f"lcaud_{lifecycle_id}_{status}",
                "lifecycle_id": lifecycle_id,
                "event": status,
                "timestamp": timestamp,
                "actor": actor,
            },
        )
        return json.dumps({"status": "ok", "lifecycle": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_lifecycle_status",
                "description": "Update lifecycle_queue status and append an audit row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "actor": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "status", "timestamp", "actor"],
                },
            },
        }