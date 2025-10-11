# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class WriteFileText(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], content, created_ts, mime_type, path, updated_ts) -> str:
        err = _require(kwargs, ["path", "content"])
        if err: return err
        tbl = data.setdefault("file_store", [])
        row = {"path": path, "file_contents_text": content,
               "file_mime_types": mime_type,
               "char_counts": len(content),
               "created_ts": created_ts, "updated_ts": updated_ts}
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