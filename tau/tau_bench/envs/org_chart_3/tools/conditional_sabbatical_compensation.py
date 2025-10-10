# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_sabbatical_compensation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, level_threshold: str,
               paid_leave_type: str, unpaid_leave_type: str) -> str:
        employees = list(data.get("employees", {}).values())
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"}, indent=2)

        current_level = employee.get("level_id", "")

        # Simple level comparison (assuming L.1, L.2, L.3, L.4, L.5 format)
        def level_to_number(level_str):
            try:
                return float(level_str.replace("L.", ""))
            except:
                return 0

        current_level_num = level_to_number(current_level)
        threshold_level_num = level_to_number(level_threshold)

        if current_level_num >= threshold_level_num:
            # Maintain full compensation - paid sabbatical
            leave_type = paid_leave_type
            compensation_maintained = True
            action_taken = f"Paid sabbatical approved - level {current_level} meets threshold {level_threshold}"
        else:
            # Reduce compensation - unpaid sabbatical
            leave_type = unpaid_leave_type
            compensation_maintained = False
            action_taken = f"Unpaid sabbatical approved - level {current_level} below threshold {level_threshold}"

        return json.dumps({
            "success": f"Sabbatical compensation decision made for employee {employee_id}",
            "current_level": current_level,
            "level_threshold": level_threshold,
            "condition_met": current_level_num >= threshold_level_num,
            "leave_type": leave_type,
            "compensation_maintained": compensation_maintained,
            "action_taken": action_taken
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_sabbatical_compensation",
                "description": "Determine sabbatical compensation based on employee level threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "level_threshold": {"type": "string", "description": "Minimum level for paid sabbatical (e.g., 'L.3')"},
                        "paid_leave_type": {"type": "string", "description": "Leave type if level meets threshold"},
                        "unpaid_leave_type": {"type": "string", "description": "Leave type if level below threshold"}
                    },
                    "required": ["employee_id", "level_threshold", "paid_leave_type", "unpaid_leave_type"],
                    "additionalProperties": False
                }
            }
        }
