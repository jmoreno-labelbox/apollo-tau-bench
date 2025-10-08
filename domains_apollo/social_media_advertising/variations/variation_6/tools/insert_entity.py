from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class InsertEntity(Tool):
    """Generic deterministic insertion into supported tables (ads, adsets)."""

    @staticmethod
    def invoke(data: dict[str, Any], table: str, row: dict, timestamp: str, request_id: str) -> str:
        err = _require({"table": table, "row": row, "timestamp": timestamp, "request_id": request_id}, ["table", "row", "timestamp", "request_id"])
        if err:
            return _fail(err)

        tbl = _assert_table(data, table)

        # Do NOT modify row fields. Simply append exactly what the caller provided.
        # Optional: if the domain requires updated_at defaults, only assign if absent.
        if table == "adsets" and "updated_at" not in row:
            row = {**row, "updated_at": timestamp}

        # Append as is and return
        tbl.append(copy.deepcopy(row))
        payload = row
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertEntity",
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
