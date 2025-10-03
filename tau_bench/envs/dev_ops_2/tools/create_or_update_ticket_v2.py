from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateOrUpdateTicketV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_key: str,
        summary: str,
        description: str,
        run_id: str,
        pr_number: int | None = None,
    ) -> str:
        pass
        work_items = _get_table(data, "work_items")
        existing = next(
            (
                w
                for w in work_items
                if w.get("run_id") == run_id and w.get("project_key") == project_key
            ),
            None,
        )
        if existing:
            existing.update(
                {"summary": summary, "description": description, "pr_number": pr_number}
            )
            payload = {"ticket_key": existing.get("ticket_key")}
            out = json.dumps(payload, indent=2)
            return out
        max_id = _max_int_suffix(work_items, "ticket_key", project_key, 0)
        ticket_key = f"{project_key}-{max_id + 1}"
        rec = {
            "ticket_key": ticket_key,
            "project_key": project_key,
            "summary": summary,
            "description": description,
            "run_id": run_id,
            "pr_number": pr_number,
            "state": "Open",
        }
        work_items.append(rec)
        payload = {"ticket_key": ticket_key}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrUpdateTicketV2",
                "description": "Creates/updates a deterministic work item ticket keyed by project and run_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_key": {"type": "string"},
                        "summary": {"type": "string"},
                        "description": {"type": "string"},
                        "run_id": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["project_key", "summary", "description", "run_id"],
                },
            },
        }
