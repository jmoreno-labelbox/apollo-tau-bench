# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables
from domains_warrior.sports_analytics.variations.variation_1.tools import _today_iso











def _require_tables(data: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None

def _now_utc_iso() -> str:
    return _today_iso() + "T00:00:00Z"

def _next_id(rows: List[Dict[str, Any]], key: str) -> int:
    max_id = 0
    for r in rows:
        try:
            max_id = max(max_id, int(r.get(key, 0)))
        except Exception:
            pass
    return max_id + 1

def _check_required(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None

class CreateScoutingReport(Tool):
    """Insert a new row into scouting_reports with deterministic links; enforces post-game gate for report_type='post-game'."""
    @staticmethod
    def invoke(data, core_narrative_text, game_pk, gslides_link, report_type, s3_pdf_path)->str:
        err = _require_tables(data, ["scouting_reports", "games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["report_type","game_pk","core_narrative_text","gslides_link","s3_pdf_path"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rtype = report_type
        gpk = game_pk
        if rtype == "post-game":
            g = next((g for g in data["games"] if g.get("game_pk") == gpk), None)
            if not g or g.get("game_status") != "Final":
                return json.dumps({"error": "post-game reports require games.game_status == 'Final'."}, indent=2)
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
        return json.dumps({"report_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"create_scouting_report","description":"Creates a scouting_reports row with deterministic links and post-game gate enforcement.","parameters":{"type":"object","properties":{"report_type":{"type":"string"},"game_pk":{"type":"integer"},"core_narrative_text":{"type":"string"},"gslides_link":{"type":"string"},"s3_pdf_path":{"type":"string"}},"required":["report_type","game_pk","core_narrative_text","gslides_link","s3_pdf_path"]}}}