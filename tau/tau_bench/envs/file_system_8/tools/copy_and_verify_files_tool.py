# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CopyAndVerifyFilesTool(Tool):
    """Simulates copying files to their new destinations and verifying checksums."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "copy_and_verify_files",
                "description": "Copies files from original path to destination path and verifies their checksums.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        copied_files: List[Dict[str, Any]] = []
        if "moved_files" not in data:
            data["moved_files"] = []

        for file in data.get("file_list", []):
            # Simulate compute checksum if missing
            if "checksum" not in file:
                file["checksum"] = hashlib.sha256(file["path"].encode()).hexdigest()

            # Simulate copy by adding an entry to moved_files (preserve checksum)
            moved = {
                "original": file["path"],
                "destination": file.get("destination_path"),
                "checksum": file["checksum"],
            }
            data["moved_files"].append(moved)
            copied_files.append(moved)

        # Post-move verification: ensure destination checksums match source checksum (simulated deterministic)
        verified_count = len(copied_files)
        return json.dumps({"status": "success", "verified_and_copied": verified_count})
