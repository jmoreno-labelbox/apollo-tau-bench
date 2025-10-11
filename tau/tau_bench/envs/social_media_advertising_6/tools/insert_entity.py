# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

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