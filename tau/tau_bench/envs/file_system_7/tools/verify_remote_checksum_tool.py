from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class VerifyRemoteChecksumTool(Tool):
    """Confirms the checksum of the archive transferred to the remote host."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifyRemoteChecksum",
                "description": "Checks the integrity of the archive file on the remote storage by comparing checksums. Simulates 'ssh remote sha256sum -c'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "remote_path": {"type": "string"},
                        "expected_checksum": {"type": "string"},
                    },
                    "required": ["remote_path"],
                },
            },
        }

    @staticmethod
    def invoke(
        data: dict[str, Any],
        remote_path: str,
        expected_checksum: str = None
    ) -> str:
        remote_file = next(
            (
                f
                for f in data.get("remote_storage", [])
                if f["path"] == remote_path
            ),
            None,
        )
        if not remote_file:
            payload = {
                "status": "error",
                "error": "remote_file_not_found",
                "remote_path": remote_path,
            }
            out = json.dumps(payload)
            return out

        # If the caller does not supply an expected checksum, use the remote stored checksum as the definitive value.
        if expected_checksum is None:
            expected_checksum = remote_file.get("checksum")

        if remote_file.get("checksum") == expected_checksum:
            payload = {"status": "verified"}
            out = json.dumps(payload)
            return out

        payload = {
            "status": "failed",
            "error": "Checksum mismatch.",
            "expected": remote_file.get("checksum"),
            "got": expected_checksum,
        }
        out = json.dumps(payload)
        return out
