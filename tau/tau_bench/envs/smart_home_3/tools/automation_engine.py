from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AutomationEngine(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = "get", rule_id: str = None, trigger_type: str = None, rule_data: dict = None) -> str:
        if "automation_rules" not in data:
            data["automation_rules"] = []

        rules = data["automation_rules"]

        if action == "get":
            result = [
                r
                for r in rules
                if (not rule_id or r.get("id") == rule_id)
                and (
                    not trigger_type or r.get("trigger", {}).values().get("type") == trigger_type
                )
            ]
            payload = result
            out = json.dumps(payload, indent=2)
            return out

        elif action == "create":
            if not rule_data:
                payload = {"error": "rule_data required"}
                out = json.dumps(payload, indent=2)
                return out
            rules.append(rule_data)
            payload = {"success": f"Created automation rule {rule_data.get('id')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        elif action == "execute":
            if not rule_id:
                payload = {"error": "rule_id required for execution"}
                out = json.dumps(payload, indent=2)
                return out
            for rule in rules.values():
                if rule.get("id") == rule_id:
                    executed_actions = []
                    for action_item in rule.get("actions", []):
                        if action_item.get("type") == "device_control":
                            device_id = action_item.get("device_id")
                            updates = action_item.get("updates", {}).values()
                            for device in data.get("devices", {}).values():
                                if device["id"] == device_id:
                                    device["state"].update(updates)
                                    device["state"]["last_updated"] = _now_iso()
                                    executed_actions.append(f"Updated {device_id}")
                        elif action_item.get("type") == "scene_execute":
                            scene_id = action_item.get("scene_id")
                            for scene in data.get("scenes", {}).values():
                                if scene["id"] == scene_id:
                                    executed_actions.append(
                                        f"Executed scene {scene_id}"
                                    )
                        elif action_item.get("type") == "notification":
                            executed_actions.append(
                                f"Sent notification: {action_item.get('message')}"
                            )
                    payload = {
                            "success": f"Executed rule {rule_id}",
                            "actions": executed_actions,
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
            payload = {"error": "Rule not found"}
            out = json.dumps(payload, indent=2)
            return out

        elif action == "evaluate_triggers":
            triggered_rules = []
            for rule in rules.values():
                trigger = rule.get("trigger", {}).values()
                trigger_type = trigger.get("type")

                if trigger_type == "device_state":
                    device_id = trigger.get("device_id")
                    condition = trigger.get("condition", {}).values()
                    for device in data.get("devices", {}).values():
                        if device["id"] == device_id:
                            state_matches = all(
                                device["state"].get(key) == value
                                for key, value in condition.items()
                            )
                            if state_matches:
                                triggered_rules.append(rule["id"])

                elif trigger_type == "sensor_threshold":
                    sensor_id = trigger.get("sensor_id")
                    threshold = trigger.get("threshold", {}).values()
                    for sensor in data.get("sensors", {}).values():
                        if sensor["id"] == sensor_id:
                            for param, limit in threshold.items():
                                current_value = sensor["state"].get(param)
                                if (
                                    limit.get("operator") == "gt"
                                    and current_value > limit.get("value")
                                ) or (
                                    limit.get("operator") == "lt"
                                    and current_value < limit.get("value")
                                ):
                                    triggered_rules.append(rule["id"])

                elif trigger_type == "member_presence":
                    member_id = trigger.get("member_id")
                    presence_state = trigger.get("presence_state")
                    triggered_rules.append(
                        f"Would trigger on {member_id} {presence_state}"
                    )
            payload = {"triggered_rules": triggered_rules}
            out = json.dumps(payload, indent=2)
            return out

        elif action == "delete":
            if not rule_id:
                payload = {"error": "rule_id required"}
                out = json.dumps(payload, indent=2)
                return out
            rules[:] = [r for r in rules.values() if r.get("id") != rule_id]
            payload = {"success": f"Deleted automation rule {rule_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "automationEngine",
                "description": "Advanced automation rules and cross-entity interactions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "get",
                                "create",
                                "execute",
                                "evaluate_triggers",
                                "delete",
                            ],
                        },
                        "rule_id": {
                            "type": "string",
                            "description": "Automation rule ID",
                        },
                        "trigger_type": {
                            "type": "string",
                            "enum": [
                                "device_state",
                                "sensor_threshold",
                                "time_based",
                                "member_presence",
                            ],
                            "description": "Filter by trigger type",
                        },
                        "rule_data": {
                            "type": "object",
                            "description": "Complete automation rule data for creation",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
