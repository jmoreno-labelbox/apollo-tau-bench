from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GenerateAuditReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        audit_id: str = None,
        format: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "artifact_id": artifact_id,
            "audit_id": audit_id,
            "format": format,
            "timestamp": timestamp,
            "request_id": request_id
        })
        miss = _require(
            p, ["artifact_id", "audit_id", "format", "timestamp", "request_id"]
        )
        if miss:
            return miss
        ext = _export_ext_from_format(p["format"])
        ymd = _ymd(p["timestamp"])
        asset_id = f"exp-{p['artifact_id']}-{ymd}-{ext}-001"
        _ensure(data, "assets", []).append(
            {
                "asset_id": asset_id,
                "artifact_id": p["artifact_id"],
                "audit_id": p["audit_id"],
                "kind": "audit_report",
            }
        )
        return _ok({"asset_id": asset_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateAuditReport",
                "description": "Generate an audit report asset for an artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "audit_id": {"type": "string"},
                        "format": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "audit_id",
                        "format",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }
