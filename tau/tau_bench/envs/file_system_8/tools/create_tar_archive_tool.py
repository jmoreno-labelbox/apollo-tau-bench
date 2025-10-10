# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTarArchiveTool(Tool):
    """Simulates creating a compressed tar archive."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_tar_archive",
                "description": "Creates a compressed .tar.gz archive with a timestamp from a list of files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "base_archive_name": {"type": "string"},
                        "file_paths": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["base_archive_name", "file_paths"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        archive_name = f"{kwargs['base_archive_name']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
        # Calculate total size of files to determine archive size
        total_size = sum(
            f["size"]
            for f in data.get("remote_files", [])
            if f["path"] in kwargs["file_paths"]
        )
        archive_size = int(total_size * 0.7)  # Compression ratio estimate
        data["archive_file"] = {
            "name": archive_name,
            "size": archive_size,
            "original_size": total_size,
        }
        return json.dumps(data["archive_file"])
