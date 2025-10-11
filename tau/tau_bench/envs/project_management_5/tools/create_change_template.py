# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateChangeTemplate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_by, template_name, template_type, required_approvals = [], risk_threshold = "medium", standard_fields = {}) -> str:

        if not all([template_name, template_type, created_by]):
            return json.dumps(
                {"error": "template_name, template_type, and created_by are required"}
            )

        if "change_templates" not in data:
            data["change_templates"] = []
        change_templates = data["change_templates"]

        existing = next(
            (t for t in change_templates if t.get("template_name") == template_name),
            None,
        )
        if existing:
            return json.dumps({"error": f"Template '{template_name}' already exists"})

        template_id = f"ct_{uuid.uuid4().hex[:8]}"

        if template_type == "standard_enhancement":
            default_fields = {
                "change_type": "scope_addition",
                "priority": "medium",
                "typical_duration_weeks": 4,
                "typical_resources": 2,
            }
        elif template_type == "emergency_fix":
            default_fields = {
                "change_type": "requirement_change",
                "priority": "critical",
                "typical_duration_weeks": 1,
                "requires_emergency_approval": True,
            }
        elif template_type == "scope_reduction":
            default_fields = {
                "change_type": "scope_reduction",
                "priority": "high",
                "typical_duration_weeks": 2,
            }
        else:
            default_fields = {}

        template_fields = {**default_fields, **standard_fields}

        new_template = {
            "template_id": template_id,
            "template_name": template_name,
            "template_type": template_type,
            "standard_fields": template_fields,
            "required_approvals": required_approvals,
            "risk_threshold": risk_threshold,
            "created_by": created_by,
            "created_date": datetime.now().isoformat(),
            "usage_count": 0,
            "active": True,
        }

        change_templates.append(new_template)

        return json.dumps({"success": True, "template": new_template})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_change_template",
                "description": "Create a template for common change request types",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_name": {
                            "type": "string",
                            "description": "Template name",
                        },
                        "template_type": {
                            "type": "string",
                            "description": "Type: standard_enhancement, emergency_fix, scope_reduction, requirement_update",
                        },
                        "standard_fields": {
                            "type": "object",
                            "description": "Pre-filled fields for this template",
                        },
                        "required_approvals": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Standard approval requirements",
                        },
                        "risk_threshold": {
                            "type": "string",
                            "description": "Default risk level",
                        },
                        "created_by": {"type": "string", "description": "Creator ID"},
                    },
                    "required": ["template_name", "template_type", "created_by"],
                },
            },
        }
