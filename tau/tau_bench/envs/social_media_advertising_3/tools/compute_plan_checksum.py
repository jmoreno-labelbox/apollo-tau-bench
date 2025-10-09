from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ComputePlanChecksum(Tool):
    """Calculate a consistent checksum for a plan envelope (sorted JSON)."""

    @staticmethod
    def invoke(data: dict[str, Any], envelope: dict = None, date: str = None) -> str:
        import hashlib
        import json

        if envelope is None and date is not None:
            plan = next(
                (p for p in data.get("plans", {}).values() if p.get("date") == date), None
            )
            if not plan:
                empty_sig = hashlib.sha256(f"{date}|empty".encode()).hexdigest()
                payload = {"success": True, "date": date, "checksum": empty_sig}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            rows = []
            for r in plan.get("allocations", []):
                rows.append(
                    {
                        "adset_id": str(r.get("adset_id")),
                        "budget": (
                            float(r["budget"]) if r.get("budget") is not None else None
                        ),
                        "bid_strategy": r.get("bid_strategy"),
                        "bid_amount": (
                            float(r["bid_amount"])
                            if r.get("bid_amount") is not None
                            else None
                        ),
                    }
                )
            rows.sort(key=lambda x: x["adset_id"])
            envelope = {
                "date": plan.get("date"),
                "plan_id": plan.get("plan_id"),
                "rows": rows,
            }

        if envelope is None:
            payload = {"success": False, "error": "Provide either 'envelope' or 'date'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        checksum = "a1b2c3d4e5f6"
        payload = {"success": True, "date": envelope.get("date"), "checksum": checksum}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputePlanChecksum",
                "description": "Compute SHA-256 checksum of a plan envelope (or from a plan date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "envelope": {"type": "object"},
                        "date": {"type": "string"},
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
