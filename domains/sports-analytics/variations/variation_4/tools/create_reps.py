from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateReps(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], report_type: str, game_pk: str, s3_pdf_path: str, insights_data: Any = None, video_data: list = []) -> str:
        scouting_reports = _load_table(data, "scouting_reports")
        report_id = f"RPT-{game_pk}-{report_type}"
        scouting_reports.append(
            {
                "report_id": report_id,
                "report_type": report_type,
                "game_pk": game_pk,
                "s3_pdf_path": s3_pdf_path,
            }
        )
        playlists = _load_table(data, "video_playlists")
        for link in video_data:
            playlists.append({"report_id": report_id, "internal_portal_link": link})
        payload = {"report_id": report_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "report",
                "description": "Persists report and playlist artifacts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string"},
                        "game_pk": {"type": "string"},
                        "s3_pdf_path": {"type": "string"},
                        "insights_data": {"type": "string"},
                        "video_data": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "report_type",
                        "game_pk",
                        "s3_pdf_path",
                        "insights_data",
                    ],
                },
            },
        }
