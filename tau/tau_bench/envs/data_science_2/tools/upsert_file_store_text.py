# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertFileStoreText(Tool):
    """
    Inserts or updates a file_store path entry with text, mime, and char count.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], path: str, file_contents_text: str, file_mime_type: str) -> str:
        rows = data.setdefault("file_store", [])
        for row in rows:
            paths = row.get("paths", [])
            if path in paths:
                i = paths.index(path)
                while len(row.get("file_contents_text", [])) <= i:
                    row.setdefault("file_contents_text", []).append("")
                while len(row.get("file_mime_types", [])) <= i:
                    row.setdefault("file_mime_types", []).append("")
                while len(row.get("char_counts", [])) <= i:
                    row.setdefault("char_counts", []).append(0)
                row["file_contents_text"][i] = file_contents_text
                row["file_mime_types"][i] = file_mime_type
                row["char_counts"][i] = len(file_contents_text)
                return json.dumps({"status": "updated", "path": path})
        rows.append({
            "paths": [path],
            "file_contents_text": [file_contents_text],
            "file_mime_types": [file_mime_type],
            "char_counts": [len(file_contents_text)]
        })
        return json.dumps({"status": "inserted", "path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_file_store_text",
                "description": "Inserts or updates a file_store path entry with text and metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "file_contents_text": {"type": "string"},
                        "file_mime_type": {"type": "string"}
                    },
                    "required": ["path", "file_contents_text", "file_mime_type"]
                }
            }
        }
