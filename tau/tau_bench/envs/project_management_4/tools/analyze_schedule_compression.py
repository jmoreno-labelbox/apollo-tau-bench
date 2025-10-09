from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class AnalyzeScheduleCompression(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        target_reduction: int,
        compression_type: str = "crashing"
    ) -> str:
        if not all([project_id, target_reduction]):
            payload = {"error": "project_id and target_reduction are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        compression_analyses = data.get("compression_analyses", [])

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        if not project_milestones:
            payload = {"error": f"No milestones found for project '{project_id}'"}
            out = json.dumps(
                payload)
            return out

        analysis_id = f"comp_{uuid.uuid4().hex[:8]}"

        compression_results = []
        achieved_reduction = 0
        total_cost = 0
        affected_milestones = 0

        for milestone in project_milestones:
            if achieved_reduction >= target_reduction:
                break

            if (
                milestone.get("is_critical_path")
                and compression_type == "resource_reduction"
            ):
                continue

            if milestone.get("float_days", 0) > 0 or milestone.get("is_critical_path"):
                start_date = datetime.fromisoformat(
                    milestone.get("start_date").replace("Z", "+00:00")
                )
                target_date = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )
                duration = (target_date - start_date).days

                if compression_type == "crashing":

                    max_reduction = int(duration * 0.2)
                    reduction = min(
                        max_reduction, target_reduction - achieved_reduction
                    )
                    cost = reduction * 500
                    risk_multiplier = 1.0
                else:

                    max_reduction = int(duration * 0.3)
                    reduction = min(
                        max_reduction, target_reduction - achieved_reduction
                    )
                    cost = 0
                    risk_multiplier = 2.0

                if reduction > 0:
                    compression_results.append(
                        {
                            "milestone_id": milestone.get("milestone_id"),
                            "milestone_name": milestone.get("milestone_name"),
                            "compression_type": compression_type,
                            "original_duration": duration,
                            "reduction_days": reduction,
                            "new_duration": duration - reduction,
                            "cost": cost,
                            "risk_multiplier": risk_multiplier,
                            "is_critical_path": milestone.get(
                                "is_critical_path", False
                            ),
                        }
                    )

                    achieved_reduction += reduction
                    total_cost += cost
                    affected_milestones += 1

        cost_benefit_ratio = (
            total_cost / achieved_reduction if achieved_reduction > 0 else 0
        )

        new_analysis = {
            "analysis_id": analysis_id,
            "project_id": project_id,
            "compression_type": compression_type,
            "target_reduction": target_reduction,
            "achieved_reduction": achieved_reduction,
            "total_cost": total_cost,
            "risk_multiplier": 2.0 if compression_type == "fast_tracking" else 1.0,
            "affected_milestones": affected_milestones,
            "compression_results": compression_results,
            "cost_benefit_ratio": cost_benefit_ratio,
            "created_date": datetime.now(timezone.utc).isoformat(),
        }

        compression_analyses.append(new_analysis)
        payload = {
                "success": True,
                "analysis": new_analysis,
                "feasible": achieved_reduction >= target_reduction * 0.8,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeScheduleCompression",
                "description": "Analyze schedule compression options for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "target_reduction": {
                            "type": "number",
                            "description": "Target reduction in days",
                        },
                        "compression_type": {
                            "type": "string",
                            "description": "Type: crashing, fast_tracking",
                        },
                    },
                    "required": ["project_id", "target_reduction"],
                },
            },
        }
