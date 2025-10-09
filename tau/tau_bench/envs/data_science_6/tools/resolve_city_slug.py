from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ResolveCitySlug(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city: str = None) -> str:
        if not city or not isinstance(city, str):
            payload = {"error": "Missing city"}
            out = json.dumps(payload)
            return out
        mapping = {
            "San Francisco": "sf",
            "Miami": "miami",
            "Boston": "boston",
            "Seattle": "seattle",
            "Charleston": "charleston",
            "New York": "new_york",
            "Los Angeles": "los_angeles",
        }
        slug = mapping.get(city, city.strip().lower().replace(" ", "_"))
        payload = {"city": city, "city_slug": slug}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveCitySlug",
                "description": "Returns canonical city_slug used by file paths (e.g., 'San Francisco' -> 'sf').",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            },
        }
