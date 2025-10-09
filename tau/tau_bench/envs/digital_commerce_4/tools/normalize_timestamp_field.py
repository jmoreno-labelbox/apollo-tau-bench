from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class NormalizeTimestampField(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], table_name: str, id_field: str, id_value: str, field: str
    ) -> str:
        id_value = _sid(id_value)
        table = data.get(table_name, [])
        row = next((r for r in table if str(r.get(id_field)) == id_value), None)
        if not row:
            payload = {"error": "row not found"}
            out = json.dumps(payload, indent=2)
            return out
        row[field] = FIXED_NOW
        _append_audit(
            data,
            "NORMALIZE_TIMESTAMP",
            f"{table_name}:{id_value}:{field}",
            {"new_value": FIXED_NOW},
        )
        _ws_append(
            data,
            f"{table_name}:{id_value}:{field}",
            "NORMALIZE_TIMESTAMP",
            {"new_value": FIXED_NOW},
        )
        payload = row
        out = json.dumps(payload, indent=2)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeTimestampField",
                "description": "Normalize a datetime field on a given row to ISO-8601 fixed time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "table_name": {"type": "string"},
                        "id_field": {"type": "string"},
                        "id_value": {"type": "string"},
                        "field": {"type": "string"},
                    },
                    "required": ["table_name", "id_field", "id_value", "field"],
                },
            },
        }
