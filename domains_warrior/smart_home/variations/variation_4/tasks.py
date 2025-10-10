from domains.dto import Task, Action

TASKS = [
    # Task 1 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        You want to set up your new TP-Link Kasa HS110 smart plug for the coffee maker in the kitchen, so you can have coffee ready when you wake up.
        You want to configure the plug with the ID "plug_kt_coffee" and the name "Kitchen Coffee Maker Plug". It's a TP-Link Kasa HS110 model with firmware 1.0.0, and it should track power and energy consumption. Its initial state is 'off' with zero energy usage.
        After adding the device, you want to add it to the kitchen's device list and schedule it to turn on automatically at 6:45 AM every morning.
        To ensure safety, you want to check the current state of the plug before making any changes, and if the plug is already on, turn it off before scheduling the automation.
        Additionally, you want to create a shopping list called "Coffee Supplies" (ID "list_coffee_supplies") with the following items: 1 pack of coffee beans, 1 bottle of milk, and 1 box of filters. You want a reminder (ID "rem_coffee_supplies_check") to check this list every Saturday at 10 AM.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "plug_kt_coffee",
                        "type": "outlet",

                        "location": "Kitchen",
                        "vendor": "TP-Link",
                        "model": "HS110",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "energy_kwh"],
                        "state": {
                            "power": "off",
                            "energy_kwh": 0,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "kitchen",
                    "device_id": "plug_kt_coffee"
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "plug_kt_coffee",
                    "updates": {
                        "power": "off"
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "plug_kt_coffee",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on"},
                                "rrule": "FREQ=DAILY;BYHOUR=6;BYMINUTE=45"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_coffee_supplies",
                        "items": [
                            {"item": "Coffee beans (pack)", "quantity": 1},
                            {"item": "Milk (bottle)", "quantity": 1},
                            {"item": "Filters (box)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_coffee_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_coffee_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 2 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_02",
        instruction="""
        You want to replace a broken desk lamp (ID "lamp_bw_desk") in your daughter's room, the West Bedroom.
        You want to remove the old lamp from both the room's device list and the main inventory, and ensure it is powered off before removal.
        Next, you want to set up the new lamp, an Ikea Nymåne LED model, with the ID "lamp_bw_desk2" and the name "West Bedroom New Desk Lamp". It supports brightness and color temperature adjustments, and its initial state is 'off' with 0 brightness and a color temperature of 4000K.
        You want to add the new lamp to the West Bedroom's device list and include it in the "Good Night" scene. As part of the scene, it should turn on at 15% brightness with a warm color (hue 30).
        Additionally, you want to create a shopping list called "Desk Lamp Replacement Supplies" (ID "list_desk_lamp_supplies") with the following items: 1 Ikea Nymåne LED lamp, 1 spare LED bulb, and 1 pack of cable ties.
        Finally, set a reminder (ID "rem_check_lamp_install") to check the installation and cable management of the new lamp every Friday at 5 PM.
        """,
        actions=[
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "remove_device",
                    "room_id": "bedroom_west",
                    "device_id": "lamp_bw_desk"
                }
            ),
            Action(
                name="delete_device_from_database",
                kwargs={"device_id": "lamp_bw_desk"}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "lamp_bw_desk2",
                        "type": "light",

                        "location": "West Bedroom",
                        "vendor": "Ikea",
                        "model": "Nymåne LED",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "brightness", "color_temperature", "color"],
                        "state": {
                            "power": "off",
                            "brightness": 0,
                            "color_temperature": 4000,
                            "color": {"hue": 0, "saturation": 0},

                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "bedroom_west",
                    "device_id": "lamp_bw_desk2"
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_good_night",
                    "updates": {
                        "actions": [
                            {
                                "device_id": "lamp_bw_desk2",
                                "update": {"power": "on", "brightness": 15, "color": {"hue": 30}}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_desk_lamp_supplies",

                        "items": [
                            {"item": "Ikea Nymåne LED lamp", "quantity": 1},
                            {"item": "Spare LED bulb", "quantity": 1},
                            {"item": "Cable ties (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_check_lamp_install",
                        "target": {
                            "type": "entity",
                            "entity_type": "device",
                            "entity_id": "lamp_bw_desk2"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=17;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 3 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_03",
        instruction="""
        To help your daughter Olivia with her summer art project, you want to create a new list called "Olivia Art Supplies" (ID "list_olivia_art_supplies").
        The list should start with these items: 1 Acrylic Paint Set, 5 Canvas Panels (8x10 size), 1 Brush Pack, and 4 Glue Sticks.
        You also want to add 2 Glitter Packs and 1 Sketchbook (A4 size) to the list, and include 1 pack of colored pencils.
        You also want to set a reminder (ID "rem_olivia_art_review") to review this list every Saturday at 10 AM, as a normal priority mobile notification, call it Review Olivia Art Supply List.
        """,
        actions=[
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_olivia_art_supplies",

                        "items": [
                            {"item": "Acrylic Paint Set",     "quantity": 1},
                            {"item": "Canvas Panels 8x10",    "quantity": 5},
                            {"item": "Brush Pack",            "quantity": 1},
                            {"item": "Glue Sticks",           "quantity": 4},
                            {"item": "Glitter Pack",          "quantity": 2},
                            {"item": "Sketchbook (A4)",       "quantity": 1},
                            {"item": "Colored Pencils (pack)","quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_olivia_art_review",
                        "name": "Review Olivia Art Supply List",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_olivia_art_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 4 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_04",
        instruction="""
        You want to set up the system for your new babysitter, Emma Marie Green (nickname "Em"). You want to add her as a member with the ID "emma_green". She is a college student at SFSU studying Early-Childhood Education, born on February 12, 2002. Her contact info is +1-415-555-8888 and emma.green@example.com.
        She will not be living in the house but will visit every Friday evening at 5:00 PM. She does not drive and has a gluten allergy.
        You also want to create a list of her favorite snacks (ID "list_emma_snacks") containing 6 Granola Bars and 3 Sparkling Waters.
        To ensure Emma has everything she needs, you want to create a shopping list called "Emma Babysitting Supplies" (ID "list_emma_supplies") with the following items: 1 pack of gluten-free granola bars, 1 bottle of hand sanitizer, and 1 box of colored pencils for activities.
        Before making any changes, add the living room TV (ID "tv_lr") to the system: type "tv", name "Living Room TV", vendor Samsung, model Q60T, firmware 1.0.0, located in the Living Room, tracks power and input, initial state: power off, input "HDMI1".
        Finally, you want a reminder (ID "rem_emma_snack_prep") to go off at 4:30 PM every Friday to prepare her snacks before she arrives, and another reminder (ID "rem_emma_supplies_check") to check the babysitting supplies list every Friday at 3:30 PM.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "tv_lr",
                        "type": "tv",
                        "location": "Living Room",
                        "vendor": "Samsung",
                        "model": "Q60T",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "input"],
                        "state": {
                            "power": "off",
                            "input": "HDMI1"
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_member_in_database",
                kwargs={
                    "action": "add",
                    "member": {
                        "id": "emma_green",
                        "first_name": "Emma",
                        "middle_name": "Marie",
                        "last_name": "Green",
                        "nickname": "Em",
                        "relation": "Babysitter",
                        "birthdate": "2002-02-12",
                        "sex": "female",
                        "contact": {"phone": "+1-415-555-8888", "email": "emma.green@example.com"},
                        "residence": {"lives_in_house": False, "room_id": None},
                        "occupation": {
                            "status": "student",
                            "title": "Early-Childhood Education Major",
                            "organization": "SFSU",
                            "work_from_home": False
                        },
                        "schedule": {},
                        "favorites": {"food": "granola bars"},
                        "transportation": {"drives": False, "needs_parking": False},
                        "accessibility": {"wheelchair": False, "allergies": ["gluten"]},
                        "visit_preferences": {
                            "visit_frequency": "every Friday evening",
                            "usual_arrival_time": "17:00"
                        }
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_emma_snacks",

                        "items": [
                            {"item": "Granola Bar", "quantity": 6},
                            {"item": "Sparkling Water", "quantity": 3}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_emma_supplies",

                        "items": [
                            {"item": "Gluten-free granola bars (pack)", "quantity": 1},
                            {"item": "Hand sanitizer (bottle)", "quantity": 1},
                            {"item": "Colored pencils (box)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emma_snack_prep",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_emma_snacks"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=16;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emma_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_emma_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=15;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 5 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_05",
        instruction="""
        A severe heatwave is forecast for this afternoon, and you want to create a new scene called "Heatwave Day" (ID "scene_heatwave_day") to keep the house cool.
        The scene should close all curtains (in the living room, master bedroom, and west bedroom), set the AC to cooling mode at 22°C with the fan on high, and ensure the heater is turned off.
        You want to schedule this scene to run at 2 PM today. You also want to save this schedule directly to the AC unit as a backup and clear any existing scheduled updates from the heater to prevent it from turning on.
        Additionally, you want to create a shopping list called "Heatwave Essentials" (ID "list_heatwave_essentials") with the following items: 2 bottles of water, 1 pack of ice, and 1 portable fan.
        You also want to add a reminder (ID "rem_heatwave_essentials_check") to check this list at noon today.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"type": "curtain"}}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"type": "ac"}}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"type": "heater"}}
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_heatwave_day",
                        "actions": [
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}},
                            {"device_id": "curtain_br", "update": {"power": "on", "position": 0}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 0}},
                            {"device_id": "ac_home",     "update": {"power": "on", "mode": "cool", "setpoint_c": 22, "fan_speed": "high"}},
                            {"device_id": "heater_home", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": ["14:00"]
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "ac_home",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "mode": "cool", "setpoint_c": 22, "fan_speed": "high"}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "heater_home",
                    "updates": {"scheduled_updates": []}
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_heatwave_essentials",

                        "items": [
                            {"item": "Water bottle", "quantity": 2},
                            {"item": "Ice pack", "quantity": 1},
                            {"item": "Portable fan", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_heatwave_essentials_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_heatwave_essentials"
                        },
                        "trigger": {"datetime": "12:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 6 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_06",
        instruction="""
        To ensure the kids have good lighting for reading in their bedrooms, you want to set up an automatic schedule for all bedroom ceiling lights.
        You want the ceiling lights in the master, west, and east bedrooms (IDs "light_br_ceiling", "light_bw_ceiling", "light_be_ceiling") to turn on every day at 7 PM. They should be set to 60% brightness.
        You also want to make sure all bedroom desk lamps ("lamp_br_night", "lamp_bw_desk", "lamp_be_bedside") are turned off before the ceiling lights turn on.
        Additionally, create a shopping list called "Bedroom Reading Supplies" (ID "list_bedroom_reading_supplies") with the following items: 3 reading lamps, 3 packs of AA batteries, and 3 bookmarks.
        Set a reminder (ID "rem_bedroom_reading_check") to check this list every Saturday at 5 PM.
        Use the exact RRULE string "FREQ=DAILY;BYHOUR=19;BYMINUTE=0" for scheduling to ensure all lights sync up perfectly.
        """,
        actions=[
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "brightness": 60},
                                "rrule": "FREQ=DAILY;BYHOUR=19;BYMINUTE=0"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_bw_ceiling",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "brightness": 60},
                                "rrule": "FREQ=DAILY;BYHOUR=19;BYMINUTE=0"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "brightness": 60},
                                "rrule": "FREQ=DAILY;BYHOUR=19;BYMINUTE=0"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_bedroom_reading_supplies",

                        "items": [
                            {"item": "Reading lamp", "quantity": 3},
                            {"item": "AA batteries (pack)", "quantity": 3},
                            {"item": "Bookmark", "quantity": 3}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_bedroom_reading_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_bedroom_reading_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=17;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 7 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_07",
        instruction="""
        You have installed a new Arlo Essential XL security camera in the garage today and want to set it up. You want to name it "Garage Security Camera" with an ID of "camera_garage" and firmware version 1.0.0.
        The camera supports detecting motion, people, and threats, as well as streaming and recording. Its initial state is: stream up, recording on, but no motion, people, or threats detected.
        Since the garage is on the basement network segment, you want to add this camera to the "basement" room.
        Before making any changes, fetch the current state of the garage camera.
        You also want to ensure the garage lights (ID "light_garage_ceiling") are off before activating any security scene, so fetch their state and turn them off if needed.
        You recently bought and installed the garage ceiling light (ID "light_garage_ceiling"), a Philips Hue White Ambiance model, firmware 1.0.0, located in the Garage. It tracks power and brightness, initial state: power off, brightness 0%.
        You want to create a new "Away Mode" scene (ID "scene_away_mode") to ensure the house is secured when nobody is home. When this scene is active, you want the garage camera to be streaming and recording, all living room lights (floor and ceiling), the AC, and the garage ceiling light to be turned off.
        Additionally, create a shopping list called "Garage Security Supplies" (ID "list_garage_security_supplies") with the following items: 1 pack of AA batteries, 1 warning sign for security camera, and 1 cleaning cloth for lens.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "camera_garage"}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "camera_garage",
                        "type": "camera",
                        "location": "Garage",
                        "vendor": "Arlo",
                        "model": "Essential XL",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "stream_online",
                            "motion_detected",
                            "person_detected",
                            "threat_detected",
                            "recording"
                        ],
                        "state": {
                            "stream_online": True,
                            "motion_detected": False,
                            "person_detected": False,
                            "threat_detected": False,
                            "recording": True,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "basement",
                    "device_id": "camera_garage"
                }
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "light_garage_ceiling",
                        "type": "light",
                        "location": "Garage",
                        "vendor": "Philips",
                        "model": "Hue White Ambiance",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "brightness"],
                        "state": {
                            "power": "off",
                            "brightness": 0
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "garage",
                    "device_id": "light_garage_ceiling"
                }
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "light_garage_ceiling"}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_garage_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_away_mode",
                        "actions": [
                            {"device_id": "camera_garage",  "update": {"recording": True, "stream_online": True}},
                            {"device_id": "light_lr_floor", "update": {"power": "off"}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "ac_home",        "update": {"power": "off"}},
                            {"device_id": "light_garage_ceiling", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_garage_security_supplies",

                        "items": [
                            {"item": "AA batteries (pack)", "quantity": 1},
                            {"item": "Security camera warning sign", "quantity": 1},
                            {"item": "Lens cleaning cloth", "quantity": 1}
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 8 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_08",
        instruction="""
        You got a new iRobot Roomba i7+ and want to set it up. It is fully charged and docked in the living room. You want to add it to the system with the ID "vacuum_home" and the name "Main Floor Robot Vacuum", running firmware 3.1.0.
        The vacuum reports power state, cleaning mode, and battery percentage. Its current state is 'off' and 'docked' with a full battery. You want to add it to the living room's device list.
        Before making any changes, fetch the current state of the vacuum.
        You want it to run automatically every day at 9:30 AM by turning on and setting its mode to "clean".
        You also want to create a scene called "Daily Clean" (ID "scene_daily_clean") that does the same thing: triggers the robot vacuum to start cleaning immediately.
        To ensure safety, fetch the state of the living room ceiling light (ID "light_lr_ceiling") and turn it off before the vacuum starts cleaning.
        Additionally, create a shopping list called "Vacuum Supplies" (ID "list_vacuum_supplies") with the following items: 1 pack of replacement filters, 1 pack of side brushes, and 1 bottle of cleaning solution.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "vacuum_home"}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "vacuum_home",
                        "type": "vacuum",

                        "location": "Living Room",
                        "vendor": "iRobot",
                        "model": "Roomba i7+",
                        "firmware_version": "3.1.0",
                        "state_params": ["power", "mode", "battery_pct"],
                        "state": {
                            "power": "off",
                            "mode": "dock",
                            "battery_pct": 100,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "vacuum_home"
                }
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "light_lr_ceiling"}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "vacuum_home",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "mode": "clean"},
                                "rrule": "FREQ=DAILY;BYHOUR=9;BYMINUTE=30"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_daily_clean",
                        "actions": [
                            {"device_id": "vacuum_home", "update": {"power": "on", "mode": "clean"}}
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_vacuum_supplies",

                        "items": [
                            {"item": "Replacement filters (pack)", "quantity": 1},
                            {"item": "Side brushes (pack)", "quantity": 1},
                            {"item": "Cleaning solution (bottle)", "quantity": 1}
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 9 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_09",
        instruction="""
        To ensure you don't forget to maintain your sensors, you want to check the details of the living room thermometer (ID "sensor_lr_thermometer") and then set up a battery replacement reminder.
        You want to schedule the reminder (ID "rem_sensor_lr_battery") for exactly one year from now, on June 27, 2026, at 8 AM. It should be a normal priority push notification to your phone.
        Additionally, you want to create a shopping list called "Sensor Maintenance Supplies" (ID "list_sensor_maintenance") with the following items: 2 AAA batteries, 1 microfiber cleaning cloth, and 1 can of compressed air.
        Before making any changes, fetch the current state of the living room thermometer.
        """,
        actions=[
            Action(
                name="get_sensor_by_id_or_filter",
                kwargs={"sensor": "sensor_lr_thermometer"}
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_sensor_maintenance",

                        "items": [
                            {"item": "AAA batteries (pack)", "quantity": 2},
                            {"item": "Microfiber cleaning cloth", "quantity": 1},
                            {"item": "Compressed air (can)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_sensor_lr_battery",
                        "target": {"type": "entity", "entity_type": "device", "entity_id": "sensor_lr_thermometer"},
                        "trigger": {"datetime": "2026-06-27T08:00:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "scheduled",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 10 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_10",
        instruction="""
        You are planning a weekend camping trip and want to organize your gear. You want to create a packing list called "Weekend Camping Packing" (ID "list_camping_weekend").
        You want the list to contain the following items in order: 1 Tent, 4 Sleeping Bags, 1 Camping Stove, 2 Propane Canisters, 4 Flashlights, 6 Water Bottles, and 1 First-Aid Kit.
        You also want a reminder (ID "rem_camping_check") for Thursday at 8 PM to double-check the list.
        Finally, you remember that you also need 2 cans of Bug Spray, and you want to add them to the list.
        """,
        actions=[
            Action(
                name="update_custom_list_in_database",
                kwargs={
                    "list_id": "list_camping_weekend",
                    "updates": {
                        "items": [
                            {"item": "Tent",            "quantity": 1},
                            {"item": "Sleeping Bag",    "quantity": 4},
                            {"item": "Camping Stove",   "quantity": 1},
                            {"item": "Propane Canister","quantity": 2},
                            {"item": "Flashlight",      "quantity": 4},
                            {"item": "Water Bottle",    "quantity": 6},
                            {"item": "First-Aid Kit",   "quantity": 1},
                            {"item": "Bug Spray",       "quantity": 2}
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 11 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_11",
        instruction="""
        Now that summer is here, you want to disable all heating automation. First, fetch the current state of the heater (ID "heater_home") before making any changes.
        You want to turn off the heater and remove any of its scheduled updates.
        You also noticed the "Good Night" scene includes the heater. You want to update that scene to remove the heater actions and instead perform the following actions:
        - Close both the living room and master bedroom curtains.
        - Turn off both the living room and master bedroom ceiling lights.
        - Turn on the master bedroom night lamp at 15% brightness with a cozy warm tone (hue 30).
        Additionally, fetch the state of the master bedroom night lamp (ID "lamp_br_night") before updating its state.
        To prepare for summer nights, create a shopping list called "Summer Night Essentials" (ID "list_summer_night_essentials") with the following items: 2 mosquito repellent sprays, 1 pack of cooling gel pads, and 1 bedside fan.
        Set a reminder (ID "rem_summer_night_essentials_check") to check this list every Friday at 6 PM.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "heater_home"}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "heater_home",
                    "updates": {
                        "power": "off",
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "lamp_br_night"}
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_good_night",
                    "updates": {
                        "actions": [
                            {"device_id": "curtain_lr",   "update": {"power": "on", "position": 0}},
                            {"device_id": "curtain_br",   "update": {"power": "on", "position": 0}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "light_br_ceiling", "update": {"power": "off"}},
                            {"device_id": "lamp_br_night",    "update": {"power": "on", "brightness": 15, "color": {"hue": 30}}}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_summer_night_essentials",

                        "items": [
                            {"item": "Mosquito repellent spray", "quantity": 2},
                            {"item": "Cooling gel pads (pack)", "quantity": 1},
                            {"item": "Bedside fan", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_summer_night_essentials_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_summer_night_essentials"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=18;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 12 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_12",
        instruction="""
        You bought a Dyson Cool AM07 standing fan for the master bedroom and want to add it to your system. The fan is set up but off. You want to add it with the ID "fan_br_stand" and the name "Master Bedroom Standing Fan", with firmware version 1.0.0. The fan has adjustable power and speed settings (state_params: power, speed; initial state: off, speed 0).
        Add it to the master bedroom's device list (room ID "bedroom_master").
        Before making any changes, fetch the current state of the fan to confirm it is off.
        You also want to incorporate it into your "Heatwave Day" scene, so that when the scene runs, the fan turns on at 70% speed to help with air circulation.
        Additionally, create a shopping list called "Heatwave Fan Supplies" (ID "list_heatwave_fan_supplies") with the following items: 1 pack of AAA batteries, 1 bottle of fan cleaning spray, and 1 microfiber cloth.
        Set a reminder (ID "rem_heatwave_fan_supplies_check") to check this list every Friday at 4 PM.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "fan_br_stand"}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "fan_br_stand",
                        "type": "fan",
                        "location": "Master Bedroom",
                        "vendor": "Dyson",
                        "model": "Cool AM07",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "speed"],
                        "state": {"power": "off", "speed": 0},
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "bedroom_master",
                    "device_id": "fan_br_stand"
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_heatwave_day",
                        "actions": [
                            {"device_id": "fan_br_stand", "update": {"power": "on", "speed": 70}}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_heatwave_fan_supplies",

                        "items": [
                            {"item": "AAA batteries (pack)", "quantity": 1},
                            {"item": "Fan cleaning spray (bottle)", "quantity": 1},
                            {"item": "Microfiber cloth", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_heatwave_fan_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_heatwave_fan_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=16;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 13 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_13",
        instruction="""
        Grandma Linda (ID "linda_johnson") no longer needs her wheelchair. You want to update her accessibility information in the system to reflect this.
        Before making any changes, fetch her current member record.
        Since she still has her monthly visit, you want to set up a reminder to prepare the West Bedroom for her stay. Schedule this reminder (ID "rem_prepare_west_bedroom") for August 1st at 10 AM. The reminder note should mention keeping the ramp available just in case, and send it via mobile push notification.
        Additionally, you want to create a shopping list called "West Bedroom Prep Supplies" (ID "list_west_bedroom_prep") with the following items: 1 set of fresh linens, 1 bottle of air freshener, and 1 pack of guest toiletries.

        After her stay, set a reminder (ID "rem_move_residence_west_to_east") for August 2nd at 10 AM to move Linda's residence record from bedroom_west to bedroom_east, remind via mobile push.
        """,
        actions=[
            Action(
                name="manage_member_in_database",
                kwargs={
                    "action": "get",
                    "member_id": "linda_johnson"
                }
            ),
            Action(
                name="manage_member_in_database",
                kwargs={
                    "action": "update",
                    "member_id": "linda_johnson",
                    "updates": {"accessibility": {"wheelchair": False}}
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_prepare_west_bedroom",
                        "target": {"type": "note", "text": "Set up linens and wheelchair ramp just in case"},
                        "trigger": {"datetime": "2025-08-01T10:00:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "scheduled",
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_west_bedroom_prep",

                        "items": [
                            {"item": "Fresh linens (set)", "quantity": 1},
                            {"item": "Air freshener (bottle)", "quantity": 1},
                            {"item": "Guest toiletries (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_move_residence_west_to_east",
                        "target": {"type": "note", "text": "Move Linda's residence record from bedroom_west to bedroom_east"},
                        "trigger": {"datetime": "2025-08-02T10:00:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 14 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_14",
        instruction="""
        You've repurposed the coffee maker's smart plug to control a new LED strip for movie nights and want to update your "Movie Time" scene.
        The living room TV (ID "tv_lr") is a Samsung Q60T, firmware 1.0.0, located in the Living Room, tracks power and input, initial state: power off, input "HDMI1". Add it as a new device and attach it to the living room.
        Then, delete the old scene (ID "scene_movie_time").
        Next, create a new version called "Movie Time v2" (ID "scene_movie_time_v2"). This scene should: close the living room curtains, dim the floor lamp to 15%, turn off the ceiling light, set the AC to low fan speed, and turn off the coffee maker plug (now controlling the LED strip).
        Additionally, create a shopping list called "Movie Night Supplies" (ID "list_movie_night_supplies") with the following items: 1 pack of popcorn, 2 bottles of soda, and 1 box of LED strip replacement parts.
        Also, ensure the living room TV (ID "tv_lr") is turned off before starting the scene by fetching its state and powering it off if needed.
        Schedule this new scene to run at 9 PM for your first movie night with the new lighting.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "tv_lr",
                        "type": "tv",
                        "location": "Living Room",
                        "vendor": "Samsung",
                        "model": "Q60T",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "input"],
                        "state": {
                            "power": "off",
                            "input": "HDMI1"
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "tv_lr"
                }
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": "tv_lr"}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "tv_lr",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="delete_scene_from_database",
                kwargs={"scene_id": "scene_movie_time"}
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_movie_time_v2",
                        "actions": [
                            {"device_id": "curtain_lr",       "update": {"power": "on", "position": 0}},
                            {"device_id": "light_lr_floor",   "update": {"power": "on", "brightness": 15}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "ac_home",          "update": {"power": "on", "fan_speed": "low"}},
                            {"device_id": "plug_kt_coffee",   "update": {"power": "off"}}
                        ],
                        "scheduled_runs": ["21:00"]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_movie_night_supplies",

                        "items": [
                            {"item": "Popcorn (pack)", "quantity": 1},
                            {"item": "Soda (bottle)", "quantity": 2},
                            {"item": "LED strip replacement parts (box)", "quantity": 1}
                        ]
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 15 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_15",
        instruction="""
        You want a quick security sweep every morning. First, check for all the cameras already installed.
        For that, you installed two new cameras: "camera_side_yard" and "camera_garage", both from Arlo, model Essential XL, firmware ver. 1.0.0. Each camera tracks stream_online, motion_detected, person_detected, threat_detected, and recording, all initially set to False. Be sure to add both cameras to the system with these parameters.
        You also installed a new garage ceiling light (ID "light_garage_ceiling"), a Philips Hue White Ambiance model, firmware 1.0.0, located in the Garage. It tracks power and brightness, initial state: power off, brightness 0%.
        You want to create a scene named "scene_morning_sweep" for Quick camera snapshots and door check that runs at 6 AM daily (RRULE "FREQ=DAILY;BYHOUR=6;BYMINUTE=0").
        The scene should ask each security camera ("camera_front_door", "camera_back_door", "camera_side_yard", "camera_garage") to take a snapshot (represented by setting 'recording' to true momentarily).
        You want to ensure these cameras are set to record during the sweep.
        It should also check the front-door contact sensor (sensor_front_door), which can be done by including a get_device call in the automation list.
        You also want to create a shopping list called "Security Sweep Supplies" (ID "list_security_sweep_supplies") with the following items: 1 pack of AA batteries for cameras, 1 lens cleaning cloth, and 1 warning sign for security sweep.
        """,
        actions=[
            Action(
                name="get_sensor_by_id_or_filter",
                kwargs={"filters": {"type": "camera"}}
            ),
            Action(
                name="add_sensor_to_database",
                kwargs={
                    "sensor": {
                        "id": "camera_side_yard",
                        "type": "camera",
                        "location": "Side Yard",
                        "vendor": "Arlo",
                        "model": "Essential XL",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "stream_online",
                            "motion_detected",
                            "person_detected",
                            "threat_detected",
                            "recording"
                        ],
                        "state": {
                            "stream_online": False,
                            "motion_detected": False,
                            "person_detected": False,
                            "threat_detected": False,
                            "recording": False,
                        }
                    }
                }
            ),
            Action(
                name="add_sensor_to_database",
                kwargs={
                    "sensor": {
                        "id": "camera_garage",
                        "type": "camera",
                        "location": "Garage",
                        "vendor": "Arlo",
                        "model": "Essential XL",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "stream_online",
                            "motion_detected",
                            "person_detected",
                            "threat_detected",
                            "recording"
                        ],
                        "state": {
                            "stream_online": False,
                            "motion_detected": False,
                            "person_detected": False,
                            "threat_detected": False,
                            "recording": False,
                        }
                    }
                }
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "light_garage_ceiling",
                        "type": "light",
                        "location": "Garage",
                        "vendor": "Philips",
                        "model": "Hue White Ambiance",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "brightness"],
                        "state": {
                            "power": "off",
                            "brightness": 0
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_security_sweep_supplies",

                        "items": [
                            {"item": "AA batteries (pack)", "quantity": 1},
                            {"item": "Lens cleaning cloth", "quantity": 1},
                            {"item": "Security sweep warning sign", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_morning_sweep",
                        "actions": [
                            {"sensor_id": "camera_front_door", "update": {"recording": True}},
                            {"sensor_id": "camera_back_door", "update": {"recording": True}},
                            {"sensor_id": "camera_side_yard", "update": {"recording": True}},
                            {"sensor_id": "camera_garage", "update": {"recording": True}},
                            {"sensor_id": "sensor_front_door", "update": {}}
                        ],
                        "scheduled_runs": [],
                        "rrule": "FREQ=DAILY;BYHOUR=6;BYMINUTE=0"
                    }
                },
            ),
        ],
        outputs=[]
    ),

    # Task 16 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_16",
        instruction="""
        You want to create an after-school routine for your daughter Olivia, who gets home at 3:15 PM. You want a new scene called "After School" (ID "scene_after_school") to make her room ideal for homework.
        In her room (West Bedroom), you want the ceiling light (ID "light_bw_ceiling") at 100% brightness and her desk lamp (ID "lamp_bw_desk") at 80% brightness with a color temperature of 4500K. You also want the curtains (ID "curtain_bw") opened halfway to let in natural light but avoid glare.
        Since she has a peanut allergy, you also want a high-priority reminder (ID "rem_olivia_snack_check") that goes off at 3:20 PM on school days to check her lunchbox and prepare a safe after-school snack, call it Safe Snack.
        To ensure safety, fetch the current state of the West Bedroom ceiling light and desk lamp before making any changes, and turn off the desk lamp if it is already on before running the scene.
        Additionally, create a shopping list called "Olivia After School Supplies" (ID "list_olivia_after_school_supplies") with the following items: 1 pack of peanut-free snack bars, 1 bottle of water, and 1 pack of colored pencils for homework.
        Set a reminder (ID "rem_olivia_supplies_check") to check this list every Monday at 8 AM.
        You want to schedule the scene to run automatically at 3:15 PM on weekdays using the RRULE string "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=15".
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"type": "light"}}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_after_school",
                        "actions": [
                            {"device_id": "light_bw_ceiling", "update": {"power": "on", "brightness": 100}},
                            {"device_id": "lamp_bw_desk", "update": {"power": "on", "brightness": 80, "color_temperature": 4500}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 50}}
                        ],
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_olivia_after_school_supplies",

                        "items": [
                            {"item": "Peanut-free snack bars (pack)", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1},
                            {"item": "Colored pencils (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_olivia_snack_check",
                        "target": {"type": "note", "text": "check Olivia's lunchbox and prepare a safe after-school snack"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=20"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_olivia_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_olivia_after_school_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_after_school",
                    "updates": {
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=15"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 17 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_17",
        instruction="""
        Your friends David and Sarah Lee visit every Sunday evening at 6:30 PM for dinner. You want to create a welcoming atmosphere for them with a scene called "Sunday Dinner" (ID "scene_sunday_dinner").
        To ensure the kitchen and living room are well-lit, you want the living room ceiling light (ID "light_lr_ceiling") set to 80% brightness with a warm color (2700K), and the floor lamp (ID "light_lr_floor") at 60% for ambient light.
        Since David is allergic to shellfish and Sarah is vegan, you want to create a list (ID "list_sunday_dinner_restrictions") to track their dietary preferences.
        You also want a shopping list called "Sunday Dinner Groceries" (ID "list_sunday_dinner_groceries") with the following items: 1 pack of vegan cheese, 1 box of gluten-free pasta, and 1 bottle of sparkling water.
        Before making any changes, fetch the current state of the living room ceiling light and floor lamp to ensure they are off before the scene runs. If any are on, turn them off before setting up the scene.
        Finally, you want a reminder (ID "rem_sunday_dinner_prep") at 5 PM every Sunday (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=17;BYMINUTE=0") to start preparing, notify me via mobile push. The scene should be scheduled to run at 6:25 PM (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=18;BYMINUTE=25").
        """,
        actions=[
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_lr_floor",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_sunday_dinner",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 80,
                                    "color": {"kelvin": 2700}
                                }
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {"power": "on", "brightness": 60}
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_sunday_dinner_restrictions",

                        "items": [
                            {"item": "David - No shellfish (allergy)", "quantity": 1},
                            {"item": "Sarah - Vegan", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_sunday_dinner_groceries",

                        "items": [
                            {"item": "Vegan cheese (pack)", "quantity": 1},
                            {"item": "Gluten-free pasta (box)", "quantity": 1},
                            {"item": "Sparkling water (bottle)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_sunday_dinner_prep",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_sunday_dinner_restrictions"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=17;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_sunday_dinner",
                    "updates": {
                        "scheduled_runs": [],
                        "rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=18;BYMINUTE=25"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 18 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_18",
        instruction="""
        Your wife Emily works early shifts at the hospital (Mon-Wed, starting at 7 AM). To make her mornings smoother, you want to create a scene called "Emily's Hospital Shift" (ID "scene_emily_shift").
        She wakes at 5:30 AM, so you want the master bedroom lights to ease her awake: the ceiling light (ID "light_br_ceiling") at 30% brightness with a cool 5000K color, and the night lamp (ID "lamp_br_night") at 20% with the same tone. The curtains (ID "curtain_br") should also open fully.
        She leaves at 6:30 AM. You want a reminder at 6:15 AM (ID "rem_emily_lunch") with note "Grab lunch", and another at 6:25 AM (ID "rem_emily_leaving") to check her nursing equipment.
        You also want a checklist of her essential items (ID "list_emily_nursing"), such as: ID Badge, Stethoscope, Scrubs, Comfortable Shoes, Water Bottle and Lunch Box, one of each, which you're creating now.
        Additionally, you want to create a shopping list called "Emily Hospital Shift Supplies" (ID "list_emily_shift_supplies") with the following items: 1 pack of medical masks, 1 bottle of hand sanitizer, and 1 pack of energy bars.
        Before making any changes, fetch the current state of the master bedroom ceiling light (ID "light_br_ceiling"), night lamp (ID "lamp_br_night"), and curtains (ID "curtain_br") to confirm their status.
        To ensure safety, if the night lamp is already on before the scene runs, turn it off first.
        Please schedule the scene and reminders using the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE;BYHOUR=5;BYMINUTE=30" (adjusting the minute for the reminders).
        """,
        actions=[
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_emily_shift",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 30,
                                    "color": {"kelvin": 5000}
                                }
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {
                                    "power": "on",
                                    "brightness": 20,
                                    "color": {"kelvin": 5000}
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {"power": "on", "position": 100}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_emily_nursing",

                        "items": [
                            {"item": "ID Badge", "quantity": 1},
                            {"item": "Stethoscope", "quantity": 1},
                            {"item": "Scrubs", "quantity": 1},
                            {"item": "Comfortable Shoes", "quantity": 1},
                            {"item": "Water Bottle", "quantity": 1},
                            {"item": "Lunch Box", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_emily_shift_supplies",

                        "items": [
                            {"item": "Medical masks (pack)", "quantity": 1},
                            {"item": "Hand sanitizer (bottle)", "quantity": 1},
                            {"item": "Energy bars (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emily_lunch",
                        "target": {"type": "note", "text": "Grab lunch"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE;BYHOUR=6;BYMINUTE=15"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emily_leaving",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_emily_nursing"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE;BYHOUR=6;BYMINUTE=25"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_emily_shift",
                    "updates": {
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE;BYHOUR=5;BYMINUTE=30"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 19 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_19",
        instruction="""
        Olivia's friend Mia Martinez, who also has a peanut allergy, comes over for a playdate every Wednesday after school. You want to set up safety measures.
        First, you want a scene called "Playdate Safety" (ID "scene_playdate") that runs at 3:10 PM. It should turn on the lights in Olivia's room (West Bedroom): ceiling light (ID "light_bw_ceiling") at 90% and desk lamp (ID "lamp_bw_desk") at 70% with a bright 4000K temperature. The curtains (ID "curtain_bw") should open fully for visibility.
        You also want a checklist for allergy safety (ID "list_playdate_safety"), which you're creating now, and it should include: "Check all snacks for peanut ingredients", "Verify no cross-contamination in kitchen", "Keep EpiPens easily accessible", "Have Ana's contact number ready", and "Clean all surfaces the girls will use".
        Additionally, you want to create a shopping list called "Playdate Snacks" (ID "list_playdate_snacks") with the following items: 2 packs of peanut-free snack bars, 1 bottle of apple juice, and 1 pack of fruit cups.
        Before making any changes, fetch the current state of the West Bedroom ceiling light, desk lamp, and curtains, and also fetch the state of the kitchen outlet (ID "plug_kt_coffee") to ensure it is off for safety during the playdate. If the plug is on, turn it off.
        The kitchen outlet (ID "plug_kt_coffee") is a TP-Link Kasa HS110 smart plug firmware 1.0.0, located in the Kitchen, tracks power and energy consumption, initial state: power off, energy_kwh 0.
        You want two reminders: one at 3:15 PM ("rem_playdate_snack") to prepare allergy-safe snacks, and another at 5:45 PM ("rem_playdate_pickup") to remind you that Mia's mom picks her up at 6 PM.
        Use the RRULE "FREQ=WEEKLY;BYDAY=WE" for all schedules, adjusting the hour and minute as needed.
        """,
        actions=[
            Action(
                name="manage_member_in_database",
                kwargs={
                    "action": "get",
                    "member_id": "mia_martinez"
                }
            ),
            Action(
                name="manage_member_in_database",
                kwargs={
                    "action": "get",
                    "member_id": "olivia_johnson"
                }
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "plug_kt_coffee",
                        "type": "outlet",
                        "location": "Kitchen",
                        "vendor": "TP-Link",
                        "model": "Kasa HS110",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "energy_kwh"],
                        "state": {
                            "power": "off",
                            "energy_kwh": 0,
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_bw_ceiling", "lamp_bw_desk", "curtain_bw", "plug_kt_coffee"]}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "plug_kt_coffee",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_playdate",
                        "actions": [
                            {"device_id": "light_bw_ceiling", "update": {"power": "on", "brightness": 90}},
                            {
                                "device_id": "lamp_bw_desk",
                                "update": {
                                    "power": "on",
                                    "brightness": 70,
                                    "color_temperature": 4000
                                }
                            },
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 100}}
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_playdate_safety",

                        "items": [
                            {"item": "Check all snacks for peanut ingredients", "quantity": 1},
                            {"item": "Verify no cross-contamination in kitchen", "quantity": 1},
                            {"item": "Keep EpiPens easily accessible", "quantity": 1},
                            {"item": "Have Ana's contact number ready", "quantity": 1},
                            {"item": "Clean all surfaces the girls will use", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_playdate_snacks",

                        "items": [
                            {"item": "Peanut-free snack bars (pack)", "quantity": 2},
                            {"item": "Apple juice (bottle)", "quantity": 1},
                            {"item": "Fruit cups (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_playdate_snack",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_playdate_safety"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=15;BYMINUTE=15"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_playdate_pickup",
                        "target": {"type": "note", "text": "Ana will pick up Mia at 6:00 PM"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=17;BYMINUTE=45"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_playdate",
                    "updates": {
                        "scheduled_runs": [],
                        "rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=15;BYMINUTE=10"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 20 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_20",
        instruction="""
        You want to create a calming bedtime routine for your son Ethan, who goes to bed at 8 PM on school nights in the East Bedroom. You want a wind-down sequence starting at 7:30 PM.
        For his room, you want to dim the lights over 30 minutes. At 7:30 PM, the ceiling light (ID "light_be_ceiling") should be at 50% with a warm color (hue 30, saturation 30). At 7:45 PM, switch to just his bedside lamp (ID "lamp_be_bedside") at 30% with the same warm color. At 7:50 PM, the curtains (ID "curtain_be") should close. At 8 PM, all lights should turn off.
        The East Bedroom desk lamp (ID "lamp_be_desk") is a Philips Hue White Ambiance model, firmware 1.0.0, located in the East Bedroom, tracks power and brightness, initial state: power off, brightness 0%.
        You want this to be a scene called "Ethan Bedtime" (ID "scene_ethan_bedtime"). You also want a reminder (ID "rem_ethan_bedtime") at 7:25 PM to start his bedtime routine (brushing teeth, etc.).
        Additionally, create a shopping list called "Ethan Bedtime Supplies" (ID "list_ethan_bedtime_supplies") with the following items: 1 pack of bedtime storybooks, 1 bottle of water, and 1 nightlight bulb.
        Please use the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" for all schedules, adjusting times as needed.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "lamp_be_desk",
                        "type": "lamp",
                        "location": "East Bedroom",
                        "vendor": "Philips",
                        "model": "Hue White Ambiance",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "brightness"],
                        "state": {
                            "power": "off",
                            "brightness": 0
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_be_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_ethan_bedtime",
                        "actions": [
                            {
                                "device_id": "light_be_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 50,
                                    "color": {"hue": 30, "saturation": 30}
                                }
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_ethan_bedtime_supplies",

                        "items": [
                            {"item": "Bedtime storybooks (pack)", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1},
                            {"item": "Nightlight bulb", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_ethan_bedtime",
                        "target": {
                            "type": "note",
                            "text": "Time for Ethan to brush teeth and get ready for bed"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=19;BYMINUTE=25"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {
                                    "power": "on",
                                    "brightness": 30,
                                    "color": {"hue": 30, "saturation": 30}
                                },
                                "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=19;BYMINUTE=45"
                            },
                            {
                                "update": {"power": "off"},
                                "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=20;BYMINUTE=0"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "off"},
                                "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=19;BYMINUTE=45"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "curtain_be",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"position": 0},
                                "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=19;BYMINUTE=50"
                            }
                        ]
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_ethan_bedtime",
                    "updates": {
                        "scheduled_runs": [],
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=19;BYMINUTE=30"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 21 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_21",
        instruction="""
        As John, you want to optimize your home for your work-from-home schedule (Senior Software Engineer at TechLabs, 7:30 AM to 4 PM). You want a "Work Mode" scene (ID "scene_work_mode") for a productive environment.
        Starting at 7:30 AM in the master bedroom, you want the ceiling light (ID "light_br_ceiling") at full brightness with a cool 5500K color. The curtains (ID "curtain_br") should be fully open, and the night lamp (ID "lamp_br_night") should be off.
        You take lunch at noon, and you want a reminder for it (ID "rem_john_lunch") with note "Lunch time". You also want a reminder (ID "rem_john_breaks") with note "Take break" every 2 hours during your workday (7:30, 9:30, 11:30, 1:30, 3:30) to take short breaks. Use the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" for all schedules.
        You also want a checklist for your daily work setup (ID "list_john_work_setup"), which you are creating now, with these items: "Laptop & charger", "External monitor setup", "Noise-canceling headphones", "Water bottle", "Ergonomic chair adjustment", "Task list review".
        Additionally, you want a shopping list called "Work Essentials" (ID "list_john_work_essentials") with the following items: 1 pack of sticky notes, 1 pack of pens, and 1 bottle of hand sanitizer.
        Before starting work, ensure the master bedroom night lamp (ID "lamp_br_night") is off for safety.
        Set a reminder (ID "rem_john_work_essentials_check") every Monday at 8 AM to check the work essentials list.
        """,
        actions=[
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_work_mode",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 100,
                                    "color": {"kelvin": 5500}
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {"power": "on", "position": 100}
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
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_john_work_setup",

                        "items": [
                            {"item": "Laptop & charger", "quantity": 1},
                            {"item": "External monitor setup", "quantity": 1},
                            {"item": "Noise-canceling headphones", "quantity": 1},
                            {"item": "Water bottle", "quantity": 1},
                            {"item": "Ergonomic chair adjustment", "quantity": 1},
                            {"item": "Task list review", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_john_work_essentials",

                        "items": [
                            {"item": "Sticky notes (pack)", "quantity": 1},
                            {"item": "Pens (pack)", "quantity": 1},
                            {"item": "Hand sanitizer (bottle)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_john_lunch",
                        "target": {"type": "note", "text": "Lunch time"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=12;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_john_breaks",
                        "target": {"type": "note", "text": "Take break"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7,9,11,13,15;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_john_work_essentials_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_john_work_essentials"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_work_mode",
                    "updates": {
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7;BYMINUTE=30"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 22 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_22",
        instruction="""
        You want to set up better monitoring and maintenance for your Bosch Series 8 dishwasher (ID "dishwasher_kt").
        First, you want to create a maintenance checklist (ID "list_dishwasher_maintenance") with monthly and quarterly tasks.
        You also want three reminders:
        1. A monthly reminder for basic maintenance (ID "rem_dishwasher_monthly") on the 1st of each month at 10 AM (RRULE "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=10;BYMINUTE=0").
        2. A quarterly reminder for deep cleaning (ID "rem_dishwasher_quarterly") every three months on the 15th at 10 AM (RRULE "FREQ=MONTHLY;INTERVAL=3;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0").
        3. A reminder (ID "rem_dishwasher_cycle") that triggers when a cycle finishes (when time_remaining_min changes to 0).
        You want to add a shopping list called "Dishwasher Supplies" (ID "list_dishwasher_supplies") with the following items: 1 bottle of rinse aid, 1 pack of dishwasher tablets, and 1 bottle of descaler.
        Finally, you want a scene called "Dishwasher Check" (ID "scene_dishwasher_check") that turns on the living room ceiling lights when the cycle is complete, and also sends a notification to check the supplies list.
        """,
        actions=[
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_dishwasher_maintenance",

                        "items": [
                            {"item": "Clean filter and spray arms", "quantity": 1},
                            {"item": "Check and refill rinse aid", "quantity": 1},
                            {"item": "Inspect door seal", "quantity": 1},
                            {"item": "Clean interior walls", "quantity": 1},
                            {"item": "Run empty hot water cycle", "quantity": 1},
                            {"item": "Check water temperature", "quantity": 1},
                            {"item": "Descale interior (quarterly)", "quantity": 1},
                            {"item": "Deep clean filters (quarterly)", "quantity": 1},
                            {"item": "Check water connections (quarterly)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_dishwasher_supplies",

                        "items": [
                            {"item": "Rinse aid (bottle)", "quantity": 1},
                            {"item": "Dishwasher tablets (pack)", "quantity": 1},
                            {"item": "Descaler (bottle)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dishwasher_monthly",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_dishwasher_maintenance"
                        },
                        "trigger": {"rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dishwasher_quarterly",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_dishwasher_maintenance"
                        },
                        "trigger": {"rrule": "FREQ=MONTHLY;INTERVAL=3;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_dishwasher_cycle",
                        "target": {
                            "type": "entity",
                            "entity_type": "device",
                            "entity_id": "dishwasher_kt"
                        },
                        "trigger": {"device_state": {"time_remaining_min": 0}},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_dishwasher_check",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "on"}},
                        ],
                        "scheduled_runs": [],
                        "notifications": [
                            {"type": "notify", "channel": "mobile_push", "target": "list_dishwasher_supplies"}
                        ]
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 23 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_23",
        instruction="""
        Your college friend Mike Brown ("michael_brown") visits quarterly (Friday-Sunday) and is allergic to cat dander, so you want to set up cleaning automations and ensure the environment is safe.
        First, you want a checklist (ID "list_mike_visit_prep") for preparing the guest room and house, which you are creating now. The checklist should include: deep clean guest room, vacuum all carpets and furniture, change air filters, wash all bedding in hot water, clean air vents, set up air purifier, stock allergy medications, and clean bathroom thoroughly.
        You also want a scene called "Guest Room Ready" (ID "scene_guest_ready") that creates a welcoming environment. It should set the East Bedroom ceiling light to 70% with a warm color (hue 30, saturation 20), the bedside lamp to 40% with the same color, open the curtains halfway, and set the AC to 23°C with low fan speed.
        Before making any changes, fetch the current state of all East Bedroom lights and curtains, and the AC. If any of these devices are already on, turn them off before running the scene.
        You want two reminders: one ("rem_mike_prep") on Thursday at 10 AM to start preparing, and another ("rem_mike_allergies") on Friday at 8 AM for a final allergy check for Do final allergy safety check before Mike arrives, notify via mobile push.
        Additionally, create a shopping list called "Mike Visit Supplies" (ID "list_mike_visit_supplies") with the following items: 1 pack of HEPA air filters, 1 bottle of allergy medication, and 1 box of hypoallergenic pillow covers.
        Also, before Mike arrives, fetch the state of the air purifier in the guest room (if present, or describe and add it if not), and ensure it is powered on and set to high mode for his visit. If you do not have an air purifier device, add a new device: ID "air_purifier_guest", type "air_purifier", name "Guest Room Air Purifier", vendor Levoit, model Core 300, firmware 1.0.0, located in the Guest Room, state_params: power, mode, filter_status; initial state: power off, mode auto, filter_status good.
        Use the RRULE "FREQ=MONTHLY;INTERVAL=3;BYDAY=4FR" (fourth Friday of every third month) for scheduling the scene and reminders, adjusting the day for the Thursday reminder.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"location": "East Bedroom"}}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"type": "ac"}}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "curtain_be",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "ac_home",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_mike_visit_prep",

                        "items": [
                            {"item": "Deep clean guest room", "quantity": 1},
                            {"item": "Vacuum all carpets and furniture", "quantity": 1},
                            {"item": "Change air filters", "quantity": 1},
                            {"item": "Wash all bedding in hot water", "quantity": 1},
                            {"item": "Clean air vents", "quantity": 1},
                            {"item": "Set up air purifier", "quantity": 1},
                            {"item": "Stock allergy medications", "quantity": 1},
                            {"item": "Clean bathroom thoroughly", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_guest_ready",
                        "actions": [
                            {
                                "device_id": "light_be_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 70,
                                    "color": {"hue": 30, "saturation": 20}
                                }
                            },
                            {
                                "device_id": "lamp_be_bedside",
                                "update": {
                                    "power": "on",
                                    "brightness": 40,
                                    "color": {"hue": 30, "saturation": 20}
                                }
                            },
                            {
                                "device_id": "curtain_be",
                                "update": {"power": "on", "position": 50}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 23,
                                    "fan_speed": "low"
                                }
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_mike_visit_supplies",

                        "items": [
                            {"item": "HEPA air filters (pack)", "quantity": 1},
                            {"item": "Allergy medication (bottle)", "quantity": 1},
                            {"item": "Hypoallergenic pillow covers (box)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"location": "Guest Room", "type": "air_purifier"}}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "air_purifier_guest",
                        "type": "air_purifier",
                        "location": "Guest Room",
                        "vendor": "Levoit",
                        "model": "Core 300",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "mode", "filter_status"],
                        "state": {"power": "off", "mode": "auto", "filter_status": "good"},
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "air_purifier_guest",
                    "updates": {"power": "on", "mode": "high"}
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_mike_prep",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_mike_visit_prep"
                        },
                        "trigger": {"rrule": "FREQ=MONTHLY;INTERVAL=3;BYDAY=4TH;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_mike_allergies",
                        "target": {
                            "type": "note",
                            "text": "Do final allergy safety check before Mike arrives"
                        },
                        "trigger": {"rrule": "FREQ=MONTHLY;INTERVAL=3;BYDAY=4FR;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_guest_ready",
                    "updates": {
                        "scheduled_runs": [],
                        "rrule": "FREQ=MONTHLY;INTERVAL=3;BYDAY=4FR;BYHOUR=16;BYMINUTE=0"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 24 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_24",
        instruction="""
        You want to create an ideal environment for Ethan's daily piano practice in the East Bedroom. He practices after school at 3:30 PM on weekdays. You want to create a "Piano Practice" scene (ID "scene_piano_practice").
        For good visibility, you want the ceiling light (ID "light_be_ceiling") at 90% brightness with a cool white light (4000K), and the bedside lamp (ID "lamp_be_bedside") at 60% with the same temperature. The curtains (ID "curtain_be") should be half-open.
        Before making any changes, fetch the current state of all East Bedroom lights and curtains to confirm their status. If any light or lamp is already on, turn it off before running the scene.
        You also want a practice checklist (ID "list_ethan_piano"), fill this list with the needed actions to piano practice: "Finger exercises (5 min)", "Scales practice (5 min)", "Review previous piece (10 min)", "Learn new section (10 min)" and "Fun piece / free play (5 min)".
        Additionally, create a shopping list called "Ethan Piano Supplies" (ID "list_ethan_piano_supplies") with the following items: 1 pack of music sheets, 1 metronome, and 1 bottle of hand sanitizer.
        You want two reminders: one to start practice at 3:30 PM ("rem_ethan_practice_start") and one to end at 4:00 PM ("rem_ethan_practice_end").
        Also, set a reminder ("rem_ethan_piano_supplies_check") every Monday at 8 AM to check the piano supplies list.
        Use the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" for all schedules. You are setting this up now for tomorrow.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"filters": {"location": "East Bedroom"}}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "curtain_be",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_piano_practice",
                        "actions": [
                            {
                                "device_id": "light_be_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 90,
                                    "color": {"kelvin": 4000}
                                }
                            },
                            {
                                "device_id": "lamp_be_bedside",
                                "update": {
                                    "power": "on",
                                    "brightness": 60,
                                    "color": {"kelvin": 4000}
                                }
                            },
                            {
                                "device_id": "curtain_be",
                                "update": {"power": "on", "position": 50}
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_ethan_piano",

                        "items": [
                            {"item": "Finger exercises (5 min)", "quantity": 1},
                            {"item": "Scales practice (5 min)", "quantity": 1},
                            {"item": "Review previous piece (10 min)", "quantity": 1},
                            {"item": "Learn new section (10 min)", "quantity": 1},
                            {"item": "Fun piece / free play (5 min)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_ethan_piano_supplies",

                        "items": [
                            {"item": "Music sheets (pack)", "quantity": 1},
                            {"item": "Metronome", "quantity": 1},
                            {"item": "Hand sanitizer (bottle)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_ethan_practice_start",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_ethan_piano"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=30"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_ethan_practice_end",
                        "target": {"type": "note", "text": "Great job, Ethan! Time to finish up practice."},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=16;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_ethan_piano_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_ethan_piano_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_piano_practice",
                    "updates": {
                        "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=30"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 25 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_25",
        instruction="""
        Emily would like to do yoga in the master bedroom on her days off (Thursday-Sunday) at 8 AM. You want to create a calming environment for her practice.
        You want a scene called "Morning Yoga" (ID "scene_morning_yoga") with these settings: master bedroom ceiling light (ID "light_br_ceiling") at 40% with a serene blue tint (hue 210, saturation 30), night lamp (ID "lamp_br_night") at 25% with the same color, curtains (ID "curtain_br") fully open, and AC (ID "ac_home") set to 24°C with the fan on low, to create a peaceful environment for Emily's yoga practice.
        Before making any changes, fetch the current state of the master bedroom ceiling light, night lamp, curtains, and AC to confirm their status. If any light or lamp is already on, turn it off before running the scene.
        You also want a shopping list (ID "list_emily_yoga_supplies") with the following items: 1 yoga mat, 2 yoga blocks, 1 water bottle, 1 towel, and 1 bottle of essential oils.
        Add a reminder at 7:45 AM ("rem_emily_yoga_prep") with note "Prepare yoga space", and another at 8:00 AM ("rem_emily_yoga_start") with note "Time to start your yoga practice - namaste!".
        Use the RRULE "FREQ=WEEKLY;BYDAY=TH,FR,SA,SU" for all schedules.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_br_ceiling", "lamp_br_night", "curtain_br", "ac_home"]}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_morning_yoga",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 40,
                                    "color": {"hue": 210, "saturation": 30}
                                }
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {
                                    "power": "on",
                                    "brightness": 25,
                                    "color": {"hue": 210, "saturation": 30}
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {"power": "on", "position": 100}
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 24,
                                    "fan_speed": "low"
                                }
                            }
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_emily_yoga_supplies",

                        "items": [
                            {"item": "Yoga mat", "quantity": 1},
                            {"item": "Yoga blocks", "quantity": 2},
                            {"item": "Water bottle", "quantity": 1},
                            {"item": "Towel", "quantity": 1},
                            {"item": "Essential oils (bottle)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emily_yoga_prep",
                        "target": {"type": "note", "text": "Prepare yoga space"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=TH,FR,SA,SU;BYHOUR=7;BYMINUTE=45"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_emily_yoga_start",
                        "target": {"type": "note", "text": "Time to start your yoga practice - namaste!"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=TH,FR,SA,SU;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_morning_yoga",
                    "updates": {
                        "rrule": "FREQ=WEEKLY;BYDAY=TH,FR,SA,SU;BYHOUR=7;BYMINUTE=45"
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 26 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_26",
        instruction="""
        You want better light-level awareness in the Living Room for automations. At 2 PM (2025-07-16), you placed a Zigbee Lux Sensor there.
        Its details are: ID "sensor_lr_lux", name "Living Room Lux Sensor", vendor Philips, model Hue Motion, firmware 1.2.0. It tracks illuminance and battery level. Initial reading: 250 lux, 97% battery.
        You want to add the sensor and attach it to the "living_room".
        Before making any changes, fetch the current state of the Living Room ceiling light (ID "light_lr_ceiling") to ensure it is off for safety before running any automation.
        You also want to extend the existing "Movie Time" scene to turn OFF the ceiling light if the lux value is below 50.
        Additionally, create a shopping list called "Living Room Lux Supplies" (ID "list_lr_lux_supplies") with the following items: 1 pack of AAA batteries for the sensor, 1 microfiber cloth for cleaning, and 1 replacement Zigbee module.
        Set a reminder (ID "rem_lr_lux_supplies_check") to check this list every Saturday at 10 AM.
        """,
        actions=[
            Action(
                name="add_sensor_to_database",
                kwargs={
                    "sensor": {
                        "id": "sensor_lr_lux",
                        "type": "sensor",
                        "location": "Living Room",
                        "vendor": "Philips",
                        "model": "Hue Motion",
                        "firmware_version": "1.2.0",
                        "state_params": ["illuminance_lux", "battery_level"],
                        "state": {
                            "illuminance_lux": 250,
                            "battery_level": 97,
                        },
                    }
                },
            ),
            Action(name="manage_room_in_database", kwargs={"action": "add_device_to_database", "room_id": "living_room", "device_id": "sensor_lr_lux"}),
            Action(name="get_device_by_id_or_filter", kwargs={"devices": ["light_lr_ceiling"]}),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(name="get_scene_by_id_or_filter", kwargs={"scene_id": "scene_movie_time"}),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_movie_time",
                    "updates": {
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}}
                        ]
                    },
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_lr_lux_supplies",

                        "items": [
                            {"item": "AAA batteries (pack)", "quantity": 1},
                            {"item": "Microfiber cloth", "quantity": 1},
                            {"item": "Zigbee module (replacement)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_lr_lux_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_lr_lux_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),
    # Task 27 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_27",
        instruction="""
        You want to automate late-night energy savings in your home. Create a scene called "Energy Save" (ID "scene_energy_save") that runs every night at 11:30 PM (RRULE "FREQ=DAILY;BYHOUR=23;BYMINUTE=30").
        The goal is to minimize unnecessary power usage after everyone is likely asleep. The scene should:
        - Turn off all living room lights.
        - Close the living room curtains to conserve heat/cool air.
        - Turn off major appliances that are not needed overnight, such as the AC and dishwasher.
        - Additionally, create a shopping list called "Energy Save Supplies" (ID "list_energy_save_supplies") with the following items: 1 pack of LED bulbs, 1 smart plug, and 1 power strip.
        - Set a reminder (ID "rem_energy_save_supplies_check") to check this list every Saturday at 10 AM.
        Set up the automation to run daily at 11:30 PM.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={
                    "filters": {
                        "location": "Living Room",
                    }
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_energy_save",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "light_lr_floor", "update": {"power": "off"}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 0}},
                            {"device_id": "ac_home", "update": {"power": "off"}},
                            {"device_id": "dishwasher_kt", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": [],
                        "rrule": "FREQ=DAILY;BYHOUR=23;BYMINUTE=30"
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_energy_save_supplies",

                        "items": [
                            {"item": "LED bulbs (pack)", "quantity": 1},
                            {"item": "Smart plug", "quantity": 1},
                            {"item": "Power strip", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_energy_save_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_energy_save_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 28 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_28",
        instruction="""
        You want to set up a basic grocery shopping system. You want a list called "Weekly Groceries" (ID "list_weekly_groceries") and a reminder to check it every Sunday morning.
        The list should start with your family's regular items: 2 gallons of milk, 1 loaf of bread, 1 dozen eggs, 2 packs of cheese, 1 bag of apples, and 3 boxes of cereal.
        You also want to add two more items to the list: 1 bottle of olive oil and 1 pack of paper towels.
        Additionally, you want to track the kitchen refrigerator's status to ensure it's off before adding perishable groceries. The fridge plug (ID "plug_kt_fridge") is a TP-Link KP115 smart plug, type "outlet", vendor TP-Link, model KP115, firmware 1.0.0, located in the Kitchen, tracks power and energy usage, initial state: power on, energy_kwh 0.0.
        If the fridge plug is off, turn it on before adding groceries to the list.
        You want a reminder (ID "rem_grocery_check") that goes off at 9 AM every Sunday (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=9;BYMINUTE=0") to review the list.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "plug_kt_fridge",
                        "type": "outlet",
                        "location": "Kitchen",
                        "vendor": "TP-Link",
                        "model": "KP115",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "energy_kwh"],
                        "state": {
                            "power": "on",
                            "energy_kwh": 0.0
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "plug_kt_fridge",
                    "updates": {"power": "on"}
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_weekly_groceries",
                        "items": [
                            {"item": "Milk (gallon)", "quantity": 2},
                            {"item": "Bread", "quantity": 1},
                            {"item": "Eggs (dozen)", "quantity": 1},
                            {"item": "Cheese (pack)", "quantity": 2},
                            {"item": "Apples (bag)", "quantity": 1},
                            {"item": "Cereal (box)", "quantity": 3},
                            {"item": "Olive oil (bottle)", "quantity": 1},
                            {"item": "Paper towels (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_grocery_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_weekly_groceries"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 29 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_29",
        instruction="""
        You want to create a cozy reading light scene for the living room that you can activate manually.
        To ensure the environment is always comfortable, first fetch the current states of the living room lights, curtains, AC, and the living room air-quality sensor (ID "sensor_lr_air_quality") before setting up the scene.
        Then, create a scene called "Reading Light" (ID "scene_reading_light") that sets the floor lamp (ID "light_lr_floor") to 70% brightness, turns off the ceiling light (ID "light_lr_ceiling"), closes the curtains (ID "curtain_lr") halfway, and sets the AC (ID "ac_home") to a comfortable 23°C with the fan on low.
        Additionally, ensure the living room TV (ID "tv_lr") is off before running the scene. The TV is a Samsung Q60T, firmware 1.0.0, located in the Living Room, tracks power and input, initial state: power off, input "HDMI1". If the TV is not present, add it with all parameters and attach it to the living room.
        Also, create a shopping list called "Reading Light Supplies" (ID "list_reading_light_supplies") with the following items: 1 pack of LED bulbs, 1 bottle of screen cleaner, and 1 reading pillow.
        You are setting this up now and do not want to schedule it.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_lr_floor"]}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_lr_ceiling"]}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["curtain_lr"]}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["ac_home"]}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["tv_lr"]}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "tv_lr",
                        "type": "tv",
                        "location": "Living Room",
                        "vendor": "Samsung",
                        "model": "Q60T",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "input"],
                        "state": {
                            "power": "off",
                            "input": "HDMI1"
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "tv_lr"
                }
            ),
            Action(
                name="get_sensor_by_id_or_filter",
                kwargs={"sensor": "sensor_lr_air_quality"}
            ),
            Action(
                name="manage_room_in_database",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "sensor_lr_air_quality"
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "tv_lr",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_reading_light",
                        "actions": [
                            {"device_id": "light_lr_floor", "update": {"power": "on", "brightness": 70}},
                            {"device_id": "light_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 50}},
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 23,
                                    "fan_speed": "low"
                                }
                            }
                        ],
                        "scheduled_runs": []
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_reading_light_supplies",

                        "items": [
                            {"item": "LED bulbs (pack)", "quantity": 1},
                            {"item": "Screen cleaner (bottle)", "quantity": 1},
                            {"item": "Reading pillow", "quantity": 1}
                        ]
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 30 ------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_30",
        instruction="""
        Since Emily likes to make special breakfasts on weekends, you want to set up a reminder and shopping list for it.
        You want a list (ID "list_weekend_breakfast") with common ingredients: 2 packs of bacon, 1 carton of pancake mix, 1 bottle of maple syrup, 2 packs of berries, and 1 carton of whipping cream.
        You also want to add 1 bottle of orange juice and 1 pack of coffee beans to the list, as these are often needed for breakfast.
        The fridge plug is a TP-Link KP115 smart plug, type "outlet", vendor TP-Link, model KP115, firmware 1.0.0, located in the Kitchen, tracks power and energy usage, initial state: power on, energy_kwh 0.0. If the fridge plug is off, turn it on.
        You also want a reminder (ID "rem_weekend_breakfast") that goes off at 7 PM every Friday (RRULE "FREQ=WEEKLY;BYDAY=FR;BYHOUR=19;BYMINUTE=0") to check the ingredients list, send it to mobile, with priority normal.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "plug_kt_fridge",
                        "type": "outlet",
                        "location": "Kitchen",
                        "vendor": "TP-Link",
                        "model": "KP115",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "energy_kwh"],
                        "state": {
                            "power": "on",
                            "energy_kwh": 0.0
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "plug_kt_fridge",
                    "updates": {"power": "on"}
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_weekend_breakfast",
                        "items": [
                            {"item": "Bacon (pack)", "quantity": 2},
                            {"item": "Pancake mix", "quantity": 1},
                            {"item": "Maple syrup", "quantity": 1},
                            {"item": "Fresh berries (pack)", "quantity": 2},
                            {"item": "Whipping cream", "quantity": 1},
                            {"item": "Orange juice (bottle)", "quantity": 1},
                            {"item": "Coffee beans (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_weekend_breakfast",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_weekend_breakfast"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=FR;BYHOUR=19;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 31 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_31",
        instruction="""
        You want to integrate two new smart ceiling fans you just installed at 2 PM today.
        The first is in the Living Room: ID "fan_lr_ceiling", name "Living Room Ceiling Fan", vendor Hunter, model Signal, firmware 1.0.0.
        The second is in the Master Bedroom: ID "fan_br_ceiling", name "Master Bedroom Ceiling Fan", vendor Haiku, model I-Series, firmware 2.3.1.
        Both support power, speed, and direction, and are currently off, speed 0, direction "forward".
        You want to add both fans to the inventory, append them to their respective room records ("living_room" and "bedroom_master").
        You want to update the "Good Morning" scene to turn both on at 70% speed (forward direction), and update the "Good Night" scene to turn both off.
        Additionally, create a shopping list called "Ceiling Fan Supplies" (ID "list_ceiling_fan_supplies") with the following items: 1 AAA batteries, 1 fan cleaning spray, and 1 microfiber cloth.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "fan_lr_ceiling",
                        "type": "fan",
                        "location": "Living Room",
                        "vendor": "Hunter",
                        "model": "Signal",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "speed", "direction"],
                        "state": {
                            "power": "off",
                            "speed": 0,
                            "direction": "forward",
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "fan_br_ceiling",
                        "type": "fan",
                        "location": "Master Bedroom",
                        "vendor": "Haiku",
                        "model": "I Series",
                        "firmware_version": "2.3.1",
                        "state_params": ["power", "speed", "direction"],
                        "state": {
                            "power": "off",
                            "speed": 0,
                            "direction": "forward",
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="manage_room_in_database",
                kwargs={"action": "add_device_to_database", "room_id": "living_room", "device_id": "fan_lr_ceiling"},
            ),
            Action(
                name="manage_room_in_database",
                kwargs={"action": "add_device_to_database", "room_id": "bedroom_master", "device_id": "fan_br_ceiling"},
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_good_morning",
                    "updates": {
                        "actions": [
                            {"device_id": "fan_lr_ceiling", "update": {"power": "on", "speed": 70, "direction": "forward"}},
                            {"device_id": "fan_br_ceiling", "update": {"power": "on", "speed": 70, "direction": "forward"}}
                        ]
                    },
                },
            ),
            Action(
                name="update_scene_in_database",
                kwargs={
                    "scene_id": "scene_good_night",
                    "updates": {
                        "actions": [
                            {"device_id": "fan_lr_ceiling", "update": {"power": "off"}},
                            {"device_id": "fan_br_ceiling", "update": {"power": "off"}}
                        ]
                    },
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_ceiling_fan_supplies",

                        "items": [
                            {"item": "AAA batteries", "quantity": 1},
                            {"item": "Fan cleaning spray", "quantity": 1},
                            {"item": "Microfiber cloth", "quantity": 1}
                        ]
                    }
                }
            ),
        ],
        outputs=[],
    ),

    # Task 32 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_32",
        instruction="""
        The Living-Room air-quality sensor (ID "sensor_lr_air_quality") has a low battery (15%) as of 4 PM today (2025-07-15).
        You want to create a reminder (ID "rem_air_sensor_battery") for tomorrow at 9 AM to swap the batteries. This should be a normal priority phone notification with a 10-minute snooze default, call it Replace Living-Room Air-Quality-Sensor, and send a note that says Swap AAA cells in LR AQ sensor to mobile.
        Additionally, create a shopping list called "Air Sensor Battery Supplies" (ID "list_air_sensor_battery_supplies") with the following items: 2 AAA batteries, 1 microfiber cloth, and 1 pack of disposable gloves.
        Since a dead battery could block the "Heatwave Day" safety automation, you also want to update that scene to turn the AC off if the sensor's battery_level ever drops to less than 5%.
        """,
        actions=[
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_air_sensor_battery",
                        "target": {"type": "note", "text": "Swap AAA cells in LR AQ sensor"},
                        "trigger": {"datetime": "2025-07-16T09:00:00"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal", "snooze_default_min": 10},
                        "status": "scheduled",
                    }
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_air_sensor_battery_supplies",

                        "items": [
                            {"item": "AAA batteries (pack)", "quantity": 2},
                            {"item": "Microfiber cloth", "quantity": 1},
                            {"item": "Disposable gloves (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_heatwave_day",
                        "actions": [
                             {"device_id": "ac_home", "update": {"power": "off"}}
                        ]
                    },
                    "threshold": {
                        "sensor_lr_air_quality": {'operator': 'lt', 'value': 5}
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 33 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_33",
        instruction="""
        To combat stuffiness in the basement, you want to set up continuous CO₂ monitoring starting today (2025-07-15, 5 PM).
        You want to add a new sensor: ID "sensor_bs_co2", name "Basement CO2 Sensor", vendor Awair, model CO₂ Mini, firmware 1.0.0, located in the Basement. It tracks co2_ppm and battery_level. Initial state: 900 ppm, 100% battery.
        You want to attach it to the basement room record.
        You also want a "Basement Ventilation" scene (ID "scene_basement_vent") that turns the AC (ID "ac_home") to fan-only mode at high speed and turns the heater (ID "heater_home") off. This scene should run daily at 8 AM (RRULE "FREQ=DAILY;BYHOUR=8;BYMINUTE=0").
        For safety, you want to program the AC itself with an identical scheduled update.
        You also want to create a shopping list called "Basement Ventilation Supplies" (ID "list_basement_vent_supplies") with the following items: 1 replacement air filter, 1 bottle of cleaning spray, and 1 pack of disposable gloves.
        Set a reminder (ID "rem_basement_vent_supplies_check") to check this list every Monday at 9 AM.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "sensor_bs_co2",
                        "type": "sensor",
                        "location": "Basement",
                        "vendor": "Awair",
                        "model": "CO2 Mini",
                        "firmware_version": "1.0.0",
                        "state_params": ["co2_ppm", "battery_level"],
                        "state": {
                            "co2_ppm": 900,
                            "battery_level": 100,
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="manage_room_in_database",
                kwargs={"action": "add_device_to_database", "room_id": "basement", "device_id": "sensor_bs_co2"},
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_basement_vent",
                        "actions": [
                            {"device_id": "ac_home", "update": {"power": "on", "mode": "fan", "fan_speed": "high"}},
                            {"device_id": "heater_home", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": [],
                        "rrule": "FREQ=DAILY;BYHOUR=8;BYMINUTE=0"
                    }
                },
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "ac_home",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "mode": "fan", "fan_speed": "high"},
                                "rrule": "FREQ=DAILY;BYHOUR=8;BYMINUTE=0",
                            }
                        ]
                    },
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_basement_vent_supplies",

                        "items": [
                            {"item": "Replacement air filter", "quantity": 1},
                            {"item": "Cleaning spray (bottle)", "quantity": 1},
                            {"item": "Disposable gloves (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_basement_vent_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_basement_vent_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 34 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_34",
        instruction="""
        You want to upgrade your kitchen's fire safety. At 6 PM today (2025-07-15), you mounted a Nest Protect v4 smoke and CO detector.
        Its details are: ID "sensor_kt_smoke", name "Kitchen Smoke & CO Detector", vendor Google, model Nest Protect v4, firmware 4.0.0, located in the Kitchen. It tracks smoke, CO, and battery level. Its initial state is all clear (false, false, 100% battery).
        You want to register the detector and attach it to the kitchen room.
        You also want an emergency scene "scene_fire_alert" that, when triggered, turns all Living Room and Kitchen ceiling lights to full brightness white (100% brightness, 6000K), opens all curtains fully ("curtain_lr", "curtain_br", "curtain_bw", "curtain_be"), and powers off both the heater and the AC.
        Additionally, create a shopping list called "Kitchen Fire Safety Supplies" (ID "list_kitchen_fire_safety_supplies") with the following items: 1 fire extinguisher, 1 pack of smoke detector batteries, and 1 emergency escape plan printout.
        Also, add a monthly high-priority reminder (ID "rem_kitchen_smoke_test") on the 1st of each month at 9 AM to test the detector (RRULE "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0").
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "sensor_kt_smoke",
                        "type": "sensor",
                        "location": "Kitchen",
                        "vendor": "Google",
                        "model": "Nest Protect v4",
                        "firmware_version": "4.0.0",
                        "state_params": ["smoke_detected", "co_detected", "battery_level"],
                        "state": {
                            "smoke_detected": False,
                            "co_detected": False,
                            "battery_level": 100,
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="manage_room_in_database",
                kwargs={"action": "add_device_to_database", "room_id": "kitchen", "device_id": "sensor_kt_smoke"}
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_fire_alert",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "on", "brightness": 100, "color": {"kelvin": 6000}}},
                            {"device_id": "light_lr_floor", "update": {"power": "on", "brightness": 100, "color": {"kelvin": 6000}}},
                            {"device_id": "light_kt_ceiling", "update": {"power": "on", "brightness": 100, "color": {"kelvin": 6000}}},
                            {"device_id": "curtain_lr", "update": {"power": "on", "position": 100}},
                            {"device_id": "curtain_br", "update": {"power": "on", "position": 100}},
                            {"device_id": "curtain_bw", "update": {"power": "on", "position": 100}},
                            {"device_id": "curtain_be", "update": {"power": "on", "position": 100}},
                            {"device_id": "heater_home", "update": {"power": "off"}},
                            {"device_id": "ac_home", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": []
                    }
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_kitchen_fire_safety_supplies",

                        "items": [
                            {"item": "Fire extinguisher", "quantity": 1},
                            {"item": "Smoke detector batteries (pack)", "quantity": 1},
                            {"item": "Emergency escape plan printout", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_kitchen_smoke_test",
                        "target": {"type": "device", "entity_type": "device", "entity_id": "sensor_kt_smoke"},
                        "trigger": {"rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                },
            ),
        ],
        outputs=[]
    ),

    # Task 35 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_35",
        instruction="""
        To combat low humidity in the master bedroom, you are adding a smart humidifier and a humidity sensor tonight.
        You want to add two devices:
        - Humidifier: ID "humidifier_br", name "Master Bedroom Humidifier", vendor Levoit, model Classic300-S, firmware 1.1.0. It tracks power, target humidity, and water level. Initial state: off, target 45%, water 100%.
        - Sensor: ID "sensor_br_humidity", name "Master Bedroom Humidity Sensor", vendor Xiaomi, model Mi Hygrometer 2, firmware 1.0.0. It tracks humidity, temperature, and battery. Initial readings: 34% RH, 22.5°C, 92% battery.
        You want to add both devices to the master bedroom and create a nightly automation. This includes a scene "scene_humidity_night" that turns the humidifier on at 1 AM with a target humidity of 45%. You want to program the humidifier with a matching scheduled update (RRULE "FREQ=DAILY;BYHOUR=1;BYMINUTE=0").
        Before making any changes, fetch the current state of both the humidifier and the humidity sensor to confirm their status.
        To ensure safety, fetch the current state of the master bedroom ceiling light (ID "light_br_ceiling") and turn it off if it is on before running the humidifier at night.
        Additionally, create a shopping list called "Humidifier Supplies" (ID "list_humidifier_supplies") with the following items: 1 bottle of distilled water, 1 pack of humidifier filters, and 1 cleaning brush.
        Set a reminder "rem_fill_humidifier" every two days at 7 PM to top up the water (RRULE "FREQ=DAILY;INTERVAL=2;BYHOUR=19;BYMINUTE=0").
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["humidifier_br", "sensor_br_humidity"]}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_br_ceiling"]}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "humidifier_br",
                        "type": "humidifier",
                        "location": "Master Bedroom",
                        "vendor": "Levoit",
                        "model": "Classic300-S",
                        "firmware_version": "1.1.0",
                        "state_params": ["power", "target_humidity_pct", "water_level_pct"],
                        "state": {
                            "power": "off",
                            "target_humidity_pct": 45,
                            "water_level_pct": 100,
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "sensor_br_humidity",
                        "type": "sensor",
                        "location": "Master Bedroom",
                        "vendor": "Xiaomi",
                        "model": "Mi Hygrometer 2",
                        "firmware_version": "1.0.0",
                        "state_params": ["humidity_pct", "temperature_c", "battery_level"],
                        "state": {
                            "humidity_pct": 34,
                            "temperature_c": 22.5,
                            "battery_level": 92,
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(name="manage_room_in_database", kwargs={"action": "add_device_to_database", "room_id": "bedroom_master", "device_id": "humidifier_br"}),
            Action(name="manage_room_in_database", kwargs={"action": "add_device_to_database", "room_id": "bedroom_master", "device_id": "sensor_br_humidity"}),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_humidity_night",
                        "actions": [
                            {"device_id": "humidifier_br", "update": {"power": "on", "target_humidity_pct": 45}}
                        ]
                    }
                },
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "humidifier_br",
                    "updates": {
                        "scheduled_updates": [
                            {
                                "update": {"power": "on", "target_humidity_pct": 45},
                                "rrule": "FREQ=DAILY;BYHOUR=1;BYMINUTE=0"
                            }
                        ]
                    },
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_humidifier_supplies",

                        "items": [
                            {"item": "Distilled water (bottle)", "quantity": 1},
                            {"item": "Humidifier filters (pack)", "quantity": 1},
                            {"item": "Cleaning brush", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_fill_humidifier",
                        "target": {"type": "device", "entity_type": "device", "entity_id": "humidifier_br"},
                        "trigger": {"rrule": "FREQ=DAILY;INTERVAL=2;BYHOUR=19;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                },
            ),
        ],
        outputs=[]
    ),

    # Task 36 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_36",
        instruction="""
        The central AC (ID "ac_home") has a new firmware version (2.2.0) and you want to update its record as of 8 AM today (2025-07-24).
        You want to create a shopping list called "AC Maintenance Supplies" (ID "list_ac_maintenance_supplies") with the following items: 1 replacement air filter, 1 bottle of coil cleaner, and 1 pack of disposable gloves.
        Finally, set a yearly maintenance reminder for the AC (ID "rem_ac_annual_service") on August 1st at 10 AM (RRULE "FREQ=YEARLY;BYMONTH=8;BYMONTHDAY=1;BYHOUR=10;BYMINUTE=0").
        """,
        actions=[
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "ac_home",
                    "updates": {
                        "firmware_version": "2.2.0",
                        "state": {
                            "power": "off",
                            "mode": "cool",
                            "setpoint_c": 24,
                            "fan_speed": "medium"
                        },
                        "scheduled_updates": []
                    },
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_ac_maintenance_supplies",

                        "items": [
                            {"item": "Replacement air filter", "quantity": 1},
                            {"item": "Coil cleaner (bottle)", "quantity": 1},
                            {"item": "Disposable gloves (pack)", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_ac_annual_service",
                        "target": {"type": "device", "entity_type": "device", "entity_id": "ac_home"},
                        "trigger": {"rrule": "FREQ=YEARLY;BYMONTH=8;BYMONTHDAY=1;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "email"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                },
            ),
        ],
        outputs=[]
    ),

    # Task 37 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_37",
        instruction="""
        For better perimeter coverage, you mounted an extra security camera in the side yard today (2025-07-16, 11 AM).
        The device details are: ID "camera_side_yard", name "Side-Yard Security Camera", vendor Eufy, model Cam 3C-Lite, firmware 1.0.0, located in the Backyard. It tracks stream status, motion, person, and threat detection, and recording status. Initial state: stream on, recording on, all detections false.
        You want to add it, attach it to the "living_room" room (as it's the closest network segment), and extend the existing "Away Mode" scene to ensure this camera is also recording when the scene is active.
        Before making any changes, fetch the current state of the camera_side_yard to confirm its status.
        Additionally, you want to ensure the living room ceiling light (ID "light_lr_ceiling") is off for security at night, so fetch its state and turn it off if needed.
        You also want to create a shopping list called "Side Yard Security Supplies" (ID "list_side_yard_security_supplies") with the following items: 1 Security camera warning sign, 1 AA batteries, and 1 Lens cleaning cloth.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["camera_side_yard"]}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "camera_side_yard",
                        "type": "camera",
                        "location": "Backyard",
                        "vendor": "Eufy",
                        "model": "Cam 3C-Lite",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "stream_online",
                            "motion_detected",
                            "person_detected",
                            "threat_detected",
                            "recording"
                        ],
                        "state": {
                            "stream_online": True,
                            "motion_detected": False,
                            "person_detected": False,
                            "threat_detected": False,
                            "recording": True,
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="manage_room_in_database",
                kwargs={"action": "add_device_to_database", "room_id": "living_room", "device_id": "camera_side_yard"}
            ),
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_lr_ceiling"]}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_away_mode",
                        "actions": [
                            {"device_id": "camera_side_yard", "update": {"recording": True, "stream_online": True}}
                        ]
                    }
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_side_yard_security_supplies",

                        "items": [
                            {"item": "Security camera warning sign", "quantity": 1},
                            {"item": "AA batteries", "quantity": 1},
                            {"item": "Lens cleaning cloth", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(name="get_scene_by_id_or_filter", kwargs={"scene_id": "scene_away_mode"}),
        ],
        outputs=[]
    ),

    # Task 38 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        You want an automatic energy-saver that kicks in every night. You want to create a scene called "scene_energy_saver" that runs at 12:05 AM each day, starting tonight, call it Night Energy Saver.
        The scene should dim all ceiling lights ("light_lr_ceiling", "light_br_ceiling", "light_bw_ceiling", "light_be_ceiling") to 30% and turn off the AC ("ac_home") and heater ("heater_home").
        Before making any changes, fetch the current state of all ceiling lights, AC, and heater to confirm their status.
        Additionally, you want to ensure the living room TV (ID "tv_lr") is off for energy savings; if not present, add it: type "tv", vendor Samsung, model Q60T, firmware 1.0.0, location Living Room, tracks power and input, initial state: power off, input "HDMI1".
        You also want to create a shopping list called "Night Energy Saver Supplies" (ID "list_energy_saver_supplies") with the following items: 1 pack of LED bulbs, 1 smart plug, and 1 power strip.
        Set a reminder (ID "rem_energy_saver_supplies_check") to check this list every Saturday at 10 AM.
        Use the RRULE "FREQ=DAILY;BYHOUR=0;BYMINUTE=5" for scheduling.
        """,
        actions=[
            Action(
                name="get_device_by_id_or_filter",
                kwargs={"devices": ["light_lr_ceiling", "light_br_ceiling", "light_bw_ceiling", "light_be_ceiling", "ac_home", "heater_home"]}
            ),
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "tv_lr",
                        "type": "tv",
                        "location": "Living Room",
                        "vendor": "Samsung",
                        "model": "Q60T",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "input"],
                        "state": {
                            "power": "off",
                            "input": "HDMI1"
                        },
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "tv_lr",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_energy_saver",
                        "actions": [
                            {"device_id": "light_lr_ceiling", "update": {"power": "on", "brightness": 30}},
                            {"device_id": "light_br_ceiling", "update": {"power": "on", "brightness": 30}},
                            {"device_id": "light_bw_ceiling", "update": {"power": "on", "brightness": 30}},
                            {"device_id": "light_be_ceiling", "update": {"power": "on", "brightness": 30}},
                            {"device_id": "ac_home", "update": {"power": "off"}},
                            {"device_id": "heater_home", "update": {"power": "off"}},
                            {"device_id": "tv_lr", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": [],
                        "rrule": "FREQ=DAILY;BYHOUR=0;BYMINUTE=5"
                    }
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_energy_saver_supplies",

                        "items": [
                            {"item": "LED bulbs (pack)", "quantity": 1},
                            {"item": "Smart plug", "quantity": 1},
                            {"item": "Power strip", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_energy_saver_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_energy_saver_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            )
        ],
        outputs=[]
    ),

    # Task 39 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_39",
        instruction="""
        The hallway can be dark at night, so you want a soft automatic light to turn on when motion is detected after 10 PM. You already have a Hallway Motion Sensor (ID "sensor_hall_motion").
        You want to create a scene "scene_night_motion" that, when run, turns the Living Room floor lamp ("light_lr_floor") ON at 15% brightness for 3 minutes, then turns it back OFF (the runtime engine can handle the timer, so just include the on/off updates).
        Additionally, create a shopping list called "Hallway Night Light Supplies" (ID "list_hallway_night_light_supplies") with the following items: 1 pack of LED bulbs, 1 motion sensor battery, and 1 nightlight cover.
        Set a reminder (ID "rem_hallway_night_light_supplies_check") to check this list every Saturday at 10 AM.
        Schedule the scene to arm itself each evening at 10 PM using the RRULE "FREQ=DAILY;BYHOUR=22;BYMINUTE=0".
        """,
        actions=[
            Action(
                name="add_scene_to_database",
                kwargs={
                    "scene": {
                        "id": "scene_night_motion",
                        "actions": [
                            {"device_id": "light_lr_floor", "update": {"power": "on", "brightness": 15}},
                            {"device_id": "light_lr_floor", "update": {"power": "off"}}
                        ],
                        "scheduled_runs": [],
                        "rrule": "FREQ=DAILY;BYHOUR=22;BYMINUTE=0"
                    }
                },
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_hallway_night_light_supplies",

                        "items": [
                            {"item": "LED bulbs (pack)", "quantity": 1},
                            {"item": "Motion sensor battery", "quantity": 1},
                            {"item": "Nightlight cover", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_hallway_night_light_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_hallway_night_light_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SA;BYHOUR=10;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),

    # Task 40 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_40",
        instruction="""
        Your refrigerator is now on an energy-monitoring smart plug that you installed at 1 PM today (2025-07-16).
        The details are: ID "plug_kt_fridge", type "outlet", name "Kitchen Fridge Plug", vendor TP-Link, model KP115, firmware 1.0.0, located in the Kitchen. It tracks power and energy usage. Initial state: power on, 0.0 kWh.
        You want to add the plug and attach it to the kitchen room.
        To ensure safety, if the fridge plug is off, turn it on before any automation.
        You also want to create a shopping list called "Fridge Maintenance Supplies" (ID "list_fridge_maintenance_supplies") with the following items: 1 bottle of cleaning spray, 1 pack of microfiber cloths, and 1 fridge thermometer.
        Additionally, create a reminder ("rem_check_fridge_energy") every Sunday at 8 AM (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=8;BYMINUTE=0") to review the fridge plug's energy report.
        Set another reminder ("rem_fridge_supplies_check") every Monday at 9 AM to check the fridge maintenance supplies list.
        """,
        actions=[
            Action(
                name="add_device_to_database",
                kwargs={
                    "device": {
                        "id": "plug_kt_fridge",
                        "type": "outlet",
                        "location": "Kitchen",
                        "vendor": "TP-Link",
                        "model": "KP115",
                        "firmware_version": "1.0.0",
                        "state_params": ["power", "energy_kwh"],
                        "state": {
                            "power": "on",
                            "energy_kwh": 0.0,
                        },
                        "scheduled_updates": []
                    }
                },
            ),
            Action(
                name="manage_room_in_database",
                kwargs={"action": "add_device_to_database", "room_id": "kitchen", "device_id": "plug_kt_fridge"}
            ),
            Action(
                name="update_device_in_database",
                kwargs={
                    "device_id": "plug_kt_fridge",
                    "updates": {"power": "on"}
                }
            ),
            Action(
                name="add_custom_list_to_database",
                kwargs={
                    "custom_list": {
                        "list_id": "list_fridge_maintenance_supplies",

                        "items": [
                            {"item": "Cleaning spray (bottle)", "quantity": 1},
                            {"item": "Microfiber cloths (pack)", "quantity": 1},
                            {"item": "Fridge thermometer", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_check_fridge_energy",
                        "target": {"type": "device", "entity_type": "device", "entity_id": "plug_kt_fridge"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=SU;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                },
            ),
            Action(
                name="add_reminder_to_database",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_fridge_supplies_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_fridge_maintenance_supplies"
                        },
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
        ],
        outputs=[]
    ),
]
