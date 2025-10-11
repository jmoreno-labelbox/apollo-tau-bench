# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EvaluateAccessibility(Tool):  # RETRIEVE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        artifact_id: str
    ) -> str:
        # Check input for correctness.
        if not isinstance(artifact_id, str) or not artifact_id:
            return json.dumps({"error": "artifact_id must be a non-empty string"})

        artifacts = list(data.get("figma_artifacts", {}).values())

        # Locate the artifact.
        artifact = next((a for a in artifacts if a.get("artifact_id") == artifact_id), None)
        if not artifact:
            return json.dumps({"error": f"Artifact {artifact_id} not found"})

        # Utilize page_id as layer_id and artifact_name as layer_name.
        layer_id = artifact.get("page_id")
        layer_name = artifact.get("artifact_name")

        if not layer_id or not layer_name:
            return json.dumps({"error": f"Missing page_id or artifact_name for artifact {artifact_id}"})

        # Produce consistent yet "random" values by hashing the artifact_id.
        hash_value = custom_hash(artifact_id)

        # Choose violation_type in a deterministic manner.
        violation_types = ["TOUCH_TARGET", "CONTRAST", "TEXT_SIZING", "RTL"]
        violation_type = violation_types[abs(hash_value) % len(violation_types)]

        # Create violation_details_json and recommended_fix_summary according to the violation_type.
        if violation_type == "TOUCH_TARGET":
            sizes = ["32x32px", "36x36px", "40x40px"]
            current_size = sizes[abs(hash_value // 3) % len(sizes)]
            violation_details_json = f'{{"current_size": "{current_size}", "required_size": "44x44px", "description": "Touch target too small for mobile accessibility"}}'
            recommended_fix_summary = "Increase button size to minimum 44x44px for touch accessibility"

        elif violation_type == "CONTRAST":
            ratios = ["2.1:1", "2.8:1", "3.2:1"]
            colors = [
                {"foreground": "#666666", "background": "#ffffff"},
                {"foreground": "#888888", "background": "#ffffff"},
                {"foreground": "#777777", "background": "#ffffff"}
            ]
            current_ratio = ratios[abs(hash_value // 5) % len(ratios)]
            color_set = colors[abs(hash_value // 7) % len(colors)]
            violation_details_json = f'{{"current_ratio": "{current_ratio}", "required_ratio": "4.5:1", "colors": {{"foreground": "{color_set["foreground"]}", "background": "{color_set["background"]}"}}}}'
            recommended_fix_summary = "Increase text color contrast to meet WCAG AA standards"

        elif violation_type == "TEXT_SIZING":
            sizes = ["12px", "14px"]
            current_size = sizes[abs(hash_value // 11) % len(sizes)]
            violation_details_json = f'{{"current_size": "{current_size}", "required_size": "16px", "description": "Text too small for readability"}}'
            recommended_fix_summary = "Increase font size to minimum 16px for better readability"

        else:  # Register Transfer Level
            issues = ["Fixed positioning", "Hardcoded margins", "Icon alignment"]
            issue = issues[abs(hash_value // 13) % len(issues)]
            violation_details_json = f'{{"issue": "{issue}", "description": "Layout doesn\'t adapt to RTL languages"}}'
            recommended_fix_summary = "Implement flexible layout that supports RTL languages"

        # Produce severity in a deterministic manner.
        severities = ["LOW", "MEDIUM", "HIGH"]
        severity = severities[abs(hash_value // 17) % len(severities)]  # Employ varied hash partitioning for diversity.

        return json.dumps({
            "artifact_id": artifact_id,
            "layer_id": layer_id,
            "layer_name": layer_name,
            "violation_type": violation_type,
            "violation_details_json": violation_details_json,
            "recommended_fix_summary": recommended_fix_summary,
            "severity": severity
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "evaluate_accessibility",
                "description": "Evaluate accessibility of a Figma artifact and identify potential violations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string", "description": "The artifact ID to evaluate for accessibility."}
                    },
                    "required": ["artifact_id"]
                }
            }
        }
