from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateScoutingReport(Tool):
    """Add a new entry to scouting_reports with consistent links; enforces post-game restrictions for report_type='post-game'."""

    @staticmethod
    def invoke(
        data, 
        report_type: str = None, 
        game_pk: int = None, 
        core_narrative_text: str = None, 
        gslides_link: str = None, 
        s3_pdf_path: str = None,
        draft_status: str = None,
        label: str = None
    ) -> str:
        err = _require_tables(data, ["scouting_reports", "games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "report_type": report_type,
                "game_pk": game_pk,
                "core_narrative_text": core_narrative_text,
                "gslides_link": gslides_link,
                "s3_pdf_path": s3_pdf_path,
            },
            [
                "report_type",
                "game_pk",
                "core_narrative_text",
                "gslides_link",
                "s3_pdf_path",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rtype = report_type
        gpk = game_pk
        if rtype == "post-game":
            g = next((g for g in data["games"] if g.get("game_pk") == gpk), None)
            if not g or g.get("game_status") != "Final":
                payload = {
                        "error": "post-game reports require games.game_status == 'Final'."
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        rows = data["scouting_reports"]
        new_id = _next_id(rows, "report_id")
        row = {
            "report_id": new_id,
            "report_type": rtype,
            "game_pk": gpk,
            "created_at": _now_utc_iso(),
            "s3_pdf_path": s3_pdf_path,
            "gslides_link": gslides_link,
            "core_narrative_text": core_narrative_text,
        }
        rows.append(row)
        payload = {"report_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateScoutingReport",
                "description": "Creates a scouting_reports row with deterministic links and post-game gate enforcement.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string"},
                        "game_pk": {"type": "integer"},
                        "core_narrative_text": {"type": "string"},
                        "gslides_link": {"type": "string"},
                        "s3_pdf_path": {"type": "string"},
                    },
                    "required": [
                        "report_type",
                        "game_pk",
                        "core_narrative_text",
                        "gslides_link",
                        "s3_pdf_path",
                    ],
                },
            },
        }
