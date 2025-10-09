from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMilestoneDependencies(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], milestone_id: str = None) -> str:
        if not milestone_id:
            payload = {"error": "milestone_id is required"}
            out = json.dumps(payload)
            return out

        milestone_dependencies = data.get("milestone_dependencies", {}).values()
        milestones = data.get("milestones", {}).values()

        predecessors = []
        successors = []

        for dep in milestone_dependencies.values():
            if dep.get("successor_id") == milestone_id:
                pred_milestone = next(
                    (
                        m
                        for m in milestones.values() if m.get("milestone_id") == dep.get("predecessor_id")
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
                        for m in milestones.values() if m.get("milestone_id") == dep.get("successor_id")
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
        payload = {
                "milestone_id": milestone_id,
                "predecessors": predecessors,
                "successors": successors,
                "total_dependencies": len(predecessors) + len(successors),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMilestoneDependencies",
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
