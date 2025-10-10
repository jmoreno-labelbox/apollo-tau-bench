# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferArchiveRsyncTool(Tool):
    """Simulates transferring an archive to a remote destination using rsync."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_archive_rsync",
                "description": "Transfers the created archive file to a remote server.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_name": {"type": "string"},
                        "remote_address": {"type": "string"},
                        "destination_path": {"type": "string"},
                    },
                    "required": ["archive_name", "remote_address", "destination_path"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], archive_name, destination_path, remote_address) -> str:
        if "remote_storage" not in data:
            data["remote_storage"] = []
        remote_file = {
            "path": f"{destination_path}/{archive_name}",
            "remote_address": remote_address,
        }
        data["remote_storage"].append(remote_file)
        return json.dumps({"status": "success", "transferred_file": remote_file})
