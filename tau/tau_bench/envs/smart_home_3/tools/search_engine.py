# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchEngine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], search_term = '', search_type = 'all') -> str:
        search_term = search_term.lower()

        if not search_term:
            return json.dumps({"error": "search_term required"}, indent=2)

        results = {}

        if search_type in ['all', 'devices']:
            devices = list(data.get('devices', {}).values())
            results['devices'] = [d for d in devices if search_term in str(d).lower()]

        if search_type in ['all', 'scenes']:
            scenes = list(data.get('scenes', {}).values())
            results['scenes'] = [s for s in scenes if search_term in str(s).lower()]

        if search_type in ['all', 'lists']:
            lists = list(data.get('custom_lists', {}).values())
            results['lists'] = [l for l in lists if search_term in str(l).lower()]

        if search_type in ['all', 'reminders']:
            reminders = list(data.get('reminders', {}).values())
            results['reminders'] = [r for r in reminders if search_term in str(r).lower()]

        if search_type in ['all', 'members']:
            members = list(data.get('members', {}).values())
            results['members'] = [m for m in members if search_term in str(m).lower()]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_engine",
                "description": "Search across all smart home entities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_term": {"type": "string", "description": "Term to search for"},
                        "search_type": {"type": "string", "enum": ["all", "devices", "scenes", "lists", "reminders", "members"], "description": "Type of entities to search"}
                    },
                    "required": ["search_term"],
                    "additionalProperties": False
                }
            }
        }
