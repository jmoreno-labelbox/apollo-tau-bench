# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportReportToCsv(Tool):
    """Export a list of dict rows to CSV with deterministic columns and encoding."""

    @staticmethod
    def _slug(s: str) -> str:
        s = s.lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _infer_basename(rows: List[Dict[str, Any]]) -> str:
        """
        Build a readable, stable basename from common fields if present.
        Preference order keeps names compact but informative.
        """
        if not rows:
            return "report"
        first = rows[0]
        parts = []
        for key in ["plan_id", "campaign_id", "adset_id", "label", "status", "note"]:
            if key in first and first[key] not in (None, ""):
                parts.append(str(first[key]))
        base = "_".join(parts) if parts else "report"
        return ExportReportToCsv._slug(base)

    @staticmethod
    def invoke(data: Dict[str, Any], rows, delimiter = ",", out_path = "") -> str:
        rows: List[Dict[str, Any]] = rows or []
        out_path: str = out_path
        delimiter: str = delimiter

        if not out_path:
            base = ExportReportToCsv._infer_basename(rows)
            out_path = f"{base}.csv"

        fieldnames = sorted({k for r in rows for k in r.keys()}) if rows else []
        with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
            if fieldnames:
                w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
                w.writeheader()
                for r in rows:
                    w.writerow({k: r.get(k, "") for k in fieldnames})
            else:
                f.write("")
        return json.dumps(
            {"success": True, "path": out_path, "rows": len(rows)},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_report_to_csv",
                "description": "Export a list of dicts to a CSV file (deterministic column order).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "List of JSON rows to write."
                        },
                        "out_path": {
                            "type": "string",
                            "description": "Destination file path. If omitted, a readable name is inferred from the rows."
                        },
                        "delimiter": {
                            "type": "string",
                            "description": "CSV delimiter (default ',')."
                        }
                    },
                    "required": ["rows"],
                    "additionalProperties": False,
                },
            },
        }
