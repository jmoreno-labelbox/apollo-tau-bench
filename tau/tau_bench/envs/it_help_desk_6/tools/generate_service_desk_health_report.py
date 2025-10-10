# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateServiceDeskHealthReport(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        run_id: str,
        started_at: str,
        completed_at: str,
        source_ticket_window_days: int,
        output_path_pdf: str,
    ) -> str:
        row = {
            "run_id": run_id,
            "report_type": "service_desk_health",
            "started_at": started_at,
            "completed_at": completed_at,
            "output_path_pdf": output_path_pdf,
            "source_ticket_window_days": source_ticket_window_days,
        }
        _append_row(data["report_runs"], row)
        return json.dumps({"status": "ok", "report": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_service_desk_health_report",
                "description": "Record a service desk health report generation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "started_at": {"type": "string"},
                        "completed_at": {"type": "string"},
                        "source_ticket_window_days": {"type": "integer"},
                        "output_path_pdf": {"type": "string"},
                    },
                    "required": ["run_id", "started_at", "completed_at", "source_ticket_window_days", "output_path_pdf"],
                },
            },
        }
