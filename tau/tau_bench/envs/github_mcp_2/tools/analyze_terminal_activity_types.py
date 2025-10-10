# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AnalyzeTerminalActivityTypes(Tool):
    """Returns frequency of inferred terminal activity types (e.g., git, docker, pytest)"""

    DEFAULT_KEYWORDS = ["git", "docker", "kubectl", "pytest", "helm", "make", "terraform", "pip", "npm"]

    @staticmethod
    def invoke(data: Dict[str, Any], keywords = AnalyzeTerminalActivityTypes.DEFAULT_KEYWORDS) -> str:
        logs = _terminal(data)

        counter = Counter()
        for entry in logs:
            msg = entry.get("message", "").lower()
            for keyword in keywords:
                if keyword in msg:
                    counter[keyword] += 1

        return json.dumps(dict(counter), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_terminal_activity_types",
                "description": "Returns frequency of terminal activity types using known or custom keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of keywords to count (e.g., git, docker)"
                        }
                    }
                }
            }
        }
