# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryLabelUsagePatternsTool(Tool):
    """Analyzes email_labels usage across emails to understand categorization patterns and missing labels."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label_category_filter = kwargs.get("label_category") # This parameter is retained but will not be utilized since the category is absent.

        labels_map = {l.get("label_id"): l for l in data.get("email_labels", [])}
        emails = data.get("emails", [])

        usage_stats = {}
        unlabeled_emails = 0

        for email in emails:
            label_ids = email.get("labels_ids", [])
            if not label_ids:
                unlabeled_emails += 1
                continue

            for label_id in label_ids:
                label = labels_map.get(label_id)
                if label:
                    label_name = label.get("name", "Unknown")
                    if label_name not in usage_stats:
                        usage_stats[label_name] = {"count": 0}
                    usage_stats[label_name]["count"] += 1

        result = {
            "label_usage_stats": usage_stats,
            "unlabeled_email_count": unlabeled_emails
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_label_usage_patterns",
                "description": "Analyzes email_labels usage across emails to understand categorization patterns and missing labels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_category": {"type": "string", "description": "Specific label type to analyze"}
                    },
                    "required": [],
                },
            },
        }
