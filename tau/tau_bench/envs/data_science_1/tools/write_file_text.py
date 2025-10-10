# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class WriteFileText(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["path", "content"])
        if err: return err
        tbl = data.setdefault("file_store", [])
        row = {"path": kwargs["path"], "file_contents_text": kwargs["content"],
               "file_mime_types": kwargs.get("mime_type"),
               "char_counts": len(kwargs["content"]),
               "created_ts": kwargs.get("created_ts"), "updated_ts": kwargs.get("updated_ts")}
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            return json.dumps(existing, indent=2)
        return json.dumps(_append(tbl, row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_file_text",
            "description": "Stores or updates a text file into file_store deterministically.",
            "parameters": {"type": "object", "properties": {
                "path": {"type": "string"}, "content": {"type": "string"}, "mime_type": {"type": "string"},
                "created_ts": {"type": "string"}, "updated_ts": {"type": "string"}}, "required": ["path", "content"]}}}
