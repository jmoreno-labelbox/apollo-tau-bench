# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateDashboardSnapshot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["snapshot_date","ytd_revenue","ytd_tax_reserve","pdf_path"]
        for k in required:
            if kwargs.get(k) is None:
                return json.dumps({"error": f"{k} is required"}, indent=2)
        snaps = data.setdefault("dashboard_snapshots", [])
        new_id = f"SNAP-AUTO-{len(snaps)+1:03d}"
        record = {"snapshot_id": new_id,"snapshot_date": kwargs["snapshot_date"],"ytd_revenue": kwargs["ytd_revenue"],"ytd_tax_reserve": kwargs["ytd_tax_reserve"],"pdf_path": kwargs["pdf_path"]}
        snaps.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "create_dashboard_snapshot","description": "Append a new dashboard snapshot with artifact path.","parameters": {"type": "object","properties": {"snapshot_date": {"type": "string"},"ytd_revenue": {"type": "number"},"ytd_tax_reserve": {"type": "number"},"pdf_path": {"type": "string"}},"required": ["snapshot_date","ytd_revenue","ytd_tax_reserve","pdf_path"]}}}
