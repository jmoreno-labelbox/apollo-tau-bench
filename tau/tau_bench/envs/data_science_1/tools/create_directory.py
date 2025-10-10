# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDirectory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["path"])
        if err: return err
        row = {"path": kwargs["path"], "created_ts": kwargs.get("created_ts"), "updated_ts": kwargs.get("updated_ts")}
        tbl = data.setdefault("file_directory", [])
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            return json.dumps(existing, indent=2)
        return json.dumps(_append(tbl, row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_directory",
            "description": "Registers a directory path in file_directory deterministically.",
            "parameters": {"type": "object", "properties": {
                "path": {"type": "string"},
                "created_ts": {"type": "string"},
                "updated_ts": {"type": "string"}
            }, "required": ["path"]}}}
