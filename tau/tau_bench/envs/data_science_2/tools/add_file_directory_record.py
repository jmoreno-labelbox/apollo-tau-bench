from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddFileDirectoryRecord(Tool):
    """Adds a new file_directory record using parallel arrays."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        paths: list[str],
        file_sizes_bytes: list[int],
        file_hashes_sha256: list[str | None],
        file_mime_types: list[str],
        created_ts: list[str],
        updated_ts: list[str],
    ) -> str:
        n = len(paths)
        if not all(
            len(lst) == n
            for lst in [
                file_sizes_bytes,
                file_hashes_sha256,
                file_mime_types,
                created_ts,
                updated_ts,
            ]
        ):
            payload = {"error": "all arrays must have the same length"}
            out = json.dumps(payload)
            return out
        row = {
            "paths": paths,
            "file_sizes_bytes": file_sizes_bytes,
            "file_hashes_sha256": file_hashes_sha256,
            "file_mime_types": file_mime_types,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        data.setdefault("file_directory", []).append(row)
        payload = {"status": "inserted", "record": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addFileDirectoryRecord",
                "description": "Appends a new file_directory record with parallel arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "paths": {"type": "array", "items": {"type": "string"}},
                        "file_sizes_bytes": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "file_hashes_sha256": {
                            "type": "array",
                            "items": {"type": ["string", "null"]},
                        },
                        "file_mime_types": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "created_ts": {"type": "array", "items": {"type": "string"}},
                        "updated_ts": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "paths",
                        "file_sizes_bytes",
                        "file_hashes_sha256",
                        "file_mime_types",
                        "created_ts",
                        "updated_ts",
                    ],
                },
            },
        }
