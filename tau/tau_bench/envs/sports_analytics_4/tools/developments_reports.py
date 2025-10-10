# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DevelopmentsReports(Tool):
    @staticmethod
        # primary call function
    def invoke(data: Dict[str, Any], report_count, week_of) -> str:
        data.setdefault("player_dev_reports", []).append({
            "dev_report_id": f"dev_{len(data.get('player_dev_reports', []))+1}",
            "week_of": week_of,
            "report_count": report_count
        })
        # return output
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "reportings", "description": "Persists player development reports to database.", "parameters": {"type": "object", "properties": {"week_of": {"type": "string"}, "report_count": {"type": "integer"}}, "required": ["week_of"]}}}
