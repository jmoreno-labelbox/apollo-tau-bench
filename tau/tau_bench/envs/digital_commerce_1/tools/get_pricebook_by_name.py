# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPricebookByName(Tool):
    @staticmethod
    def invoke(data, pricebook_name: str) -> str:
        rows = data.setdefault("pricebooks", [])
        row = next(
            (
                r
                for r in rows
                if str(r.get("pricebook_name")) == pricebook_name
                or str(r.get("name")) == pricebook_name
            ),
            None,
        )
        if not row:
            raise ValueError(f"pricebook not found: {pricebook_name}")
        return json.dumps(
            {
                "pricebook_id": row.get("pricebook_id") or row.get("id"),
                "pricebook_name": row.get("pricebook_name") or row.get("name"),
                "is_active": bool(row.get("is_active", True)),
                "is_standard": bool(row.get("is_standard", False)),
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_pricebook_by_name",
                "description": "Read an existing pricebook by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"pricebook_name": {"type": "string"}},
                    "required": ["pricebook_name"],
                },
            },
        }
