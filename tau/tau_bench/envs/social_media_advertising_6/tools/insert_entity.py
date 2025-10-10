# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertEntity(Tool):
    """Generic deterministic insert into supported tables (ads, adsets)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["table", "row", "timestamp", "request_id"])
        if err:
            return _fail(err)

        table = str(kwargs["table"])
        row = kwargs["row"]
        ts = str(kwargs["timestamp"])

        tbl = _assert_table(data, table)

        # Do NOT coerce row fields. Just append exactly what caller passed.
        # Optional: if the domain wants updated_at defaults, only set if missing.
        if table == "adsets" and "updated_at" not in row:
            row = {**row, "updated_at": ts}

        # Append verbatim and echo back
        tbl.append(copy.deepcopy(row))
        return json.dumps(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insert_entity",
                "description": "Insert a new row into a supported table (ads, adsets) with strict validation and deterministic timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "table": {"type": "string", "enum": ["ads", "adsets"]},
                        "row": {"type": "object"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["table", "row", "timestamp", "request_id"],
                },
            },
        }
