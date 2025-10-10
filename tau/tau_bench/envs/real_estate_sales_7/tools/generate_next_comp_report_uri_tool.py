# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateNextCompReportUriTool(Tool):
    """Generates next comp_###.pdf URI based on highest report_id in comp_reports."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        base_url = kwargs.get("base_url") or "https://storage.example.com/reports/"
        prefix = kwargs.get("prefix") or "comp_"
        ext = kwargs.get("ext") or ".pdf"
        pad_width = _as_int(kwargs.get("pad_width")) or 3  # 21 -> 021

        # Find current max report_id
        max_id = 0
        for r in data.get("comp_reports", []):
            rid = _as_int(r.get("report_id") or r.get("id") or r.get("entity_id"))
            if rid is not None and rid > max_id:
                max_id = rid

        next_id = max_id + 1
        padded = str(next_id).zfill(pad_width)
        uri = f"{base_url}{prefix}{padded}{ext}"

        out = {
            "next_report_id": next_id,
            "padded_id": padded,
            "file_uri": uri,  # convenience
            "doc_uri": uri,  # compat with update_comp_report_doc_uri
            "generated_at": HARD_TS,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_next_comp_report_uri",
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
