# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class AddFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        files = data.get("file_store", [])
        max_id = 0
        for f in files:
            try:
                fid = int(f.get("file_id", 0))
                if fid > max_id: max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "file_id": new_id,
            "path": kwargs.get("path"),
            "mime_type": kwargs.get("mime_type"),
            "size": kwargs.get("size"),
            "created_at": _fixed_now_iso()
        }
        files.append(row)
        return json.dumps({"file_id": new_id, "path": row["path"]}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_file",
            "description":"Insert a file metadata row into the file store.",
            "parameters":{"type":"object","properties":{
                "path":{"type":"string"},
                "mime_type":{"type":"string"},
                "size":{"type":["integer","null"]}
            },"required":["path","mime_type"]}
        }}
