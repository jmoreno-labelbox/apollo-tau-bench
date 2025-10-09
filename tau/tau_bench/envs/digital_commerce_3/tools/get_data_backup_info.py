from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetDataBackupInfo(Tool):
    """Retrieve backup metadata using backup_id or provide the most recent backup."""

    @staticmethod
    def invoke(data: dict[str, Any], backup_id: Any = None) -> str:
        backups = data.get("data_backups", [])
        if not backups:
            return _error("No backups found.")
        if backup_id:
            match = _find_one(backups, "backup_id", backup_id)
            if not match:
                return _error(f"Backup '{backup_id}' not found.")
            payload = match
            out = json.dumps(payload, indent=2)
            return out
        payload = backups[-1]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDataBackupInfo",
                "description": "Fetch backup metadata by backup_id or the latest backup if none specified.",
                "parameters": {
                    "type": "object",
                    "properties": {"backup_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
