# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUsersByCity(Tool):
    """List users in a given city (exact match)."""
    @staticmethod
    def invoke(data, city) -> str:
        if not city:
            return json.dumps({"error":"city is required"}, indent=2)
        users = list(data.get('users', {}).values())
        out = [u for u in users if u.get('address',{}).get('city') == city]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"find_users_by_city","description":"Find all users whose address.city equals the given city.","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}
