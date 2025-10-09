from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogSupplierPerformanceIssue(Tool):
    """Records a performance concern related to a supplier's record."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, issue_code: str = None, shipment_id: str = None) -> str:
        if not all([supplier_id, issue_code]):
            payload = {"error": "supplier_id and issue_code are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        supplier_to_update = next(
            (
                s
                for s in data.get("supplier_master", [])
                if s.get("supplier_id") == supplier_id
            ),
            None,
        )
        if not supplier_to_update:
            payload = {"error": f"Supplier '{supplier_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if "performance_logs" not in supplier_to_update:
            supplier_to_update["performance_logs"] = []
        log_entry = {"issue_code": issue_code, "related_shipment": shipment_id}
        supplier_to_update["performance_logs"].append(log_entry)
        payload = supplier_to_update
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogSupplierPerformanceIssue",
                "description": "Logs a performance issue against a supplier's record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "issue_code": {"type": "string"},
                        "shipment_id": {"type": "string"},
                    },
                    "required": ["supplier_id", "issue_code"],
                },
            },
        }
