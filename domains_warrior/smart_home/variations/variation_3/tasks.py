from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        You want to set up an automated morning routine for John Smith who wakes up at 6:30 AM on weekdays.
        You want to first find John's current member information and his room assignment. Then you want to create a scene called "john_morning_routine"
        that triggers at 6:30 AM on weekdays. The scene should: turn on the Master Bedroom ceiling light at 60% brightness,
        open the Master Bedroom curtain to 100% position, set the central heater, that is in the basement, to 22 degrees Celsius in heat mode,
        and create a reminder for John to take his medication at 7:00 AM with high priority using mobile push notifications.
        You also want to check the current status of all devices in the Master Bedroom before setting up the automation.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "john_smith"
                }
            ),
            Action(
                name="room_manager",
                kwargs={
                    "action": "get",
                    "room_id": "bedroom_master"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Master Bedroom"
                }
            ),
            Action(
                name="room_manager",
                kwargs={
                    "action": "get",
                    "room_id": "basement"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "basement"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "john_morning_routine",
                        "description": "John's morning routine",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {"power": "on", "brightness": 60}
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {"position": 100}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 22}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "john_morning_medication",

                        "target": {
                            "type": "note",
                            "text": "Take morning medication"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "high"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_02",
        instruction="""
        Emily Smith works part-time at St. Jude Hospital on Monday, Tuesday, and Wednesday from 7:00. She is on the job now.
        You want to optimize energy usage during her work hours. You want to find all devices currently in the Master Bedroom where Emily lives,
        then create a bulk operation to turn off all lights in the Master Bedroom.
        You also want to set the central (from the Living Room) AC to 26 degrees Celsius.
        Create a new scene called "emily_work_energy_save" and set description as "Energy saving mode during Emily's work hours" and actions as the three device changes above.
        You want this scene to be automatically scheduled for next Monday (2025-07-28) at 7:00 AM.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Master Bedroom",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "ac"
                }
            ),
            Action(
                name="bulk_operator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"location": "Master Bedroom", "type": "light"},
                    "updates": {"power": "off", "brightness": 0}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "ac_home",
                    "state_updates": {"power": "on", "mode": "cool", "setpoint_c": 26}
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "emily_work_energy_save",
                        "description": "Energy saving mode during Emily's work hours",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "on", "mode": "cool", "setpoint_c": 26}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "emily_work_energy_save",
                    "execute_time": "2025-07-28T07:00:00"
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_03",
        instruction="""
        You want to set up a comprehensive security system for when the family goes on vacation.
        You want to create a scene called "vacation_security_mode" that triggers when the front door sensor detects it's been closed for more than 2 hours.
        The scene should: turn off all lights except all lights in the Living Room at 30% brightness for security, close all curtains to 0% position,
        set both heater and AC to off. You also want to add 4 "Security camera batteries" to the existing shopping list.
        """,
        actions=[
            Action(
                name="sensor_reader",
                kwargs={
                    "type": "sensor"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "vacation_security_mode",
                        "description": "Vacation security mode",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 30}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 30}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 0}
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {"position": 0}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "off"}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Security camera batteries",
                        "quantity": 4
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_04",
        instruction="""
        Linda Johnson (Grandma) is visiting on 2025-08-04 and needs wheelchair accessibility. She's 70 years old and has specific needs.
        First, you want to find Linda's member information and visit preferences. Then you want to check the status of all devices on the first
        floor where she'll spend most time.
        You want to create a new scene called "grandma_visit_comfort" that: sets the Living Room temperature to 24 degrees via the central heater,
        it's in the basement,turns on the Living Room ceiling light at 80% brightness, opens the Living Room curtains to 100% for natural light,
        and turns off the dishwasher to reduce noise. You want to schedule this scene for 2025-08-04 at 14:00 PM when she usually arrives.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "linda_johnson"
                }
            ),
            Action(
                name="room_manager",
                kwargs={
                    "action": "get",
                    "floor": 1
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Basement"
                }
            ),

            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "grandma_visit_comfort",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 24}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 80}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 100}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "grandma_visit_comfort",
                    "execute_time": "2025-08-04T14:00:00"
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_05",
        instruction="""
        You want to create a sophisticated bedtime routine for both kids - Olivia Smith (9 years old, West Bedroom, bedtime 20:30) and Ethan Smith (6 years old, East Bedroom, bedtime 20:00).
        You want to create a coordinated scene called "kids_bedtime_prep" that parents can manually trigger 30 to Prepare house for kids bedtime minutes before bedtime to:
        set central heater to 20 degrees for comfortable sleep, and turn off all devices in the Living Room for quiet time.
        You also want to set up a weekly reminder for parents every Sunday at 7:00 PM with note "Review and adjust the kids' bedtime routines, and check the air quality sensor in the Living Room to ensure it's healthy for the kids.".
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "olivia_smith"
                }
            ),
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "ethan_smith"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "kids_bedtime_prep",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 20}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "kids_bedtime_review",

                        "target": {
                            "type": "note",
                            "text": "Review and adjust the kids' bedtime routines, and check the air quality sensor in the Living Room to ensure it's healthy for the kids."
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=19;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_06",
        instruction="""
        David Lee and Sarah Lee visit every Sunday evening at 6:30 PM for dinner. David has shellfish allergies and Sarah brings homemade sourdread.
        You want to prepare the house for their weekly visit. First, you want to check their member information and visit preferences, then get the current status
        of all devices in the Living Room and Kitchen areas. You want to create a new scene called "sunday_dinner_prep" that: sets the Living Room temperature
        to 23 degrees Celsius via heater in the basement, turns on both Living Room lights (ceiling at 70% and floor lamp at 40%),
        opens Living Room curtains to 100%,
        and starts the dishwasher on auto cycle for post-dinner cleanup. You want to schedule this scene for next Sunday (2025-07-27) at 6:00 PM.
        You also want to create a shopping reminder that triggers every Saturday at 10:00 AM to buy ingredients for Sunday dinner, avoiding shellfish due to David's allergy.
        You want to update Sarah's member record to note that she brings sourdough bread and fresh herbs from her garden, and add "Sunday dinner ingredients (no shellfish)" to the weekend groceries list.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "david_lee"
                }
            ),
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "sarah_lee"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Basement"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "sunday_dinner_prep",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 23}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 70}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 40}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 100}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "on", "cycle": "auto"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "sunday_dinner_prep",
                    "execute_time": "2025-07-27T18:00:00"
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "sunday_dinner_shopping",

                        "target": {
                            "type": "note",
                            "text": "Buy ingredients for Sunday dinner with David and Sarah (no shellfish due to David's allergy)"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="member_manager",
                kwargs={
                    "action": "update",
                    "member_id": "sarah_lee",
                    "field_updates": {
                        "visit_preferences.brings": ["homemade sourdough", "fresh herbs from garden"]
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Sunday dinner ingredients (no shellfish)",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_07",
        instruction="""
        You want to set up a comprehensive home maintenance system.
        You want to create a new custom list called "home_maintenance_checklist" with tags "maintenance" and "house" with items: "Replace smoke detector batteries", "Clean air quality sensor filters",
        "Check door sensor alignment", and "Test motion sensor coverage".
        You also want to set up a monthly reminder on the 1st at 9:00 AM to review the maintenance checklist and check all device firmware versions.
        Finally, you want to bulk update all sensors that have battery levels below 90% to add a note in their metadata about needing attention, and export all sensor data for maintenance records.
        """,
        actions=[
            Action(
                name="search_engine",
                kwargs={
                    "search_term": "maintenance",
                    "search_type": "reminders"
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "create",
                    "list_data": {
                        "list_id": "home_maintenance_checklist",
                        "tags": ["maintenance", "house"],
                        "items": [
                            {
                                "item": "Replace smoke detector batteries",
                                "quantity": 1
                            },
                            {
                                "item": "Clean air quality sensor filters",
                                "quantity": 1
                            },
                            {
                                "item": "Check door sensor alignment",
                                "quantity": 1
                            },
                            {
                                "item": "Test motion sensor coverage",
                                "quantity": 1
                            }
                        ]
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "monthly_maintenance_review",

                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "home_maintenance_checklist"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="status_monitor",
                kwargs={
                    "report_type": "detailed",
                    "category": "devices"
                }
            ),
            Action(
                name="data_porter",
                kwargs={
                    "action": "export",
                    "data_types": ["sensors"]
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_08",
        instruction="""
        Tonight is family movie night and you want to set up the perfect entertainment environment. First you want to check the current "Movie Time" scene and its actions,
        then get the status of all devices in the Living Room. You want to create an enhanced version called "movie_night_deluxe" that: closes Living Room curtains to 0% for darkness,
        dims the Living Room ceiling light to 15% and turns the floor lamp to 25% for ambient lighting, sets the AC to 22 degrees,
        and turns off the dishwasher to eliminate noise. You also want to create a bulk operation to turn off all unnecessary lights in other rooms, thats: West Bedroom, East Bedroom, Kitchen
        to reduce electricity usage during movie time. You want to set up a reminder for 30 minutes into typical movie time (8:30 PM) to check if anyone needs snacks,
        and add "Movie night snacks" and "Popcorn" to the weekend groceries list. Finally, you want to schedule the enhanced scene for tonight at 7:45 PM.
        """,
        actions=[
            Action(
                name="scene_manager",
                kwargs={
                    "action": "get",
                    "scene_id": "scene_movie_time"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "movie_night_deluxe",


                        "actions": [
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 0}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 15}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 25}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "on", "setpoint_c": 22}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="bulk_operator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"type": "light", "location":"West Bedroom"},
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="bulk_operator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"type": "light", "location":"East Bedroom"},
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="bulk_operator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"type": "light", "location":"Kitchen"},
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "movie_night_deluxe",
                    "execute_time": "2025-07-30T19:45:00"
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "movie_snack_check",

                        "target": {
                            "type": "note",
                            "text": "Check if family needs snacks during movie night"
                        },
                        "trigger": {
                            "datetime": "2025-07-30T20:30:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal",
                            "snooze_default_min": 10
                        },
                        "status": "scheduled"
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Movie night snacks",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Popcorn",
                        "quantity": 2
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_09",
        instruction="""
        John Smith works from home and you want to create an optimized office environment. First, you want to find John's work schedule and occupation details, then check all devices in the Master Bedroom where he works.
        You want to create a new scene called "john_work_focus" that: sets the room temperature to 21 degrees via heater in the basement for optimal focus, turns the Master Bedroom ceiling light to 85% brightness for good visibility,
        opens the curtains to 75% position for natural light but not glare, and ensures the night lamp is off to avoid distraction. You want to schedule this scene to activate Monday through Friday at 7:30 AM when his work starts.
        You want to add "Ergonomic office supplies" to the shopping list for his workspace improvement.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "john_smith"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Master Bedroom"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Basement"
                }
            ),
            Action(
                name="sensor_reader",
                kwargs={
                    "sensor_id": "sensor_lr_air_quality"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "john_work_focus",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 21}
                            },
                            {
                                "device_id": "light_br_ceiling",
                                "update": {"power": "on", "brightness": 85}
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {"position": 75}
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "john_work_focus",
                    "execute_time": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;07:30:00"
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Ergonomic office supplies",
                        "quantity": 1
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_10",
        instruction="""
        You want to plan a comprehensive emergency response system for the house. First, you want to check all smoke detectors, door sensors, and motion sensors for their current status and battery levels.
        You want to create a "safe_mode" scene that can be manually triggered to: turn off heater and AC and dishwasher.
        You want to set up a monthly reminder with id "monthly_emergency_test" on the 15th with note "Test all emergency systems, check batteries, and review emergency procedures" and high priority.
        """,
        actions=[
            Action(
                name="sensor_reader",
                kwargs={
                    "type": "sensor"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "safe_mode",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            },
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "monthly_emergency_test",
                        "target": {
                            "type": "note",
                            "text": "Test all emergency systems, check batteries, and review emergency procedures"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "high"
                        },
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_11",
        instruction="""
        You want to create a comprehensive health and wellness monitoring system for the family. First, you want to check Emily Smith's member information and her nursing background, then review all existing medication and health-related reminders.
        You want to create a new custom list called "family_health_tracker" with tags "health" and "wellness" that includes: "Check Olivia's peanut allergy medications", "Emily's penicillin allergy alert", add all of them once.
        "Monitor air quality for kids' respiratory health", and "Weekly family exercise planning".
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "emily_smith"
                }
            ),
            Action(
                name="search_engine",
                kwargs={
                    "search_term": "medication",
                    "search_type": "reminders"
                }
            ),
            Action(
                name="search_engine",
                kwargs={
                    "search_term": "allergy",
                    "search_type": "members"
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "create",
                    "list_data": {
                        "list_id": "family_health_tracker",

                        "tags": ["health", "wellness"],
                        "items": [
                            {
                                "item": "Check Olivia's peanut allergy medications",
                                "quantity": 1
                            },
                            {
                                "item": "Emily's penicillin allergy alert",
                                "quantity": 1
                            },
                            {
                                "item": "Monitor air quality for kids' respiratory health",
                                "quantity": 1
                            },
                            {
                                "item": "Weekly family exercise planning",
                                "quantity": 1
                            }
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_12",
        instruction="""
        You want to set up an advanced kitchen automation system for meal preparation and cooking efficiency. First, you want to check the current status of the dishwasher and any kitchen-related devices, then search for existing cooking or meal-related lists.
        You want to create a new scene called "cooking_preparation" that: sets the kitchen temperature to 20 degrees via the central heater to keep it cool during cooking, turns on all Living Room lights at 60% brightness for good visibility while moving between kitchen and dining,
        starts the dishwasher on auto cycle for pre-cooking cleanup, and turns off the AC to prevent interference with cooking aromas. You want to schedule this scene to run on 2025-07-25 at 17:30 PM for dinner preparation.
        You also want to create a weekly reminder with id "weekly_meal_planning" every Sunday at 11:00 AM for the weekend groceries list review.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "device_id": "dishwasher_kt"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="search_engine",
                kwargs={
                    "search_term": "groceries",
                    "search_type": "lists"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "cooking_preparation",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 20}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 60}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 60}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "on", "cycle": "auto"}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "cooking_preparation",
                    "execute_time": "2025-07-25T17:30:00"
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "weekly_meal_planning",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_groceries_weekend"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=11;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_13",
        instruction="""
        You want to create a comprehensive family coordination system for managing everyone's schedules and activities. First, you want to check the member information for all family members who live in the house, then review their individual schedules and preferences.
        You want to create a scene called "family_meeting_mode" that optimizes the Living Room for family discussions with ceiling light set to 75% brightness, floor light set to 50% brightness, heater set to 22 degrees, curtain set to 60% position, and dishwasher set to off.
        You also want to create a weekly reminder with id "weekly_family_schedule_review" every Saturday at 9:00 AM with note "Review and coordinate family schedules, school events, work commitments, and activities for the upcoming week" and normal priority.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "lives_in_house": True
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "family_meeting_mode",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 75}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 50}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 22}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 60}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "weekly_family_schedule_review",

                        "target": {
                            "type": "note",
                            "text": "Review and coordinate family schedules, school events, work commitments, and activities for the upcoming week"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_14",
        instruction="""
        You want to set up a reminder with id "daily_energy_review" daily at 18:00 with note "Review daily energy consumption and adjust device settings for optimal efficiency".
        You also want to create a weekly reminder with id "weekly_firmware_check" every Thursday at 8:00 PM with note "Check for device firmware updates that improve energy efficiency" and normal priority.
        You want to add one "Energy monitoring devices" and eight "LED light bulb replacements" to the shopping list for further energy savings.
        """,
        actions=[
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "daily_energy_review",
                        "target": {
                            "type": "note",
                            "text": "Review daily energy consumption and adjust device settings for optimal efficiency"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=18;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "weekly_firmware_check",

                        "target": {
                            "type": "note",
                            "text": "Check for device firmware updates that improve energy efficiency"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=TH;BYHOUR=20;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Energy monitoring devices",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "LED light bulb replacements",
                        "quantity": 8
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_15",
        instruction="""
        You want to create a scene called "smart_home_maintenance_schedule" with tags "maintenance", "backup", and "system" that includes: "Monthly sensor battery replacement", "Quarterly device firmware updates",
        "Semi-annual automation rule review", and "Annual system configuration backup".
        You also want to create a scene called "maintenance_mode" that can be manually triggered to: turn off heater and AC, turn off dishwasher, turn on all ceiling lights at 100% brightness, and turn off all devices; schedule to run on "2025-06-28T22:00:00-07:00".
        """,
        actions=[
            Action(
                name="list_manager",
                kwargs={
                    "action": "create",
                    "list_data": {
                        "list_id": "smart_home_maintenance_schedule",
                        "tags": ["maintenance", "backup", "system"],
                        "items": [
                            {
                                "item": "Monthly sensor battery replacement",
                                "quantity": 1
                            },
                            {
                                "item": "Quarterly device firmware updates",
                                "quantity": 1
                            },
                            {
                                "item": "Semi-annual automation rule review",
                                "quantity": 1
                            },
                            {
                                "item": "Annual system configuration backup",
                                "quantity": 1
                            }
                        ]
                    }
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "maintenance_mode",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 100}
                            },
                            {
                                "device_id": "light_br_ceiling",
                                "update": {"power": "on", "brightness": 100}
                            },
                            {
                                "device_id": "light_bw_ceiling",
                                "update": {"power": "on", "brightness": 100}
                            },
                            {
                                "device_id": "light_be_ceiling",
                                "update": {"power": "on", "brightness": 100}
                            }
                        ],
                        "scheduled_runs": [
                            "2025-06-28T22:00:00-07:00"
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_16",
        instruction="""
        You want to set up an intelligent sleep optimization system for the entire family based on their individual bedtimes.
        You want to create a scene called "family_sleep_optimization" that sets central heater to 19, master bedroom ceiling light to 10% brightness, west bedroom ceiling light to 10% brightness, and east bedroom ceiling light to 5% brightness.
        You also want to add "Sleep optimization supplies" to the shopping list and set up a weekly reminder id family_sleep every Sunday at 2:00 PM with note "Review and adjust family sleep schedules based on school and activity changes" and high priority.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "family_sleep_optimization",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "mode": "heat", "setpoint_c": 19}
                            },
                            {
                                "device_id": "light_br_ceiling",
                                "update": {"power": "on", "brightness": 10}
                            },
                            {
                                "device_id": "light_bw_ceiling",
                                "update": {"power": "on", "brightness": 5}
                            },
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Sleep optimization supplies",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "family_sleep",
                        "target": {
                            "type": "note",
                            "text": "Review and adjust family sleep schedules based on school and activity changes"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;IBYDAY=SA;BYHOUR=14;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "high"
                        },
                        "status": "active"
                    }
                }
            ),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_17",
        instruction="""
        You want to create a visitor management system for when Michael Brown (John's college friend) visits.
        You want to create a scene called "guest_comfort_mode" that can be manually activated to: optimize temperature at 22 degrees throughout the house, turn on all lights in living room at 55% brightness,
        and prepare quiet environment by ensuring dishwasher is off.
        You also want to set up a reminder 1 week before his next expected visit, that is, on 2025-08-15T10:00:00, with id "guest_visit_preparation" and note "Remember Michael's alergy: (put in his allergy)" and normal priority.
        You want to add 2 quantity of Michael's favorite food to the shopping list.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "michael_brown",
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "guest_comfort_mode",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 22}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"brightness": 55}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"brightness": 55}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "guest_visit_preparation",
                        "target": {
                            "type": "note",
                            "text": "Remember Michael's alergy: cat dander"
                        },
                        "trigger": {
                            "datetime": "2025-08-15T10:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Thai green curry",
                        "quantity": 2
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_18",
        instruction="""
        You want to create a weekly reminder every Saturday at 8:00 AM with id "weekly_cleaning_coordination" and note "Coordinate family cleaning tasks, check supply levels, and plan weekend housework" and normal priority.
        You want to add "Cleaning supplies restock" to the shopping list list_shopping.
        """,
        actions=[
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "weekly_cleaning_coordination",

                        "target": {
                            "type": "note",
                            "text": "Coordinate family cleaning tasks, check supply levels, and plan weekend housework"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=8;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Cleaning supplies restock",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_19",
        instruction="""
        You want to create a scene called "homework_focus_mode" to:
        set optimal study lighting in West Bedroom at 80% brightness for Olivia's homework, set East Bedroom lighting at 75% for Ethan's activities, and the heater to maintain comfortable 21-degree temperature for concentration the objective is Optimal study environment for children's after-school activities.
        You also want to add "Child safety equipment" and "Educational supplies" to the shopping list list_shopping.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "West Bedroom"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "East Bedroom"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "homework_focus_mode",
                        "actions": [
                            {
                                "device_id": "light_bw_ceiling",
                                "update": {"power": "on", "brightness": 80}
                            },
                            {
                                "device_id": "light_be_ceiling",
                                "update": {"power": "on", "brightness": 75}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 21}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Child safety equipment",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_20",
        instruction="""
        You want to prepare for the family's arrival from vacation.
        You want to create a scene called "family_arrival_preparation" that can be activated when the family returns from vacation to:
        turn on all lights in the living room at 60% brightness for welcoming ambiance, set the central heater to 22 degrees for comfort since they've been away,
        open Living Room curtains to 90% for natural light. You want to schedule this scene to run on 2025-08-04 at 14:00 PM when they arrive.
        You also want to add "Costco cake" to the shopping list list_shopping.
        """,
        actions=[
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "family_arrival_preparation",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 60}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 60}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "setpoint_c": 22}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 90}
                            }
                        ],
                        "scheduled_runs": ["2025-08-04T14:00:00-07:00"]
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Costco cake",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_21",
        instruction="""
        You want to prepare for Isabel Martinez's visit.
        You want to create a scene called "isabel_visit_preparation" that can be activated when Isabel visits to:
        set the central heater to 22 degrees for comfort since she's coming from a different climate,
        open Living Room curtains to 90% for natural light, and ensure the dishwasher is turned off.
        You want to schedule this scene to run on 2025-08-04 at 14:00 PM when she arrives.
        You want to add her favorite food to the shopping list list_shopping.
         """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "isabel_visit_preparation",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 22}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 90}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": ["2025-08-04T14:00:00"]
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "strawberry ice-cream",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_22",
        instruction="""
        You want to create a scene called "reading_time_family" that can be activated for family reading sessions to: increase all Living Room lighting to 75% brightness for clear reading visibility,
        open curtains to 70% position for natural reading light, maintain comfortable 21-degree temperature for extended concentration, turn off the dishwasher.
        You want to set up a weekly reminder every Friday at 5:00 PM with id "plan_weekend_entretaiment" and note "Plan weekend family entertainment activities and check entertainment device functionality" and normal priority.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen",
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Basement",
                }
            ),

            Action(
                name="search_engine",
                kwargs={
                    "search_term": "entertainment",
                    "search_type": "scenes"
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "plan_weekend_entretaiment",

                        "target": {
                            "type": "note",
                            "text": "Plan weekend family entertainment activities and check entertainment device functionality"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=17;BYMINUTE=00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "reading_time_family",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 75}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 75}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 70}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 21}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_23",
        instruction="""
        You want to turn the light off in the living room.
        You want to create a daily reminder at 6:45 AM on each weekday with id "morning_schedule_check" and note "Check family morning schedules and adjust wake-up timing for the day" and normal priority.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_floor",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "morning_schedule_check",

                        "target": {
                            "type": "note",
                            "text": "Check family morning schedules and adjust wake-up timing for the day"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=6;BYMINUTE=45"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_24",
        instruction="""
        You want to set up a scene called "optimal_health_environment" that can be activated to: maintain the ac at perfect temperature at 21 degrees for respiratory comfort,
        ensure optimal lighting at 70% brightness for lights in the living room for vitamin D synthesis and circadian rhythm support, balance humidity levels by coordinating heating and cooling systems,
        minimize air pollutants by turning off dust-generating appliances like the dishwasher, and create gentle air circulation with low-speed AC fan mode.
        You want to create a new shopping list with id "health_supplies" and add two "Air purification filter" and a "Health monitoring devices" to it.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "ac"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "optimal_health_environment",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 70}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 70}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"power": "on", "mode": "fan", "fan_speed": "low", "setpoint_c": 21}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "create",
                    "list_data": {
                        "list_id": "health_supplies",
                        "items": [
                            {"item": "Air purification filter", "quantity": 2},
                            {"item": "Health monitoring devices", "quantity": 1}
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_25",
        instruction="""
        You want to create a new list with id "family_fitness_goals" and add three items to it: "Daily family exercise 30 minutes", "Weekend outdoor activities", and "Monthly fitness progress review".
        You also want to create a weekly reminder every Sunday at 7:00 PM with id "weekly_fitness_plan" and note "plan family fitness activities and coordinate exercise schedules for the upcoming week" and normal priority.
        """,
        actions=[
            Action(
                name="list_manager",
                kwargs={
                    "action": "create",
                    "list_data": {
                        "list_id": "family_fitness_goals",

                        "items": [
                            {
                                "item": "Daily family exercise 30 minutes",
                                "quantity": 1
                            },
                            {
                                "item": "Weekend outdoor activities",
                                "quantity": 1
                            },
                            {
                                "item": "Monthly fitness progress review",
                                "quantity": 1
                            }
                        ]
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "weekly_fitness_plan",

                        "target": {
                            "type": "note",
                            "text": "plan family fitness activities and coordinate exercise schedules for the upcoming week"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=19;BYMINUTE=00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_26",
        instruction="""
        Mia is visiting.
        You want to create a scene called "guest_child_bedtime" that can be activated when Mia visits that:
        sets girls' rooms (West Bedroom) ceiling light to 30% brightness for social comfort, maintains the central heater at
        slightly warmer 25-degree temperature for visiting child adaptation.
        You also want to set up a weekly reminder every Tuesday at 7:00 PM to coordinate Wednesday
        playdate bedtime logistics with reminder id "playdate_bedtime_coordination" and note "Coordinate Mia's pickup time and adjust bedtime routine for Wednesday playdate" and normal priority.
        You want to add "Child-friendly sleep aids" for both childs to the shopping list.
        """,
        actions=[
            Action(
              name="device_manager",
              kwargs={
                "action":"get",
                "type": "light"
              }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "guest_child_bedtime",
                        "actions": [
                            {
                                "device_id": "light_bw_ceiling",
                                "update": {"power": "on", "brightness": 30}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 25}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "playdate_bedtime_coordination",

                        "target": {
                            "type": "note",
                            "text": "Coordinate Mia's pickup time and adjust bedtime routine for Wednesday playdate"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=TU;BYHOUR=19;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Child-friendly sleep aids",
                        "quantity": 2
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_27",
        instruction="""
        You want to set all lights in the living room to 100% brightness.
        You also want to set the central heater to 22 degrees for comfort.
        You also want to set the dishwasher to on and in eco mode.
        You also want to set the living room curtains to 25% position for privacy.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "dishwasher"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "curtain"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "dishwasher_kt",
                    "updates": {"power": "on", "mode": "eco"}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "curtain_lr",
                    "updates": {"position": 25}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "heater_home",
                    "updates": {"setpoint_c": 22}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "on", "brightness": 100}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_floor",
                    "updates": {"power": "on", "brightness": 100}
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_28",
        instruction="""
        If there is no motion detected in the front door camera, you want to set the scene "movie_time" to be activated now.
        Also, you want to turn off the lights in the west bedroom and east bedroom.
        """,
        actions=[
            Action(
                name="sensor_reader",
                kwargs={
                    "location": "Entrance"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "execute",
                    "scene_id": "movie_time"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "West Bedroom",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "East Bedroom",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_bw_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_29",
        instruction="""
        You want to create a scene called "storm_preparation_mode" that can be activated during severe weather to: ensure optimal indoor temperature at comfortable 21 degrees for extended indoor time,
        That means, you want to set the central heater to 21 degrees, set the living room lights to 80% brightness, close the living room curtains to 0% position, turn off the dishwasher.
        You want to create a daily reminder at 7:00 AM with id "daily_weather_adaptation" and note "Check weather forecast and adjust home climate settings for optimal comfort and efficiency" and normal priority.
        """,
        actions=[
            Action(
                name= "device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "curtain"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "dishwasher"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "storm_preparation_mode",


                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {"power": "on", "setpoint_c": 21}
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 80}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 80}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 0}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "daily_weather_adaptation",

                        "target": {
                            "type": "note",
                            "text": "Check weather forecast and adjust home climate settings for optimal comfort and efficiency"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=7;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_30",
        instruction="""
        David Lee and Sarah Lee are visiting on 2025-08-02.
        You want to add their favorite food to the shopping list, one quantity each.
        You also want to set up a reminder the day before their visit at 6:00 PM with id "guest_food_reminder" and note "Remind David and Sarah about their favorite food" and normal priority.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "david_lee"
                }
            ),
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "sarah_lee"
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "ramen",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "vegan tacos",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "guest_food_reminder",
                        "target": {
                            "type": "note",
                            "text": "Remind David and Sarah about their favorite food"
                        },
                        "trigger": {
                            "datetime": "2025-08-01T18:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_31",
        instruction="""
        You want to set up a simple morning coffee preparation routine for John Smith's 7:30 AM work start. First, you want to check John's member information and his morning schedule.
        You want to create a scene called "morning_coffee_routine" that activates at 7:15 AM weekdays to: turn on the kitchen and living room areas lights at 85% brightness for visibility,
        set the dishwasher to run a quick rinse cycle for fresh coffee mugs, and adjust room temperature to energizing 20 degrees.
        You want to add two "Premium coffee beans" and one "Coffee filters" to the shopping list for his daily routine.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "john_smith"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "device_id": "heater_home"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "morning_coffee_routine",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 85}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "on", "cycle": "quick"}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 20}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Premium coffee beans",
                        "quantity": 2
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Coffee filters",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_32",
        instruction="""
        You want to prepare a quick guest bathroom setup for when David Lee and Sarah Lee visit on Sundays. You want to check their member information and visit preferences.
        You want to create a scene called "guest_bathroom_ready" that can be activated before their 6:30 PM arrival to: turn on all Living Room lights at 70% brightness for welcoming ambiance,
        open Living Room curtains to 60% position for natural evening light, and set heater to 23 degrees.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "david_lee"
                }
            ),
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "sarah_lee"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "guest_bathroom_ready",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 70}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 70}
                            },

                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 60}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 23}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_33",
        instruction="""
        You want to create a simple grocery list management system for Emily Smith's weekend shopping trips. You want to check Emily's member information and the current list groceries weekend.
        You want to update the weekend groceries list to add 5 "Fresh vegetables" and 5 "Organic fruits" for healthy family meals, then create a scene called "shopping_prep"
        that can be activated before grocery runs to: turn on all lights at 75% brightness for list review, open curtains to 100% for natural light, and set comfortable 21-degree temperature.
        You want to set up a reminder every Friday at 6:00 PM to review and finalize the weekend shopping list.
        """,
        actions=[
            Action(
                name="member_manager",
                kwargs={
                    "action": "get",
                    "member_id": "emily_smith"
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "get",
                    "list_id": "list_groceries_weekend",
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Fresh vegetables",
                        "quantity": 5
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Organic fruits",
                        "quantity": 5
                    }
                }
            ),

            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "shopping_prep",


                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 75}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 100}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 21}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "friday_shopping_review",

                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_groceries_weekend"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=18;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_34",
        instruction="""
        You want to set up a basic device maintenance check system for the smart home. You want to check the current device status and search for any existing maintenance reminders.
        You want to create a scene called "maintenance_check_mode" that can be activated monthly to: turn on all lights at 100% brightness for device inspection visibility,
        ensure heating and cooling systems are at moderate 21-degree setting for technician comfort, and turn off the dishwasher to reduce noise during checks.
        You want to create a monthly reminder on the 15th at 2:00 PM to perform device maintenance checks and update the home maintenance checklist.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get"
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "get",
                    "reminder_id": "*"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "maintenance_check_mode",


                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 100}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 21}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "off"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "monthly_device_maintenance",

                        "target": {
                            "type": "note",
                            "text": "Perform monthly device maintenance checks and update maintenance records"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=15;BYHOUR=14;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="res_35",
        instruction="""
        You want to create a quick party mode setup for family celebrations and special occasions. You want to check the current Living Room device configuration and lighting settings.
        You want to set up a scene called "celebration_party_mode" that can be activated for parties to: increase all Living Room lighting to festive 85% brightness,
        set warm party temperature at 23 degrees for guest comfort, open curtains to 80% position for an open atmosphere, and ensure the dishwasher from kitchen is ready for post-party cleanup.
        You want to add "Party decorations" and "Celebration supplies" to the shopping list for future events.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "celebration_party_mode",


                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 85}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {"setpoint_c": 23}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 80}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "on", "cycle": "auto"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Party decorations",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_shopping",
                    "item_data": {
                        "item": "Celebration supplies",
                        "quantity": 1
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_36",
        instruction="""
        You want to decrease every item in the weekend groceries list (list_groceries_weekend) by 1 quantity since you already went on shopping and wouldn't need any.
        You also want to set up a reminder every Sunday at 7:00 PM to activate the scene "shopping_prep" and note "Prepare for the weekend shopping" and normal priority.
        """,
        actions=[
            Action(
                name="list_manager",
                kwargs={
                    "action": "get",
                    "list_id": "list_groceries_weekend"
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "update_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Chicken Breast",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "update_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Apples",
                        "quantity": 0
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "update_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Olive Oil",
                        "quantity": 0
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "update_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Cheese",
                        "quantity": 0
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "update_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Eggs",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "weekly_shopping_prep",
                        "target": {
                            "type": "note",
                            "text": "Prepare for the weekend shopping"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=19;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_37",
        instruction="""
        You want to create a scene called "party_mode" that can be activated for parties to: increase all Living Room lighting to festive 85% brightness,
        set heater to 23 degrees for guest comfort, open curtains to 80% position for an open atmosphere, and ensure the dishwasher is put on auto cycle.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="scene_manager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "party_mode",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {"power": "on", "brightness": 85}
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 85}
                            },
                            {
                                "device_id": "heater_home",
                                "update": {"setpoint_c": 23}
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {"position": 80}
                            },
                            {
                                "device_id": "dishwasher_kt",
                                "update": {"power": "on", "cycle": "auto"}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        You want to make sure kids get rest by 10:00 PM on weekdays. To do so, every weekday you want to schedule the heater to 20 degrees at 10:00 PM.
        You also want to turn off the ceiling lights in the west bedroom and east bedroom at that time.
        This change starts on 2025-07-29.
        """,
        actions=[
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_bw_ceiling",
                    "updates": {"power": "off"},
                    "schedule_updates": {
                        "timestamp": "2025-07-29T22:00:00",
                        "update": {"power": "off"},
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=22;BYMINUTE=0"
                    }
                }
            ),
            Action(
                name="device_manager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"},
                    "schedule_updates": {
                        "timestamp": "2025-07-29T22:00:00",
                        "update": {"power": "off"},
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=22;BYMINUTE=0"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_39",
        instruction="""
        You need to create a reminder with id "daily_weather_adaptation" and note "Check weather forecast and adjust home climate settings for optimal comfort and efficiency" and normal priority.
        This reminder should be triggered every day at 7:00 AM with high priority and notify via email.
        """,
        actions=[
            Action(
                name="reminder_manager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "daily_weather_adaptation",
                        "target": {
                            "type": "note",
                            "text": "Check weather forecast and adjust home climate settings for optimal comfort and efficiency"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=7;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "email"
                            }
                        ],
                        "meta": {
                            "priority": "high"
                        },
                        "status": "active"
                    }
                }
            )
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="res_40",
        instruction="""
        You need to create a weekend grocery list with 3 of Eggs and 1 of Strawberries.
        If there already exists a weekend grocery list, just update the list with the new items.
        If eggs or strawberries are already in the list, just update the quantity to 3 and 1 respectively.
        """,
        actions=[
            Action(
                name="list_manager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "remove_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Eggs",
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Strawberries",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="list_manager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Eggs",
                        "quantity": 3
                    }
                }
            )
        ],
        outputs=[]
    ),
]
