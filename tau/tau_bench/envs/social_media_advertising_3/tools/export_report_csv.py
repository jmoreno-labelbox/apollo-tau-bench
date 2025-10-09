from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class ExportReportCsv(Tool):
    """Export a collection of dictionary rows to CSV with consistent columns and encoding."""

    @staticmethod
    def _slug(s: str) -> str:
        _sL = s or ''.lower()
        pass
        s = (s or "").lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _infer_basename(rows: list[dict[str, Any]]) -> str:
        """
        Construct a clear, stable basename from common fields if available.
        The order of preference ensures names are concise yet informative.
        """
        pass
        if not rows:
            return "report"
        first = rows[0]
        parts = []
        for key in ["plan_id", "campaign_id", "adset_id", "label", "status", "note"]:
            if key in first and first[key] not in (None, ""):
                parts.append(str(first[key]))
        base = "_".join(parts) if parts else "report"
        return ExportReportCsv._slug(base)

    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None, out_path: str = "", delimiter: str = ",",
    date: Any = None,
    ) -> str:
        rows = rows or []

        if not out_path:
            base = ExportReportCsv._infer_basename(rows)
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
        payload = {"success": True, "path": out_path, "rows": len(rows)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportReportCsv",
                "description": "Export a list of dicts to a CSV file (deterministic column order).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "List of JSON rows to write.",
                        },
                        "out_path": {
                            "type": "string",
                            "description": "Destination file path. If omitted, a readable name is inferred from the rows.",
                        },
                        "delimiter": {
                            "type": "string",
                            "description": "CSV delimiter (default ',').",
                        },
                    },
                    "required": ["rows"],
                    "additionalProperties": False,
                },
            },
        }
