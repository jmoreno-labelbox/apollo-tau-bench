from domains.dto import Task, Action

TASKS = [
    # Task 1 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_01",
        instruction="""
        You wish to set up your TP-Link Kasa HS110 smart plug for the coffee maker in the kitchen, ensuring that coffee is ready when you wake up.
        Aim to configure the plug using the ID "plug_kt_coffee" and the name "Kitchen Coffee Maker Plug". The model is TP-Link Kasa HS110 with firmware 1.0.0, designed to track power and energy consumption. Initially, it should be 'off' with no energy usage recorded.
        Upon adding the device, add it to the kitchen's device list and schedule it to activate automatically at 6:45 AM daily.
        For safety, verify the current state of the plug before any modifications; if it is already turned on, switch it off before setting up the automation.
        Moreover, create a shopping list titled "Coffee Supplies" (ID "list_coffee_supplies") that includes: 1 pack of coffee beans, 1 bottle of milk, and 1 box of filters. Schedule a reminder (ID "rem_coffee_supplies_check") to check this list every Saturday at 10 AM.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "kitchen",
                    "device_id": "plug_kt_coffee"
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "plug_kt_coffee",
                    "updates": {
                        "power": "off"
                    }
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        You aim to replace a malfunctioning desk lamp (ID "lamp_bw_desk") in your daughter's room, the West Bedroom.
        Remove the old lamp from both the room's device list and the central inventory, ensuring it is turned off before you proceed with the removal.
        Proceed to set up the new lamp, an Ikea Nymåne LED model, with the ID "lamp_bw_desk2" and the name "West Bedroom New Desk Lamp". This lamp allows for brightness and color temperature adjustments, starting in the 'off' state with 0 brightness and a color temperature of 4000K.
        Add the new lamp to the West Bedroom's device list and integrate it into the "Good Night" scene. Within this scene, it should illuminate at 15% brightness with a warm color (hue 30).
        Additionally, create a shopping list named "Desk Lamp Replacement Supplies" (ID "list_desk_lamp_supplies"), including: 1 Ikea Nymåne LED lamp, 1 spare LED bulb, and 1 pack of cable ties.
        Lastly, set up a reminder (ID "rem_check_lamp_install") to assess the installation and cable management of the new lamp each Friday at 5 PM.
        """,
        actions=[
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "remove_device",
                    "room_id": "bedroom_west",
                    "device_id": "lamp_bw_desk"
                }
            ),
            Action(
                name="DeleteDeviceFromDatabase",
                kwargs={"device_id": "lamp_bw_desk"}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "bedroom_west",
                    "device_id": "lamp_bw_desk2"
                }
            ),
            Action(
                name="UpdateSceneInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        In order to assist your daughter Emma with her summer art project, initiate creating a new list named "Olivia Art Supplies" (ID "list_olivia_art_supplies").
        Begin the list with the following items: 1 Acrylic Paint Set, 5 Canvas Panels (8x10 size), 1 Brush Pack, and 4 Glue Sticks.
        Additionally, include 2 Glitter Packs and 1 Sketchbook (A4 size) in the list, along with 1 pack of colored pencils.
        Furthermore, establish a reminder (ID "rem_olivia_art_review") to review this list every Saturday at 10 AM, set as a normal priority mobile notification titled Review Emma Art Supply List.
        """,
        actions=[
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_olivia_art_review",
                        "name": "Review Emma Art Supply List",
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
        Organize the system for your new babysitter, Emma Marie Green (nickname "Em"). Add her as a member with the ID "emma_green". She is a college student at SFSU studying Early-Childhood Education, born on February 12, 2002. Her contact information is +1-415-555-8888 and emma.green@example.com.
        Although she will not reside in the house, she will visit every Friday evening at 5:00 PM. Note that she does not drive and has a gluten allergy.
        Compile a list of her favorite snacks (ID "list_emma_snacks") that includes 6 Granola Bars and 3 Sparkling Waters.
        To ensure Emma is fully equipped, generate a shopping list titled "Emma Babysitting Supplies" (ID "list_emma_supplies") containing these items: 1 pack of gluten-free granola bars, 1 bottle of hand sanitizer, and 1 box of colored pencils for activities.
        Prior to implementing any changes, integrate the living room TV (ID "tv_lr") into the system: type "tv", name "Living Room TV", vendor Samsung, model Q60T, firmware 1.0.0, located in the Living Room, tracks power and input, initial state: power off, input "HDMI1".
        Lastly, establish a reminder (ID "rem_emma_snack_prep") to activate at 4:30 PM every Friday for preparing her snacks before her arrival, and another reminder (ID "rem_emma_supplies_check") set to inspect the babysitting supplies list every Friday at 3:30 PM.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageMemberInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
        Anticipate a severe heatwave this afternoon, and establish a new scene labeled "Heatwave Day" (ID "scene_heatwave_day") to maintain a cool environment at home.
        The scene should draw all curtains (in the living room, master bedroom, and west bedroom), adjust the AC to cooling mode at 22°C with the fan set to high, and confirm the heater is switched off.
        Schedule this scene to activate at 2 PM today. Additionally, ensure the schedule is saved directly onto the AC unit as a backup and eliminate any pre-existing scheduled instructions on the heater to stop it from turning on.
        Further, generate a shopping list titled "Heatwave Essentials" (ID "list_heatwave_essentials") including the following items: 2 bottles of water, 1 pack of ice, and 1 portable fan.
        Set a reminder (ID "rem_heatwave_essentials_check") to review this list at noon today.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"type": "curtain"}}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"type": "ac"}}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"type": "heater"}}
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "heater_home",
                    "updates": {"scheduled_updates": []}
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        To provide adequate lighting for the children to read in their bedrooms, configure an automated schedule for all bedroom ceiling lights.
        Arrange the ceiling lights in the master, west, and east bedrooms (IDs "light_br_ceiling", "light_bw_ceiling", "light_be_ceiling") to illuminate daily at 7 PM and set them to 60% brightness.
        Ensure all bedroom desk lamps ("lamp_br_night", "lamp_bw_desk", "lamp_be_bedside") are turned off before activating the ceiling lights.
        Additionally, compile a shopping list named "Bedroom Reading Supplies" (ID "list_bedroom_reading_supplies") with the following items: 3 reading lamps, 3 packs of AA batteries, and 3 bookmarks.
        Schedule a reminder (ID "rem_bedroom_reading_check") to assess this list every Saturday at 5 PM.
        Implement the exact RRULE string "FREQ=DAILY;BYHOUR=19;BYMINUTE=0" for scheduling to guarantee synchronization of all lights.
        """,
        actions=[
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        You have installed a new Arlo Essential XL security camera in the garage today and want to set it up. Aim to name it "Garage Security Camera" with an ID of "camera_garage" and firmware version 1.0.0.
        The camera is capable of detecting motion, people, and threats, in addition to streaming and recording. Initially, it is in a state where streaming is up, recording is on, but there's no detection of motion, people, or threats.
        As the garage is part of the basement network segment, aim to add this camera to the "basement" room.
        Prior to implementing any changes, retrieve the current state of the garage camera.
        You also need to ensure the garage lights (ID "light_garage_ceiling") are turned off before activating any security scene, so check their state and switch them off if necessary.
        You recently purchased and installed the garage ceiling light (ID "light_garage_ceiling"), a Philips Hue White Ambiance model with firmware 1.0.0, placed in the Garage. It monitors power and brightness, with an initial state of power off and brightness at 0%.
        You wish to create a new "Away Mode" scene (ID "scene_away_mode") to secure the house when unoccupied. In this scene, the garage camera should be streaming and recording, and all living room lights (floor and ceiling), the AC, and the garage ceiling light should be off.
        Additionally, organize a shopping list called "Garage Security Supplies" (ID "list_garage_security_supplies") containing these items: 1 pack of AA batteries, 1 warning sign for the security camera, and 1 cleaning cloth for lens.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "camera_garage"}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "basement",
                    "device_id": "camera_garage"
                }
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "garage",
                    "device_id": "light_garage_ceiling"
                }
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "light_garage_ceiling"}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_garage_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
        You've acquired a new iRobot Roomba i7+ and need to set it up. It is fully charged and docked in the living room. Aim to add it to the system with the ID "vacuum_home" and the name "Main Floor Robot Vacuum", operating on firmware 3.1.0.
        The vacuum tracks power state, cleaning mode, and battery percentage. At present, it is 'off' and 'docked' with a full battery. Aim to include it in the living room's device list.
        Prior to making any modifications, retrieve the current state of the vacuum.
        You want it to automatically start every day at 9:30 AM by switching it on and setting its mode to "clean".
        Additionally, intend to establish a scene called "Daily Clean" (ID "scene_daily_clean") that accomplishes the same task: activating the robot vacuum to commence cleaning right away.
        For safety, obtain the state of the living room ceiling light (ID "light_lr_ceiling") and switch it off before the vacuum begins to clean.
        Additionally, compile a shopping list called "Vacuum Supplies" (ID "list_vacuum_supplies") with these items: 1 pack of replacement filters, 1 pack of side brushes, and 1 bottle of cleaning solution.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "vacuum_home"}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "vacuum_home"
                }
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "light_lr_ceiling"}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
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
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
        To ensure you don't overlook sensor maintenance, review the details of the living room thermometer (ID "sensor_lr_thermometer") and proceed to set a battery replacement alert.
        Schedule this reminder (ID "rem_sensor_lr_battery") precisely one year from now, on June 27, 2026, at 8 AM. It should be dispatched as a normal priority push notification to your phone.
        Additionally, assemble a shopping list named "Sensor Maintenance Supplies" (ID "list_sensor_maintenance") including these items: 2 AAA batteries, 1 microfiber cleaning cloth, and 1 can of compressed air.
        Retrieve the current state of the living room thermometer before implementing any modifications.
        """,
        actions=[
            Action(
                name="GetSensorByIdOrFilter",
                kwargs={"sensor": "sensor_lr_thermometer"}
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        As you plan for a weekend camping trip, arrange your equipment by establishing a packing list named "Weekend Camping Packing" (ID "list_camping_weekend").
        Ensure the list includes these items in sequence: 1 Tent, 4 Sleeping Bags, 1 Camping Stove, 2 Propane Canisters, 4 Flashlights, 6 Water Bottles, and 1 First-Aid Kit.
        Coordinate a reminder (ID "rem_camping_check") for Thursday at 8 PM to verify the list again.
        Lastly, recall the necessity for 2 cans of Bug Spray and incorporate them into the list.
        """,
        actions=[
            Action(
                name="UpdateCustomListInDatabase",
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
        As summer has arrived, ensure all heating automation is turned off. Begin by retrieving the current status of the heater (ID "heater_home") before proceeding with any modifications.
        Proceed by deactivating the heater and eliminating any of its scheduled events.
        It has come to your attention that the "Good Night" scene incorporates the heater. Update this scene to exclude heater actions and instead execute the following steps:
        - Close the curtains in both the living room and master bedroom.
        - Switch off the ceiling lights in both the living room and master bedroom.
        - Activate the master bedroom night lamp at 15% brightness with a cozy warm hue (hue 30).
        Moreover, retrieve the state of the master bedroom night lamp (ID "lamp_br_night") before updating its configuration.
        To get ready for summer nights, compile a shopping list named "Summer Night Essentials" (ID "list_summer_night_essentials") including these items: 2 mosquito repellent sprays, 1 pack of cooling gel pads, and 1 bedside fan.
        Schedule a reminder (ID "rem_summer_night_essentials_check") to verify this list every Friday at 6 PM.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "heater_home"}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "heater_home",
                    "updates": {
                        "power": "off",
                        "scheduled_updates": []
                    }
                }
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "lamp_br_night"}
            ),
            Action(
                name="UpdateSceneInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        You have purchased a Dyson Cool AM07 standing fan for the master bedroom and need to integrate it into your system. The fan has been set up but is currently off. Register it with the ID "fan_br_stand" and the designation "Master Bedroom Standing Fan", with firmware version 1.0.0. The fan supports modifiable power and speed settings (state_params: power, speed; initial state: off, speed 0).
        Incorporate it into the master bedroom's collection of devices (room ID "bedroom_master").
        Prior to implementing any alterations, obtain the fan's current status to ensure it is turned off.
        You also intend to embed it into your "Heatwave Day" scene, ensuring the fan activates at 70% speed for enhanced air circulation when the scene is initiated.
        Furthermore, generate a shopping list named "Heatwave Fan Supplies" (ID "list_heatwave_fan_supplies") containing the following goods: 1 pack of AAA batteries, 1 bottle of fan cleaning spray, and 1 microfiber cloth.
        Arrange a reminder (ID "rem_heatwave_fan_supplies_check") to review this list every Friday at 4 PM.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "fan_br_stand"}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "bedroom_master",
                    "device_id": "fan_br_stand"
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        Update the accessibility information for Grandma Linda (ID "linda_johnson") as she no longer requires a wheelchair.
        Prior to updating, retrieve her current member record.
        With her monthly visit approaching, it's important to schedule a reminder to ready the West Bedroom. Set this reminder (ID "rem_prepare_west_bedroom") for August 1st at 10 AM, with a note to keep the ramp available just in case, to be sent via mobile push notification.
        Additionally, initiate a shopping list named "West Bedroom Prep Supplies" (ID "list_west_bedroom_prep") containing the following: 1 set of fresh linens, 1 bottle of air freshener, and 1 pack of guest toiletries.

        After her stay, arrange a reminder (ID "rem_move_residence_west_to_east") for August 2nd at 10 AM to transfer Linda's residence record from bedroom_west to bedroom_east, delivering the reminder via mobile push.
        """,
        actions=[
            Action(
                name="ManageMemberInDatabase",
                kwargs={
                    "action": "get",
                    "member_id": "linda_johnson"
                }
            ),
            Action(
                name="ManageMemberInDatabase",
                kwargs={
                    "action": "update",
                    "member_id": "linda_johnson",
                    "updates": {"accessibility": {"wheelchair": False}}
                }
            ),
            Action(
                name="AddReminderToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        The smart plug previously used for the coffee maker is now used for controlling a new LED strip for movie nights, requiring updates to your "Movie Time" scene.
        A Samsung Q60T TV (ID "tv_lr"), with firmware 1.0.0, located in the living room and initially in a power-off state with "HDMI1" input, should be added as a device.
        Proceed to remove the old scene (ID "scene_movie_time").
        Form a new version entitled "Movie Time v2" (ID "scene_movie_time_v2") which should perform these actions: close the living room curtains, dim the floor lamp to 15%, turn off the ceiling light, set the AC to low fan speed, and power off the coffee maker plug controlling the LED strip.
        Moreover, compile a shopping list titled "Movie Night Supplies" (ID "list_movie_night_supplies") with these items: 1 pack of popcorn, 2 bottles of soda, and 1 box of LED strip replacement parts.
        Furthermore, verify that the living room TV (ID "tv_lr") is off before initiating the scene by checking its state and powering off as required.
        Set a schedule for this new scene to commence at 9 PM for your first movie night featuring the new lighting.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "tv_lr"
                }
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": "tv_lr"}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "tv_lr",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="DeleteSceneFromDatabase",
                kwargs={"scene_id": "scene_movie_time"}
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
        Initiate a swift security check each morning. Begin by verifying all pre-existing cameras. 
        For this task, you incorporated two additional cameras: "camera_side_yard" and "camera_garage", both Arlo, model Essential XL, firmware version 1.0.0. Each camera monitors stream_online, motion_detected, person_detected, threat_detected, and recording, all initially configured to False. Ensure both cameras are integrated into the system with these specifications.
        Additionally, you installed a new garage ceiling light (ID "light_garage_ceiling"), a Philips Hue White Ambiance model, firmware 1.0.0, positioned in the Garage. It monitors power and brightness, with an initial state of power off and brightness at 0%.
        Configure a scene named "scene_morning_sweep" for taking rapid camera snapshots and verifying doors at 6 AM daily (RRULE "FREQ=DAILY;BYHOUR=6;BYMINUTE=0").
        This scene must request each security camera ("camera_front_door", "camera_back_door", "camera_side_yard", "camera_garage") to capture a snapshot (by temporarily setting 'recording' to true).
        Ensure these cameras are active to record during the sweep.
        It should also inspect the front-door contact sensor (sensor_front_door), which can be accomplished by incorporating a get_device call in the automation list.
        You also need to compile a shopping list named "Security Sweep Supplies" (ID "list_security_sweep_supplies") including the following: 1 pack of AA batteries for cameras, 1 lens cleaning cloth, and 1 warning sign for security sweep.
        """,
        actions=[
            Action(
                name="GetSensorByIdOrFilter",
                kwargs={"filters": {"type": "camera"}}
            ),
            Action(
                name="AddSensorToDatabase",
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
                name="AddSensorToDatabase",
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
                name="AddDeviceToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddSceneToDatabase",
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
        Develop a post-school routine for your daughter Emma, who arrives home at 3:15 PM. Create a new scene called "After School" (ID "scene_after_school") to prepare her room for homework.
        In her room (West Bedroom), adjust the ceiling light (ID "light_bw_ceiling") to 100% brightness and her desk lamp (ID "lamp_bw_desk") to 80% brightness with a color temperature of 4500K. Set the curtains (ID "curtain_bw") to a half-open position, allowing natural light while minimizing glare.
        Given her peanut allergy, set up a high-priority reminder (ID "rem_olivia_snack_check") that activates at 3:20 PM on school days to check her lunchbox and arrange a safe after-school snack, termed Safe Snack.
        For safety, retrieve the current status of the West Bedroom ceiling light and desk lamp before implementing changes, and switch off the desk lamp if it is already illuminated before executing the scene.
        Furthermore, assemble a shopping list titled "Emma After School Supplies" (ID "list_olivia_after_school_supplies") including: 1 pack of peanut-free snack bars, 1 bottle of water, and 1 pack of colored pencils for homework.
        Schedule a reminder (ID "rem_olivia_supplies_check") to verify this list each Monday at 8 AM.
        Automate the scene to commence at 3:15 PM on weekdays using the RRULE string "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=15".
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"type": "light"}}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_bw_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_olivia_snack_check",
                        "target": {"type": "note", "text": "check Emma's lunchbox and prepare a safe after-school snack"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=15;BYMINUTE=20"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="AddReminderToDatabase",
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
                name="UpdateSceneInDatabase",
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
        Your friends Michael and Jennifer Chen visit every Sunday evening at 6:30 PM for dinner. You wish to create an inviting ambiance for them with a scene named "Sunday Dinner" (ID "scene_sunday_dinner").
        To ensure the kitchen and living room are well-illuminated, have the living room ceiling light (ID "light_lr_ceiling") set at 80% brightness with a warm tone (2700K), and the floor lamp (ID "light_lr_floor") at 60% for ambient lighting.
        Since Michael is allergic to shellfish and Jennifer follows a vegan diet, you should create a list (ID "list_sunday_dinner_restrictions") to monitor their dietary restrictions.
        You also intend to prepare a shopping list titled "Sunday Dinner Groceries" (ID "list_sunday_dinner_groceries") including these items: 1 pack of vegan cheese, 1 box of gluten-free pasta, and 1 bottle of sparkling water.
        Prior to implementing any changes, retrieve the current status of the living room ceiling light and floor lamp to make sure they are off before the scene is initiated. If any are found on, switch them off before setting up the scene.
        Finally, set a reminder (ID "rem_sunday_dinner_prep") for 5 PM every Sunday (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=17;BYMINUTE=0") to begin preparations, alert me via mobile notification. The scene must be scheduled to run at 6:25 PM (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=18;BYMINUTE=25").
        """,
        actions=[
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_lr_floor",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
                kwargs={
                    "custom_list": {
                        "list_id": "list_sunday_dinner_restrictions",

                        "items": [
                            {"item": "Michael - No shellfish (allergy)", "quantity": 1},
                            {"item": "Jennifer - Vegan", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="UpdateSceneInDatabase",
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
        Your wife Jessica works early shifts at the hospital (Mon-Wed, starting at 7 AM). To facilitate her mornings, you intend to organize a scene called "Emily's Hospital Shift" (ID "scene_emily_shift").
        She gets up at 5:30 AM, so you want the master bedroom lights to gently wake her: having the ceiling light (ID "light_br_ceiling") at 30% brightness with a cool 5000K color, and the night lamp (ID "lamp_br_night") at 20% with the same color tone. The curtains (ID "curtain_br") should also open completely.
        She departs at 6:30 AM. Schedule a reminder at 6:15 AM (ID "rem_emily_lunch") with the note "Grab lunch", and another at 6:25 AM (ID "rem_emily_leaving") to verify her nursing tools.
        You also need a checklist of her essential items (ID "list_emily_nursing"), such as: ID Badge, Stethoscope, Scrubs, Comfortable Shoes, Water Bottle and Lunch Box, one each, which you're creating at this moment.
        Additionally, organize a shopping list named "Emily Hospital Shift Supplies" (ID "list_emily_shift_supplies") containing these items: 1 pack of medical masks, 1 bottle of hand sanitizer, and 1 pack of energy bars.
        Prior to making any modifications, obtain the current state of the master bedroom ceiling light (ID "light_br_ceiling"), night lamp (ID "lamp_br_night"), and curtains (ID "curtain_br") to verify their status.
        To ensure safety, if the night lamp is on before the scene starts, switch it off first.
        Please arrange the scene and reminders using the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE;BYHOUR=5;BYMINUTE=30" (adjust the minute for the reminders accordingly).
        """,
        actions=[
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="UpdateSceneInDatabase",
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
        Emma's friend Sofia Rodriguez, who also has a peanut allergy, visits for a playdate every Wednesday after school. Arrange the necessary safety precautions.
        Start by creating a scene named "Playdate Safety" (ID "scene_playdate") scheduled to activate at 3:10 PM. This should illuminate Emma's room (West Bedroom): the ceiling light (ID "light_bw_ceiling") at a brightness of 90% and the desk lamp (ID "lamp_bw_desk") at 70% with a bright 4000K setting. The curtains (ID "curtain_bw") should be fully opened to enhance visibility.
        Prepare a checklist for allergy safety (ID "list_playdate_safety"), which is being developed now, and include: "Check all snacks for peanut ingredients", "Verify no cross-contamination in kitchen", "Keep EpiPens easily accessible", "Have Ana's contact number ready", and "Clean all surfaces the girls will use".
        Also, establish a shopping list entitled "Playdate Snacks" (ID "list_playdate_snacks") containing: 2 packs of peanut-free snack bars, 1 bottle of apple juice, and 1 pack of fruit cups.
        Prior to implementing any changes, retrieve the current conditions of the West Bedroom ceiling light, desk lamp, and curtains, as well as the kitchen outlet state (ID "plug_kt_coffee"), ensuring it remains off for playdate safety. If the plug is active, switch it off.
        The kitchen outlet (ID "plug_kt_coffee") is a TP-Link Kasa HS110 smart plug, firmware 1.0.0, residing in the Kitchen, monitoring power and energy use, initial setting: power off, energy_kwh 0.
        Set two reminders: one at 3:15 PM ("rem_playdate_snack") for preparing allergy-safe snacks, and another at 5:45 PM ("rem_playdate_pickup") for Sofia's mom's arrival at 6 PM.
        Use the RRULE "FREQ=WEEKLY;BYDAY=WE" for all timing schedules, modifying hours and minutes as necessary.
        """,
        actions=[
            Action(
                name="ManageMemberInDatabase",
                kwargs={
                    "action": "get",
                    "member_id": "mia_rodriguez"
                }
            ),
            Action(
                name="ManageMemberInDatabase",
                kwargs={
                    "action": "get",
                    "member_id": "olivia_johnson"
                }
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_bw_ceiling", "lamp_bw_desk", "curtain_bw", "plug_kt_coffee"]}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "plug_kt_coffee",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
                kwargs={
                    "custom_list": {
                        "list_id": "list_playdate_safety",

                        "items": [
                            {"item": "Check all snacks for peanut ingredients", "quantity": 1},
                            {"item": "Verify no cross-contamination in kitchen", "quantity": 1},
                            {"item": "Keep EpiPens easily accessible", "quantity": 1},
                            {"item": "Have Maria's contact number ready", "quantity": 1},
                            {"item": "Clean all surfaces the girls will use", "quantity": 1}
                        ]
                    }
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_playdate_pickup",
                        "target": {"type": "note", "text": "Maria will pick up Sofia at 6:00 PM"},
                        "trigger": {"rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=17;BYMINUTE=45"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "normal"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="UpdateSceneInDatabase",
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
        Develop a soothing bedtime routine for your son Ethan, who sleeps at 8 PM on school nights in the East Bedroom. Introduce a wind-down process beginning at 7:30 PM.
        In his room, gradually dim the lights over a 30-minute period. At 7:30 PM, the ceiling light (ID "light_be_ceiling") should be set to 50% brightness with a warm tone (hue 30, saturation 30). At 7:45 PM, transition to using only his bedside lamp (ID "lamp_be_bedside") at 30% with the same warm tone. By 7:50 PM, ensure the curtains (ID "curtain_be") are closed. At 8 PM, all lights should be switched off.
        The East Bedroom desk lamp (ID "lamp_be_desk") is a Philips Hue White Ambiance model, firmware 1.0.0, positioned in the East Bedroom, monitoring power consumption and brightness, default state: power off, brightness 0%.
        Name this scene "Ethan Bedtime" (ID "scene_ethan_bedtime"). Additionally, enable a reminder (ID "rem_ethan_bedtime") at 7:25 PM for initiating his bedtime sequence (brushing teeth, etc.).
        Additionally, create a shopping list titled "Ethan Bedtime Supplies" (ID "list_ethan_bedtime_supplies") including: 1 pack of bedtime storybooks, 1 bottle of water, and 1 nightlight bulb.
        Apply the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" for all timings, making necessary adjustments to the schedules.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_be_desk",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="UpdateSceneInDatabase",
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
        As Robert, concentrate on enhancing your home to suit your remote working schedule (Senior Software Engineer at DataSystems, 7:30 AM to 4 PM). Design a "Work Mode" scene (ID "scene_work_mode") to create a conducive atmosphere.
        Initiating at 7:30 AM in the master bedroom, ensure the ceiling light (ID "light_br_ceiling") is at maximum brightness with a cool 5500K color. Fully draw open the curtains (ID "curtain_br"), and switch off the night lamp (ID "lamp_br_night").
        Lunch is at noon, and you require a reminder for it (ID "rem_john_lunch") with the message "Lunch time". You also need reminders (ID "rem_john_breaks") with the note "Take break" every 2 hours during your shift (7:30, 9:30, 11:30, 1:30, 3:30) for short breaks. Apply the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" for all planners.
        A checklist for your daily work arrangement (ID "list_john_work_setup") is necessary, comprising these items: "Laptop & charger", "External monitor setup", "Noise-canceling headphones", "Water bottle", "Ergonomic chair adjustment", "Task list review".
        Moreover, curate a shopping list titled "Work Essentials" (ID "list_john_work_essentials") including 1 pack of sticky notes, 1 pack of pens, and 1 bottle of hand sanitizer.
        Prior to commencing work, confirm the master bedroom night lamp (ID "lamp_br_night") remains off for safety reasons.
        Schedule a reminder (ID "rem_john_work_essentials_check") every Monday at 8 AM to inspect the work essentials roster.
        """,
        actions=[
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="UpdateSceneInDatabase",
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
        Aim to enhance monitoring and upkeep for your Bosch Series 8 dishwasher (ID "dishwasher_kt").
        Initially, compose a maintenance checklist (ID "list_dishwasher_maintenance") to include both monthly and quarterly tasks.
        You also require three alerts:
        1. A monthly alert for routine maintenance (ID "rem_dishwasher_monthly") to occur on the 1st of each month at 10 AM (RRULE "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=10;BYMINUTE=0").
        2. A quarterly alert for intensive cleaning (ID "rem_dishwasher_quarterly") scheduled every three months on the 15th at 10 AM (RRULE "FREQ=MONTHLY;INTERVAL=3;BYMONTHDAY=15;BYHOUR=10;BYMINUTE=0").
        3. An alert (ID "rem_dishwasher_cycle") activates at the completion of a cycle (when time_remaining_min adjusts to 0).
        Create a shopping list called "Dishwasher Supplies" (ID "list_dishwasher_supplies") listing these items: 1 bottle of rinse aid, 1 pack of dishwasher tablets, and 1 bottle of descaler.
        Conclude by configuring a scene identified as "Dishwasher Check" (ID "scene_dishwasher_check") that switches on the living room ceiling lights when the cycle ends, along with dispatching a notification to verify the supplies list.
        """,
        actions=[
            Action(
                name="AddCustomListToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddSceneToDatabase",
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
        Handle the preparations for your college friend Chris Brown ("michael_brown"), who visits quarterly (Friday-Sunday) and is allergic to cat dander, by setting up cleaning automations and ensuring a safe environment.
        Initially, coordinate the creation of a checklist (ID "list_mike_visit_prep") for preparing the guest room and house. The checklist must include tasks such as deep cleaning the guest room, vacuuming all carpets and furniture, changing air filters, washing all bedding in hot water, cleaning air vents, setting up the air purifier, stocking allergy medications, and thoroughly cleaning the bathroom.
        Establish a scene named "Guest Room Ready" (ID "scene_guest_ready") to create a welcoming atmosphere. It should configure the East Bedroom ceiling light to 70% with a warm color (hue 30, saturation 20), adjust the bedside lamp to 40% using the same color, partially open the curtains, and set the AC to 23°C with low fan speed.
        Prior to making any adjustments, obtain the current state of all East Bedroom lights, curtains, and the AC. Turn off any devices that are already on before initiating the scene.
        Set two reminders: one ("rem_mike_prep") on Thursday at 10 AM to begin preparations, and another ("rem_mike_allergies") on Friday at 8 AM for conducting a final allergy safety check before Chris's arrival, with notifications sent via mobile push.
        Also, develop a shopping list titled "Chris Visit Supplies" (ID "list_mike_visit_supplies") containing items such as 1 pack of HEPA air filters, 1 bottle of allergy medication, and 1 box of hypoallergenic pillow covers.
        Furthermore, before Chris's arrival, ensure you verify the state of the air purifier in the guest room (if available, or describe and add it if not), and confirm it is powered on and set to high mode for his visit. In the absence of an air purifier device, incorporate a new device: ID "air_purifier_guest", type "air_purifier", name "Guest Room Air Purifier", vendor Levoit, model Core 300, firmware 1.0.0, located in the Guest Room, state_params: power, mode, filter_status; initial state: power off, mode auto, filter_status good.
        Schedule the scene and reminders using the RRULE "FREQ=MONTHLY;INTERVAL=3;BYDAY=4FR" (fourth Friday of every third month), adapting the schedule for the Thursday reminder.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"location": "East Bedroom"}}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"type": "ac"}}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "curtain_be",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "ac_home",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"location": "Guest Room", "type": "air_purifier"}}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "air_purifier_guest",
                    "updates": {"power": "on", "mode": "high"}
                }
            ),
            Action(
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
                kwargs={
                    "reminder": {
                        "reminder_id": "rem_mike_allergies",
                        "target": {
                            "type": "note",
                            "text": "Do final allergy safety check before Chris arrives"
                        },
                        "trigger": {"rrule": "FREQ=MONTHLY;INTERVAL=3;BYDAY=4FR;BYHOUR=8;BYMINUTE=0"},
                        "actions": [{"type": "notify", "channel": "mobile_push"}],
                        "meta": {"priority": "high"},
                        "status": "active",
                    }
                }
            ),
            Action(
                name="UpdateSceneInDatabase",
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
        Facilitate the creation of an ideal setting for Ethan's daily piano practice in the East Bedroom. He practices after school at 3:30 PM on weekdays. Develop a "Piano Practice" scene (ID "scene_piano_practice").
        For optimal visibility, set the ceiling light (ID "light_be_ceiling") at 90% brightness with a cool white light (4000K), and adjust the bedside lamp (ID "lamp_be_bedside") to 60% with the identical temperature. Ensure the curtains (ID "curtain_be") are half-open.
        Prior to making any modifications, retrieve the current state of all East Bedroom lights and curtains to confirm their condition. Turn off any light or lamp that is already on before activating the scene.
        Prepare a practice checklist (ID "list_ethan_piano"), populating this list with necessary actions for piano practice: "Finger exercises (5 min)", "Scales practice (5 min)", "Review previous piece (10 min)", "Learn new section (10 min)" and "Fun piece / free play (5 min)".
        Additionally, compile a shopping list titled "Ethan Piano Supplies" (ID "list_ethan_piano_supplies") consisting of 1 pack of music sheets, 1 metronome, and 1 bottle of hand sanitizer.
        Set two reminders: one to commence practice at 3:30 PM ("rem_ethan_practice_start") and another to conclude it at 4:00 PM ("rem_ethan_practice_end").
        Also, schedule a reminder ("rem_ethan_piano_supplies_check") every Monday at 8 AM to review the piano supplies list.
        Utilize the RRULE "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR" for all schedules, implementing these from tomorrow.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"filters": {"location": "East Bedroom"}}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_be_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_be_bedside",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "curtain_be",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="UpdateSceneInDatabase",
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
        Jessica wants to engage in yoga sessions in the master bedroom during her days off (Thursday through Sunday) at 8 AM. Aim to create a tranquil setting for her practice.
        Establish a scene named "Morning Yoga" (ID "scene_morning_yoga") with the following configurations: master bedroom ceiling light (ID "light_br_ceiling") set to 40% with a calming blue hue (hue 210, saturation 30), night lamp (ID "lamp_br_night") at 25% with the identical color, curtains (ID "curtain_br") fully drawn open, and AC (ID "ac_home") adjusted to 24°C with the fan at a low setting, to foster a serene atmosphere for Jessica's yoga sessions.
        Prior to implementing any alterations, retrieve the current status of the master bedroom ceiling light, night lamp, curtains, and AC to verify their condition. Should any light or lamp be on, ensure it is turned off before activating the scene.
        Compile a shopping list (ID "list_emily_yoga_supplies") including these items: 1 yoga mat, 2 yoga blocks, 1 water bottle, 1 towel, and 1 bottle of essential oils.
        Schedule a reminder at 7:45 AM ("rem_emily_yoga_prep") with the message "Prepare yoga space", and another at 8:00 AM ("rem_emily_yoga_start") stating "Time to start your yoga practice - namaste!".
        Apply the RRULE "FREQ=WEEKLY;BYDAY=TH,FR,SA,SU" for all schedules.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_br_ceiling", "lamp_br_night", "curtain_br", "ac_home"]}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "lamp_br_night",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
                name="UpdateSceneInDatabase",
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
        Enhance light-level detection for automations in the Living Room. On 2025-07-16, at 2 PM, a Zigbee Lux Sensor was installed there.
        Details of the device: ID "sensor_lr_lux", named "Living Room Lux Sensor", produced by Philips, model Hue Motion, firmware version 1.2.0. It monitors light intensity and battery status. Initial data: 250 lux, 97% battery.
        Incorporate the sensor and link it to the "living_room".
        Retrieve the current state of the Living Room ceiling light (ID "light_lr_ceiling") beforehand to confirm that it is off for safety prior to initiating any automation tasks.
        Augment the existing "Movie Time" scene to switch OFF the ceiling light if the lux reading falls below 50.
        Also, curate a shopping list titled "Living Room Lux Supplies" (ID "list_lr_lux_supplies") with these items: 1 pack of AAA batteries for the sensor, 1 microfiber cleaning cloth, and 1 replacement Zigbee module.
        Set up a reminder (ID "rem_lr_lux_supplies_check") to inspect this list every Saturday at 10 AM.
        """,
        actions=[
            Action(
                name="AddSensorToDatabase",
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
            Action(name="ManageRoomInDatabase", kwargs={"action": "add_device_to_database", "room_id": "living_room", "device_id": "sensor_lr_lux"}),
            Action(name="GetDeviceByIdOrFilter", kwargs={"devices": ["light_lr_ceiling"]}),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(name="GetSceneByIdOrFilter", kwargs={"scene_id": "scene_movie_time"}),
            Action(
                name="UpdateSceneInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        Automate energy savings at night in your home. Develop a scene titled "Energy Save" (ID "scene_energy_save") that activates each night at 11:30 PM (RRULE "FREQ=DAILY;BYHOUR=23;BYMINUTE=30").
        The purpose is to reduce unnecessary electricity usage when everyone is likely sleeping. This scene should:
        - Switch off all lights in the living room.
        - Draw the living room curtains to retain heat or cold air.
        - Deactivate major overnight appliances, including the AC and dishwasher.
        - Also, assemble a shopping list named "Energy Save Supplies" (ID "list_energy_save_supplies") containing these items: 1 pack of LED bulbs, 1 smart plug, and 1 power strip.
        - Schedule a reminder (ID "rem_energy_save_supplies_check") to review this list every Saturday at 10 AM.
        Ensure the automation runs daily at 11:30 PM.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={
                    "filters": {
                        "location": "Living Room",
                    }
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        Implement a simple grocery shopping system. Set up a list titled "Weekly Groceries" (ID "list_weekly_groceries") along with a reminder to verify it every Sunday morning.
        Initially, the list should include your household's standard items: 2 gallons of milk, 1 loaf of bread, 1 dozen eggs, 2 packs of cheese, 1 bag of apples, and 3 boxes of cereal.
        Additionally, incorporate two extra items to the list: 1 bottle of olive oil and 1 pack of paper towels.
        Moreover, monitor the kitchen fridge's status to confirm it's powered off before adding perishable groceries. The fridge plug (ID "plug_kt_fridge") is a TP-Link KP115 smart plug, type "outlet", vendor TP-Link, model KP115, firmware 1.0.0, located in the Kitchen, tracks power and energy usage, initial state: power on, energy_kwh 0.0.
        If the fridge plug is not on, switch it on before appending groceries to the list.
        Establish a reminder (ID "rem_grocery_check") that triggers at 9 AM every Sunday (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=9;BYMINUTE=0") to assess the list.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "plug_kt_fridge",
                    "updates": {"power": "on"}
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        You need to initiate the creation of a cozy reading light scene for the living room, capable of being activated manually.
        To maintain a comfortable environment, begin by retrieving the latest states of the living room lights, curtains, AC, and the living room air-quality sensor (ID "sensor_lr_air_quality") prior to setting the scene.
        Proceed by setting up a scene named "Reading Light" (ID "scene_reading_light") that adjusts the floor lamp (ID "light_lr_floor") to 70% brightness, deactivates the ceiling light (ID "light_lr_ceiling"), positions the curtains (ID "curtain_lr") to a half-closed state, and configures the AC (ID "ac_home") to a comfortable 23°C with the fan running on low.
        Furthermore, verify the living room TV (ID "tv_lr") is switched off before executing the scene. The TV is a Samsung Q60T, firmware 1.0.0, positioned in the Living Room, monitors power and input, initial state: power off, input "HDMI1". Should the TV not be present, integrate it with all parameters and connect it to the living room.
        Additionally, establish a shopping list titled "Reading Light Supplies" (ID "list_reading_light_supplies") including these items: 1 pack of LED bulbs, 1 bottle of screen cleaner, and 1 reading pillow.
        You are configuring this currently and intend not to schedule it.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_lr_floor"]}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_lr_ceiling"]}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["curtain_lr"]}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["ac_home"]}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["tv_lr"]}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "tv_lr"
                }
            ),
            Action(
                name="GetSensorByIdOrFilter",
                kwargs={"sensor": "sensor_lr_air_quality"}
            ),
            Action(
                name="ManageRoomInDatabase",
                kwargs={
                    "action": "add_device_to_database",
                    "room_id": "living_room",
                    "device_id": "sensor_lr_air_quality"
                }
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "tv_lr",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
        As Jessica enjoys preparing unique breakfasts during the weekends, you need to organize a reminder and a shopping list for it.
        Construct a list (ID "list_weekend_breakfast") containing typical ingredients: 2 packs of bacon, 1 carton of pancake mix, 1 bottle of maple syrup, 2 packs of berries, and 1 carton of whipping cream.
        Include 1 bottle of orange juice and 1 pack of coffee beans to the list since these are frequently required for breakfast.
        The fridge plug is identified as a TP-Link KP115 smart plug, type "outlet", vendor TP-Link, model KP115, firmware 1.0.0, situated in the Kitchen, monitors power and energy consumption, initial state: power on, energy_kwh 0.0. If the fridge plug is turned off, activate it.
        You also require a reminder (ID "rem_weekend_breakfast") set to trigger at 7 PM each Friday (RRULE "FREQ=WEEKLY;BYDAY=FR;BYHOUR=19;BYMINUTE=0") to review the ingredients list, transmit it to mobile, with normal priority.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "plug_kt_fridge",
                    "updates": {"power": "on"}
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        You aim to integrate two newly installed smart ceiling fans at 2 PM today.
        The first fan is located in the Living Room: ID "fan_lr_ceiling", name "Living Room Ceiling Fan", vendor Hunter, model Signal, firmware 1.0.0.
        The second fan is situated in the Master Bedroom: ID "fan_br_ceiling", name "Master Bedroom Ceiling Fan", vendor Haiku, model I-Series, firmware 2.3.1.
        Both fans support power, speed, and direction controls, and are initially set to off, speed 0, direction "forward".
        Include both fans in the inventory and link them to their corresponding room records ("living_room" and "bedroom_master").
        Modify the "Good Morning" scene to activate both fans at 70% speed (forward direction), and adjust the "Good Night" scene to switch them off.
        Furthermore, compile a shopping list titled "Ceiling Fan Supplies" (ID "list_ceiling_fan_supplies") consisting of these items: 1 AAA batteries, 1 fan cleaning spray, and 1 microfiber cloth.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={"action": "add_device_to_database", "room_id": "living_room", "device_id": "fan_lr_ceiling"},
            ),
            Action(
                name="ManageRoomInDatabase",
                kwargs={"action": "add_device_to_database", "room_id": "bedroom_master", "device_id": "fan_br_ceiling"},
            ),
            Action(
                name="UpdateSceneInDatabase",
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
                name="UpdateSceneInDatabase",
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
                name="AddCustomListToDatabase",
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
        The Living-Room air-quality sensor (ID "sensor_lr_air_quality") has a battery level of 15% as of 4 PM today (2025-07-15).
        Arrange a reminder (ID "rem_air_sensor_battery") for 9 AM tomorrow to replace the batteries. This should be a standard priority phone notification with a default 10-minute snooze, name it Replace Living-Room Air-Quality-Sensor, and include a note saying Swap AAA cells in LR AQ sensor to mobile.
        Also, organize a shopping list named "Air Sensor Battery Supplies" (ID "list_air_sensor_battery_supplies") that contains the following items: 2 AAA batteries, 1 microfiber cloth, and 1 pack of disposable gloves.
        Given that a dead battery might impede the "Heatwave Day" safety automation, update that scene to deactivate the AC if the sensor's battery_level ever falls below 5%.
        """,
        actions=[
            Action(
                name="AddReminderToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddSceneToDatabase",
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
        In order to address basement stuffiness, initiate ongoing CO₂ monitoring starting today (2025-07-15, 5 PM).
        Include a new sensor: ID "sensor_bs_co2", name "Basement CO2 Sensor", vendor Awair, model CO₂ Mini, firmware 1.0.0, located in the Basement. It measures co2_ppm and battery_level. Begin with 900 ppm, 100% battery.
        Attach this sensor to the basement room entry.
        Create a "Basement Ventilation" scene (ID "scene_basement_vent") that switches the AC (ID "ac_home") to fan-only at high speed and powers off the heater (ID "heater_home"). This scene should trigger daily at 8 AM (RRULE "FREQ=DAILY;BYHOUR=8;BYMINUTE=0").
        For safety assurance, synchronize the AC with the same scheduled update.
        Formulate a shopping list titled "Basement Ventilation Supplies" (ID "list_basement_vent_supplies") comprising these items: 1 replacement air filter, 1 bottle of cleaning spray, and 1 pack of disposable gloves.
        Schedule a reminder (ID "rem_basement_vent_supplies_check") to verify this list every Monday at 9 AM.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={"action": "add_device_to_database", "room_id": "basement", "device_id": "sensor_bs_co2"},
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        To enhance fire safety in your kitchen, as of 6 PM today (2025-07-15), install a Nest Protect v4 smoke and CO detector.
        Its specifics are: ID "sensor_kt_smoke", name "Kitchen Smoke & CO Detector", vendor Google, model Nest Protect v4, firmware 4.0.0, located in the Kitchen. It monitors smoke, CO, and battery level. It starts off as all clear (false, false, 100% battery).
        Register this detector and link it to the kitchen room.
        Establish an emergency scene "scene_fire_alert" that fully brightens Living Room and Kitchen ceiling lights to white (100% brightness, 6000K), completely opens all curtains ("curtain_lr", "curtain_br", "curtain_bw", "curtain_be"), and shuts down both the heater and the AC.
        Additionally, prepare a shopping list named "Kitchen Fire Safety Supplies" (ID "list_kitchen_fire_safety_supplies") with these essentials: 1 fire extinguisher, 1 pack of smoke detector batteries, and 1 emergency escape plan printout.
        Also, set a monthly high-priority reminder (ID "rem_kitchen_smoke_test") on the 1st of each month at 9 AM to test the detector (RRULE "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0").
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={"action": "add_device_to_database", "room_id": "kitchen", "device_id": "sensor_kt_smoke"}
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        To address the issue of low humidity in the master bedroom, introduce a smart humidifier alongside a humidity sensor this evening.
        You need to install two devices:
        - Humidifier: ID "humidifier_br", named "Master Bedroom Humidifier", supplier Levoit, model Classic300-S, firmware 1.1.0. It monitors power, target humidity, and water level. Begins in state: off, target 45%, water supply full.
        - Sensor: ID "sensor_br_humidity", named "Master Bedroom Humidity Sensor", supplier Xiaomi, model Mi Hygrometer 2, firmware 1.0.0. It monitors humidity, temperature, and battery life. Initial readings: 34% RH, 22.5°C, 92% battery life.
        Ensure both devices are placed in the master bedroom and set up a nightly automation. Incorporate a scene "scene_humidity_night" that activates the humidifier at 1 AM aiming for 45% humidity. Synchronize the humidifier with a scheduled update (RRULE "FREQ=DAILY;BYHOUR=1;BYMINUTE=0").
        Prior to implementing any changes, confirm the current status of both the humidifier and the humidity sensor.
        For added security, verify the status of the master bedroom ceiling light (ID "light_br_ceiling") and switch it off if active before the humidifier runs at night.
        Additionally, compile a shopping list named "Humidifier Supplies" (ID "list_humidifier_supplies") featuring these items: 1 bottle of distilled water, 1 pack of humidifier filters, and 1 cleaning brush.
        Schedule a reminder "rem_fill_humidifier" every two days at 7 PM to refill the water (RRULE "FREQ=DAILY;INTERVAL=2;BYHOUR=19;BYMINUTE=0").
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["humidifier_br", "sensor_br_humidity"]}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_br_ceiling"]}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_br_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="AddDeviceToDatabase",
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
            Action(name="ManageRoomInDatabase", kwargs={"action": "add_device_to_database", "room_id": "bedroom_master", "device_id": "humidifier_br"}),
            Action(name="ManageRoomInDatabase", kwargs={"action": "add_device_to_database", "room_id": "bedroom_master", "device_id": "sensor_br_humidity"}),
            Action(
                name="AddSceneToDatabase",
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
                name="UpdateDeviceInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        The central AC (ID "ac_home") has a freshly released firmware version (2.2.0) and it needs the record to be updated today at 8 AM (2025-07-24).
        Compile a shopping list titled "AC Maintenance Supplies" (ID "list_ac_maintenance_supplies") containing: 1 replacement air filter, 1 bottle of coil cleaner, and 1 pack of disposable gloves.
        Lastly, arrange a yearly maintenance notification for the AC (ID "rem_ac_annual_service") on the 1st of August at 10 AM (RRULE "FREQ=YEARLY;BYMONTH=8;BYMONTHDAY=1;BYHOUR=10;BYMINUTE=0").
        """,
        actions=[
            Action(
                name="UpdateDeviceInDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        To enhance perimeter coverage, you installed an additional security camera in the side yard today (2025-07-16, 11 AM).
        The device particulars are: ID "camera_side_yard", name "Side-Yard Security Camera", vendor Eufy, model Cam 3C-Lite, firmware 1.0.0, situated in the Backyard. It monitors stream status, motion, person, and threat detection, and recording status. Initial setup: stream active, recording active, all detections false.
        You aim to integrate it, link it to the "living_room" room (as it's the nearest network segment), and expand the current "Away Mode" scene to ensure this camera records while the scene is active.
        Before proceeding with any modifications, retrieve the current status of the camera_side_yard to verify its condition.
        Additionally, verify the state of the living room ceiling light (ID "light_lr_ceiling") to ensure it's off for night security, and turn it off if necessary.
        Furthermore, create a shopping list titled "Side Yard Security Supplies" (ID "list_side_yard_security_supplies") containing the following items: 1 Security camera warning sign, 1 AA batteries, and 1 Lens cleaning cloth.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["camera_side_yard"]}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={"action": "add_device_to_database", "room_id": "living_room", "device_id": "camera_side_yard"}
            ),
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_lr_ceiling"]}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "light_lr_ceiling",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
            Action(name="GetSceneByIdOrFilter", kwargs={"scene_id": "scene_away_mode"}),
        ],
        outputs=[]
    ),

    # Task 38 -------------------------------------------------------------
    Task(
        annotator="0",
        user_id="res_38",
        instruction="""
        You intend to implement an automatic energy-saver that activates every night. Establish a scene named "scene_energy_saver" set to run at 12:05 AM daily, beginning tonight, and label it Night Energy Saver.
        This scene should adjust all ceiling lights ("light_lr_ceiling", "light_br_ceiling", "light_bw_ceiling", "light_be_ceiling") to 30% brightness and switch off the AC ("ac_home") and heater ("heater_home").
        Before making adjustments, acquire the current state of all ceiling lights, AC, and heater to verify their condition.
        Likewise, verify that the living room TV (ID "tv_lr") is off to conserve energy; if absent, add it: type "tv", vendor Samsung, model Q60T, firmware 1.0.0, located in Living Room, monitors power and input, initial state: power off, input "HDMI1".
        Also, create a shopping list named "Night Energy Saver Supplies" (ID "list_energy_saver_supplies") including these items: 1 pack of LED bulbs, 1 smart plug, and 1 power strip.
        Set a reminder (ID "rem_energy_saver_supplies_check") to review this list every Saturday at 10 AM.
        Utilize the RRULE "FREQ=DAILY;BYHOUR=0;BYMINUTE=5" for scheduling.
        """,
        actions=[
            Action(
                name="GetDeviceByIdOrFilter",
                kwargs={"devices": ["light_lr_ceiling", "light_br_ceiling", "light_bw_ceiling", "light_be_ceiling", "ac_home", "heater_home"]}
            ),
            Action(
                name="AddDeviceToDatabase",
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
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "tv_lr",
                    "updates": {"power": "off"}
                }
            ),
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        Since the hallway may be dim at night, ensure a gentle automatic light activates upon motion detection after 10 PM. You already possess a Hallway Motion Sensor (ID "sensor_hall_motion").
        Aim to establish a scene "scene_night_motion" that, once initiated, switches the Living Room floor lamp ("light_lr_floor") ON to 15% brightness for 3 minutes, and then switches it back OFF (the runtime engine will manage the timer, so only incorporate the on/off directives).
        Furthermore, compile a shopping list named "Hallway Night Light Supplies" (ID "list_hallway_night_light_supplies") including these items: 1 pack of LED bulbs, 1 motion sensor battery, and 1 nightlight cover.
        Arrange a reminder (ID "rem_hallway_night_light_supplies_check") to inspect this list each Saturday at 10 AM.
        Organize the scene to activate itself daily at 10 PM with the RRULE "FREQ=DAILY;BYHOUR=22;BYMINUTE=0".
        """,
        actions=[
            Action(
                name="AddSceneToDatabase",
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
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
        The refrigerator has been connected to an energy-monitoring smart plug you fitted at 1 PM today (2025-07-16).
        The related information is: ID "plug_kt_fridge", type "outlet", name "Kitchen Fridge Plug", vendor TP-Link, model KP115, firmware 1.0.0, located in the Kitchen. It monitors power and energy consumption. Initial status: power on, 0.0 kWh.
        You should incorporate the plug and designate it for the kitchen room.
        To maintain safety, if the fridge plug is off, activate it prior to any automation.
        Additionally, compile a shopping list titled "Fridge Maintenance Supplies" (ID "list_fridge_maintenance_supplies") including: 1 bottle of cleaning spray, 1 pack of microfiber cloths, and 1 fridge thermometer.
        Also, establish a reminder ("rem_check_fridge_energy") each Sunday at 8 AM (RRULE "FREQ=WEEKLY;BYDAY=SU;BYHOUR=8;BYMINUTE=0") to evaluate the fridge plug's energy report.
        Initiate another reminder ("rem_fridge_supplies_check") every Monday at 9 AM to assess the fridge maintenance supplies list.
        """,
        actions=[
            Action(
                name="AddDeviceToDatabase",
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
                name="ManageRoomInDatabase",
                kwargs={"action": "add_device_to_database", "room_id": "kitchen", "device_id": "plug_kt_fridge"}
            ),
            Action(
                name="UpdateDeviceInDatabase",
                kwargs={
                    "device_id": "plug_kt_fridge",
                    "updates": {"power": "on"}
                }
            ),
            Action(
                name="AddCustomListToDatabase",
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
                name="AddReminderToDatabase",
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
                name="AddReminderToDatabase",
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
