# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewTrainingRecords(Tool):
    """
    API tool to get crew member training records and certification progress.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], crew_id: str = None) -> str:
        if not crew_id:
            return json.dumps({
                "status": "missing_parameter",
                "message": "The crew_id parameter is required to retrieve crew training records.",
                "required": "crew_id"
            })

        crew_members = data.get("crew_members", [])
        target_crew = None

        for crew in crew_members:
            if crew.get("crew_member_id") == crew_id:
                target_crew = crew
                break

        if not target_crew:
            return json.dumps({
                "status": "not_found",
                "message": f"No crew member found with ID '{crew_id}'. Please check the crew ID and try again.",
                "crew_id": crew_id
            })

        # Create training logs from crew information.
        training_records = [
            {
                "training_type": "Initial Flight Training",
                "completion_date": "2020-03-15",
                "status": "Completed",
                "score": 92
            },
            {
                "training_type": "Emergency Procedures",
                "completion_date": "2021-08-22",
                "status": "Completed",
                "score": 88
            },
            {
                "training_type": "Advanced Aircraft Systems",
                "completion_date": "2022-11-10",
                "status": "Completed",
                "score": 95
            },
            {
                "training_type": "Recurrent Training",
                "completion_date": "2023-06-18",
                "status": "Completed",
                "score": 90
            }
        ]

        # Compute training overview.
        completed_trainings = len([t for t in training_records if t["status"] == "Completed"])
        average_score = sum(t["score"] for t in training_records if t["status"] == "Completed") / completed_trainings if completed_trainings > 0 else 0
        latest_training = max(training_records, key=lambda x: x["completion_date"]) if training_records else None

        training_summary = {
            "crew_id": crew_id,
            "name": f"{target_crew.get('first_name', '')} {target_crew.get('last_name', '')}".strip(),
            "role": target_crew.get("role", ""),
            "total_trainings_completed": completed_trainings,
            "average_score": round(average_score, 1),
            "latest_training": latest_training,
            "training_records": training_records,
            "training_status": "Up to date" if latest_training and (datetime(2025, 9, 15, 0, 0, 0).date() - datetime.strptime(latest_training["completion_date"], "%Y-%m-%d").date()).days <= 365 else "Needs refresh"
        }

        return json.dumps({
            "status": "success",
            "training_records": training_summary
        })

    def get_info(self):
        return {
            "type": "function",
            "function": {
                "name": "get_crew_training_records",
                "description": "Get crew member training records, certification progress, and training history including completion dates, scores, and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_id": {"type": "string", "description": "The crew member ID. Format: CM followed by 3-digit number."}
                    },
                    "required": ["crew_id"]
                }
            }
        }
