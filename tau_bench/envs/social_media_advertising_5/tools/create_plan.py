from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class CreatePlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str = None,
        date: str = None,
        total_budget: float = None,
        author: str = None,
        created_at: str = None,
        checksum: str = None,
        allocations: list = None
    ) -> str:
        if allocations is None:
            allocations = []
        rec = {
            "plan_id": plan_id,
            "date": date,
            "total_budget": total_budget,
            "author": author,
            "created_at": created_at,
            "checksum": checksum,
            "allocations": allocations,
        }
        data.setdefault("plans", []).append(rec)
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePlan",
                "description": "Creates a plan with allocations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "total_budget": {"type": "number"},
                        "author": {"type": "string"},
                        "created_at": {"type": "string"},
                        "checksum": {"type": "string"},
                        "allocations": {"type": "array"},
                    },
                    "required": [
                        "plan_id",
                        "date",
                        "total_budget",
                        "author",
                        "created_at",
                        "checksum",
                        "allocations",
                    ],
                },
            },
        }
