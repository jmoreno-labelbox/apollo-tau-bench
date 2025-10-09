from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class SummarizeAccessChecks(Tool):
    @staticmethod
    def _safe_name(s: str) -> str:
        pass
        return re.sub(r"[^A-Za-z0-9]+", "_", s or "").strip("_") or "unknown"

    @staticmethod
    def invoke(db: dict[str, Any], candidate_id: str) -> str:
        cand_id = candidate_id
        cand_row = next(
            (r for r in db.get("candidates", []) if r.get("candidate_id") == cand_id),
            None,
        )
        name = cand_row.get("candidate_name") if cand_row else cand_id
        checks = [
            r for r in db.get("access_checks", []) if r.get("candidate_id") == cand_id
        ]
        by_sys: dict[str, dict[str, int]] = {}
        for r in checks:
            sysn = r.get("system_name") or ""
            st = r.get("status") or ""
            by_sys.setdefault(sysn, {}).values().setdefault(st, 0)
            by_sys[sysn][st] += 1
        summary = {"candidate_id": cand_id, "counts": by_sys, "total": len(checks)}
        file_path = (
            f"/onboarding/{SummarizeAccessChecks._safe_name(name)}/access_summary.json"
        )
        WriteOnboardingFile.invoke(
            db,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=json.dumps(summary, sort_keys=True, indent=2),
            mime_type="application/json",
            updated_ts=_fixed_ts(None),
        )
        payload = {"file_path": file_path, "total_checks": len(checks)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeAccessChecks",
                "description": "Aggregate access_checks and write an access_summary.json artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
