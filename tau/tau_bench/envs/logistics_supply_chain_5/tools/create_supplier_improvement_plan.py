from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateSupplierImprovementPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, review_cycle_days: int = 90, recommendation: str = "maintain_active",
    reason: Any = None,
    ) -> str:
        suppliers = data.get("supplier_master", [])
        supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)

        if not supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found"})

        plan_id = f"SIP-{supplier_id}"

        improvement_plan = {
            "plan_id": plan_id,
            "supplier_id": supplier_id,
            "supplier_name": supplier.get("supplier_name"),
            "review_cycle_days": review_cycle_days,
            "created_date": get_current_timestamp(),
            "next_review_date": (get_current_timestamp_object() + timedelta(days=review_cycle_days)).isoformat(),
            "status": "Active",
            "current_performance_rating": supplier.get("performance_rating"),
            "target_improvements": [
                "Improve on-time delivery performance",
                "Enhance quality control processes",
                "Strengthen communication protocols",
                "Proper forecast and path planning"
            ]
        }

        if "supplier_improvement_plans" not in data:
            data["supplier_improvement_plans"] = []
        data["supplier_improvement_plans"].append(improvement_plan)

        recommended_value = "maintain_active"
        if recommendation:
            recommended_value = recommendation

        return json.dumps({
            "plan_id": plan_id,
            "status": "Created",
            "next_review_date": improvement_plan["next_review_date"],
            "supplier_status_recommendation": recommended_value
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSupplierImprovementPlan",
                "description": "Create a performance improvement plan for a supplier",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier identifier"},
                        "review_cycle_days": {"type": "integer", "description": "Review cycle in days"},
                        "recommendation": {"type": "string", "description": "Supplier status recommendation"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }
