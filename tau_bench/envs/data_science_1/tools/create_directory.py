from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateDirectory(Tool):
    def invoke(
        data: dict[str, Any],
        created_ts: Any = None,
        path: str = None,
        updated_ts: Any = None
    ) -> str:
        err = _require({"path": path}, ["path"])
        if err:
            return err
        row = {
            "path": path,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        tbl = data.setdefault("file_directory", [])
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        payload = _append(tbl, row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDirectory",
                "description": "Registers a directory path in file_directory deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["path"],
                },
            },
        }
