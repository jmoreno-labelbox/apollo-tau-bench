# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ResolveCitySlug(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], city) -> str:
        if not city or not isinstance(city, str):
            return json.dumps({"error": "Missing city"})
        mapping = {"San Francisco": "sf", "Miami": "miami", "Boston": "boston", "Seattle": "seattle", "Charleston": "charleston", "New York": "new_york", "Los Angeles": "los_angeles"}
        slug = mapping.get(city, city.strip().lower().replace(" ", "_"))
        return json.dumps({"city": city, "city_slug": slug})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"resolve_city_slug","description":"Returns canonical city_slug used by file paths (e.g., 'San Francisco' -> 'sf').","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}
