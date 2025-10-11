# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddFileDirectoryRecord(Tool):
    """
    Appends a new file_directory record with parallel arrays.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], paths: List[str], file_sizes_bytes: List[int], file_hashes_sha256: List[Optional[str]], file_mime_types: List[str], created_ts: List[str], updated_ts: List[str]) -> str:
        n = len(paths)
        if not all(len(lst) == n for lst in [file_sizes_bytes, file_hashes_sha256, file_mime_types, created_ts, updated_ts]):
            return json.dumps({"error": "all arrays must have the same length"})
        row = {
            "paths": paths,
            "file_sizes_bytes": file_sizes_bytes,
            "file_hashes_sha256": file_hashes_sha256,
            "file_mime_types": file_mime_types,
            "created_ts": created_ts,
            "updated_ts": updated_ts
        }
        data.setdefault("file_directory", []).append(row)
        return json.dumps({"status": "inserted", "record": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_file_directory_record",
                "description": "Appends a new file_directory record with parallel arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "paths": {"type": "array", "items": {"type": "string"}},
                        "file_sizes_bytes": {"type": "array", "items": {"type": "integer"}},
                        "file_hashes_sha256": {"type": "array", "items": {"type": ["string", "null"]}},
                        "file_mime_types": {"type": "array", "items": {"type": "string"}},
                        "created_ts": {"type": "array", "items": {"type": "string"}},
                        "updated_ts": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["paths", "file_sizes_bytes", "file_hashes_sha256", "file_mime_types", "created_ts", "updated_ts"]
                }
            }
        }
