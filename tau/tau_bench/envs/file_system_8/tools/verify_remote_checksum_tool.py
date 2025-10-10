# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyRemoteChecksumTool(Tool):
    """Verifies the checksum of the transferred archive on the remote host."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_remote_checksum",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        remote_file = next(
            (
                f
                for f in data.get("remote_storage", [])
                if f["path"] == kwargs["remote_path"]
            ),
            None,
        )
        if not remote_file:
            return json.dumps(
                {
                    "status": "error",
                    "error": "remote_file_not_found",
                    "remote_path": kwargs["remote_path"],
                }
            )
        expected = kwargs.get("expected_checksum")
        # If caller didn't provide an expected checksum, accept the remote stored checksum as the authoritative value
        if expected is None:
            expected = remote_file.get("checksum")

        if remote_file.get("checksum") == expected:
            return json.dumps({"status": "verified"})
        return json.dumps(
            {
                "status": "failed",
                "error": "Checksum mismatch.",
                "expected": remote_file.get("checksum"),
                "got": expected,
            }
        )
