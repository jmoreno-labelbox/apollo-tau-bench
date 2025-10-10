# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMilestoneDependencies(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        milestone_id = kwargs.get("milestone_id")
        if not milestone_id:
            return json.dumps({"error": "milestone_id is required"})

        milestone_dependencies = data.get("milestone_dependencies", [])
        milestones = list(data.get("milestones", {}).values())

        predecessors = []
        successors = []

        for dep in milestone_dependencies:
            if dep.get("successor_id") == milestone_id:
                pred_milestone = next(
                    (
                        m
                        for m in milestones
                        if m.get("milestone_id") == dep.get("predecessor_id")
                    ),
                    None,
                )
                if pred_milestone:
                    predecessors.append(
                        {
                            "dependency_id": dep.get("dependency_id"),
                            "milestone_id": pred_milestone.get("milestone_id"),
                            "milestone_name": pred_milestone.get("milestone_name"),
                            "status": pred_milestone.get("status"),
                            "target_date": pred_milestone.get("target_date"),
                            "dependency_type": dep.get("dependency_type"),
                            "lag_days": dep.get("lag_days"),
                            "is_mandatory": dep.get("is_mandatory"),
                            "zero_lag": dep.get("zero_lag", False),
                        }
                    )

            if dep.get("predecessor_id") == milestone_id:
                succ_milestone = next(
                    (
                        m
                        for m in milestones
                        if m.get("milestone_id") == dep.get("successor_id")
                    ),
                    None,
                )
                if succ_milestone:
                    successors.append(
                        {
                            "dependency_id": dep.get("dependency_id"),
                            "milestone_id": succ_milestone.get("milestone_id"),
                            "milestone_name": succ_milestone.get("milestone_name"),
                            "status": succ_milestone.get("status"),
                            "target_date": succ_milestone.get("target_date"),
                            "dependency_type": dep.get("dependency_type"),
                            "lag_days": dep.get("lag_days"),
                            "is_mandatory": dep.get("is_mandatory"),
                            "zero_lag": dep.get("zero_lag", False),
                        }
                    )

        return json.dumps(
            {
                "milestone_id": milestone_id,
                "predecessors": predecessors,
                "successors": successors,
                "total_dependencies": len(predecessors) + len(successors),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_milestone_dependencies",
                "description": "Get all dependencies (predecessors and successors) for a milestone",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        }
                    },
                    "required": ["milestone_id"],
                },
            },
        }
