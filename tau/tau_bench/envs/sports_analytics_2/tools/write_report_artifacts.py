# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteReportArtifacts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_type = kwargs.get("report_type")
        game_pk = kwargs.get("game_pk")
        s3_pdf_path = kwargs.get("s3_pdf_path")
        insights_data = kwargs.get("insights_data")
        video_data = kwargs.get("video_data", [])
        scouting_reports = _load_table(data, "scouting_reports")
        report_id = f"RPT-{game_pk}-{report_type}"
        scouting_reports.append({"report_id": report_id, "report_type": report_type, "game_pk": game_pk, "s3_pdf_path": s3_pdf_path})
        playlists = _load_table(data, "video_playlists")
        for link in video_data:
            playlists.append({"report_id": report_id, "internal_portal_link": link})
        return json.dumps({"report_id": report_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_report_artifacts", "description": "Writes report and playlist artifacts.", "parameters": {"type": "object", "properties": {"report_type": {"type": "string"}, "game_pk": {"type": "string"}, "s3_pdf_path": {"type": "string"}, "insights_data": {"type": "string"}, "video_data": {"type": "array", "items": {"type": "string"}}}, "required": ["report_type", "game_pk", "s3_pdf_path", "insights_data"]}}}
