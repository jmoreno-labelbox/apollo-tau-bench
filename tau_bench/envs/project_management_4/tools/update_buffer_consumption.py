from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

class UpdateBufferConsumption(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        buffer_type: str,
        days_consumed: int,
        milestone_id: str = None,
        scope: str = "false",
        change_request_id: str = None
    ) -> str:
        if not all([project_id, buffer_type, days_consumed]):
            payload = {"error": "project_id, buffer_type and days_consumed are required"}
            out = json.dumps(payload)
            return out

        if scope.lower() == "true" and not change_request_id:
            payload = {
                "error": "Buffer cannot be consumed for scope additions without change request approval. Provide change_request_id."
            }
            out = json.dumps(payload)
            return out

        schedule_buffers = data.get("schedule_buffers", [])

        buffer = next(
            (b for b in schedule_buffers if b.get("project_id") == project_id), None
        )
        if not buffer:
            total_project_days = 180
            buffer = {
                "project_id": project_id,
                "total_buffer": int(total_project_days * 0.3),
                "project_buffer": int(total_project_days * 0.3 * 0.5),
                "phase_gate_buffer": int(total_project_days * 0.3 * 0.3),
                "integration_buffer": int(total_project_days * 0.3 * 0.2),
                "project_consumed": 0,
                "phase_gate_consumed": 0,
                "integration_consumed": 0,
                "buffer_history": [],
            }
            schedule_buffers.append(buffer)

        if buffer_type == "project":
            buffer["project_consumed"] = (
                buffer.get("project_consumed", 0) + days_consumed
            )
            consumption_percentage = (
                buffer["project_consumed"] / buffer["project_buffer"]
            ) * 100
        elif buffer_type == "phase_gate":
            buffer["phase_gate_consumed"] = (
                buffer.get("phase_gate_consumed", 0) + days_consumed
            )
            consumption_percentage = (
                buffer["phase_gate_consumed"] / buffer["phase_gate_buffer"]
            ) * 100
        elif buffer_type == "integration":
            buffer["integration_consumed"] = (
                buffer.get("integration_consumed", 0) + days_consumed
            )
            consumption_percentage = (
                buffer["integration_consumed"] / buffer["integration_buffer"]
            ) * 100
        else:
            payload = {
                "error": "Invalid buffer_type. Must be: project, phase_gate, or integration"
            }
            out = json.dumps(payload)
            return out

        if "buffer_history" not in buffer:
            buffer["buffer_history"] = []

        history_entry = {
            "change_id": f"buf_{uuid.uuid4().hex[:8]}",
            "buffer_type": buffer_type,
            "action": "consume",
            "days": days_consumed,
            "milestone_id": milestone_id,
            "scope": scope,
            "change_request_id": change_request_id,
            "consumption_percentage": consumption_percentage,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        buffer["buffer_history"].append(history_entry)

        total_consumed = (
            buffer.get("project_consumed", 0)
            + buffer.get("phase_gate_consumed", 0)
            + buffer.get("integration_consumed", 0)
        )
        total_buffer = buffer.get("total_buffer", 0)
        remaining_buffer = total_buffer - total_consumed
        total_consumption_percentage = (
            (total_consumed / total_buffer * 100) if total_buffer > 0 else 0
        )

        risk_review_required = total_consumption_percentage > 60

        if risk_review_required:
            risk_reviews = data.get("risk_reviews", [])
            review_id = f"risk_{uuid.uuid4().hex[:8]}"
            risk_reviews.append(
                {
                    "review_id": review_id,
                    "project_id": project_id,
                    "trigger": "buffer_consumption_exceeded_60",
                    "consumption_percentage": total_consumption_percentage,
                    "status": "pending",
                    "created_date": datetime.now(timezone.utc).isoformat(),
                }
            )
        payload = {
            "success": True,
            "buffer_status": {
                "project_id": project_id,
                "total_buffer": total_buffer,
                "total_consumed": total_consumed,
                "remaining_buffer": remaining_buffer,
                "consumption_percentage": round(total_consumption_percentage, 1),
                "buffer_type_consumed": {
                    "project": buffer.get("project_consumed", 0),
                    "phase_gate": buffer.get("phase_gate_consumed", 0),
                    "integration": buffer.get("integration_consumed", 0),
                },
                "risk_review_required": risk_review_required,
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateBufferConsumption",
                "description": "Update buffer consumption for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "buffer_type": {
                            "type": "string",
                            "description": "Buffer type: project, phase_gate, integration",
                        },
                        "days_consumed": {
                            "type": "number",
                            "description": "Number of days consumed",
                        },
                        "milestone_id": {
                            "type": "string",
                            "description": "Related milestone ID",
                        },
                        "escope": {
                            "type": "bool",
                            "description": "Flag to indicate if consumption is scope-related",
                        },
                        "change_request_id": {
                            "type": "string",
                            "description": "Change request ID (required for scope additions)",
                        },
                    },
                    "required": [
                        "project_id",
                        "buffer_type",
                        "days_consumed",
                    ],
                },
            },
        }
