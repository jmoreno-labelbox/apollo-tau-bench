# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_int_id(rows: List[Dict[str, Any]], key: str) -> int:
    mx = 0
    for r in rows:
        try:
            v = int(r.get(key, 0))
            if v > mx:
                mx = v
        except Exception:
            continue
    return mx + 1

def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class CreateCompReportEntryTool(Tool):
    """Creates new entry in comp_reports table."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by_broker_id, subject_property_id) -> str:

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
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_comp_report_entry",
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