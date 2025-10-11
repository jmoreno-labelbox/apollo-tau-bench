# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug


def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], ):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

class RunCacheWarmJobs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mode: str) -> str:
        jobs = _ensure_table(data, "cache_jobs")
        job_name = "Load API Metadata" if mode == "metadata" else "Populate Cache Job"
        job_id = _stable_id("job", job_name)
        row = _find_one(jobs, job_id=job_id)
        if row:
            row["last_run_status"] = "Succeeded"
            row["last_run_time"] = FIXED_NOW
        else:
            jobs.append(
                {
                    "job_id": job_id,
                    "job_name": job_name,
                    "last_run_status": "Succeeded",
                    "last_run_time": FIXED_NOW,
                }
            )
        items_warmed = 1234 if mode == "metadata" else 9876
        return _json(
            {
                "job_run_id": _stable_id("run", job_name, FIXED_NOW),
                "status": "Succeeded",
                "items_warmed": items_warmed,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_cache_warm_jobs",
                "description": "Execute cache warm jobs for metadata or populate.",
                "parameters": {
                    "type": "object",
                    "properties": {"mode": {"type": "string", "enum": ["metadata", "populate"]}},
                    "required": ["mode"],
                },
            },
        }