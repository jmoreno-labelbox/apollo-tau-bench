from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class CreateCompReportEntryTool(Tool):
    """Inserts a new record into the comp_reports table."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: int = None, subject_property_id: str = None, created_by_broker_id: int = None, start_address: Any = None) -> str:
        if client_id is None or not subject_property_id or created_by_broker_id is None:
            return _err(
                "client_id, subject_property_id, created_by_broker_id are required"
            )

        rows = data.setdefault("comp_reports", [])
        report_id = _next_int_id(rows, "report_id")
        rec = {
            "report_id": report_id,
            "client_id": int(client_id),
            "subject_property_id": str(subject_property_id),
            "created_by_broker_id": int(created_by_broker_id),
            "created_at": HARD_TS,
            "doc_uri": None,
            "status": "draft",
        }
        rows.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCompReportEntry",
                "description": "Creates new entry in comp_reports table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "subject_property_id": {"type": "string"},
                        "created_by_broker_id": {"type": "integer"},
                    },
                    "required": [
                        "client_id",
                        "subject_property_id",
                        "created_by_broker_id",
                    ],
                },
            },
        }
