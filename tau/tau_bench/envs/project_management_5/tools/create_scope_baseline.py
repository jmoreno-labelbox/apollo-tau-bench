# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateScopeBaseline(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        baseline_name = kwargs.get("baseline_name")
        scope_items = kwargs.get("scope_items", [])
        deliverables = kwargs.get("deliverables", [])
        acceptance_criteria = kwargs.get("acceptance_criteria", {})
        success_metrics = kwargs.get("success_metrics", {})
        created_by = kwargs.get("created_by")

        if not all([project_id, baseline_name, created_by]):
            return json.dumps(
                {"error": "project_id, baseline_name, and created_by are required"}
            )

        if not deliverables:
            return json.dumps({"error": "RULE 2: Baseline must include deliverables"})

        if not acceptance_criteria:
            return json.dumps(
                {"error": "RULE 2: Baseline must include acceptance criteria"}
            )

        if not success_metrics:
            return json.dumps(
                {"error": "RULE 2: Baseline must include success metrics"}
            )

        scope_baselines = data.get("scope_baselines", [])

        existing = next(
            (
                b
                for b in scope_baselines
                if b.get("project_id") == project_id and b.get("status") == "approved"
            ),
            None,
        )
        if existing:

            current_version = existing.get("version", "1.0")
            major, minor = map(int, current_version.split("."))
            new_version = f"{major}.{minor + 1}"
        else:
            new_version = "1.0"

        baseline_id = kwargs.get("baseline_id", f"bl_{uuid.uuid4().hex[:8]}")

        total_hours = sum(d.get("estimated_hours", 0) for d in deliverables)

        new_baseline = {
            "baseline_id": baseline_id,
            "project_id": project_id,
            "baseline_name": baseline_name,
            "version": new_version,
            "scope_items": scope_items,
            "deliverables": deliverables,
            "acceptance_criteria": acceptance_criteria,
            "success_metrics": success_metrics,
            "status": "draft",
            "created_by": created_by,
            "created_date": datetime.now().isoformat(),
            "metrics": {
                "total_deliverables": len(deliverables),
                "total_scope_items": len(scope_items),
                "estimated_effort_hours": total_hours,
                "success_metrics_count": len(success_metrics),
            },
            "change_history": [],
        }

        scope_baselines.append(new_baseline)

        return json.dumps({"success": True, "baseline": new_baseline})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_scope_baseline",
                "description": "Create a new scope baseline for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_id": {"type": "string", "description": "Baseline ID"},
                        "baseline_name": {
                            "type": "string",
                            "description": "Name for the baseline",
                        },
                        "scope_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "description": {"type": "string"},
                                    "category": {"type": "string"},
                                },
                            },
                            "description": "List of scope items",
                        },
                        "deliverables": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "deliverable_id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "description": {"type": "string"},
                                    "estimated_hours": {"type": "number"},
                                },
                            },
                            "description": "List of deliverables",
                        },
                        "acceptance_criteria": {
                            "type": "object",
                            "description": "Acceptance criteria mapping",
                        },
                        "success_metrics": {
                            "type": "object",
                            "description": "Success metrics for the project",
                        },
                        "created_by": {"type": "string", "description": "Creator ID"},
                    },
                    "required": ["project_id", "baseline_name", "created_by"],
                },
            },
        }
