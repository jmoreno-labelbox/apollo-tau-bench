# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class ProcessDataBackup(Tool):
    """Manage data backup and recovery operations."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], backup_type: Any = "incremental", storage_location: Any = "s3"
    ) -> str:
        backup_type = backup_type
        storage_location = storage_location

        backups = data.setdefault("data_backups", [])
        backup_id = f"BKP_{len(backups) + 1:04d}"

        backup = {
            "backup_id": backup_id,
            "backup_type": backup_type,
            "storage_location": storage_location,
            "data_size_mb": 1024,
            "started_at": FIXED_NOW,
            "status": "completed",
        }
        backups.append(backup)

        result = {
            "backup_id": backup_id,
            "backup_type": backup_type,
            "storage_location": storage_location,
            "status": "completed",
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_data_backup",
                "description": "Manage data backup and recovery operations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "backup_type": {"type": "string"},
                        "storage_location": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
