from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class QueryLabelUsagePatternsTool(Tool):
    """Examines the usage of email_labels across emails to comprehend categorization patterns and identify missing labels."""

    @staticmethod
    def invoke(data: dict[str, Any], label_category: str = None) -> str:
        pass
        label_category_filter = label_category  # This parameter remains but will not be utilized since the category is absent

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
            "unlabeled_email_count": unlabeled_emails,
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "queryLabelUsagePatterns",
                "description": "Analyzes email_labels usage across emails to understand categorization patterns and missing labels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_category": {
                            "type": "string",
                            "description": "Specific label type to analyze",
                        }
                    },
                    "required": [],
                },
            },
        }
