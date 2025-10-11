# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertEntity(Tool):
    """Generic deterministic insert into supported tables (ads, adsets)."""

    @staticmethod
    def invoke(data: Dict[str, Any], row, table, timestamp) -> str:
        err = _require(kwargs, ["table", "row", "timestamp", "request_id"])
        if err:
            return _fail(err)

        table = str(table)
        ts = str(timestamp)

        tbl = _assert_table(data, table)

        # Avoid modifying row fields. Simply add what the caller provided.
        # Optional: set updated_at defaults only if they are not already provided.
        if table == "adsets" and "updated_at" not in row:
            row = {**row, "updated_at": ts}

        # Concatenate and return the input as is.
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
