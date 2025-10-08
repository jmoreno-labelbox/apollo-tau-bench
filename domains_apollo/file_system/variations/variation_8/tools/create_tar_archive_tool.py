from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CreateTarArchiveTool(Tool):
    """Emulates the creation of a compressed tar archive."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createTarArchive",
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
    def invoke(data: dict[str, Any], base_archive_name: str, file_paths: list[str]) -> str:
        archive_name = f"{base_archive_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
        # Compute the total size of files to ascertain archive size
        total_size = sum(
            f["size"]
            for f in data.get("remote_files", [])
            if f["path"] in file_paths
        )
        archive_size = int(total_size * 0.7)  # Estimate of the compression ratio
        data["archive_file"] = {
            "name": archive_name,
            "size": archive_size,
            "original_size": total_size,
        }
        payload = data["archive_file"]
        out = json.dumps(payload)
        return out
