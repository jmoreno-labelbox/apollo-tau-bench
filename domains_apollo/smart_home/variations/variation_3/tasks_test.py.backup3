from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        Initiate an automated morning schedule for Robert Johnson, who rises at 6:30 AM on weekdays.
        Begin by retrieving Robert's existing member details and his room allocation. Proceed to compose a scene named "john_morning_routine"
        that activates at 6:30 AM on weekdays. Within this scene: illuminate the Master Bedroom ceiling light at 60% intensity,
        unveil the Master Bedroom curtain fully, adjust the central heater located in the basement to 22 degrees Celsius in heating mode,
        and schedule a notification reminding Robert to take his medication at 7:00 AM with high importance via mobile push alerts.
        Additionally, review the current status of all devices in the Master Bedroom prior to establishing the automation.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "john_johnson"
                }
            ),
            Action(
                name="RoomManager",
                kwargs={
                    "action": "get",
                    "room_id": "bedroom_master"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Master Bedroom"
                }
            ),
            Action(
                name="RoomManager",
                kwargs={
                    "action": "get",
                    "room_id": "basement"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "basement"
                }
            ),
            Action(
                name="SceneManager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "john_morning_routine",
                        "description": "Robert's morning routine",
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
                name="ReminderManager",
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
        Jessica Johnson is employed part-time at Memorial Medical Center on Monday, Tuesday, and Wednesday starting from 7:00. She is currently at work.
        Optimize energy consumption during her working hours. Locate all devices now in the Master Bedroom where Jessica resides,
        then organize a bulk action to switch off all lights in the Master Bedroom.
        Also, set the central AC (from the Living Room) to 26 degrees Celsius.
        Develop a new scene named "emily_work_energy_save" with the description "Energy saving mode during Emily's work hours" and actions including the three aforementioned device adjustments.
        Schedule this scene to automatically initiate next Monday (2025-07-28) at 7:00 AM.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Master Bedroom",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "ac"
                }
            ),
            Action(
                name="BulkOperator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"location": "Master Bedroom", "type": "light"},
                    "updates": {"power": "off", "brightness": 0}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "ac_home",
                    "state_updates": {"power": "on", "mode": "cool", "setpoint_c": 26}
                }
            ),
            Action(
                name="SceneManager",
                kwargs={
                    "action": "create",
                    "scene_data": {
                        "id": "emily_work_energy_save",
                        "description": "Energy saving mode during Jessica's work hours",
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
                name="SceneManager",
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
        You need to establish a comprehensive security system for when the family goes on vacation.
        A scene named "vacation_security_mode" should be created to activate when the front door sensor identifies it's been shut for over 2 hours.
        The scene is required to: switch off all lights except those in the Living Room set at 30% brightness for security, close all curtains completely to 0% position,
        and turn off both the heater and AC. Additionally, you should add 4 "Security camera batteries" to the current shopping list.
        """,
        actions=[
            Action(
                name="SensorReader",
                kwargs={
                    "type": "sensor"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="ListManager",
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
        Linda Johnson (Grandma) is visiting on 2025-08-04 and needs wheelchair accessibility. She is 70 years old and has specific requirements.
        Initially, find Linda's member information and visit preferences. Then verify the status of all devices on the first
        floor, where she will spend most of her time.
        Create a scene titled "grandma_visit_comfort" that: adjusts the Living Room temperature to 24 degrees using the central heater,
        located in the basement, turns on the Living Room ceiling light to 80% brightness, opens the Living Room curtains to 100% for natural light,
        and turns off the dishwasher to lower noise. Schedule this scene for 2025-08-04 at 14:00 PM when she typically arrives.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "linda_johnson"
                }
            ),
            Action(
                name="RoomManager",
                kwargs={
                    "action": "get",
                    "floor": 1
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Basement"
                }
            ),

            Action(
                name="SceneManager",
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
                name="SceneManager",
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
        Devise an elaborate bedtime protocol for both children - Emma Johnson (9 years old, West Bedroom, bedtime 20:30) and Ethan Smith (6 years old, East Bedroom, bedtime 20:00).
        Formulate a harmonized scene named "kids_bedtime_prep" that parents can manually activate 30 minutes before bedtime to Prepare house for kids bedtime to:
        adjust the central heater to 20 degrees for optimal sleep conditions and shut off all electronic devices in the Living Room for tranquil hours.
        Establish a recurring reminder for parents every Sunday at 7:00 PM with the note "Review and adjust the kids' bedtime routines, and check the air quality sensor in the Living Room to ensure it's healthy for the kids.".
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "olivia_johnson"
                }
            ),
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "ethan_johnson"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
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
        Christopher Chen and Jennifer Chen arrive every Sunday evening at 6:30 PM for dinner. Michael is allergic to shellfish and Jennifer brings homemade sourdread.
        Arrange the house for their customary visit. Start by confirming their member information and visit preferences, then obtain the current status
        of all devices in the Living Room and Kitchen areas. Construct a new scene titled "sunday_dinner_prep" that: sets the Living Room temperature
        to 23 degrees Celsius via the heater in the basement, activates both Living Room lights (ceiling at 70% and floor lamp at 40%),
        fully opens Living Room curtains,
        and initiates the dishwasher on auto cycle for cleanup after dinner. Schedule this scene for the upcoming Sunday (2025-07-27) at 6:00 PM.
        Implement a shopping prompt that triggers every Saturday at 10:00 AM to purchase ingredients for Sunday dinner, ensuring shellfish is avoided due to Michael's allergy.
        Update Jennifer's member record to document that she brings sourdough bread and fresh herbs from her garden, and append "Sunday dinner ingredients (no shellfish)" to the weekend groceries list.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "david_chen"
                }
            ),
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "sarah_chen"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Basement"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="SceneManager",
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
                name="SceneManager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "sunday_dinner_prep",
                    "execute_time": "2025-07-27T18:00:00"
                }
            ),
            Action(
                name="ReminderManager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "sunday_dinner_shopping",

                        "target": {
                            "type": "note",
                            "text": "Buy ingredients for Sunday dinner with Michael and Jennifer (no shellfish due to Michael's allergy)"
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
                name="MemberManager",
                kwargs={
                    "action": "update",
                    "member_id": "sarah_chen",
                    "field_updates": {
                        "visit_preferences.brings": ["homemade sourdough", "fresh herbs from garden"]
                    }
                }
            ),
            Action(
                name="ListManager",
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
        Aim to establish a detailed home maintenance system.
        Proceed to create a new custom list titled "home_maintenance_checklist" incorporating tags "maintenance" and "house" with items: "Replace smoke detector batteries", "Clean air quality sensor filters",
        "Check door sensor alignment", and "Test motion sensor coverage".
        Schedule a monthly reminder on the 1st at 9:00 AM to review the maintenance checklist and verify all device firmware versions.
        Conclude by bulk updating all sensors with battery levels below 90% to include a note in their metadata indicating the need for attention, and export all sensor data for maintenance records.
        """,
        actions=[
            Action(
                name="SearchEngine",
                kwargs={
                    "search_term": "maintenance",
                    "search_type": "reminders"
                }
            ),
            Action(
                name="ListManager",
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
                name="ReminderManager",
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
                name="StatusMonitor",
                kwargs={
                    "report_type": "detailed",
                    "category": "devices"
                }
            ),
            Action(
                name="DataPorter",
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
        Tonight is family movie night, and you wish to establish the optimal entertainment setting. Start by reviewing the current "Movie Time" scene along with its actions,
        followed by checking the status of all devices in the Living Room. Proceed to create an upgraded version named "movie_night_deluxe" that: closes Living Room curtains to 0% for complete darkness,
        dims the Living Room ceiling light to 15% and sets the floor lamp to 25% for ambient lighting, regulates the AC to 22 degrees,
        and switches off the dishwasher to avoid noise. Initiate a bulk operation to switch off all non-essential lights in other areas, namely: West Bedroom, East Bedroom, Kitchen
        to conserve electricity during movie time. Set up a reminder for 30 minutes into typical movie time (8:30 PM) to see if anyone requires snacks,
        and add "Movie night snacks" and "Popcorn" to the weekend groceries list. Schedule the enhanced scene for tonight at 7:45 PM.
        """,
        actions=[
            Action(
                name="SceneManager",
                kwargs={
                    "action": "get",
                    "scene_id": "scene_movie_time"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="SceneManager",
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
                name="BulkOperator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"type": "light", "location":"West Bedroom"},
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="BulkOperator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"type": "light", "location":"East Bedroom"},
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="BulkOperator",
                kwargs={
                    "operation": "bulk_state_update",
                    "target_type": "devices",
                    "filters": {"type": "light", "location":"Kitchen"},
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="SceneManager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "movie_night_deluxe",
                    "execute_time": "2025-07-30T19:45:00"
                }
            ),
            Action(
                name="ReminderManager",
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
                name="ListManager",
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
                name="ListManager",
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
        Robert Johnson works from home and you aim to establish an optimized office environment. Begin by locating Robert's work schedule and occupation specifics, followed by inspecting all devices in the Master Bedroom, his workspace.
        Initiate the creation of a new scene titled "john_work_focus" which will: adjust the room temperature to 21 degrees using the basement heater for optimal focus, set the Master Bedroom ceiling light to 85% brightness for adequate visibility,
        position the curtains at 75% for natural light without glare, and switch off the night lamp to avoid distractions. Schedule this scene to activate every Monday through Friday at 7:30 AM, coinciding with his work commencement.
        Include "Ergonomic office supplies" in the shopping list to enhance his workspace.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "john_johnson"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Master Bedroom"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Basement"
                }
            ),
            Action(
                name="SensorReader",
                kwargs={
                    "sensor_id": "sensor_lr_air_quality"
                }
            ),
            Action(
                name="SceneManager",
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
                name="SceneManager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "john_work_focus",
                    "execute_time": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;07:30:00"
                }
            ),
            Action(
                name="ListManager",
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
        Your objective is to develop a comprehensive emergency response system for the house. Initially, review all smoke detectors, door sensors, and motion sensors to determine their current status and check battery levels.
        Create a "safe_mode" scene that can be manually activated to: switch off the heater, AC, and dishwasher.
        Arrange a monthly reminder with id "monthly_emergency_test" on the 15th with the note "Test all emergency systems, check batteries, and review emergency procedures" and assign it high priority.
        """,
        actions=[
            Action(
                name="SensorReader",
                kwargs={
                    "type": "sensor"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
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
        Aim to develop a detailed health and wellness tracking system for the family. Begin by verifying Jessica Johnson's member details and reviewing her nursing credentials, then assess all current medication and health-related alerts.
        Proceed to establish a new custom list titled "family_health_tracker" with tags "health" and "wellness" to encompass: "Check Emma's peanut allergy medications", "Emily's penicillin allergy alert", incorporate them all at once.
        "Monitor air quality for kids' respiratory health", and "Weekly family exercise planning".
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "emily_johnson"
                }
            ),
            Action(
                name="SearchEngine",
                kwargs={
                    "search_term": "medication",
                    "search_type": "reminders"
                }
            ),
            Action(
                name="SearchEngine",
                kwargs={
                    "search_term": "allergy",
                    "search_type": "members"
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "create",
                    "list_data": {
                        "list_id": "family_health_tracker",

                        "tags": ["health", "wellness"],
                        "items": [
                            {
                                "item": "Check Emma's peanut allergy medications",
                                "quantity": 1
                            },
                            {
                                "item": "Jessica's penicillin allergy alert",
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
        Set up an advanced kitchen automation system to enhance meal preparation and cooking efficiency. Start by examining the current status of the dishwasher and related kitchen devices, then locate any existing lists related to cooking or meals.
        Proceed to organize a new scene called "cooking_preparation" that: adjusts the kitchen temperature to 20 degrees via the central heater for a cool environment during cooking, illuminates all Living Room lights at 60% brightness for clear navigation between kitchen and dining,
        initiates the dishwasher on auto cycle for pre-cooking clean-up, and deactivates the AC to avoid conflicting with cooking aromas. Arrange for this scene to activate on 2025-07-25 at 17:30 PM for dinner preparation.
        Additionally, you wish to establish a weekly reminder identified as "weekly_meal_planning" every Sunday at 11:00 AM for reviewing the weekend groceries list.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "device_id": "dishwasher_kt"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="SearchEngine",
                kwargs={
                    "search_term": "groceries",
                    "search_type": "lists"
                }
            ),
            Action(
                name="SceneManager",
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
                name="SceneManager",
                kwargs={
                    "action": "schedule",
                    "scene_id": "cooking_preparation",
                    "execute_time": "2025-07-25T17:30:00"
                }
            ),
            Action(
                name="ReminderManager",
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
        Initiate the establishment of a detailed family coordination system to oversee everyone's schedules and activities. Begin by examining the member information for all family inhabitants, followed by reviewing their personal schedules and preferences.
        Develop a scene named "family_meeting_mode" to enhance the Living Room for family discussions, with ceiling light adjusted to 75% brightness, floor light to 50% brightness, heater to 22 degrees, curtain to 60% position, and dishwasher turned off.
        Arrange for a weekly reminder with id "weekly_family_schedule_review" every Saturday at 9:00 AM, with a note "Review and coordinate family schedules, school events, work commitments, and activities for the upcoming week" and set it to normal priority.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "lives_in_house": True
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
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
        Arrange a reminder with id "daily_energy_review" to occur daily at 18:00, accompanied by the note "Review daily energy consumption and adjust device settings for optimal efficiency".
        Additionally, establish a weekly reminder with id "weekly_firmware_check" to take place every Thursday at 8:00 PM, featuring the note "Check for device firmware updates that improve energy efficiency" and assign normal priority.
        Include one "Energy monitoring devices" and eight "LED light bulb replacements" in the shopping list to promote energy savings.
        """,
        actions=[
            Action(
                name="ReminderManager",
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
                name="ReminderManager",
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
                name="ListManager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="ListManager",
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
                name="ListManager",
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
        Aim to establish a scene named "smart_home_maintenance_schedule" with the tags "maintenance", "backup", and "system" involving: "Monthly sensor battery replacement", "Quarterly device firmware updates",
        "Semi-annual automation rule review", and "Annual system configuration backup".
        Additionally, plan to create a scene titled "maintenance_mode" which can be manually activated to: disable heater and AC, switch off the dishwasher, illuminate all ceiling lights at 100% brightness, and power down all devices; schedule this for "2025-06-28T22:00:00-07:00".
        """,
        actions=[
            Action(
                name="ListManager",
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
                name="DeviceManager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="SceneManager",
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
        Intend to configure a smart sleep optimization system for the entire family, considering each individual's bedtime.
        Establish a scene called "family_sleep_optimization" that adjusts the central heater to 19, the master bedroom ceiling light to 10% brightness, the west bedroom ceiling light to 10% brightness, and the east bedroom ceiling light to 5% brightness.
        Furthermore, intend to include "Sleep optimization supplies" on the shopping list and set up a weekly reminder with the id family_sleep every Sunday at 2:00 PM, containing the note "Review and adjust family sleep schedules based on school and activity changes" and marked with high priority.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
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
                name="ReminderManager",
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
        Plan to develop a visitor management system for Christopher Wilson (Robert's college friend) when he comes over.
        Create a scene termed "guest_comfort_mode" that can be activated manually to: set the house temperature to 22 degrees, illuminate all living room lights at 55% brightness,
        and ensure a quiet ambiance by turning off the dishwasher.
        Schedule a reminder for 1 week prior to his anticipated visit, that is, on 2025-08-15T10:00:00, with id "guest_visit_preparation" and note "Remember Michael's allergy: (put in his allergy)" with normal priority.
        Add 2 quantity of Christopher's favorite food to the shopping list.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "michael_wilson",
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "guest_visit_preparation",
                        "target": {
                            "type": "note",
                            "text": "Remember Christopher's alergy: cat dander"
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
                name="ListManager",
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
        Arrange a weekly reminder for each Saturday at 8:00 AM with id "weekly_cleaning_coordination" and note "Coordinate family cleaning tasks, check supply levels, and plan weekend housework" with normal priority.
        Include "Cleaning supplies restock" in the list_shopping shopping list.
        """,
        actions=[
            Action(
                name="ReminderManager",
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
                name="ListManager",
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
        Initiate the creation of a scene titled "homework_focus_mode" to:
        adjust study lighting in West Bedroom to 80% brightness for Emma's homework, configure East Bedroom lighting to 75% for Ethan's activities, and set the heater to maintain a steady 21-degree temperature for better focus. The goal is to provide an optimal study environment for the children's after-school tasks.
        Additionally, include "Child safety equipment" and "Educational supplies" in the shopping list list_shopping.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "West Bedroom"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "East Bedroom"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
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
        Prepare for the family's homecoming from their vacation.
        Design a scene named "family_arrival_preparation" that will activate upon the family's return from vacation to:
        illuminate all lights in the living room at a 60% brightness to create a welcoming atmosphere, set the central heater to 22 degrees for comfort after their absence,
        and open Living Room curtains to 90% for ample natural light. Plan this scene to activate on 2025-08-04 at 14:00 PM for their arrival.
        Furthermore, you wish to incorporate "Costco cake" into the shopping list list_shopping.
        """,
        actions=[
            Action(
                name="SceneManager",
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
                name="ListManager",
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
        Prepare accordingly for Isabel Martinez's visit.
        Create a scene titled "isabel_visit_preparation" that will be activated during Isabel's visit to:
        adjust the central heater to 22 degrees for her comfort since she's coming from a different climate,
        open the Living Room curtains to 90% to allow natural light, and ensure the dishwasher is turned off.
        Schedule this scene to operate on 2025-08-04 at 14:00 PM upon her arrival.
        Add her favorite food to the shopping list list_shopping.
         """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
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
        Develop a scene called "reading_time_family" to initiate during family reading sessions to: elevate all Living Room lighting to 75% brightness for optimal reading visibility,
        adjust curtains to 70% position for natural reading light, maintain a comfortable 21-degree temperature for extended concentration, and turn off the dishwasher.
        Set up a weekly reminder every Friday at 5:00 PM with id "plan_weekend_entretaiment" and note "Plan weekend family entertainment activities and check entertainment device functionality" with normal priority.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen",
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Basement",
                }
            ),

            Action(
                name="SearchEngine",
                kwargs={
                    "search_term": "entertainment",
                    "search_type": "scenes"
                }
            ),
            Action(
                name="ReminderManager",
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
                name="SceneManager",
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
        Handle turning off the light in the living room.
        Coordinate creating a daily reminder at 6:45 AM for each weekday with id "morning_schedule_check" and note "Check family morning schedules and adjust wake-up timing for the day" and normal priority.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_floor",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="ReminderManager",
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
        Arrange the setting up of a scene titled "optimal_health_environment" that allows activation to: maintain the AC at an ideal temperature of 21 degrees for respiratory comfort,
        ensure optimal lighting set at 70% brightness for lights in the living room to support vitamin D synthesis and circadian rhythm, balance humidity levels by managing heating and cooling systems,
        minimize air pollutants by turning off dust-generating appliances like the dishwasher, and facilitate gentle air circulation with low-speed AC fan mode.
        Organize the creation of a new shopping list with id "health_supplies" and include two "Air purification filter" and a "Health monitoring devices" to it.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "ac"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
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
        Handle the creation of a new list with id "family_fitness_goals" and incorporate three items: "Daily family exercise 30 minutes", "Weekend outdoor activities", and "Monthly fitness progress review".
        Additionally, set up a weekly reminder every Sunday at 7:00 PM with id "weekly_fitness_plan" and note "plan family fitness activities and coordinate exercise schedules for the upcoming week" and assign it normal priority.
        """,
        actions=[
            Action(
                name="ListManager",
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
                name="ReminderManager",
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
        Sofia is visiting.
        Coordinate the setup of a scene titled "guest_child_bedtime" for activation during Sofia's visit that:
        adjusts girls' rooms (West Bedroom) ceiling light to 30% brightness for social comfort and keeps the central heater at a slightly warmer 25-degree temperature suitable for a visiting child.
        Moreover, organize a weekly reminder every Tuesday at 7:00 PM to coordinate Wednesday
        playdate bedtime logistics with reminder id "playdate_bedtime_coordination" and note "Coordinate Sofia's pickup time and adjust bedtime routine for Wednesday playdate" and normal priority.
        Include "Child-friendly sleep aids" for both children in the shopping list.
        """,
        actions=[
            Action(
              name="DeviceManager",
              kwargs={
                "action":"get",
                "type": "light"
              }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "playdate_bedtime_coordination",

                        "target": {
                            "type": "note",
                            "text": "Coordinate Sofia's pickup time and adjust bedtime routine for Wednesday playdate"
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
                name="ListManager",
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
        Adjust all lights in the living room to maximum brightness of 100%.
        Additionally, configure the central heater to 22 degrees for comfort.
        Turn on the dishwasher and set it to eco mode as well.
        Set the living room curtains to 25% position to ensure privacy.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "dishwasher"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "curtain"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "dishwasher_kt",
                    "updates": {"power": "on", "mode": "eco"}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "curtain_lr",
                    "updates": {"position": 25}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "heater_home",
                    "updates": {"setpoint_c": 22}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "on", "brightness": 100}
                }
            ),
            Action(
                name="DeviceManager",
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
        If no motion is detected by the front door camera, activate the "movie_time" scene immediately.
        Moreover, switch off the lights in both the west bedroom and the east bedroom.
        """,
        actions=[
            Action(
                name="SensorReader",
                kwargs={
                    "location": "Entrance"
                }
            ),
            Action(
                name="SceneManager",
                kwargs={
                    "action": "execute",
                    "scene_id": "scene_movie_time"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "West Bedroom",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "East Bedroom",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_bw_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "update_state",
                    "device_id": "light_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="DeviceManager",
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
        Initiate the creation of a scene labeled "storm_preparation_mode" for activation during severe weather events to: maintain an optimal indoor temperature at a comfortable 21 degrees for prolonged indoor stays.
        Therefore, configure the central heater to 21 degrees, adjust the living room lights to 80% brightness, set the living room curtains to fully closed (0% position), and switch off the dishwasher.
        Schedule a daily reminder at 7:00 AM with id "daily_weather_adaptation" and note "Check weather forecast and adjust home climate settings for optimal comfort and efficiency" with normal priority.
        """,
        actions=[
            Action(
                name= "DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "curtain"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "dishwasher"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
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
        Christopher Chen and Jennifer Chen are planning to visit on 2025-08-02.
        Add their preferred food items to the shopping list, ensuring one quantity each.
        Additionally, set up a reminder for the day prior to their visit at 6:00 PM with id "guest_food_reminder" and note "Remind Michael and Jennifer about their favorite food" maintaining normal priority.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "david_chen"
                }
            ),
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "sarah_chen"
                }
            ),
            Action(
                name="ListManager",
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
                name="ListManager",
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
                name="ReminderManager",
                kwargs={
                    "action": "create",
                    "reminder_data": {
                        "reminder_id": "guest_food_reminder",
                        "target": {
                            "type": "note",
                            "text": "Remind Michael and Jennifer about their favorite food"
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
        Initiate a straightforward morning coffee preparation plan for Robert Johnson's 7:30 AM start at work. Begin by reviewing Robert's member details and his morning timetable.
        Create a scene named "morning_coffee_routine" to trigger at 7:15 AM on weekdays, which will: illuminate the kitchen and living room areas to 85% brightness for clear visibility,
        initiate the dishwasher for a quick rinse cycle to prepare fresh coffee mugs, and set the room temperature to an invigorating 20 degrees.
        Incorporate two "Premium coffee beans" and one "Coffee filters" into the shopping list for his daily needs.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "john_johnson"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "device_id": "heater_home"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
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
                name="ListManager",
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
        Arrange for a swift guest bathroom setup in anticipation of Christopher Chen and Jennifer Chen's Sunday visits. Evaluate their member details and visit preferences.
        Design a scene titled "guest_bathroom_ready" to be activated before their 6:30 PM arrival, which will: adjust all Living Room lights to 70% brightness for a welcoming atmosphere,
        draw Living Room curtains to 60% position to allow natural evening light, and adjust the heater to 23 degrees.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "david_chen"
                }
            ),
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "sarah_chen"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="SceneManager",
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
        Handle a straightforward grocery list management system for Jessica Johnson's weekend shopping excursions. Check Jessica's membership details and her current weekend grocery list.
        Update the weekend grocery list by adding 5 "Fresh vegetables" and 5 "Organic fruits" for nutritious family meals, then establish a scene named "shopping_prep"
        to be activated before grocery trips: set all lights to 75% brightness for list examination, fully open curtains to enhance natural light, and maintain a cozy 21-degree temperature.
        Schedule a reminder every Friday at 6:00 PM for reviewing and finalizing the weekend shopping list.
        """,
        actions=[
            Action(
                name="MemberManager",
                kwargs={
                    "action": "get",
                    "member_id": "emily_johnson"
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "get",
                    "list_id": "list_groceries_weekend",
                }
            ),
            Action(
                name="ListManager",
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
                name="ListManager",
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
                name="SceneManager",
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
                name="ReminderManager",
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
        Coordinate a fundamental device maintenance check system for the smart home. Review the current device status and look for any pre-existing maintenance reminders.
        Set up a scene titled "maintenance_check_mode" to activate on a monthly basis, ensuring: all lights are at full 100% brightness for optimal device inspection,
        the heating and cooling systems are at a moderate 21-degree setting for technician ease, and the dishwasher is turned off to minimize noise during inspections.
        Arrange for a monthly reminder on the 15th at 2:00 PM to handle device maintenance checks and update the home maintenance checklist.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get"
                }
            ),
            Action(
                name="ReminderManager",
                kwargs={
                    "action": "get",
                    "reminder_id": "*"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ReminderManager",
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
        Ensure a prompt party mode setup to use for family gatherings and special events. Verify the existing Living Room device configuration and lighting settings.
        Establish a scene titled "celebration_party_mode" to activate during parties aiming to: elevate all Living Room lighting to a festive 85% brightness,
        maintain a warm party temperature of 23 degrees for guest comfort, draw back curtains to 80% position for an open ambiance, and confirm that the kitchen dishwasher is ready for post-party cleaning.
        Include "Party decorations" and "Celebration supplies" in the shopping list for upcoming events.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Kitchen"
                }
            ),
            Action(
                name="SceneManager",
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
                name="ListManager",
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
                name="ListManager",
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
        Reduce each item on the weekend groceries list (list_groceries_weekend) by 1 quantity since you've already completed your shopping and will not require more.
        Set a reminder for every Sunday at 7:00 PM to trigger the scene "shopping_prep" and note "Prepare for the weekend shopping" with normal priority.
        """,
        actions=[
            Action(
                name="ListManager",
                kwargs={
                    "action": "get",
                    "list_id": "list_groceries_weekend"
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Chicken Breast",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Apples",
                        "quantity": 0
                    }
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Olive Oil",
                        "quantity": 0
                    }
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Cheese",
                        "quantity": 0
                    }
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "add_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Eggs",
                        "quantity": 1
                    }
                }
            ),
            Action(
                name="ReminderManager",
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
        Handle the creation of a scene called "party_mode" which can be triggered for parties to: elevate all Living Room lighting to a celebratory 85% brightness,
        adjust the heater to 23 degrees for guest comfort, position curtains to 80% open for an inviting atmosphere, and ensure the dishwasher is set to auto cycle.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "location": "Living Room",
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="SceneManager",
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
        Coordinate activities to ensure kids get rest by 10:00 PM on weekdays. To achieve this, every weekday you want to program the heater to 20 degrees at 10:00 PM.
        Additionally, you want to switch off the ceiling lights in the west bedroom and east bedroom at that time.
        This adjustment begins on 2025-07-29.
        """,
        actions=[
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "heater"
                }
            ),
            Action(
                name="DeviceManager",
                kwargs={
                    "action": "get",
                    "type": "light"
                }
            ),
            Action(
                name="DeviceManager",
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
                name="DeviceManager",
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
        Handle the creation of a reminder with id "daily_weather_adaptation" and note "Check weather forecast and adjust home climate settings for optimal comfort and efficiency" maintaining normal priority.
        Ensure this reminder activates daily at 7:00 AM with high priority and sends a notification via email.
        """,
        actions=[
            Action(
                name="ReminderManager",
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
        Organize a weekend grocery list including 3 of Eggs and 1 of Strawberries.
        If a weekend grocery list is already present, simply enhance it with the new items.
        Should eggs or strawberries be listed, adjust the quantities to 3 and 1 respectively.
        """,
        actions=[
            Action(
                name="ListManager",
                kwargs={
                    "action": "get",
                }
            ),
            Action(
                name="ListManager",
                kwargs={
                    "action": "remove_item",
                    "list_id": "list_groceries_weekend",
                    "item_data": {
                        "item": "Eggs",
                    }
                }
            ),
            Action(
                name="ListManager",
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
                name="ListManager",
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
