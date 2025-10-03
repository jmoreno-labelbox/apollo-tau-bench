
tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "\n        The current time is 2025-07-25 07:30. You need to handle several tasks.\n        1. Check the current temperature from the living-room thermometer.\n        2. If the temperature exceeds 22 degrees Celsius, schedule the central AC to activate at 13:00 today. Configure the AC to: power=on, mode=cool, setpoint_c=22, and fan_speed=auto.\n        3. Simultaneously, at 13:00, ensure the living-room curtain is closed by setting its power=on and position=0.\n        4. Set up a daily routine: each day at 19:00, adjust the ceiling light to power=on and brightness=30, and switch off the floor lamp.\n        5. Finally, establish a one-time reminder titled \"Close windows before AC starts\". It should instigate a mobile_push notification at 2025-07-25T12:55:00 with \"normal\" priority.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 22,
                        "fan_speed": "auto"
                    },
                    "schedule_at": "2025-07-25T13:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_lr",
                    "update": {
                        "power": "on",
                        "position": 0
                    },
                    "schedule_at": "2025-07-25T13:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 30
                    },
                    "schedule_at": "2025-07-25T19:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-07-25T19:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_close_windows",
                        "target": {
                            "type": "note",
                            "text": "Close windows before AC starts"
                        },
                        "trigger": {
                            "datetime": "2025-07-25T12:55:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "scheduled",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                }
            }
        ],
        "outputs": [
                "\"temperature_c\": 22.3"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_02",
        "instruction": "\n        It's 10am on 2025-07-26. You need to arrange for family movie night.\n        Begin by creating a custom list named \"Friday Movie Night Snacks\" with id \"list_movie_snacks\", tagging it with \"shopping\" and \"movie\".\n        Next, include 2 portions of popcorn, 6 sodas, and 5 chocolates in that list.\n        You also have to update the existing \"Movie Time\" scene. For this scene, adjust the floor lamp brightness to 15, set the AC fan_speed to \"low\", and make the setpoint_c 23. Replace other existing configurations.\n        Lastly, schedule this scene to run at 2025-07-27T20:00:00; eliminate any existing scheduled runs.\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "custom_lists",
                    "filters": {
                        "name": "Friday Movie Night Snacks"
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_movie_snacks",
                        "tags": [
                            "shopping",
                            "movie"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_movie_snacks",
                    "item": {
                        "item": "Popcorn",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_movie_snacks",
                    "item": {
                        "item": "Soda",
                        "quantity": 6
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_movie_snacks",
                    "item": {
                        "item": "Chocolate",
                        "quantity": 5
                    },
                    "action": "add"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "scenes"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_movie_time",
                        "actions": [
                            {
                                "device_id": "light_lr_floor",
                                "update": {
                                    "power": "on",
                                    "brightness": 15
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "fan_speed": "low",
                                    "setpoint_c": 23
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-27T20:00:00"
                        ]
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_03",
        "instruction": "\n        Today is 2025-07-26 at 10:00:00\n        You wish to set up a new smart air-purifier in the East Bedroom.\n        The air-purifier is from vendor \"Coway\", model \"AP-1512HH\", firmware version \"1.0.0\" and you would like to assign it the id \"purifier_be\".\n        Its adjustable parameters are power, mode, and fan_speed.\n        You prefer its default state to be power=off, mode=auto, and fan_speed=1.\n        The purifier currently has an empty scheduled_updates list.\n        You intend to add the purifier to the \"bedroom_east\" room.\n        Additionally, you wish to schedule it to turn on daily at 22:00 with fan_speed=3, and shut it off daily at 06:00.\n        Following that, you want to create a custom list named \"Air-Filter Replacements\" with id \"list_air_filters\" and include one \"Purifier Filter Type X\" in it.\n        Finally, you intend to set up a reminder to \"Replace purifier filter\" that sends a mobile_push notification on the 1st of every month at 09:00.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "rooms",
                    "entity_id": "bedroom_east"
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "purifier_be",
                        "type": "air_purifier",
                        "location": "East Bedroom",
                        "vendor": "Coway",
                        "model": "AP-1512HH",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "mode",
                            "fan_speed"
                        ],
                        "state": {
                            "power": "off",
                            "mode": "auto",
                            "fan_speed": 1
                        },
                        "scheduled_updates": []
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "bedroom_east",
                    "device_id": "purifier_be"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "purifier_be",
                    "update": {
                        "power": "on",
                        "mode": "auto",
                        "fan_speed": 3
                    },
                    "schedule_at": "2025-07-26T22:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "purifier_be",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-07-27T06:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_air_filters",
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_air_filters",
                    "item": {
                        "item": "Purifier Filter Type X",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_purifier_filter",
                        "target": {
                            "type": "note",
                            "text": "Replace purifier filter"
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
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "\n        You wish to create an \"After-School Study\" scene.\n        This scene should:\n          \u2022 Turn the West-Bedroom desk lamp on with brightness 60 and color_temperature 5000.\n          \u2022 Keep the West-Bedroom ceiling light on, but reduce its brightness to 40.\n          \u2022 Open the living-room curtain to position 100.\n          \u2022 With description \"Prep lighting & curtains for homework time\".\n        You plan to schedule this scene to activate every weekday at 16:00, starting from 2025-07-25.\n        You also need to set up a reminder for \"Emma, start your homework\" that triggers a mobile_push every weekday at 16:10.\n        Lastly, you wish to add \"Review math homework\" (quantity 1) to the todo list.\n        Set description as \"Prep lighting & curtains for homework time\".\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_after_school_study",
                        "description": "Prep lighting & curtains for homework time",
                        "actions": [
                            {
                                "device_id": "lamp_bw_desk",
                                "update": {
                                    "power": "on",
                                    "brightness": 60,
                                    "color_temperature": 5000
                                }
                            },
                            {
                                "device_id": "light_bw_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 40
                                }
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-25T16:00:00"
                        ],
                        "meta": {
                            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                        }
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_olivia_homework",
                        "target": {
                            "type": "note",
                            "text": "Emma, start your homework"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=16;BYMINUTE=10"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_todo",
                    "item": {
                        "item": "Review math homework",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "\n        Check the status of the kitchen sink leak sensor.\n        If its battery_level is less than 95, add two \"CR123A batteries\" to the shopping list.\n        Given the same condition, also set up a weekly reminder every Monday at 09:00 named \"Check leak-sensor battery\".\n        Separately, plan the dishwasher to start a self-clean cycle this evening (2025-07-26) at 23:00. Ensure the settings are power=on and cycle=self_clean.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "CR123A batteries",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_sink_battery",
                        "target": {
                            "type": "note",
                            "text": "Check leak-sensor battery"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "on",
                        "cycle": "self_clean"
                    },
                    "schedule_at": "2025-07-26T23:00:00"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "\n        Establish a \"Weekday Morning\" scene with id \"scene_weekday_morning\".\n        This scene should carry out the following actions:\n          \u2022 Adjust the living room and bedroom curtains to position 100.\n          \u2022 Switch on the living room ceiling light with brightness 70 and kelvin 4000.\n          \u2022 Switch the heater off and activate the AC with setpoint_c=24.\n        Schedule the first execution for 2025-07-26T07:00:00 and set it as a repeating event from Monday to Friday.\n        You additionally need to create a mobile_push reminder to \"Pack kids' lunches\" at 07:15 on weekdays.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_weekday_morning",
                        "actions": [
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 70,
                                    "color": {
                                        "kelvin": 4000
                                    }
                                }
                            },
                            {
                                "device_id": "heater_home",
                                "update": {
                                    "power": "off"
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "setpoint_c": 24
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-26T07:00:00"
                        ],
                        "meta": {
                            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                        }
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_pack_lunch",
                        "target": {
                            "type": "note",
                            "text": "Pack kids' lunches"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7;BYMINUTE=15"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_07",
        "instruction": "\n        Departing for a holiday on 2025-08-10 at 08:00 requires setting up your home.\n        \u2022 Schedule the living-room ceiling & floor lights, all bedroom ceiling lights, and the bedroom night light to deactivate at 08:00 on 2025-08-10.\n        \u2022 Additionally, program the heater and AC to turn off simultaneously.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_be_ceiling",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "heater_home",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-08-10T08:00:00"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_08",
        "instruction": "\n        Today's date is 2025-07-25 at 11:00:00.\n        Anticipating Robert and Linda's arrival on 2025-07-26 at 14:00 necessitates preparation.\n        Initiating from 2025-07-26, coordinate the following schedules:\n        \u2022 Program the ceiling light in the West Bedroom to switch off at 22:30 each day.\n        \u2022 Arrange the heater to adjust to a setpoint_c of 22 at 22:00 daily.\n        Establish a custom list titled \"Guest Comfort\" (id list_guest_comfort) tagged \"guest\" and incorporate \"Extra Pillows\"x4 and \"Lavender Room Spray\"x1 into it.\n        Furthermore, create a reminder identified as \"rem_pickup_grandparents\" for \"Pick up grandparents at SFO\" for 2025-07-26T13:30 via mobile_push.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-07-26T22:30:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "heater_home",
                    "update": {
                        "power": "on",
                        "mode": "heat",
                        "setpoint_c": 22
                    },
                    "schedule_at": "2025-07-26T22:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_guest_comfort",
                        "name": "Guest Comfort",
                        "tags": [
                            "guest"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_guest_comfort",
                    "item": {
                        "item": "Extra Pillows",
                        "quantity": 4
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_guest_comfort",
                    "item": {
                        "item": "Lavender Room Spray",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_pickup_grandparents",
                        "target": {
                            "type": "note",
                            "text": "Pick up grandparents at SFO"
                        },
                        "trigger": {
                            "datetime": "2025-07-26T13:30:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ]
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "\n        The current date and time is 2025-07-25 at 11:30\n        You intend to incorporate a new smart dog feeder identified as \"feeder_dog\" within the Kitchen.\n        \u2022 PetTech is the vendor, the model is \"FeedMaster 2\" with firmware version 1.0.0, and its state_params include power and portion_g.\n        \u2022 The desired default state should be power=off and portion_g=0.\n        \u2022 Presently, the feeder's scheduled_updates list is empty.\n        \u2022 You intend to link it to the kitchen room.\n        \u2022 Plan to schedule daily feedings at 07:00 and 18:00 with power=on and portion_g=120.\n        \u2022 You also wish to create or update the custom list \"Pet Supplies\" (id list_pet_supplies) tagged \"pet\" and add \"Dog Food\"x5.\n        \u2022 Lastly, set a reminder to \"Buy dog food\" to recur monthly on the 25th at 18:00.\n        ",
        "actions": [
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "feeder_dog",
                        "type": "feeder",
                        "location": "Kitchen",
                        "vendor": "PetTech",
                        "model": "FeedMaster 2",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "portion_g"
                        ],
                        "state": {
                            "power": "off",
                            "portion_g": 0
                        }
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "kitchen",
                    "device_id": "feeder_dog"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "feeder_dog",
                    "update": {
                        "power": "on",
                        "portion_g": 120
                    },
                    "schedule_at": "2025-07-26T07:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "feeder_dog",
                    "update": {
                        "power": "on",
                        "portion_g": 120
                    },
                    "schedule_at": "2025-07-25T18:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_pet_supplies",
                        "tags": [
                            "pet"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_pet_supplies",
                    "item": {
                        "item": "Dog Food",
                        "quantity": 5
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_buy_dog_food",
                        "target": {
                            "type": "note",
                            "text": "Buy dog food"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=25;BYHOUR=18;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "\n        You are to arrange monthly dishwasher maintenance.\n        \u2022 A reminder is needed on the first Monday of each month at 10:00 to \"Run dishwasher cleaning cycle\".\n        \u2022 Additionally, schedule the dishwasher to switch to power=on with cycle=self_clean at 10:05 under the same criteria.\n        \u2022 Ensure that \"Descaling tablets\"x1 is included on your shopping list.\n        \u2022 Arrange a reminder to \"Refill the descaling tablets into the dishwasher\" for the following day after cleaning, on the first Tuesday of the month.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_dishwasher_clean",
                        "target": {
                            "type": "note",
                            "text": "Run dishwasher cleaning cycle"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYDAY=MO;BYSETPOS=1;BYHOUR=10;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "on",
                        "cycle": "self_clean"
                    },
                    "schedule_at": "2025-08-04T10:05:00",
                    "rrule": "FREQ=MONTHLY;BYDAY=MO;BYSETPOS=1"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "Descaling tablets",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_dishwasher_refill",
                        "target": {
                            "type": "note",
                            "text": "Refill the descaling tablets into the dishwasher"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYDAY=TU;BYSETPOS=1;BYHOUR=10;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_11",
        "instruction": "\n        You need to check the battery of the bedroom smoke detector.\n        \u2022 Be sure to read the state of the bedroom smoke detector. If the battery_level is below 95, make sure to add \"9 V batteries\"x2 to the shopping list.\n        \u2022 Establish a \"Fire Alert\" scene, defined as an \"Emergency red lighting\", where both the bedroom night light and living room floor light are set with power=on, brightness=100, and color hue=0.\n        \u2022 Ensure that there is no automated scheduling for this scene, as it should be triggered manually only.\n        \u2022 Schedule a yearly reminder on Jan 1 at 09:00 to \"Replace smoke-detector battery\".\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "9 V batteries",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_fire_alert",
                        "actions": [
                            {
                                "device_id": "lamp_br_night",
                                "update": {
                                    "power": "on",
                                    "brightness": 100,
                                    "color": {
                                        "hue": 0
                                    }
                                }
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {
                                    "power": "on",
                                    "brightness": 100,
                                    "color": {
                                        "hue": 0
                                    }
                                }
                            }
                        ],
                        "scheduled_runs": []
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_replace_smoke_battery",
                        "target": {
                            "type": "note",
                            "text": "Replace smoke-detector battery"
                        },
                        "trigger": {
                            "rrule": "FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_12",
        "instruction": "\n        Your goal is to enhance front-door security.\n        \u2022 Confirm immediately that the camera_front_door has stream_online=true and recording=true.\n        \u2022 Set up a reminder to \"Review security footage\" with id \"rem_review_footage\" every day at 21:00 via mobile_push.\n        \u2022 Additionally, initiate a custom list titled \"Security Logs\" (id list_security_logs) and include \"Review finished\"x0 as a placeholder.\n        ",
        "actions": [
            {
                "name": "ModifySensorState",
                "arguments": {
                    "sensor_id": "camera_front_door",
                    "update": {
                        "stream_online": true,
                        "recording": true
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_review_footage",
                        "target": {
                            "type": "note",
                            "text": "Review security footage"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=21;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_security_logs",
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_security_logs",
                    "item": {
                        "item": "Review finished",
                        "quantity": 0
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "\n        You need to include a household member, Noah Chen (id liam_chen, male, born 2003-02-11, relation Cousin), who will stay in the East Bedroom.\n        \u2022 It is necessary to create a packing list for him named \"Liam Packing\" (id list_liam_pack).\n        \u2022 To this list, add \"Towels\"x2 and \"Extra Blanket\"x1.\n        ",
        "actions": [
            {
                "name": "UpsertMember",
                "arguments": {
                    "member": {
                        "id": "liam_chen",
                        "first_name": "Noah",
                        "last_name": "Chen",
                        "relation": "Cousin",
                        "birthdate": "2003-02-11",
                        "sex": "male",
                        "residence": {
                            "lives_in_house": true,
                            "room_id": "bedroom_east"
                        }
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_liam_pack",
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_liam_pack",
                    "item": {
                        "item": "Towels",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_liam_pack",
                    "item": {
                        "item": "Extra Blanket",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "\n        You need to install a soil-moisture sensor (id sensor_garden_moisture, vendor Eve, model SoilGuard, firmware version 1.0.0) and a sprinkler controller (id sprinkler_garden, vendor Rachio, model R3, firmware version 1.0.0) in the garden. Initially, you'll manage them in the basement.\n        \u2022 The sensor's state_params include moisture_pct and battery_level.\n        \u2022 The sprinkler's state_params include power and duration_min.\n        \u2022 Ensure the default sprinkler state is set to power=off, duration_min=0.\n        \u2022 Currently, the sprinkler has an empty scheduled_updates list.\n        \u2022 Plan to schedule the sprinkler_garden to activate with power=on and duration_min=15 daily at 06:00.\n        \u2022 Additionally, arrange a reminder to \"Change sprinkler filter\" every year on Mar 1 at 09:00.\n        ",
        "actions": [
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "sensor_garden_moisture",
                        "type": "sensor",
                        "location": "Basement",
                        "vendor": "Eve",
                        "model": "SoilGuard",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "moisture_pct",
                            "battery_level"
                        ],
                        "state": {
                            "moisture_pct": 30,
                            "battery_level": 100
                        }
                    }
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "sprinkler_garden",
                        "type": "sprinkler",
                        "location": "Basement",
                        "vendor": "Rachio",
                        "model": "R3",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "duration_min"
                        ],
                        "state": {
                            "power": "off",
                            "duration_min": 0
                        }
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "basement",
                    "device_id": "sensor_garden_moisture"
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "basement",
                    "device_id": "sprinkler_garden"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "sprinkler_garden",
                    "update": {
                        "power": "on",
                        "duration_min": 15
                    },
                    "schedule_at": "2025-07-26T06:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_sprinkler_filter",
                        "target": {
                            "type": "note",
                            "text": "Change sprinkler filter"
                        },
                        "trigger": {
                            "rrule": "FREQ=YEARLY;BYMONTH=3;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_15",
        "instruction": "\n        Initiate routines for the East-Bedroom on school nights (Sun-Thu), commencing today 2025-06-29.\n        \u2022 The bedside lamp in the bedroom should activate at 20:00 with brightness set to 10, and deactivate at 22:00.\n        \u2022 At 20:10, ensure the curtain in the bedroom closes (position 0).\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceStateTimer",
                "arguments": {
                    "device_id": "lamp_be_bedside",
                    "schedule_end": "2025-06-29T22:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 10
                    },
                    "schedule_at": "2025-06-29T20:00:00",
                    "rrule": "FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_be",
                    "update": {
                        "position": 0
                    },
                    "schedule_at": "2025-06-29T20:10:00",
                    "rrule": "FREQ=WEEKLY;BYDAY=SU,MO,TU,WE,TH"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "\n        With today being 2025-02-16 and Robert Johnson's birthday tomorrow, establish a new shopping list for him labeled as \"list_john_birthday_shopping\", incorporating the tags \"birthday\" and \"shopping\".\n        Add 1 quantity of his preferred dish, Sushi, to this list.\n        You've acquired a new speaker with these specifications:\n        - Vendor: Sonos\n        - Model: Move 2\n        - Firmware version: 1.0.0\n        - Adjustable parameters include: power, volume, playlist\n        - blank scheduled_updates list\n        - Designate this for the bedroom, naming it \"Bedroom Speaker\"\n        Assign it to the Master Bedroom with the id \"speaker_bedroom\".\n        Arrange for this speaker to activate at 8am on his birthday, playing his favorite music at volume 50.\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "members",
                    "filters": {
                        "first_name": "Robert",
                        "last_name": "Smith"
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_john_birthday_shopping",
                        "tags": [
                            "birthday",
                            "shopping"
                        ],
                        "items": [
                            {
                                "item": "Sushi",
                                "quantity": 1
                            }
                        ]
                    }
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "speaker_bedroom",
                        "type": "speaker",
                        "location": "Master Bedroom",
                        "vendor": "Sonos",
                        "model": "Move 2",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "volume",
                            "playlist"
                        ],
                        "state": {
                            "power": "off",
                            "volume": 0,
                            "playlist": ""
                        },
                        "scheduled_updates": []
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "speaker_bedroom",
                    "update": {
                        "power": "on",
                        "volume": 50,
                        "playlist": "classic rock"
                    },
                    "schedule_at": "2025-02-17T08:00:00"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "\n        The date and time are 2025-07-25 14:00. There are several tasks on your list.\n        \u2022 Schedule the dishwasher to begin a self-clean cycle at 02:00 on 2025-07-26 with settings of power=on and cycle=self_clean.\n        \u2022 Set up a daily reminder at 21:00 to \"Empty dryer lint trap\".\n        \u2022 Include \"High-efficiency detergent\" x2 in the household shopping list.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "on",
                        "cycle": "self_clean"
                    },
                    "schedule_at": "2025-07-26T02:00:00"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_dryer_lint",
                        "target": {
                            "type": "note",
                            "text": "Empty dryer lint trap"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=21;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active"
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "High-efficiency detergent",
                        "quantity": 2
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "\n        The current date is 2025-07-29 and you need to prepare for the severe heat-wave forecasted for tomorrow, 2025-07-30. Ensure you complete the following tasks:\n        1. Read the temperature from the Living-Room thermometer and log it.\n        2. Close the Living-Room curtain (device id \"curtain_lr\") to position 0 at 12:50 tomorrow, executing as a one-time action.\n        3. Dim the Living-Room ceiling light (device id \"light_lr_ceiling\") to a brightness of 30 precisely at 12:55 tomorrow, also as a single occurrence.\n        4. Set up a new scene titled \"Heatwave Afternoon\" (id \"scene_heatwave_afternoon\") that incorporates the two device changes mentioned earlier, no scheduling required.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_lr",
                    "update": {
                        "power": "on",
                        "position": 0
                    },
                    "schedule_at": "2025-07-30T12:50:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 30
                    },
                    "schedule_at": "2025-07-30T12:55:00"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_heatwave_afternoon",
                        "name": "Heatwave Afternoon",
                        "actions": [
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 0
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 30
                                }
                            }
                        ]
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_19",
        "instruction": "\n        You have acquired a new Bosch \"Series 6 Silence\" Dishwasher for the Kitchen.\n        \u2022 Assign it the id \"dishwasher_kt2\", firmware 1.0.0, with the same state-params as the existing dishwasher, and refer to it as Kitchen Dishwasher 2. Ensure the power is initially set to OFF.\n        \u2022 Connect it to the Kitchen room record.\n        \u2022 Plan for it to automatically turn ON and commence the \"eco\" cycle every Monday at 02:00 starting from 2025-07-28.\n        \u2022 Set up a monthly reminder to \"Replace Dishwasher Salt\" on the 1st of every month at 09:00 with an email notification with id \"rem_dishwasher_salt\", ensuring priority is \"normal\" and status \"active\".\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices",
                    "entity_id": "dishwasher_kt"
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "dishwasher_kt2",
                        "type": "dishwasher",
                        "location": "Kitchen",
                        "vendor": "Bosch",
                        "model": "Series 6 Silence",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "cycle",
                            "time_remaining_min",
                            "door"
                        ],
                        "state": {
                            "power": "off",
                            "cycle": "eco",
                            "time_remaining_min": 0,
                            "door": "closed"
                        },
                        "scheduled_updates": []
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "kitchen",
                    "device_id": "dishwasher_kt2"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt2",
                    "update": {
                        "power": "on",
                        "cycle": "eco"
                    },
                    "schedule_at": "2025-07-28T02:00:00",
                    "rrule": "FREQ=WEEKLY;BYDAY=MO"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_dishwasher_salt",
                        "target": {
                            "type": "note",
                            "text": "Replace Dishwasher Salt"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "email"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        },
                        "status": "active"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_20",
        "instruction": "\n        Grandma Linda Johnson is visiting from 2025-07-26 to 2025-07-30. To prepare, you need to:\n        1. Confirm (read) her member record.\n        2. Introduce a new scene named \"Grandma Welcome\" (id \"scene_grandma_welcome\") which, at execution:\n           \u2022 opens the Master-Bedroom curtain to 100 and activates the night lamp at brightness 25,\n           \u2022 configures the Central Heater to heat mode 23 \u00b0C,\n           \u2022 deactivates the Central AC.\n           \u2022 The aim is to apply Comfort settings for Grandma's stay.\n        3. Arrange for this scene to be executed at 14:00 on 2025-07-26 and subsequently at 08:00 every morning from 2025-07-27 to 2025-07-30.\n        4. Compile a custom list \"grandma_visit_prep\" with id \"list_grandma_visit_prep\" tagged as \"guest\".\n        5. Insert three items into it: \"Fresh Flowers\" x 1, \"Extra Towels\" x 3, \"Chamomile Tea\" x 2.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "members",
                    "entity_id": "linda_johnson"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_grandma_welcome",
                        "actions": [
                            {
                                "device_id": "curtain_br",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {
                                    "power": "on",
                                    "brightness": 25
                                }
                            },
                            {
                                "device_id": "heater_home",
                                "update": {
                                    "power": "on",
                                    "mode": "heat",
                                    "setpoint_c": 23
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "off"
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-26T14:00:00",
                            "2025-07-27T08:00:00",
                            "2025-07-28T08:00:00",
                            "2025-07-29T08:00:00",
                            "2025-07-30T08:00:00"
                        ]
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_grandma_visit_prep",
                        "name": "grandma_visit_prep",
                        "tags": [
                            "guest"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_grandma_visit_prep",
                    "item": {
                        "item": "Fresh Flowers",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_grandma_visit_prep",
                    "item": {
                        "item": "Extra Towels",
                        "quantity": 3
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_grandma_visit_prep",
                    "item": {
                        "item": "Chamomile Tea",
                        "quantity": 2
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "\n        It's Sunday evening (2025-07-29). You aim to prepare next week's grocery workflow.\n        \u2022 Begin by checking every custom list tagged \"groceries\".\n        \u2022 Proceed to create a fresh list \"next_week_groceries\" (id \"list_groceries_next\") by copying today's weekend list items. Ensure to increase the quantity of anything currently below 2 to exactly 2.\n        \u2022 Schedule a reminder for \"Grocery Pickup\" for Saturday (2025-07-29) at 09:00 via mobile-push.\n        \u2022 For budget tracking purposes, immediately output (get) the newly created list object.\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "custom_lists",
                    "filters": {
                        "tags": [
                            "groceries"
                        ]
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_groceries_next",
                        "name": "next_week_groceries",
                        "items": [
                            {
                                "item": "Chicken Breast",
                                "quantity": 2
                            },
                            {
                                "item": "Eggs",
                                "quantity": 2
                            }
                        ]
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_groceries_next",
                    "item": {
                        "item": "Olive Oil",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_groceries_next",
                    "item": {
                        "item": "Apples",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_groceries_next",
                    "item": {
                        "item": "Cheese",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_grocery_pickup_next",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_groceries_next"
                        },
                        "trigger": {
                            "datetime": "2025-07-29T09:00:00"
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
                        "status": "scheduled"
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists",
                    "entity_id": "list_groceries_next"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "\n        Today is 2025-07-29. Jessica Johnson's hospital shift concludes tomorrow (Mon 2025-07-30) at 15:00. Prepare the house for her arrival.\n        \u2022 At 14:55, activate the **heater_home** with mode \"heat\" and setpoint_c 22 \u00b0C.\n        \u2022 At the same time, switch on **light_lr_ceiling** with brightness 70 and color {{\"kelvin\": 3500}}.\n        \u2022 At 15:00, start the **dishwasher_kt** and initiate the \"auto\" cycle.\n        \u2022 By 18:00, turn off **heater_home** and commence **ac_home** cooling with setpoint_c 23 and fan_speed \"auto\".\n        \u2022 Add 2 x \"Salmon Fillet\" to the current list \"weekend_groceries\", id: (list_groceries_weekend).\n        \u2022 Set up a one-time reminder for Jessica at 14:50 tomorrow: \"Time to stretch before heading home!\", with id \"rem_stretch_emily\".\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "members",
                    "filters": {
                        "first_name": "Jessica",
                        "last_name": "Smith"
                    }
                },
            },
            {
                "name": "ModifyDeviceStateTimer",
                "arguments": {
                    "device_id": "heater_home",
                    "schedule_end": "2025-07-30T18:00:00",
                    "update": {
                        "power": "on",
                        "mode": "heat",
                        "setpoint_c": 22
                    },
                    "schedule_at": "2025-07-30T14:55:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 70,
                        "color": {
                            "kelvin": 3500
                        }
                    },
                    "schedule_at": "2025-07-30T14:55:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "on",
                        "cycle": "auto"
                    },
                    "schedule_at": "2025-07-30T15:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 23,
                        "fan_speed": "auto"
                    },
                    "schedule_at": "2025-07-30T18:00:00"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_groceries_weekend",
                        "items": [
                            {
                                "item": "Chicken Breast",
                                "quantity": 2
                            },
                            {
                                "item": "Apples",
                                "quantity": 1
                            },
                            {
                                "item": "Olive Oil",
                                "quantity": 1
                            },
                            {
                                "item": "Cheese",
                                "quantity": 1
                            },
                            {
                                "item": "Eggs",
                                "quantity": 2
                            },
                            {
                                "item": "Salmon Fillet",
                                "quantity": 2
                            }
                        ]
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_stretch_emily",
                        "member_id": "emily_johnson",
                        "target": {
                            "type": "note",
                            "text": "Time to stretch before heading home!"
                        },
                        "trigger": {
                            "datetime": "2025-07-30T14:50:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_23",
        "instruction": "\n        You intend to install a new side-lamp next to the sofa.\n        \u2022 Assign its ID as: lamp_lr_side.\n        \u2022 It is a light of type: light, from vendor Ikea, model \"Tradfri Floor Lamp v2\", with firmware 2.0.0, and it is adjustable (power, brightness, color_temperature).\n        Your plan is to place it in the Living Room.\n        Next, coordinate the creation of a \"Saturday Movie Night\" plan:\n        1. Include lamp_lr_side in scene_movie_time so when the scene triggers at 19:00, the lamp activates with brightness 35.\n        2. Execute scene_movie_time.\n        3. Adjust the **ac_home** fan_speed to \"low\".\n        4. Include \"Popcorn (3 bags)\" on the shopping list.\n        ",
        "actions": [
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "lamp_lr_side",
                        "type": "light",
                        "location": "Living Room",
                        "vendor": "Ikea",
                        "model": "Tradfri Floor Lamp v2",
                        "firmware_version": "2.0.0",
                        "state_params": [
                            "power",
                            "brightness",
                            "color_temperature"
                        ],
                        "state": {
                            "power": "off",
                            "brightness": 0,
                            "color_temperature": 3000
                        }
                    }
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_movie_time",
                        "actions": [
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 0
                                }
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {
                                    "power": "on",
                                    "brightness": 20
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "off"
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "fan_speed": "low"
                                }
                            },
                            {
                                "device_id": "lamp_lr_side",
                                "update": {
                                    "power": "on",
                                    "brightness": 35
                                }
                            }
                        ]
                    }
                },
            },
            {
                "name": "RunScene",
                "arguments": {
                    "scene_id": "scene_movie_time"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "fan_speed": "low"
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "Popcorn",
                        "quantity": 3
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_24",
        "instruction": "\n        The family plans to leave for vacation from 2025-08-10 to 2025-08-18. Create a \"Holiday Mode\" scene (id scene_holiday_mode).\n        \u2022 Turn off **heater_home**.\n        \u2022 Set **ac_home** to eco-cool at 26 \u00b0C with fan_speed \"auto\".\n        \u2022 Switch **light_lr_ceiling** off and program it to randomly turn on at 20:00 (brightness 30, kelvin 2700) and turn off again at 23:00 each night during the vacation.\n        Additionally, add a reminder with id \"rem_water_valve\" for Robert Johnson at 2025-08-09T21:00 to \"Shut main water valve\".\n        Lastly, formulate a packing list named \"vacation_packing\" with id \"list_vacation_packing\" including 1 x \"Sunscreen\", \"Chargers\", and \"Passports\".\n        ",
        "actions": [
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_holiday_mode",
                        "actions": [
                            {
                                "device_id": "heater_home",
                                "update": {
                                    "power": "off"
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 26,
                                    "fan_speed": "auto"
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "off"
                                }
                            }
                        ]
                    }
                },
            },
            {
                "name": "ModifyDeviceStateTimer",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "schedule_end": "2025-08-10T23:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 30,
                        "color": {
                            "kelvin": 2700
                        }
                    },
                    "schedule_at": "2025-08-10T20:00:00",
                    "rrule": "FREQ=DAILY;UNTIL=20250818T230000Z"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_water_valve",
                        "member_id": "john_johnson",
                        "target": {
                            "type": "note",
                            "text": "Shut main water valve"
                        },
                        "trigger": {
                            "datetime": "2025-08-09T21:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "high"
                        }
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_vacation_packing",
                        "name": "vacation_packing",
                        "items": [
                            {
                                "item": "Sunscreen",
                                "quantity": 1
                            },
                            {
                                "item": "Chargers",
                                "quantity": 1
                            },
                            {
                                "item": "Passports",
                                "quantity": 1
                            }
                        ]
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_25",
        "instruction": "\n        You aim to establish Ethan's \"Bedtime Wind-Down\" routine.\n        \u2022 At 19:30, handle the closing of **curtain_be** (position 0) and adjust **light_be_ceiling** to brightness 25, hue 260, and sat 20.\n        \u2022 At 19:40, ensure **lamp_be_bedside** is switched on with brightness 5 and hue 30.\n        \u2022 At 20:00, switch both lights off.\n        Additionally, set a new reminder each night at 19:25: \"Brush teeth!\" for Ethan.\n        Finally, update the to-do list \"todo\" by appending \"Lay out school clothes\".\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists",
                    "entity_id": "list_todo"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_be",
                    "update": {
                        "position": 0
                    },
                    "schedule_at": "2025-07-29T19:30:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceStateTimer",
                "arguments": {
                    "device_id": "light_be_ceiling",
                    "schedule_end": "2025-07-29T20:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 25,
                        "color": {
                            "hue": 260,
                            "saturation": 20
                        }
                    },
                    "schedule_at": "2025-07-29T19:30:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceStateTimer",
                "arguments": {
                    "device_id": "lamp_be_bedside",
                    "schedule_end": "2025-07-29T20:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 5,
                        "color": {
                            "hue": 30
                        }
                    },
                    "schedule_at": "2025-07-29T19:40:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_brush_teeth_ethan",
                        "member_id": "ethan_johnson",
                        "target": {
                            "type": "note",
                            "text": "Brush teeth!"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=19;BYMINUTE=25"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_todo",
                    "item": {
                        "item": "Lay out school clothes",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_26",
        "instruction": "\n        You intend to add a kitchen air-purifier (id purifier_kt). It is from vendor Coway, model AP-1512HHS, firmware 1.0.0, and features adjustable settings (power, fan_speed, eco_mode).\n        Position it in the Kitchen.\n        Each day at 07:00, commencing today 2025-07-29, access the **sensor_lr_air_quality**. Irrespective of the read value, operate purifier_kt at fan_speed \"high\" for 30 minutes, then switch it to eco_mode.\n        Also, append \"Replacement filter (Coway 1512)\" to the reading_list already containing Clean Code and Designing Data-Intensive Applications, both quantity 1, and remember the tag \"books\".\n        ",
        "actions": [
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "purifier_kt",
                        "type": "air_purifier",
                        "location": "Kitchen",
                        "vendor": "Coway",
                        "model": "AP-1512HHS",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "fan_speed",
                            "eco_mode"
                        ],
                        "state": {
                            "power": "off",
                            "fan_speed": "low",
                            "eco_mode": false
                        },
                        "scheduled_updates": []
                    }
                },
            },
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "sensors",
                    "filters": {
                        "id": "sensor_lr_air_quality"
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "purifier_kt",
                    "update": {
                        "power": "on",
                        "fan_speed": "high"
                    },
                    "schedule_at": "2025-07-29T07:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "purifier_kt",
                    "update": {
                        "fan_speed": "low",
                        "eco_mode": true
                    },
                    "schedule_at": "2025-07-29T07:30:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_reading",
                        "tags": [
                            "books"
                        ],
                        "items": [
                            {
                                "item": "Clean Code",
                                "quantity": 1
                            },
                            {
                                "item": "Designing Data-Intensive Applications",
                                "quantity": 1
                            },
                            {
                                "item": "Replacement filter (Coway 1512)",
                                "quantity": 1
                            }
                        ]
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "\n        Today is 2025-07-15 08:00. Robert Johnson is working from home today and you want to set up an optimal work environment for him.\n        1. Initially, handle checking the current temperature from the Living Room thermometer sensor.\n        2. In the event that the temperature exceeds 24\u00b0C, proceed to activate the Central AC with mode=cool, setpoint_c=22, fan_speed=medium.\n        3. Ensure to verify the current air quality using the Living Room air quality sensor.\n        4. Should CO2 levels surpass 600 ppm, proceed to open the Living Room curtain to position 100 for ventilation.\n        5. Proceed to configure Robert's work lighting: switch on the Living Room ceiling light with brightness=80, color kelvin=5000.\n        6. Initiate the creation of a new custom list termed \"John's Work Setup\" (id \"list_john_work\") tagged \"work\" and \"productivity\".\n        7. Include the following items to the work list: \"Ergonomic mouse pad\" x1, \"Blue light glasses\" x1, \"Desk organizer\" x1.\n        8. Schedule the dishwasher to commence operation at 10:00 today with power=on, cycle=eco aiming to minimize noise during work hours.\n        9. Establish a daily reminder set for 11:30 titled \"Take work break\" featuring a mobile_push notification.\n        10. At 17:00 today, arrange for the Living Room ceiling light to automatically dim to brightness=50 and adjust the curtain to position=20.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 22,
                        "fan_speed": "medium"
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_lr_air_quality"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_lr",
                    "update": {
                        "power": "on",
                        "position": 100
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 80,
                        "color": {
                            "kelvin": 5000
                        }
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_john_work",
                        "name": "Robert's Work Setup",
                        "tags": [
                            "work",
                            "productivity"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_john_work",
                    "item": {
                        "item": "Ergonomic mouse pad",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_john_work",
                    "item": {
                        "item": "Blue light glasses",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_john_work",
                    "item": {
                        "item": "Desk organizer",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "on",
                        "cycle": "eco"
                    },
                    "schedule_at": "2025-07-15T10:00:00"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_work_break",
                        "target": {
                            "type": "note",
                            "text": "Take work break"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=11;BYMINUTE=30"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 50
                    },
                    "schedule_at": "2025-07-15T17:00:00"
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_lr",
                    "update": {
                        "power": "on",
                        "position": 20
                    },
                    "schedule_at": "2025-07-15T17:00:00"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_28",
        "instruction": "\n        It's 2025-07-16 19:30. Jessica Johnson is returning from her hospital shift and you want to set up a relaxing evening routine for her.\n        1. Verify Jessica's member profile to confirm her work schedule and preferences.\n        2. Check the bedroom smoke detector to ensure the battery level remains above 85%.\n        3. Develop a \"Post-Shift Relaxation\" scene (id \"scene_emily_relax\") that incorporates:\n           - Master bedroom ceiling light on with brightness=40, hue=270, saturation=30 (purple ambiance)\n           - Master bedroom night lamp on with brightness=20, hue=30 (warm orange)\n           - Master bedroom curtain closed to position=0\n           - Central heater on with mode=heat, setpoint_c=23\n        4. Organize this scene to execute at 20:00 today.\n        5. Revise Jessica's existing diet plan list by inserting \"Chamomile tea\" x2 and \"Dark chocolate\" x1.\n        6. Formulate a weekly reminder every Wednesday at 19:00 titled \"Prep relaxation bath\" featuring mobile_push.\n        7. At 21:30 tonight, ensure the master bedroom ceiling light automatically turns off, and dim the night lamp to brightness=10.\n        8. Add \"Lavender essential oil\" x1 to the shopping list intended for aromatherapy.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "members",
                    "entity_id": "emily_johnson"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_bed_smoke"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_emily_relax",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 40,
                                    "color": {
                                        "hue": 270,
                                        "saturation": 30
                                    }
                                }
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {
                                    "power": "on",
                                    "brightness": 20,
                                    "color": {
                                        "hue": 30
                                    }
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {
                                    "power": "on",
                                    "position": 0
                                }
                            },
                            {
                                "device_id": "heater_home",
                                "update": {
                                    "power": "on",
                                    "mode": "heat",
                                    "setpoint_c": 23
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-16T20:00:00"
                        ]
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "update": {
                        "power": "off"
                    },
                    "schedule_at": "2025-07-16T21:30:00"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists",
                    "entity_id": "list_diet_plan"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_diet_plan",
                    "item": {
                        "item": "Chamomile tea",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_diet_plan",
                    "item": {
                        "item": "Dark chocolate",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_emily_bath",
                        "target": {
                            "type": "note",
                            "text": "Prepare relaxing bath with oils"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=19;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "update": {
                        "brightness": 10
                    },
                    "schedule_at": "2025-07-16T21:30:00"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "Lavender essential oil",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_29",
        "instruction": "\n        The current date and time is 2025-07-25 14:00. Emma Johnson has a playdate scheduled with Sofia Rodriguez at 16:00, and preparation is required.\n        1. Begin by reviewing Emma's member profile to determine her room assignment and any preferences.\n        2. Check Sofia's member profile to find out her pickup requirements and any allergies.\n        3. Confirm that both girls have peanut allergies and verify that no peanut products are included on any grocery lists.\n        4. Develop a \"Playdate Setup\" scene (id \"scene_playdate\") incorporating the West Bedroom ceiling light set to power on and brightness=70, and adjust the West Bedroom curtain to position=100.\n        5. Plan to run the dishwasher at 15:30 using cycle=quiet to ensure minimal noise during the playdate.\n        6. Create a custom list \"Playdate Snacks\" (id \"list_playdate_snacks\") with tags \"kids\" and \"snacks\".\n        7. Include safe snacks in the list: \"Apple slices\" x2, \"Cheese sticks\" x4, \"Juice boxes\" x2.\n        8. Program a reminder set for 17:30 today to \"Call Maria Martinez for Sofia pickup\" using mobile_push and high priority notification.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "members"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_playdate",
                        "actions": [
                            {
                                "device_id": "light_bw_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 70
                                }
                            },
                            {
                                "device_id": "curtain_bw",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            }
                        ],
                        "scheduled_runs": []
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "on",
                        "cycle": "quiet"
                    },
                    "schedule_at": "2025-07-25T15:30:00"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_playdate_snacks",
                        "name": "Playdate Snacks",
                        "tags": [
                            "kids",
                            "snacks"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_playdate_snacks",
                    "item": {
                        "item": "Apple slices",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_playdate_snacks",
                    "item": {
                        "item": "Cheese sticks",
                        "quantity": 4
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_playdate_snacks",
                    "item": {
                        "item": "Juice boxes",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_mia_pickup",
                        "target": {
                            "type": "note",
                            "text": "Call Maria Martinez for Sofia pickup"
                        },
                        "trigger": {
                            "datetime": "2025-07-25T17:30:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "high"
                        }
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_30",
        "instruction": "\n        The date and time are now 2025-07-18 09:00. The family is getting ready for the visit of Christopher Chen and Jennifer Chen on Sunday evening at 18:30.\n        1. Start by checking Christopher Chen's member profile to verify his vehicle type and parking needs.\n        2. Examine Jennifer Chen's member profile to understand her dietary preferences and what she will bring.\n        3. Inspect the front door contact sensor and hallway motion sensor to ensure the security systems are operational.\n        4. Set up a \"Sunday Dinner Prep\" scene (id \"scene_sunday_dinner\"), featuring a \"Warm and welcoming atmosphere for dinner guests\", including:\n           - Living room ceiling light activated at brightness=75, kelvin=3000 (warm lighting)\n           - Living room floor lamp turned on with brightness=50\n           - Living room curtain opened to position=80\n           - Central AC running with mode=cool, setpoint_c=24, fan_speed=auto\n        5. Schedule this scene to initiate at 17:30 today.\n        6. Refresh the weekend groceries list by adding \"Vegan cheese\" x1 and \"Sourdough bread\" x1 for Jennifer.\n        7. Construct a custom list \"Sunday Dinner Menu\" (id \"list_sunday_menu\") with tags \"dinner\" and \"guests\".\n        8. Introduce menu items: \"Grilled salmon\" x4, \"Roasted vegetables\" x1, \"Rice pilaf\" x1, \"Chocolate dessert\" x1.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "members",
                    "entity_id": "david_chen"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "members",
                    "entity_id": "sarah_chen"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_front_door"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_hall_motion"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_sunday_dinner",
                        "actions": [
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 75,
                                    "color": {
                                        "kelvin": 3000
                                    }
                                }
                            },
                            {
                                "device_id": "light_lr_floor",
                                "update": {
                                    "power": "on",
                                    "brightness": 50
                                }
                            },
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 80
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 24,
                                    "fan_speed": "auto"
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-18T17:30:00"
                        ]
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists",
                    "entity_id": "list_groceries_weekend"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_groceries_weekend",
                    "item": {
                        "item": "Vegan cheese",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_groceries_weekend",
                    "item": {
                        "item": "Sourdough bread",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_sunday_menu",
                        "tags": [
                            "dinner",
                            "guests"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_sunday_menu",
                    "item": {
                        "item": "Grilled salmon",
                        "quantity": 4
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_sunday_menu",
                    "item": {
                        "item": "Roasted vegetables",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_sunday_menu",
                    "item": {
                        "item": "Rice pilaf",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_sunday_menu",
                    "item": {
                        "item": "Chocolate dessert",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_31",
        "instruction": "\n        Today is 2025-07-19 07:00. Your task is to assist Ethan Smith with his morning piano practice routine.\n        1. Begin by checking Ethan's member profile for his room assignment, schedule, and music preferences.\n        2. Examine the current states of the East Bedroom ceiling light and bedside lamp.\n        3. Develop a \"Piano Practice\" scene (id \"scene_piano_practice\") that includes:\n           - East bedroom ceiling light on with brightness=90, hue=60, saturation=20 (bright yellow-green for focus)\n           - East bedroom bedside lamp off to avoid glare\n           - East bedroom curtain open to position=100 for natural light\n           - Central heater on with mode=heat, setpoint_c=21 (cooler for concentration)\n        4. Schedule this scene to activate on 2025-07-19 at 07:30 (after Ethan wakes up at 07:15).\n        5. Create a custom list \"Ethan's Music Goals\" (id \"list_ethan_music\") tagged \"education\" and \"music\".\n        6. Add practice goals: \"Scale exercises\" x1, \"Beginner songs\" x2, \"Rhythm practice\" x1.\n        7. Set a daily reminder at 07:25: \"Time for piano practice!\" with mobile_push.\n        8. Ensure that at 08:00 daily, the East bedroom ceiling light is turned off and the curtain is closed to position=50.\n        9. Update the todo list by adding \"Schedule Ethan's piano lesson\" x1.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "members",
                    "entity_id": "ethan_johnson"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_piano_practice",
                        "actions": [
                            {
                                "device_id": "light_be_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 90,
                                    "color": {
                                        "hue": 60,
                                        "saturation": 20
                                    }
                                }
                            },
                            {
                                "device_id": "lamp_be_bedside",
                                "update": {
                                    "power": "off"
                                }
                            },
                            {
                                "device_id": "curtain_be",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "heater_home",
                                "update": {
                                    "power": "on",
                                    "mode": "heat",
                                    "setpoint_c": 21
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-19T07:30"
                        ]
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_ethan_music",
                        "tags": [
                            "education",
                            "music"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_ethan_music",
                    "item": {
                        "item": "Scale exercises",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_ethan_music",
                    "item": {
                        "item": "Beginner songs",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_ethan_music",
                    "item": {
                        "item": "Rhythm practice",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_ethan_piano",
                        "target": {
                            "type": "note",
                            "text": "Time for piano practice!"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=7;BYMINUTE=25"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "ModifyDeviceState",
                "arguments": {
                    "device_id": "curtain_be",
                    "update": {
                        "power": "on",
                        "position": 50
                    },
                    "schedule_at": "2025-07-20T08:00:00",
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_todo",
                    "item": {
                        "item": "Schedule Ethan's piano lesson",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "\n        Today is 2025-07-20 15:00. With Christopher Wilson arriving for a weekend visit, prepare guest accommodations.\n        1. First, check Christopher Wilson's member profile for his visit preferences, allergies, and hobbies.\n        2. Analyze all bedroom devices to determine the best setup for the guest room.\n        3. Review the current status of all existing reminders to prevent conflicts.\n        4. Set up a \"Guest Welcome\" scene (id \"scene_guest_welcome\") to provide a comfortable and welcoming environment for Christopher's visit that includes:\n           - Master bedroom ceiling light on with brightness=60, hue=45, saturation=40 (warm amber)\n           - Master bedroom night lamp on with brightness=25\n           - Master bedroom curtain open to position=90\n           - Central AC on with mode=cool, setpoint_c=25, fan_speed=low (comfortable for guest)\n        5. Schedule this scene to execute at 16:30 today (30 minutes before expected arrival).\n        6. Develop a custom list \"Guest Comfort Items\" (id \"list_guest_comfort\") tagged \"guest\" and \"hospitality\".\n        7. Include comfort items: \"Extra towels\" x3, \"Board games\" x2; and if he is allergic to cats, add \"Cat-free bedding\" x1.\n        8. Update the weekend groceries list by adding 1 quantity of his favorite food.\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "members",
                    "filters": {
                        "first_name": "Christopher",
                        "last_name": "Brown"
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "rooms"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "reminders"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_guest_welcome",
                        "actions": [
                            {
                                "device_id": "light_br_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 60,
                                    "color": {
                                        "hue": 45,
                                        "saturation": 40
                                    }
                                }
                            },
                            {
                                "device_id": "lamp_br_night",
                                "update": {
                                    "power": "on",
                                    "brightness": 25
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {
                                    "power": "on",
                                    "position": 90
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 25,
                                    "fan_speed": "low"
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-20T16:30:00"
                        ]
                    }
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_guest_comfort",
                        "tags": [
                            "guest",
                            "hospitality"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_guest_comfort",
                    "item": {
                        "item": "Extra towels",
                        "quantity": 3
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_guest_comfort",
                    "item": {
                        "item": "Board games",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_guest_comfort",
                    "item": {
                        "item": "Cat-free bedding",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_groceries_weekend",
                    "item": {
                        "item": "Thai green curry",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "\n        Since summer is hot, replace the default morning routine just for July.\n        \u2022 Clear out the scheduled_runs array for **scene_good_morning**.\n        \u2022 Establish a new scene **scene_summer_morning** for a Cool-summer wake-up routine, which:\n            - opens curtain_lr, curtain_br, curtain_bw, curtain_be (position 100)\n            - switches heater_home power:off\n            - activates ac_home power:on, mode:cool, setpoint_c:23, fan_speed:low\n            - turns light_lr_ceiling power:on, brightness:50, color:{kelvin:5000}\n          Schedule this routine to run daily at 06:45 in July solely (`scheduled_runs=[\"RRULE:FREQ=DAILY;BYMONTH=7;BYHOUR=6;BYMINUTE=45\"]`).\n        Execute the new scene once immediately.\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "scenes",
                    "filters": {
                        "id": "scene_good_morning"
                    }
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_good_morning",
                        "scheduled_runs": []
                    }
                },
            },
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "rooms",
                    "filters": {
                        "id": "living_room"
                    }
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_summer_morning",
                        "actions": [
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "curtain_br",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "curtain_bw",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "curtain_be",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                }
                            },
                            {
                                "device_id": "heater_home",
                                "update": {
                                    "power": "off"
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 23,
                                    "fan_speed": "low"
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "on",
                                    "brightness": 50,
                                    "color": {
                                        "kelvin": 5000
                                    }
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "RRULE:FREQ=DAILY;BYMONTH=7;BYHOUR=6;BYMINUTE=45"
                        ]
                    }
                },
            },
            {
                "name": "RunScene",
                "arguments": {
                    "scene_id": "scene_summer_morning"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "\n        Activate the recording for the front door camera and back door camera now, and also enable online streaming.\n        \u2022 Additionally, set up two reminders:\n            - **rem_cam_front_batt**: \"Front Camera - check battery\" on a monthly basis on the 1st at 09:00 (push)\n            - **rem_cam_back_batt**: \"Back Camera - check battery\" monthly on the 1st at 09:05 (push).\n        \u2022 To do this, both cameras were installed at the Front door and Back door respectively, as their new batteries are still at 100%.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors"
                },
            },
            {
                "name": "ModifySensorState",
                "arguments": {
                    "sensor_id": "camera_front_door",
                    "update": {
                        "stream_online": true,
                        "recording": true
                    }
                },
            },
            {
                "name": "ModifySensorState",
                "arguments": {
                    "sensor_id": "camera_back_door",
                    "update": {
                        "stream_online": true,
                        "recording": true
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_cam_front_batt",
                        "target": {
                            "type": "note",
                            "text": "Front Camera - check battery"
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
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_cam_back_batt",
                        "target": {
                            "type": "note",
                            "text": "Back Camera - check battery"
                        },
                        "trigger": {
                            "rrule": "FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=5"
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
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_35",
        "instruction": "\n        You are organizing a camping trip for 2025-07-18 and need to arrange your packing.\n        \u2022 You aim to craft a new custom list **list_camping_packing** (\"Camping Packing List\", with tags camping+travel). The required items include:\n            - Tent x1, Sleeping Bag x4, Flashlight x3, Marshmallows x2.\n            (Set the current time to: 2025-07-29T14:40:00)\n        \u2022 Additionally, add 2 x \"Bug Spray\" to the list.\n        \u2022 You intend to create a new reminder with id **rem_camping_packing_check** named \"Camping packing check\" focusing on that list for 2025-07-17 at 20:00 (push) with normal priority.\n        \u2022 Another reminder is necessary with id **rem_camping_car_pack**, containing the note \"Pack car\" for 2025-07-18 at 07:00 (push) and normal priority.\n        ",
        "actions": [
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_camping_packing",
                        "tags": [
                            "camping",
                            "travel"
                        ],
                        "items": [
                            {
                                "item": "Tent",
                                "quantity": 1
                            },
                            {
                                "item": "Sleeping Bag",
                                "quantity": 4
                            },
                            {
                                "item": "Flashlight",
                                "quantity": 3
                            },
                            {
                                "item": "Marshmallows",
                                "quantity": 2
                            }
                        ]
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_camping_packing",
                    "item": {
                        "item": "Bug Spray",
                        "quantity": 2
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_camping_packing_check",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_camping_packing"
                        },
                        "trigger": {
                            "datetime": "2025-07-17T20:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_camping_car_pack",
                        "target": {
                            "type": "note",
                            "text": "Pack car"
                        },
                        "trigger": {
                            "datetime": "2025-07-18T07:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "custom_lists",
                    "filters": {
                        "list_id": "list_camping_packing"
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_36",
        "instruction": "\n        You are looking to automate Ethan's routine for his Wednesday piano lesson.\n        \u2022 Set up a new reminder with id **rem_ethan_piano_practice** for \"Leave for piano lesson\" every Wednesday at 15:30 (repeating weekly), via push notification, with high priority.\n        \u2022 On each lesson day, starting 2025-07-25, program Ethan's bedside lamp to perform the following:\n            - At 15:25, it should turn on with power:on and brightness:100.\n            - At 15:40, it should turn off with power:off.\n        \u2022 It is also necessary to add 1 x \"Piano Sheet Book - Level 2\" to the shopping list.\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "members",
                    "filters": {
                        "first_name": "Ethan",
                        "last_name": "Smith"
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "rooms",
                    "entity_id": "bedroom_east"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices",
                    "entity_id": "lamp_be_bedside"
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "lamp_be_bedside",
                        "scheduled_updates": [
                            {
                                "timestamp": "2025-07-25T15:25:00",
                                "update": {
                                    "power": "on",
                                    "brightness": 100
                                },
                                "rrule": "FREQ=WEEKLY;BYDAY=WE"
                            },
                            {
                                "timestamp": "2025-07-25T15:40:00",
                                "update": {
                                    "power": "off"
                                },
                                "rrule": "FREQ=WEEKLY;BYDAY=WE"
                            }
                        ]
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "Piano Sheet Book - Level 2",
                        "quantity": 1
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_ethan_piano_practice",
                        "target": {
                            "type": "note",
                            "text": "Leave for piano lesson"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=WE;BYHOUR=15;BYMINUTE=30"
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
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "\n        You need to update the outdated yearly car-maintenance reminder.\n        \u2022 Initially, remove the existing car maintenance reminder.\n        \u2022 Next, establish a new reminder **rem_car_maintenance_new** with the note \"Annual car maintenance\" set for yearly on Dec 1st at 08:00 (via push).\n        \u2022 Also, initiate a new custom list **list_home_maintenance** (tagged maintenance) including the item \"Change HVAC filter\" x1. (The current time should be: 2025-07-29T14:50:00)\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "reminders",
                    "filters": {}
                },
            },
            {
                "name": "DeleteReminder",
                "arguments": {
                    "reminder_id": "rem_8f9fd8ae"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_car_maintenance_new",
                        "target": {
                            "type": "note",
                            "text": "Annual car maintenance"
                        },
                        "trigger": {
                            "rrule": "FREQ=YEARLY;BYMONTH=12;BYMONTHDAY=1;BYHOUR=8;BYMINUTE=0"
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
                },
            },
            {
                "name": "UpsertCustomList",
                "arguments": {
                    "custom_list": {
                        "list_id": "list_home_maintenance",
                        "tags": [
                            "maintenance"
                        ],
                        "items": []
                    }
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_home_maintenance",
                    "item": {
                        "item": "Change HVAC filter",
                        "quantity": 1
                    },
                    "action": "add"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "\n        You need to get ready for the upcoming heat-wave.\n        \u2022 Begin by setting up a new scene with id **scene_heat_wave**.\n            - The name must be: \"Heat Wave\"\n            - The description must be: \"Cool house & keep sun out.\"\n            - The actions include:\n                - curtain_lr should be power:on, position:0\n                - ac_home should be power:on, mode:cool, setpoint_c:21, fan_speed:high\n                - light_lr_ceiling should be power:off\n          (Do not set a schedule yet).\n        \u2022 Execute this scene immediately.\n        \u2022 Additionally, create a new reminder with id **rem_heat_wave_check** for \"Check indoor temperature\" daily at 12:00 via push.\n        \u2022 Conclude by adding 5 x \"Ice cream\" to the shopping list.\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "sensors",
                    "entity_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_heat_wave",
                        "name": "Heat Wave",
                        "description": "Cool house & keep sun out.",
                        "actions": [
                            {
                                "device_id": "curtain_lr",
                                "update": {
                                    "power": "on",
                                    "position": 0
                                }
                            },
                            {
                                "device_id": "ac_home",
                                "update": {
                                    "power": "on",
                                    "mode": "cool",
                                    "setpoint_c": 21,
                                    "fan_speed": "high"
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "off"
                                }
                            }
                        ]
                    }
                },
            },
            {
                "name": "RunScene",
                "arguments": {
                    "scene_id": "scene_heat_wave"
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "custom_lists"
                },
            },
            {
                "name": "ModifyCustomListItem",
                "arguments": {
                    "list_id": "list_shopping",
                    "item": {
                        "item": "Ice cream",
                        "quantity": 5
                    },
                    "action": "add"
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_heat_wave_check",
                        "target": {
                            "type": "note",
                            "text": "Check indoor temperature"
                        },
                        "trigger": {
                            "rrule": "FREQ=DAILY;BYHOUR=12;BYMINUTE=0"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "status": "active",
                        "meta": {
                            "priority": "normal"
                        }
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_39",
        "instruction": "\n        Beginning tomorrow (2025-07-30), set up Emma Johnson's weekday wake-up routine to be automated. Ensure this happens every weekday.\n        \u2022 At 06:55 every weekday, turn on her bedroom light (set brightness at 80).\n        \u2022 Concurrently, open her bedroom curtain (to position 100, power on).\n        \u2022 Create a reminder **rem_olivia_pack_lunch** (\"Olivia \u2013 pack lunch\") that pushes a notification at 07:10 every weekday (with high priority).\n        ",
        "actions": [
            {
                "name": "QueryEntities",
                "arguments": {
                    "entity_type": "members",
                    "filters": {
                        "first_name": "Emma",
                        "last_name": "Smith"
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "rooms",
                    "entity_id": "bedroom_west"
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "light_bw_ceiling",
                        "scheduled_updates": [
                            {
                                "timestamp": "2025-07-30T06:55:00",
                                "update": {
                                    "power": "on",
                                    "brightness": 80
                                },
                                "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                            }
                        ]
                    }
                },
            },
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "devices",
                    "entity_id": "curtain_bw"
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "curtain_bw",
                        "scheduled_updates": [
                            {
                                "timestamp": "2025-07-30T06:55:00",
                                "update": {
                                    "power": "on",
                                    "position": 100
                                },
                                "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                            }
                        ]
                    }
                },
            },
            {
                "name": "UpsertReminder",
                "arguments": {
                    "reminder": {
                        "reminder_id": "rem_olivia_pack_lunch",
                        "target": {
                            "type": "note",
                            "text": "Pack lunch"
                        },
                        "trigger": {
                            "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR;BYHOUR=7;BYMINUTE=10"
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
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "\n        Set up bedtime comfort arrangements for the children.\n        \u2022 Add a new night-light device with the id **nightlight_be**.\n          Its type is light, from the vendor Hatch, model \"Rest 2nd Gen\", with firmware 1.0.0.\n          The state_params are [power, brightness, color], and its initial state is off/0/kelvin:2700.\n          (Updated at time is 2025-07-29T15:00:00)\n        \u2022 Connect it to the east bedroom.\n        \u2022 Configure its daily scheduled_updates as follows:\n            - 19:30 each day \u2192 power:on, brightness:10, color:{kelvin:2700}\n            - 07:00 each day \u2192 power:off.\n        \u2022 Develop a new scene with id **scene_kids_bedtime**.\n            - Name it \"Kids Bedtime\"\n            - Describe it as \"Wind-down lights for the kids.\"\n            - The actions include:\n                - nightlight_be should be power:on, brightness:10, color:{kelvin:2700}\n                - light_lr_ceiling should be power:off\n            Schedule it to activate at 20:00 tomorrow (2025-07-30).\n        ",
        "actions": [
            {
                "name": "GetEntity",
                "arguments": {
                    "entity_type": "rooms"
                },
            },
            {
                "name": "UpsertDevice",
                "arguments": {
                    "device": {
                        "id": "nightlight_be",
                        "type": "light",
                        "location": "East Bedroom",
                        "vendor": "Hatch",
                        "model": "Rest 2nd Gen",
                        "firmware_version": "1.0.0",
                        "state_params": [
                            "power",
                            "brightness",
                            "color"
                        ],
                        "state": {
                            "power": "off",
                            "brightness": 0,
                            "color": {
                                "kelvin": 2700
                            }
                        },
                        "scheduled_updates": [
                            {
                                "timestamp": "2025-07-29T19:30:00",
                                "update": {
                                    "power": "on",
                                    "brightness": 10,
                                    "color": {
                                        "kelvin": 2700
                                    }
                                },
                                "rrule": "FREQ=DAILY"
                            },
                            {
                                "timestamp": "2025-07-30T07:00:00",
                                "update": {
                                    "power": "off"
                                },
                                "rrule": "FREQ=DAILY"
                            }
                        ]
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "bedroom_east",
                    "device_id": "nightlight_be"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "scene": {
                        "id": "scene_kids_bedtime",
                        "name": "Kids Bedtime",
                        "description": "Wind-down lights for the kids.",
                        "actions": [
                            {
                                "device_id": "nightlight_be",
                                "update": {
                                    "power": "on",
                                    "brightness": 10,
                                    "color": {
                                        "kelvin": 2700
                                    }
                                }
                            },
                            {
                                "device_id": "light_lr_ceiling",
                                "update": {
                                    "power": "off"
                                }
                            }
                        ],
                        "scheduled_runs": [
                            "2025-07-30T20:00:00"
                        ]
                    }
                }
            }
        ],
        "outputs": []
    }
]
