from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateNextCompReportUriTool(Tool):
    """Creates the next comp_###.pdf URI based on the highest report_id in comp_reports."""

    @staticmethod
    def invoke(data: dict[str, Any], base_url: str = "https://storage.example.com/reports/", 
               prefix: str = "comp_", ext: str = ".pdf", pad_width: int = 3) -> str:
        pass
        # Locate the current maximum report_id
        max_id = 0
        for r in data.get("comp_reports", {}).values():
            rid = _as_int(r.get("report_id") or r.get("id") or r.get("entity_id"))
            if rid is not None and rid > max_id:
                max_id = rid

        next_id = max_id + 1
        padded = str(next_id).zfill(pad_width)
        uri = f"{base_url}{prefix}{padded}{ext}"

        out = {
            "next_report_id": next_id,
            "padded_id": padded,
            "file_uri": uri,  # ease of use
            "doc_uri": uri,  # compatible with update_comp_report_doc_uri
            "generated_at": HARD_TS,
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateNextCompReportUri",
                "description": (
                    "Builds https://storage.example.com/reports/comp_###.pdf using max report_id + 1 from comp_reports."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "base_url": {
                            "type": "string",
                            "description": (
                                "Defaults to https://storage.example.com/reports/"
                            ),
                        },
                        "prefix": {"type": "string", "default": "comp_"},
                        "ext": {"type": "string", "default": ".pdf"},
                        "pad_width": {"type": "integer", "default": 3},
                    },
                    "required": [],
                },
            },
        }
