# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one






def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class GetDataBackupInfo(Tool):
    """Fetch backup metadata by backup_id or return the latest backup."""

    @staticmethod
    def invoke(data: Dict[str, Any], backup_id: Any = None) -> str:
        backup_id = backup_id
        backups = data.get("data_backups", [])
        if not backups:
            return _error("No backups found.")
        if backup_id:
            match = _find_one(backups, "backup_id", backup_id)
            if not match:
                return _error(f"Backup '{backup_id}' not found.")
            return json.dumps(match, indent=2)
        return json.dumps(backups[-1], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_data_backup_info",
                "description": "Fetch backup metadata by backup_id or the latest backup if none specified.",
                "parameters": {
                    "type": "object",
                    "properties": {"backup_id": {"type": "string"}},
                    "required": [],
                },
            },
        }