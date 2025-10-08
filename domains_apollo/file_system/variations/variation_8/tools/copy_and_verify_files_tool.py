from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CopyAndVerifyFilesTool(Tool):
    """Emulates transferring files to their new locations and validating checksums."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CopyAndVerifyFiles",
                "description": "Copies files from original path to destination path and verifies their checksums.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any],
    source_directory: Any = None,
    ) -> str:
        copied_files: list[dict[str, Any]] = []
        if "moved_files" not in data:
            data["moved_files"] = []

        for file in data.get("file_list", []):
            # Emulate checksum computation if absent
            if "checksum" not in file:
                file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()

            # Emulate copying by appending an entry to moved_files (maintain checksum)
            moved = {
                "original": file["path"],
                "destination": file.get("destination_path"),
                "checksum": file["checksum"],
            }
            data["moved_files"].append(moved)
            copied_files.append(moved)

        # Verification after moving: confirm destination checksums align with source checksum (simulated deterministic)
        verified_count = len(copied_files)
        payload = {"status": "success", "verified_and_copied": verified_count}
        out = json.dumps(payload)
        return out
