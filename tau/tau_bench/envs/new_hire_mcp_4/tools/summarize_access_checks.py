# Copyright Sierra

import re
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

class WriteOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id=None, content_text=None, created_ts=None, file_path=None, mime_type=None, updated_ts=None) -> str:
        cand_id = candidate_id
        file_path = file_path
        content_text = (content_text if content_text is not None else "")
        mime_type = (mime_type if mime_type is not None else "text/markdown")
        created_ts = _fixed_ts(created_ts)
        updated_ts = _fixed_ts(updated_ts)

        files = data.setdefault("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path and f.get("candidate_id") == cand_id:
                f["content_text"] = content_text
                f["mime_type"] = mime_type
                f["updated_ts"] = updated_ts
                return json.dumps({"file_path": file_path, "status": "updated"}, indent=2)

        files.append({
            "file_path": file_path,
            "content_text": content_text,
            "mime_type": mime_type,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
            "candidate_id": cand_id
        })
        return json.dumps({"file_path": file_path, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_onboarding_file",
                "description": "Create or update an onboarding file record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "file_path"]
                }
            }
        }

class SummarizeAccessChecks(Tool):
    @staticmethod
    def _safe_name(s: str) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "_", s or "").strip("_") or "unknown"

    @staticmethod
    def invoke(db: Dict[str, Any], candidate_id) -> str:
        cand_id = candidate_id
        cand_row = next((r for r in db.get("candidates", []) if r.get("candidate_id") == cand_id), None)
        name = cand_row.get("candidate_name") if cand_row else cand_id
        checks = [r for r in db.get("access_checks", []) if r.get("candidate_id") == cand_id]
        by_sys: Dict[str, Dict[str, int]] = {}
        for r in checks:
            sysn = r.get("system_name") or ""
            st = r.get("status") or ""
            by_sys.setdefault(sysn, {}).setdefault(st, 0)
            by_sys[sysn][st] += 1
        summary = {"candidate_id": cand_id, "counts": by_sys, "total": len(checks)}
        file_path = f"/onboarding/{SummarizeAccessChecks._safe_name(name)}/access_summary.json"
        WriteOnboardingFile.invoke(db, candidate_id=cand_id, file_path=file_path, content_text=json.dumps(summary, sort_keys=True, indent=2), mime_type="application/json", updated_ts=_fixed_ts(None))
        return json.dumps({"file_path": file_path, "total_checks": len(checks)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"summarize_access_checks",
            "description":"Aggregate access_checks and write an access_summary.json artifact.",
            "parameters":{"type":"object","properties":{"candidate_id":{"type":"string"}},"required":["candidate_id"]}
        }}