from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class UpdateMilestoneDates(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        milestone_id: str = None, 
        new_start_date: str = None, 
        new_target_date: str = None
    ) -> str:
        if not milestone_id or not (new_start_date or new_target_date):
            payload = {"error": "milestone_id, and at least one date are required"}
            out = json.dumps(payload)
            return out

        milestones = data.get("milestones", [])
        schedule_changes = data.get("schedule_changes", [])
        milestone_dependencies = data.get("milestone_dependencies", [])

        milestone = next(
            (m for m in milestones if m.get("milestone_id") == milestone_id), None
        )
        if not milestone:
            payload = {"error": f"Milestone '{milestone_id}' not found"}
            out = json.dumps(payload)
            return out

        old_start = milestone.get("start_date")
        old_target = milestone.get("target_date")

        is_critical = milestone.get("is_critical_path", False)
        if is_critical and new_target_date:
            old_target_dt = datetime.fromisoformat(old_target.replace("Z", "+00:00"))
            new_target_dt = datetime.fromisoformat(
                new_target_date.replace("Z", "+00:00")
            )
            slippage_days = (new_target_dt - old_target_dt).days

            if slippage_days > 5:
                schedule_impact_analyses = data.get("schedule_impact_analyses", [])
                analysis_id = f"sia_{uuid.uuid4().hex[:8]}"

                downstream_milestones = []
                for dep in milestone_dependencies:
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
                            downstream_milestones.append(
                                {
                                    "milestone_id": succ_milestone.get("milestone_id"),
                                    "milestone_name": succ_milestone.get(
                                        "milestone_name"
                                    ),
                                    "expected_impact_days": slippage_days,
                                }
                            )

                impact_analysis = {
                    "analysis_id": analysis_id,
                    "milestone_id": milestone_id,
                    "slippage_days": slippage_days,
                    "downstream_impacts": downstream_milestones,
                    "critical_path_extension": slippage_days,
                    "created_date": datetime.now(timezone.utc).isoformat(),
                    "status": "mandatory_review_required",
                }

                schedule_impact_analyses.append(impact_analysis)
                payload = {
                    "error": f"Critical path milestone slippage of {slippage_days} days exceeds 5-day threshold. Mandatory schedule impact analysis created.",
                    "impact_analysis": impact_analysis,
                }
                out = json.dumps(payload)
                return out

        impacted_milestones = []
        for dep in milestone_dependencies:
            if dep.get("predecessor_id") == milestone_id:
                impacted_milestones.append(dep.get("successor_id"))

        change_id = f"chg_{uuid.uuid4().hex[:8]}"
        change_record = {
            "change_id": change_id,
            "milestone_id": milestone_id,
            "old_start_date": old_start,
            "old_target_date": old_target,
            "new_start_date": new_start_date or old_start,
            "new_target_date": new_target_date or old_target,
            "impacted_milestones": impacted_milestones,
            "is_critical_path": is_critical,
            "change_date": datetime.now(timezone.utc).isoformat(),
        }
        schedule_changes.append(change_record)

        if new_start_date:
            milestone["start_date"] = new_start_date
        if new_target_date:
            milestone["target_date"] = new_target_date

        if milestone.get("baseline_target"):
            baseline = datetime.fromisoformat(
                milestone["baseline_target"].replace("Z", "+00:00")
            )
            new_target = datetime.fromisoformat(
                milestone["target_date"].replace("Z", "+00:00")
            )
            milestone["float_days"] = (new_target - baseline).days

        result = {
            "success": True,
            "milestone": milestone,
            "change_record": change_record,
            "impacted_count": len(impacted_milestones),
            "critical_path_update_required": len(impacted_milestones) > 0,
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateMilestoneDates",
                "description": "Update milestone start and/or target dates",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "milestone_id": {
                            "type": "string",
                            "description": "Milestone ID",
                        },
                        "new_start_date": {
                            "type": "string",
                            "description": "New start date (ISO format)",
                        },
                        "new_target_date": {
                            "type": "string",
                            "description": "New target date (ISO format)",
                        },
                    },
                    "required": ["milestone_id"],
                },
            },
        }
