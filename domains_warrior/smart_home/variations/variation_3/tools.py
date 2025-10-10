import json
from typing import Any, Dict, List, Optional
from datetime import datetime
from domains.dto import Tool

def _now_iso() -> str:
    # return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"

class DeviceManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        devices = data.get('devices', [])
        action = kwargs.get('action', 'get')
        device_id = kwargs.get('device_id')
        device_type = kwargs.get('type')
        location = kwargs.get('location')
        state_updates = kwargs.get('state_updates', {})
        schedule_updates = kwargs.get('schedule_updates')
        device_data = kwargs.get('device_data', {})

        if action == 'get':
            result = [d for d in devices if (not device_id or d['id'] == device_id) and
                     (not device_type or d['type'] == device_type) and
                     (not location or d['location'] == location)]
            return json.dumps(result, indent=2)
        elif action == 'update_state':
            if not device_id:
                return json.dumps({"error": "device_id required for state update"}, indent=2)
            for device in devices:
                if device['id'] == device_id:
                    device['state'].update(state_updates)
                    device['state']['last_updated'] = _now_iso()
                    return json.dumps({"success": f"Updated {device_id} state"}, indent=2)
            return json.dumps({"error": "Device not found"}, indent=2)
        elif action == 'add_schedule':
            if not device_id or not schedule_updates:
                return json.dumps({"error": "device_id and schedule_updates required"}, indent=2)
            for device in devices:
                if device['id'] == device_id:
                    device['scheduled_updates'].append(schedule_updates)
                    return json.dumps({"success": f"Added schedule to {device_id}"}, indent=2)
        elif action == 'create':
            if not device_data:
                return json.dumps({"error": "device_data required for creation"}, indent=2)
            devices.append(device_data)
            return json.dumps({"success": f"Created device {device_data.get('id')}"}, indent=2)
        elif action == 'delete':
            if not device_id:
                return json.dumps({"error": "device_id required for deletion"}, indent=2)
            devices[:] = [d for d in devices if d['id'] != device_id]
            return json.dumps({"success": f"Deleted device {device_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "device_manager",
                "description": "Comprehensive device management - CRUD, state updates, scheduling",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "update_state", "add_schedule", "create", "delete"]},
                        "device_id": {"type": "string", "description": "Device ID for operations"},
                        "type": {"type": "string", "description": "Filter by device type"},
                        "location": {"type": "string", "description": "Filter by location"},
                        "state_updates": {"type": "object", "description": "State parameters to update"},
                        "schedule_updates": {"type": "object", "description": "Schedule data to add (Dict with fields timestamp (String), update (Dict), rrule (String))"},
                        "device_data": {"type": "object", "description": "Full device data for creation"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class RoomManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rooms = data.get('rooms', [])
        action = kwargs.get('action', 'get')
        room_id = kwargs.get('room_id')
        device_id = kwargs.get('device_id')
        floor = kwargs.get('floor')

        if action == 'get':
            result = [r for r in rooms if (not room_id or r['id'] == room_id) and
                     (not floor or r['floor'] == floor)]
            return json.dumps(result, indent=2)
        elif action == 'add_device':
            if not room_id or not device_id:
                return json.dumps({"error": "room_id and device_id required"}, indent=2)
            for room in rooms:
                if room['id'] == room_id:
                    if device_id not in room['devices']:
                        room['devices'].append(device_id)
                    return json.dumps({"success": f"Added {device_id} to {room_id}"}, indent=2)
        elif action == 'remove_device':
            if not room_id or not device_id:
                return json.dumps({"error": "room_id and device_id required"}, indent=2)
            for room in rooms:
                if room['id'] == room_id:
                    if device_id in room['devices']:
                        room['devices'].remove(device_id)
                    return json.dumps({"success": f"Removed {device_id} from {room_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "room_manager",
                "description": "Manage rooms and device assignments",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "add_device", "remove_device"]},
                        "room_id": {"type": "string", "description": "Room ID"},
                        "device_id": {"type": "string", "description": "Device ID to add/remove"},
                        "floor": {"type": "integer", "description": "Filter by floor number"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class SceneManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        scenes = data.get('scenes', [])
        action = kwargs.get('action', 'get')
        scene_id = kwargs.get('scene_id')
        scene_data = kwargs.get('scene_data', {})
        execute_time = kwargs.get('execute_time')

        if action == 'get':
            result = [s for s in scenes if (not scene_id or s['id'] == scene_id)]
            return json.dumps(result, indent=2)
        elif action == 'execute':
            if not scene_id:
                return json.dumps({"error": "scene_id required for execution"}, indent=2)
            for scene in scenes:
                if scene['id'] == scene_id:
                    return json.dumps({"success": f"Executed scene {scene_id}", "actions": scene['actions']}, indent=2)
        elif action == 'create':
            if not scene_data:
                return json.dumps({"error": "scene_data required"}, indent=2)
            scenes.append(scene_data)
            return json.dumps({"success": f"Created scene {scene_data.get('id')}"}, indent=2)
        elif action == 'schedule':
            if not scene_id or not execute_time:
                return json.dumps({"error": "scene_id and execute_time required"}, indent=2)
            for scene in scenes:
                if scene['id'] == scene_id:
                    scene['scheduled_runs'].append(execute_time)
                    return json.dumps({"success": f"Scheduled {scene_id} for {execute_time}"}, indent=2)
        elif action == 'delete':
            if not scene_id:
                return json.dumps({"error": "scene_id required"}, indent=2)
            scenes[:] = [s for s in scenes if s['id'] != scene_id]
            return json.dumps({"success": f"Deleted scene {scene_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scene_manager",
                "description": "Manage automation scenes - CRUD and execution",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "execute", "create", "schedule", "delete"]},
                        "scene_id": {"type": "string", "description": "Scene ID"},
                        "scene_data": {"type": "object", "description": "Scene data for creation"},
                        "execute_time": {"type": "string", "description": "Schedule execution time"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class ListManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        lists = data.get('custom_lists', [])
        action = kwargs.get('action', 'get')
        list_id = kwargs.get('list_id')
        list_name = kwargs.get('list_name')
        tags = kwargs.get('tags', [])
        item_data = kwargs.get('item_data', {})
        list_data = kwargs.get('list_data', {})

        if action == 'get':
            result = [l for l in lists if (not list_id or l['list_id'] == list_id) and
                     (not list_name or l['name'] == list_name) and
                     (not tags or any(tag in l.get('tags', []) for tag in tags))]
            return json.dumps(result, indent=2)
        elif action == 'add_item':
            if not list_id or not item_data:
                return json.dumps({"error": "list_id and item_data required"}, indent=2)
            for lst in lists:
                if lst['list_id'] == list_id:
                    lst['items'].append(item_data)
                    lst['updated_at'] = _now_iso()
                    return json.dumps({"success": f"Added item to {list_id}"}, indent=2)
        elif action == 'remove_item':
            if not list_id or not item_data.get('item'):
                return json.dumps({"error": "list_id and item name required"}, indent=2)
            for lst in lists:
                if lst['list_id'] == list_id:
                    lst['items'] = [i for i in lst['items'] if i['item'] != item_data['item']]
                    lst['updated_at'] = _now_iso()
                    return json.dumps({"success": f"Removed item from {list_id}"}, indent=2)
        elif action == 'create':
            if not list_data:
                return json.dumps({"error": "list_data required"}, indent=2)
            lists.append(list_data)
            return json.dumps({"success": f"Created list {list_data.get('list_id')}"}, indent=2)
        elif action == 'delete':
            if not list_id:
                return json.dumps({"error": "list_id required"}, indent=2)
            lists[:] = [l for l in lists if l['list_id'] != list_id]
            return json.dumps({"success": f"Deleted list {list_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_manager",
                "description": "Manage custom lists and their items",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "add_item", "remove_item", "create", "delete"]},
                        "list_id": {"type": "string", "description": "List ID (already exists)"},
                        "list_name": {"type": "string", "description": "Filter by list name"},
                        "tags": {"type": "array", "items": {"type": "string"}, "description": "Filter by tags"},
                        "item_data": {"type": "object", "description": "Item data to add/remove"},
                        "list_data": {"type": "object", "description": "Full list data for creation (needs list_id (str) and items (list of dicts with item (str) and quantity (int)))"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class ReminderManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reminders = data.get('reminders', [])
        action = kwargs.get('action', 'get')
        reminder_id = kwargs.get('reminder_id')
        status = kwargs.get('status')
        priority = kwargs.get('priority')
        reminder_data = kwargs.get('reminder_data', {})

        if action == 'get':
            result = [r for r in reminders if (not reminder_id or r['reminder_id'] == reminder_id) and
                     (not status or r['status'] == status) and
                     (not priority or r['meta'].get('priority') == priority)]
            return json.dumps(result, indent=2)
        elif action == 'create':
            if not reminder_data:
                return json.dumps({"error": "reminder_data required"}, indent=2)
            reminders.append(reminder_data)
            return json.dumps({"success": f"Created reminder {reminder_data.get('reminder_id')}"}, indent=2)
        elif action == 'update_status':
            if not reminder_id or not status:
                return json.dumps({"error": "reminder_id and status required"}, indent=2)
            for reminder in reminders:
                if reminder['reminder_id'] == reminder_id:
                    reminder['status'] = status
                    return json.dumps({"success": f"Updated {reminder_id} status to {status}"}, indent=2)
        elif action == 'snooze':
            if not reminder_id:
                return json.dumps({"error": "reminder_id required"}, indent=2)
            for reminder in reminders:
                if reminder['reminder_id'] == reminder_id:
                    reminder['status'] = 'snoozed'
                    return json.dumps({"success": f"Snoozed reminder {reminder_id}"}, indent=2)
        elif action == 'delete':
            if not reminder_id:
                return json.dumps({"error": "reminder_id required"}, indent=2)
            reminders[:] = [r for r in reminders if r['reminder_id'] != reminder_id]
            return json.dumps({"success": f"Deleted reminder {reminder_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reminder_manager",
                "description": "Manage reminders and notifications",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "create", "update_status", "snooze", "delete"]},
                        "reminder_id": {"type": "string", "description": "Reminder ID"},
                        "status": {"type": "string", "description": "Filter by or set status"},
                        "priority": {"type": "string", "description": "Filter by priority"},
                        "reminder_data": {"type": "object", "description": "Full reminder data for creation"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class SensorReader(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sensors = data.get('sensors', [])
        sensor_id = kwargs.get('sensor_id')
        sensor_type = kwargs.get('type')
        location = kwargs.get('location')
        state_param = kwargs.get('state_param')
        threshold = kwargs.get('threshold')

        result = [s for s in sensors if (not sensor_id or s['id'] == sensor_id) and
                 (not sensor_type or s['type'] == sensor_type) and
                 (not location or s['location'] == location)]

        if state_param:
            if threshold:
                result = [s for s in result if (s['state'].get(state_param)) and ((threshold.get('operator') == 'gt' and s['state'].get(state_param) > threshold.get('value')) or (threshold.get('operator') == 'lt' and s['state'].get(state_param) < threshold.get('value')))]
            else:
                result = [{**s, 'filtered_state': {state_param: s['state'].get(state_param)}} for s in result]

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sensor_reader",
                "description": "Read sensor data (read-only access)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {"type": "string", "description": "Sensor ID"},
                        "type": {"type": "string", "description": "Filter by sensor type"},
                        "location": {"type": "string", "description": "Filter by location"},
                        "state_param": {"type": "string", "description": "Get specific state parameter only"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class SensorUpdate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sensors = data.get('sensors', [])
        sensor_id = kwargs.get('sensor_id')
        sensor_type = kwargs.get('type')
        location = kwargs.get('location')
        state_param = kwargs.get('state_param')
        if not state_param:
            return json.dumps({"error": "New state ins obligatory"},indent=2)
        result = [s for s in sensors if (not sensor_id or s['id'] == sensor_id) and
                 (not sensor_type or s['type'] == sensor_type) and
                 (not location or s['location'] == location)]
        if len(result) == 0:
            return json.dumps({"error": "No device fund"}, indent=2)
        for s in result:
            for key in state_param:
                if not s['state'][key]:
                    return json.dumps({"error": "State not found in sensors filtered"}, indent=2)
                s['state'][key] = state_param[key]

        return json.dumps({"success": f"Sensors updated {result}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sensor_update",
                "description": "Update sensor state",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sensor_id": {"type": "string", "description": "Sensor ID"},
                        "type": {"type": "string", "description": "Filter by sensor type"},
                        "location": {"type": "string", "description": "Filter by location"},
                        "state_param": {"type": "string", "description": "Get specific state parameter only"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class MemberManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        members = data.get('members', [])
        action = kwargs.get('action', 'get')
        member_id = kwargs.get('member_id')
        relation = kwargs.get('relation')
        lives_in_house = kwargs.get('lives_in_house')
        member_data = kwargs.get('member_data', {})
        field_updates = kwargs.get('field_updates', {})

        if action == 'get':
            result = [m for m in members if (not member_id or m['id'] == member_id) and
                     (not relation or relation.lower() in m['relation'].lower()) and
                     (lives_in_house is None or m['residence']['lives_in_house'] == lives_in_house)]
            return json.dumps(result, indent=2)
        elif action == 'update':
            if not member_id or not field_updates:
                return json.dumps({"error": "member_id and field_updates required"}, indent=2)
            for member in members:
                if member['id'] == member_id:
                    for field, value in field_updates.items():
                        if '.' in field:  # nested field like 'contact.phone'
                            parts = field.split('.')
                            obj = member
                            for part in parts[:-1]:
                                obj = obj[part]
                            obj[parts[-1]] = value
                        else:
                            member[field] = value
                    return json.dumps({"success": f"Updated member {member_id}"}, indent=2)
        elif action == 'create':
            if not member_data:
                return json.dumps({"error": "member_data required"}, indent=2)
            members.append(member_data)
            return json.dumps({"success": f"Created member {member_data.get('id')}"}, indent=2)
        elif action == 'delete':
            if not member_id:
                return json.dumps({"error": "member_id required"}, indent=2)
            members[:] = [m for m in members if m['id'] != member_id]
            return json.dumps({"success": f"Deleted member {member_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "member_manager",
                "description": "Manage household members and visitors",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "update", "create", "delete"]},
                        "member_id": {"type": "string", "description": "Member ID (first_name.last_name)"},
                        "relation": {"type": "string", "description": "Filter by relation"},
                        "lives_in_house": {"type": "boolean", "description": "Filter by residence status"},
                        "member_data": {"type": "object", "description": "Full member data for creation"},
                        "field_updates": {"type": "object", "description": "Fields to update (supports nested with dots)"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class SearchEngine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        search_term = kwargs.get('search_term', '').lower()
        search_type = kwargs.get('search_type', 'all')

        if not search_term:
            return json.dumps({"error": "search_term required"}, indent=2)

        results = {}

        if search_type in ['all', 'devices']:
            devices = data.get('devices', [])
            results['devices'] = [d for d in devices if search_term in str(d).lower()]

        if search_type in ['all', 'scenes']:
            scenes = data.get('scenes', [])
            results['scenes'] = [s for s in scenes if search_term in str(s).lower()]

        if search_type in ['all', 'lists']:
            lists = data.get('custom_lists', [])
            results['lists'] = [l for l in lists if search_term in str(l).lower()]

        if search_type in ['all', 'reminders']:
            reminders = data.get('reminders', [])
            results['reminders'] = [r for r in reminders if search_term in str(r).lower()]

        if search_type in ['all', 'members']:
            members = data.get('members', [])
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

class BulkOperator(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        operation = kwargs.get('operation')
        target_type = kwargs.get('target_type')
        filters = kwargs.get('filters', {})
        updates = kwargs.get('updates', {})

        if not operation or not target_type:
            return json.dumps({"error": "operation and target_type required"}, indent=2)

        targets = data.get(target_type, [])
        affected = []

        if operation == 'bulk_update':
            for item in targets:
                match = True
                for key, value in filters.items():
                    if item.get(key) != value:
                        match = False
                        break
                if match:
                    item.update(updates)
                    affected.append(item.get('id', item.get('name', 'unnamed')))

        elif operation == 'bulk_state_update' and target_type == 'devices':
            for device in targets:
                match = True
                for key, value in filters.items():
                    if device.get(key) != value:
                        match = False
                        break
                if match:
                    existing_updates = {
                       k: v for k, v in updates.items()
                        if k in device['state']
                    }
                    device['state'].update(existing_updates)
                    device['state']['last_updated'] = _now_iso()
                    affected.append(device['id'])

        return json.dumps({"success": f"Updated {len(affected)} items"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulk_operator",
                "description": "Perform bulk operations across multiple entities",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "operation": {"type": "string", "enum": ["bulk_update", "bulk_state_update"]},
                        "target_type": {"type": "string", "enum": ["devices", "scenes", "custom_lists", "reminders", "members"]},
                        "filters": {"type": "object", "description": "Criteria to match items"},
                        "updates": {"type": "object", "description": "Updates to apply"}
                    },
                    "required": ["operation", "target_type"],
                    "additionalProperties": False
                }
            }
        }

class StatusMonitor(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_type = kwargs.get('report_type', 'summary')
        category = kwargs.get('category')

        status = {}

        if report_type == 'summary' or not category:
            status['devices'] = {
                'total': len(data.get('devices', [])),
                'by_type': {},
                'by_location': {},
                'powered_on': 0
            }

            for device in data.get('devices', []):
                device_type = device.get('type', 'unknown')
                location = device.get('location', 'unknown')
                status['devices']['by_type'][device_type] = status['devices']['by_type'].get(device_type, 0) + 1
                status['devices']['by_location'][location] = status['devices']['by_location'].get(location, 0) + 1
                if device.get('state', {}).get('power') == 'on':
                    status['devices']['powered_on'] += 1

            status['scenes'] = {'total': len(data.get('scenes', []))}
            status['lists'] = {'total': len(data.get('custom_lists', []))}
            status['reminders'] = {
                'total': len(data.get('reminders', [])),
                'active': len([r for r in data.get('reminders', []) if r.get('status') == 'active'])
            }
            status['members'] = {
                'total': len(data.get('members', [])),
                'residents': len([m for m in data.get('members', []) if m.get('residence', {}).get('lives_in_house')])
            }

        if category == 'devices' or report_type == 'detailed':
            devices = data.get('devices', [])
            status['device_details'] = [
                {
                    'id': d['id'],
                    'type': d['type'],
                    'location': d['location'],
                    'power': d.get('state', {}).get('power', 'unknown'),
                    'last_updated': d.get('state', {}).get('last_updated')
                } for d in devices
            ]

        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "status_monitor",
                "description": "Get system status and analytics",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["summary", "detailed"], "description": "Type of report"},
                        "category": {"type": "string", "enum": ["devices", "scenes", "lists", "reminders", "members"], "description": "Focus on specific category"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }

class ConfigManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action = kwargs.get('action', 'get')
        config_key = kwargs.get('config_key')
        config_value = kwargs.get('config_value')

        if 'config' not in data:
            data['config'] = {
                'timezone': 'America/Los_Angeles',
                'default_schedule_format': 'RRULE',
                'notification_channels': ['mobile_push', 'email', 'speaker'],
                'auto_backup': True,
                'data_retention_days': 365
            }

        config = data['config']

        if action == 'get':
            if config_key:
                return json.dumps({config_key: config.get(config_key)}, indent=2)
            return json.dumps(config, indent=2)
        elif action == 'set':
            if not config_key:
                return json.dumps({"error": "config_key required"}, indent=2)
            config[config_key] = config_value
            return json.dumps({"success": f"Set {config_key} to {config_value}"}, indent=2)
        elif action == 'reset':
            data['config'] = {
                'timezone': 'America/Los_Angeles',
                'default_schedule_format': 'RRULE',
                'notification_channels': ['mobile_push', 'email', 'speaker'],
                'auto_backup': True,
                'data_retention_days': 365
            }
            return json.dumps({"success": "Configuration reset to defaults"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "config_manager",
                "description": "Manage system configuration and settings",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "set", "reset"]},
                        "config_key": {"type": "string", "description": "Configuration key"},
                        "config_value": {"type": "string", "description": "Configuration value to set"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class DataPorter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action = kwargs.get('action')
        data_types = kwargs.get('data_types', ['all'])
        import_data = kwargs.get('import_data', {})

        if action == 'export':
            export_result = {}
            if 'all' in data_types or 'devices' in data_types:
                export_result['devices'] = data.get('devices', [])
            if 'all' in data_types or 'scenes' in data_types:
                export_result['scenes'] = data.get('scenes', [])
            if 'all' in data_types or 'lists' in data_types:
                export_result['custom_lists'] = data.get('custom_lists', [])
            if 'all' in data_types or 'reminders' in data_types:
                export_result['reminders'] = data.get('reminders', [])
            if 'all' in data_types or 'members' in data_types:
                export_result['members'] = data.get('members', [])
            if 'all' in data_types or 'rooms' in data_types:
                export_result['rooms'] = data.get('rooms', [])

            return json.dumps(export_result, indent=2)

        elif action == 'import':
            if not import_data:
                return json.dumps({"error": "import_data required"}, indent=2)

            imported = []
            for key, value in import_data.items():
                if key in ['devices', 'scenes', 'custom_lists', 'reminders', 'members', 'rooms']:
                    data[key] = value
                    imported.append(key)

            return json.dumps({"success": f"Imported data types: {imported}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "data_porter",
                "description": "Import/export system data for backup and restore",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["export", "import"]},
                        "data_types": {"type": "array", "items": {"type": "string"}, "description": "Data types to export/import"},
                        "import_data": {"type": "object", "description": "Data to import"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

class AutomationEngine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action = kwargs.get('action', 'get')
        rule_id = kwargs.get('rule_id')
        trigger_type = kwargs.get('trigger_type')
        rule_data = kwargs.get('rule_data', {})

        if 'automation_rules' not in data:
            data['automation_rules'] = []

        rules = data['automation_rules']

        if action == 'get':
            result = [r for r in rules if (not rule_id or r.get('id') == rule_id) and
                     (not trigger_type or r.get('trigger', {}).get('type') == trigger_type)]
            return json.dumps(result, indent=2)

        elif action == 'create':
            if not rule_data:
                return json.dumps({"error": "rule_data required"}, indent=2)
            rules.append(rule_data)
            return json.dumps({"success": f"Created automation rule {rule_data.get('id')}"}, indent=2)

        elif action == 'execute':
            if not rule_id:
                return json.dumps({"error": "rule_id required for execution"}, indent=2)
            for rule in rules:
                if rule.get('id') == rule_id:
                    executed_actions = []
                    for action_item in rule.get('actions', []):
                        if action_item.get('type') == 'device_control':
                            device_id = action_item.get('device_id')
                            updates = action_item.get('updates', {})
                            for device in data.get('devices', []):
                                if device['id'] == device_id:
                                    device['state'].update(updates)
                                    device['state']['last_updated'] = _now_iso()
                                    executed_actions.append(f"Updated {device_id}")
                        elif action_item.get('type') == 'scene_execute':
                            scene_id = action_item.get('scene_id')
                            for scene in data.get('scenes', []):
                                if scene['id'] == scene_id:
                                    executed_actions.append(f"Executed scene {scene_id}")
                        elif action_item.get('type') == 'notification':
                            executed_actions.append(f"Sent notification: {action_item.get('message')}")

                    return json.dumps({"success": f"Executed rule {rule_id}", "actions": executed_actions}, indent=2)

            return json.dumps({"error": "Rule not found"}, indent=2)

        elif action == 'evaluate_triggers':
            triggered_rules = []
            for rule in rules:
                trigger = rule.get('trigger', {})
                trigger_type = trigger.get('type')

                if trigger_type == 'device_state':
                    device_id = trigger.get('device_id')
                    condition = trigger.get('condition', {})
                    for device in data.get('devices', []):
                        if device['id'] == device_id:
                            state_matches = all(
                                device['state'].get(key) == value
                                for key, value in condition.items()
                            )
                            if state_matches:
                                triggered_rules.append(rule['id'])

                elif trigger_type == 'sensor_threshold':
                    sensor_id = trigger.get('sensor_id')
                    threshold = trigger.get('threshold', {})
                    for sensor in data.get('sensors', []):
                        if sensor['id'] == sensor_id:
                            for param, limit in threshold.items():
                                current_value = sensor['state'].get(param)
                                if (limit.get('operator') == 'gt' and current_value > limit.get('value')) or \
                                   (limit.get('operator') == 'lt' and current_value < limit.get('value')):
                                    triggered_rules.append(rule['id'])

                elif trigger_type == 'member_presence':
                    member_id = trigger.get('member_id')
                    presence_state = trigger.get('presence_state')
                    triggered_rules.append(f"Would trigger on {member_id} {presence_state}")

            return json.dumps({"triggered_rules": triggered_rules}, indent=2)

        elif action == 'delete':
            if not rule_id:
                return json.dumps({"error": "rule_id required"}, indent=2)
            rules[:] = [r for r in rules if r.get('id') != rule_id]
            return json.dumps({"success": f"Deleted automation rule {rule_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "automation_engine",
                "description": "Advanced automation rules and cross-entity interactions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "create", "execute", "evaluate_triggers", "delete"]},
                        "rule_id": {"type": "string", "description": "Automation rule ID"},
                        "trigger_type": {"type": "string", "enum": ["device_state", "sensor_threshold", "time_based", "member_presence"], "description": "Filter by trigger type"},
                        "rule_data": {"type": "object", "description": "Complete automation rule data for creation"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }

TOOLS = [
    DeviceManager(),
    RoomManager(),
    SceneManager(),
    ListManager(),
    ReminderManager(),
    SensorReader(),
    SensorUpdate(),
    MemberManager(),
    SearchEngine(),
    BulkOperator(),
    StatusMonitor(),
    ConfigManager(),
    DataPorter(),
    AutomationEngine(),
]
