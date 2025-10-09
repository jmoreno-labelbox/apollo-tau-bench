from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class AnalyzeTerminalActivityTypes(Tool):
    """Provides the frequency of inferred terminal activity types (e.g., git, docker, pytest)"""

    DEFAULT_KEYWORDS = [
        "git",
        "docker",
        "kubectl",
        "pytest",
        "helm",
        "make",
        "terraform",
        "pip",
        "npm",
    ]

    @staticmethod
    def invoke(data: dict[str, Any], keywords: list[str] = None) -> str:
        if keywords is None:
            keywords = AnalyzeTerminalActivityTypes.DEFAULT_KEYWORDS
        logs = _terminal(data)

        counter = Counter()
        for entry in logs:
            msg = entry.get("message", "").lower()
            for keyword in keywords:
                if keyword in msg:
                    counter[keyword] += 1
        payload = dict(counter)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyzeTerminalActivityTypes",
                "description": "Returns frequency of terminal activity types using known or custom keywords.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of keywords to count (e.g., git, docker)",
                        }
                    },
                },
            },
        }
