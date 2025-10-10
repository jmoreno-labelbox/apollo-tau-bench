# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class OpenDraftPrV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], head: str, base: str, run_id: str) -> str:
        prs = _get_table(data, "pull_requests")
        # Identify the highest numeric PR among all schemas.
        current_max = 0
        for p in prs:
            for key in ("pr_number", "number"):
                val = p.get(key)
                if isinstance(val, int) and val > current_max:
                    current_max = val
        pr_number = current_max + 1
        record = {
            "pr_number": pr_number,
            "head": head,
            "base": base,
            "title": f"auto fix build break {run_id}",
            "body": f"summary for run {run_id}",
            "draft": True,
            "links": {"run_id": run_id},
        }
        prs.append(record)
        return json.dumps({"pr_number": pr_number}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "open_draft_pr_v2", "description": "Opens a draft PR deterministically with template title/body and pr_number sequencing.", "parameters": {"type": "object", "properties": {"head": {"type": "string"}, "base": {"type": "string"}, "run_id": {"type": "string"}}, "required": ["head", "base", "run_id"]}}}
