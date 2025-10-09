from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RecordQcReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        figure_label: str = None,
        figure_path: str = None,
        artifact_type: str = None,
        related_model_name: str = None
    ) -> str:
        figs = data.get("qc_figures", [])
        max_id = 0
        for f in figs:
            try:
                fid = int(f.get("figure_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "figure_id": new_id,
            "figure_label": figure_label,
            "figure_path": figure_path,
            "artifact_type": artifact_type,
            "related_model_name": related_model_name,
            "created_at": _now_iso_fixed(),
        }
        figs.append(row)
        payload = {"figure_id": new_id, "figure_label": row["figure_label"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordQcReport",
                "description": "Insert a QC report metadata row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figure_label": {"type": "string"},
                        "figure_path": {"type": "string"},
                        "artifact_type": {"type": "string"},
                        "related_model_name": {"type": ["string", "null"]},
                    },
                    "required": ["figure_label", "figure_path", "artifact_type"],
                },
            },
        }
