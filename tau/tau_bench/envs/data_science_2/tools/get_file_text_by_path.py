# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFileTextByPath(Tool):
    """
    Returns file text and metadata from file_store by path.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], path: str) -> str:
        rows = list(data.get("file_store", {}).values())
        for row in rows:
            paths = row.get("paths", [])
            if path in paths:
                i = paths.index(path)
                out = {
                    "path": path,
                    "file_contents_text": row.get("file_contents_text", [None]*len(paths))[i] if i < len(row.get("file_contents_text", [])) else None,
                    "file_mime_types": row.get("file_mime_types", [None]*len(paths))[i] if i < len(row.get("file_mime_types", [])) else None,
                    "char_counts": row.get("char_counts", [None]*len(paths))[i] if i < len(row.get("char_counts", [])) else None
                }
                return json.dumps(out)
        return json.dumps({"error": "file not found", "path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_file_text_by_path",
                "description": "Returns file text and metadata from file_store by path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Exact file path stored in file_store.paths."}
                    },
                    "required": ["path"]
                }
            }
        }
