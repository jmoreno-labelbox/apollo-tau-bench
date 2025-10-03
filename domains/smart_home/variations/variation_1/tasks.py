# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "res_01",
        "instruction": "\n        The time is 15:00 on 2025-07-28. Check the current temperature from the Living Room Thermometer and the CO2 level from the Living Room Air-Quality Sensor.\n\n        You need the following actions to take place if either the temperature rises above 22\u00b0C OR the CO2 levels surpass 750 ppm:\n        \u2022 Activate your central AC with these specific settings: cool mode, 22\u00b0C, and high fan speed\n        \u2022 Fully open your Living Room curtain\n        \u2022 Adjust your Living Room floor lamp to 40% brightness\n\n        Additionally, you want all these devices to automatically readjust to different settings at 16:30 on 2025-07-28:\n        \u2022 AC should power off\n        \u2022 Curtain should adjust to a 50% position\n        \u2022 Floor lamp should be set to 60% brightness\n        ",
        "actions": [
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_lr_air_quality"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "ac_home"
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "ac_home",
                    "timestamp_end": "2025-07-28T16:30:00",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 22,
                        "fan_speed": "high"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_lr",
                    "update": {
                        "position": 100
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "update": {
                        "power": "on",
                        "brightness": 40
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_lr",
                    "timestamp": "2025-07-28T16:30:00",
                    "update": {
                        "position": 50
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "timestamp": "2025-07-28T16:30:00",
                    "update": {
                        "brightness": 60
                    }
                }
            }
        ],
        "outputs": [
                "\"temperature_c\": 22.3",
                "\"co2_ppm\": 650"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_02",
        "instruction": "\n        Initiate a \"Movie Night\" mode starting at 20:00 on 2025-07-28. This entails the following:\n\n        First, apply these changes:\n        \u2022 Switch off your living room ceiling light\n        \u2022 Set your living room floor lamp to 15% brightness\n        \u2022 Close your living room curtain completely\n        \u2022 Set the central AC to cool mode at 21\u00b0C with low fan speed\n\n        Ensure the system remembers the current settings of all these devices. Then at 22:30, you want everything to revert to these specific settings:\n        \u2022 Ceiling light: on, at 70% brightness\n        \u2022 Floor lamp: 60% brightness\n        \u2022 Curtain: fully open\n        \u2022 AC: turned off\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "light_lr_ceiling"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "light_lr_floor"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "curtain_lr"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "ac_home"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "camera_front_door"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-07-28T20:00:00",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "timestamp": "2025-07-28T20:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 15
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_lr",
                    "timestamp": "2025-07-28T20:00:00",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "ac_home",
                    "timestamp": "2025-07-28T20:00:00",
                    "timestamp_end": "2025-07-28T22:30:00",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 21,
                        "fan_speed": "low"
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-07-28T22:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 70
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "timestamp": "2025-07-28T22:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 60
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_lr",
                    "timestamp": "2025-07-28T22:30:00",
                    "update": {
                        "position": 100
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
        "instruction": "\n        Commencing on Monday, August 1st, 2025, you aim to establish a weekday home routine:\n\n        Arrange the following schedule for each weekday morning:\n        \u2022 06:45 - Fully open the curtain in the west bedroom\n        \u2022 06:50 - Adjust the west bedroom ceiling light to 70% brightness\n        \u2022 06:55 - Fully open the curtain in the living room\n\n        Moreover, ensure the dishwasher operates in eco mode every weekday night at 23:00, with a cycle duration of 120 minutes, confirming the door is securely closed.\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "dishwasher"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_bw",
                    "timestamp": "2025-08-01T06:45:00",
                    "update": {
                        "position": 100
                    },
                    "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "timestamp": "2025-08-01T06:50:00",
                    "update": {
                        "power": "on",
                        "brightness": 70
                    },
                    "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_lr",
                    "timestamp": "2025-08-01T06:55:00",
                    "update": {
                        "position": 100
                    },
                    "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "timestamp": "2025-08-01T23:00:00",
                    "update": {
                        "power": "on",
                        "cycle": "eco",
                        "time_remaining_min": 120,
                        "door": "closed"
                    },
                    "rrule": "FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_04",
        "instruction": "\n        As you head out this morning, you need to carry out an extensive shutdown routine. Here's your requirement:\n\n        Initially, have the system provide a report if the front door is open (sensor_id: sensor_front_door) and if there is any motion detected in the hallway (sensor_id: sensor_hall_motion).\n\n        Next, execute these tasks:\n        \u2022 Turn off every light in the house (including living room ceiling and floor lights, all bedroom ceiling lights, night lamps, and desk lamps)\n        \u2022 Switch off the AC\n        \u2022 Completely close all curtains in the house\n\n        For added security, ensure the living room ceiling light is activated at 30% brightness at 19:30 that evening (July 29th, 2025).\n        ",
        "actions": [
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_front_door"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_hall_motion"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_bw_desk",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_be_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_be_bedside",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_lr",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_br",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_bw",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_be",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-07-29T19:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 30
                    }
                }
            }
        ],
        "outputs": [
                "\"door_open\": false",
                "\"motion_detected\": false"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_05",
        "instruction": "\n        Upon detecting the smell of smoke, you require:\n\n        \u2022 An immediate shutdown of both your heater and AC\n        \u2022 The ceiling light and night lamp in your bedroom to activate at full brightness using a red alert color\n        \u2022 Both your front and back door cameras to initiate recording\n        \u2022 Automatic shutdown of the bedroom lights at 02:00 on July 29th, 2025\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "heater"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "heater_home",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "timestamp_end": "2025-07-29T02:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 100,
                        "color": {
                            "hue": 0,
                            "saturation": 100
                        }
                    }
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "timestamp_end": "2025-07-29T02:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 100,
                        "color": {
                            "hue": 0,
                            "saturation": 100
                        }
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "camera_front_door",
                    "update": {
                        "recording": true
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "camera_back_door",
                    "update": {
                        "recording": true
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_06",
        "instruction": "\n        For integrating a new humidifier into your living room setup, ensure it is configured with these precise details:\n        \u2022 ID: humidifier_lr\n        \u2022 Name: Living Room Humidifier\n        \u2022 Location: Living Room\n        \u2022 Vendor: Levoit\n        \u2022 Model: Classic300S\n        \u2022 Firmware version: 1.0.0\n        \u2022 State parameters: power, mode, humidity_setpoint_pct\n        \u2022 State: power=off, mode=auto, humidity_setpoint_pct=45\n\n        Once configuration is complete, direct the system to:\n        \u2022 Include it in your living room's device list\n        \u2022 Activate the humidifier in continuous mode with a 45% target at 15:00 on July 28th, 2025\n        \u2022 Arrange for it to automatically deactivate at 17:00 on July 28th, 2025\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "humidifier_lr",
                    "type": "humidifier",
                    "name": "Living Room Humidifier",
                    "location": "Living Room",
                    "vendor": "Levoit",
                    "model": "Classic300S",
                    "firmware_version": "1.0.0",
                    "state_params": [
                        "power",
                        "mode",
                        "humidity_setpoint_pct"
                    ],
                    "state": {
                        "power": "off",
                        "mode": "auto",
                        "humidity_setpoint_pct": 45
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "living_room",
                    "device_id": "humidifier_lr"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "humidifier_lr",
                    "timestamp": "2025-07-28T15:00:00",
                    "update": {
                        "power": "on",
                        "mode": "continuous",
                        "humidity_setpoint_pct": 45
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "humidifier_lr",
                    "timestamp": "2025-07-28T17:00:00",
                    "update": {
                        "power": "off"
                    }
                }
            }
        ],
        "outputs": [
                "\"humidity_pct\": 45.2"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_07",
        "instruction": "\n        You purchased a Dyson HP04 auxiliary heater. Configure it with these settings:\n        \u2022 ID: heater_bs_aux\n        \u2022 Initial settings: off, heat mode, 15\u00b0C target\n        \u2022 Location: Basement\n        \u2022 Vendor: Dyson\n        \u2022 Model: HP04\n        \u2022 Firmware version: 2.0.0\n        \u2022 State parameters: power, mode, setpoint_c\n        \u2022 State: power=off, mode=heat, setpoint_c=15\n\n        Ensure that, for safety reasons, the heater automatically shuts off at 07:00 daily starting July 29th, 2025\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "heater_bs_aux",
                    "type": "heater",
                    "location": "Basement",
                    "vendor": "Dyson",
                    "model": "HP04",
                    "firmware_version": "2.0.0",
                    "state_params": [
                        "power",
                        "mode",
                        "setpoint_c"
                    ],
                    "state": {
                        "power": "off",
                        "mode": "heat",
                        "setpoint_c": 15
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "basement",
                    "device_id": "heater_bs_aux"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "heater_bs_aux",
                    "timestamp": "2025-07-29T07:00:00",
                    "update": {
                        "power": "off"
                    },
                    "rrule": "FREQ=DAILY"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_08",
        "instruction": "\n        You are setting up a Rachio Gen 3 smart sprinkler controller for your garden. Configure it as follows:\n        \u2022 ID: sprinkler_garden\n        \u2022 Initial state: off, auto mode\n        \u2022 Vendor: Rachio\n        \u2022 Name: Backyard Sprinkle\n        \u2022 Location: \"Backyard\"\n        \u2022 Model: Gen 3\n        \u2022 Firmware version: 3.0.0\n        \u2022 And set state with:\n            \u2022 Power: Off\n            \u2022 Mode: Auto\n            \u2022 duration_min: 0\n\n        For the watering schedule, arrange the following:\n        \u2022 Daily watering should begin at 06:00 commencing July 29th, 2025\n        \u2022 Each session is to run for 20 minutes in manual mode\n        \u2022 Ensure the system automatically turns off at 06:20\n        \u2022 Skip watering sessions on July 4th and 5th, 2026\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "sprinkler_garden",
                    "type": "sprinkler",
                    "name": "Backyard Sprinkle",
                    "location": "Backyard",
                    "vendor": "Rachio",
                    "model": "Gen 3",
                    "firmware_version": "3.0.0",
                    "state_params": [
                        "power",
                        "mode",
                        "duration_min"
                    ],
                    "state": {
                        "power": "off",
                        "mode": "auto",
                        "duration_min": 0
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "sprinkler_garden",
                    "timestamp": "2025-07-29T06:00:00",
                    "timestamp_end": "2025-07-29T06:20:00",
                    "update": {
                        "power": "on",
                        "mode": "manual",
                        "duration_min": 20
                    },
                    "rrule": "FREQ=DAILY;UNTIL=20260703T235959"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "sprinkler_garden",
                    "timestamp": "2026-07-06T06:00:00",
                    "timestamp_end": "2026-07-06T06:20:00",
                    "update": {
                        "power": "on",
                        "mode": "manual",
                        "duration_min": 20
                    },
                    "rrule": "FREQ=DAILY"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_09",
        "instruction": "\n        Ensure a rooftop solar power meter is added to enhance energy efficiency of AC usage. Specifications include:\n\n        An Enphase IQ7 power meter installation with:\n        \u2022 ID: device_solar_power\n        \u2022 Type: sensor\n        \u2022 Initial reading: 4200W generation\n        \u2022 Name: Rooftop Solar Power Meter\n        \u2022 Location: Roof\n        \u2022 Vendor: Enphase\n        \u2022 Model: IQ7\n        \u2022 Firmware version: 1.0.1\n        \u2022 State parameters: power_generation_w\n        \u2022 State: power_generation_w=4200\n\n        Coordinate the system to verify power generation and living room temperature, and set the AC to cool mode at 20\u00b0C with auto fan speed.\n\n        Request the system to report on living room temperature and power generation.\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "device_solar_power",
                    "type": "sensor",
                    "name": "Rooftop Solar Power Meter",
                    "location": "Roof",
                    "vendor": "Enphase",
                    "model": "IQ7",
                    "firmware_version": "1.0.1",
                    "state_params": [
                        "power_generation_w"
                    ],
                    "state": {
                        "power_generation_w": 4200
                    }
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "device_solar_power"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 20,
                        "fan_speed": "auto"
                    }
                }
            }
        ],
        "outputs": [
                "\"temperature_c\": 22.3",
                "\"power_generation_w\": 4200"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_10",
        "instruction": "\n        Implement an Aqara T1 ambient light sensor for automatic control of living room lighting. Requirements include:\n        \u2022 ID: device_lr_lux\n        \u2022 Name: Aqara T1 Ambient Light Sensor\n        \u2022 Type: sensor\n        \u2022 Location: Living Room\n        \u2022 Vendor: Aqara\n        \u2022 Model: T1 Ambient Light\n        \u2022 Firmware version: 1.0.0\n        \u2022 State parameters: illuminance_lux, battery_level\n        \u2022 State: illuminance_lux=400, battery_level=100\n\n        Ensure the system reports the illuminance level provided by it. Subsequently, have the system activate the living room ceiling light at 50% brightness.\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "device_lr_lux",
                    "type": "sensor",
                    "name": "Aqara T1 Ambient Light Sensor",
                    "location": "Living Room",
                    "vendor": "Aqara",
                    "model": "T1 Ambient Light",
                    "firmware_version": "1.0.0",
                    "state_params": [
                        "illuminance_lux",
                        "battery_level"
                    ],
                    "state": {
                        "illuminance_lux": 400,
                        "battery_level": 100
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "living_room",
                    "device_id": "device_lr_lux"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "device_lr_lux"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 50
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
        "instruction": "\n        In the master bedroom, you wish to take a nap. To prepare, please:\n        \u2022 Completely close the bedroom curtain\n        \u2022 Switch off the ceiling light\n        \u2022 Adjust the night lamp to 10% brightness with hue 30 and saturation 20\n        \u2022 Set the AC to cool mode at 24\u00b0C with a low fan speed\n\n        At 15:30 on the same day (July 28th), you would like everything to revert to these settings:\n        \u2022 Open the curtain fully\n        \u2022 Illuminate the ceiling light to 60% brightness\n        \u2022 Adjust the night lamp to 30% brightness with hue 30 and saturation 60\n        \u2022 Power off the AC\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "GetDevice",
                "arguments": {
                    "device_id": "curtain_br"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_br",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "update": {
                        "power": "on",
                        "brightness": 10,
                        "color": {
                            "hue": 30,
                            "saturation": 20
                        }
                    }
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "ac_home",
                    "timestamp_end": "2025-07-28T15:30:00",
                    "update": {
                        "power": "on",
                        "mode": "cool",
                        "setpoint_c": 24,
                        "fan_speed": "low"
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_br",
                    "timestamp": "2025-07-28T15:30:00",
                    "update": {
                        "position": 100
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "timestamp": "2025-07-28T15:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 60
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "timestamp": "2025-07-28T15:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 30,
                        "color": {
                            "hue": 30,
                            "saturation": 60
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
        "user_id": "res_12",
        "instruction": "\n        You suspect that your sink may be leaking. Therefore, please:\n\n        \u2022 Immediately switch off the dishwasher\n        \u2022 Change the living room ceiling light to bright red as a visual alert\n        \u2022 Activate recording on both front and back door cameras\n\n        You desire a report from the system indicating if the leak detection sensor (sensor_id: sensor_sink_leak) confirms a leak.\n        ",
        "actions": [
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 100,
                        "color": {
                            "hue": 0,
                            "saturation": 100
                        }
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "camera_front_door",
                    "update": {
                        "recording": true
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "camera_back_door",
                    "update": {
                        "recording": true
                    }
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_sink_leak"
                }
            }
        ],
        "outputs": [
                "\"leak_detected\": false"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_13",
        "instruction": "\n        Initiate an energy-saving examination. Initially, generate a report on these conditions:\n        \u2022 Presence of motion in the hallway\n        \u2022 Detection of individuals at either the front or back door cameras\n\n        If there is an absence of motion or individuals, you require:\n        \u2022 All bedroom lighting fixtures to be deactivated (ceiling lights, night lamps, and desk lamps)\n        \u2022 The system to examine the living room temperature and:\n          - Deactivate the heater if it exceeds 20\u00b0C\n          - Deactivate the AC if it is under 23\u00b0C\n        ",
        "actions": [
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_hall_motion"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "camera_front_door"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "camera_back_door"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_bw_desk",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_be_ceiling",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "lamp_be_bedside",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "heater"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "heater_home",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "ac_home",
                    "update": {
                        "power": "off"
                    }
                }
            }
        ],
        "outputs": [
                "\"motion_detected\": false",
                "\"person_detected\": false",
                "\"person_detected\": false"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_14",
        "instruction": "\n        Arrange the East Bedroom for an upcoming guest set to arrive on July 29th, 2025. By 21:00, ensure the following:\n\n        \u2022 Fully close the curtain\n        \u2022 Adjust the bedside lamp to 40% brightness with hue 50 and saturation 80\n        \u2022 Adjust the ceiling light to 30% brightness with hue 210 and saturation 50\n\n        By midnight (00:00 on July 30th), you necessitate:\n        \u2022 Both lights to be switched off\n        \u2022 The curtain to be fully open\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_be",
                    "timestamp": "2025-07-29T21:00:00",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "lamp_be_bedside",
                    "timestamp": "2025-07-29T21:00:00",
                    "timestamp_end": "2025-07-30T00:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 40,
                        "color": {
                            "hue": 50,
                            "saturation": 80
                        }
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_be_ceiling",
                    "timestamp": "2025-07-29T21:00:00",
                    "timestamp_end": "2025-07-30T00:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 30,
                        "color": {
                            "hue": 210,
                            "saturation": 50
                        }
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_be",
                    "timestamp": "2025-07-30T00:00:00",
                    "update": {
                        "position": 100
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
        "instruction": "\n        Have the system perform the following tasks:\n\n        \u2022 Evaluate the battery levels of your key sensors:\n          - Living room thermometer\n          - Hall motion sensor\n          - Front door sensor\n          - Bedroom smoke detector\n          - Sink leak sensor\n\n        Request the system to provide a full report. If any battery is under 80%, schedule a reminder to recharge it.\n        Create reminder id: rem_battery_charge. Name: Charge battery (include sensor_id). Priority: normal. Notify via: mobile push.\n        ",
        "actions": [
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_hall_motion"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_front_door"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_bed_smoke"
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_sink_leak"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "create",
                    "reminder_id": "rem_battery_charge",
                    "reminder": {
                        "name": "Charge battery (sensor_front_door)",
                        "reminder_id": "rem_battery_charge",
                        "priority": "normal",
                        "notify_via": "mobile_push"
                    }
                }
            }
        ],
        "outputs": [
                "\"battery_level\": 95",
                "\"battery_level\": 88",
                "\"battery_level\": 79",
                "\"battery_level\": 90",
                "\"battery_level\": 93"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_16",
        "instruction": "\n        You are Robert, and on Monday (2025-07-30) desire a gentle 06:25 bedroom wake-up:\n        \u2022 Include a smart coffee maker with the following specifications:\n          - ID: coffee_maker_kt\n          - Type: coffee_maker\n          - Name: Kitchen Coffee Maker\n          - Location: Kitchen\n          - Vendor: Keurig\n          - Model: K-Elite\n          - Firmware version: 1.0.0\n          - State parameters: power, brew_size, temperature_c\n          - State: power=off, brew_size=mug, temperature_c=90\n        \u2022 Position it in the kitchen and program it to brew a large\n          travel cup at 06:28, then shut off at 06:40.\n        \u2022 Partially open the master-bedroom blackout curtain immediately, then fully\n          open it at 06:30.\n        \u2022 Currently set the master-bedroom ceiling light to a very dim warm glow (brightness 10, hue 30, saturation 20),\n          increasing to 50% brightness at 06:30.\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "coffee_maker_kt",
                    "type": "coffee_maker",
                    "location": "Kitchen",
                    "vendor": "Keurig",
                    "model": "K-Elite",
                    "firmware_version": "1.0.0",
                    "state_params": [
                        "power",
                        "brew_size",
                        "temperature_c"
                    ],
                    "state": {
                        "power": "off",
                        "brew_size": "mug",
                        "temperature_c": 90
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "kitchen",
                    "device_id": "coffee_maker_kt"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "coffee_maker_kt",
                    "timestamp": "2025-07-30T06:28:00",
                    "timestamp_end": "2025-07-30T06:40:00",
                    "update": {
                        "power": "on",
                        "brew_size": "travel",
                        "temperature_c": 90
                    }
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_br",
                    "update": {
                        "position": 50
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_br",
                    "timestamp": "2025-07-30T06:30:00",
                    "update": {
                        "position": 100
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "update": {
                        "power": "on",
                        "brightness": 10,
                        "color": {
                            "hue": 30,
                            "saturation": 20
                        }
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "timestamp": "2025-07-30T06:30:00",
                    "update": {
                        "brightness": 50
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_17",
        "instruction": "\n        You have recently acquired an EV charger with the following specifications:\n        id=ev_charger_garage, type=ev_charger, name=\"Garage EV Charger\",\n        location=\"Basement\", vendor=\"ChargePoint\", model=\"Home Flex\",\n        firmware_version=\"1.0.0\",\n        state_params=[\"power\",\"mode\",\"current_a\"],\n        state={\"power\":\"off\",\"mode\":\"charge\",\"current_a\":0}\n\n        The next weekday is Monday 2025-07-30.\n        You require the system to verify and provide Jessica's (emily_johnson) shift details.\n        Subsequently, get the car ready by switching it ON at 06:00 with mode \"preheat\" and current_a:16.\n        Proceed to turn it back OFF at 06:50.\n\n        Additionally, give a report on the living room's temperature (sensor_id: sensor_lr_thermometer). If the temperature falls below 25 celsius, then\n        activate the central heater with a temperature setting of 22.\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "ev_charger_garage",
                    "type": "ev_charger",
                    "location": "Basement",
                    "vendor": "ChargePoint",
                    "model": "Home Flex",
                    "firmware_version": "1.0.0",
                    "state_params": [
                        "power",
                        "mode",
                        "current_a"
                    ],
                    "state": {
                        "power": "off",
                        "mode": "charge",
                        "current_a": 0
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "basement",
                    "device_id": "ev_charger_garage"
                },
            },
            {
                "name": "ListMembers",
                "arguments": {
                {}
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "ev_charger_garage",
                    "timestamp": "2025-07-30T06:00:00",
                    "timestamp_end": "2025-07-30T06:50:00",
                    "update": {
                        "power": "on",
                        "mode": "preheat",
                        "current_a": 16
                    }
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_lr_thermometer"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "heater"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "heater_home",
                    "update": {
                        "power": "on",
                        "setpoint_c": 22
                    }
                }
            }
        ],
        "outputs": [
                "\"shift\": \"Mon-Wed 07:00-15:00\"",
                "\"temperature_c\": 22.3"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_18",
        "instruction": "\n        On Tuesday (2025-07-01), Emma boards the bus:\n        \u2022 At 06:50, fully open the window-side curtain in her bedroom and adjust its\n          ceiling light to 60% brightness.\n        \u2022 Turn off that light at 07:40 and draw the curtain at 07:45.\n        ",
        "actions": [
            {
                "name": "ListMembers",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_bw",
                    "timestamp": "2025-07-01T06:50:00",
                    "update": {
                        "position": 100
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "timestamp": "2025-07-01T06:50:00",
                    "update": {
                        "power": "on",
                        "brightness": 60
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "timestamp": "2025-07-01T07:40:00",
                    "update": {
                        "power": "off"
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_bw",
                    "timestamp": "2025-07-01T07:45:00",
                    "update": {
                        "position": 0
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
        "instruction": "\n        A friend named Sofia is coming over for a play-date on 2025-07-02:\n        \u2022 Handle a high-priority reminder at 17:30 to drive Sofia home. (reminder_id: rem_mia_pickup, name: Sofia Pickup, priority: high, notify via mobile push)\n        \u2022 Initiate recording now on the front-door camera and set the living-room\n          ceiling light to 80% to guide her in.\n        \u2022 Switch the light off at 17:45.\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "create",
                    "reminder_id": "rem_mia_pickup",
                    "reminder": {
                        "reminder_id": "rem_mia_pickup",
                        "target": {
                            "type": "note",
                            "text": "Drive Sofia home"
                        },
                        "trigger": {
                            "datetime": "2025-07-02T17:30:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "high"
                        }
                    }
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "get",
                    "reminder_id": "rem_mia_pickup"
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "camera_front_door",
                    "update": {
                        "recording": true
                    }
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp_end": "2025-07-02T17:45:00",
                    "update": {
                        "power": "on",
                        "brightness": 80
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
        "instruction": "\n        It's trash night (2025-07-03). Kindly:\n        \u2022 Request the system to report the details of the existing trash-night reminder (reminder_id: rem_eb55e94b).\n        \u2022 Adjust the living-room floor lamp to full brightness now, and\n          turn it off at 19:30.\n        \u2022 Ask the system to check if the front door is open (sensor_id: sensor_front_door).\n        ",
        "actions": [
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "list_all_names_ids"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "get",
                    "reminder_id": "rem_eb55e94b"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "timestamp_end": "2025-07-03T19:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 100
                    }
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_front_door"
                }
            }
        ],
        "outputs": [
                "\"text\": \"Take out trash\"",
                "\"door_open\": false"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_21",
        "instruction": "\n        You purchased a motorized patio umbrella and a smart speaker for your backyard.\n        The motorized umbrella is manufactured by SunSetter and the smart speaker is created by Sonos.\n        The umbrella's model is SmartShade Pro (firmware version 1.0.0) and the speaker's model is Move 2 (firmware version 1.0.0).\n        Both devices can be either on or off.\n        The umbrella's position registers as 0 when it is closed and 100 when it's fully open.\n        The speaker's volume level stands at 0 when turned off and 100 at maximum volume.\n        The speaker also features a playlist option where you can set a playlist name.\n\n        With these newly acquired devices, you plan to organize a relaxing \"Sunday-Garden Morning\" for this weekend (2025-07-06):\n\n        \u2022 At 06 : 30, fully extend the newly-installed motorized patio umbrella in\n        the backyard and initiate an outdoor speaker to play a gentle-jazz playlist\n        at a volume of 30.\n        \u2022 Make sure the music turns off by 07 : 10.\n        \u2022 Automatically retract the umbrella at 10 : 30.\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "umbrella_by",
                    "type": "motorized_umbrella",
                    "location": "Backyard",
                    "vendor": "SunSetter",
                    "model": "SmartShade Pro",
                    "firmware_version": "1.0.0",
                    "state_params": [
                        "position",
                        "power"
                    ],
                    "state": {
                        "position": 0,
                        "power": "off"
                    }
                },
            },
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "speaker_by",
                    "type": "speaker",
                    "location": "Backyard",
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
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "umbrella_by",
                    "timestamp": "2025-07-06T06:30:00",
                    "update": {
                        "power": "on",
                        "position": 100
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "speaker_by",
                    "timestamp": "2025-07-06T06:30:00",
                    "timestamp_end": "2025-07-06T07:10:00",
                    "update": {
                        "power": "on",
                        "volume": 30,
                        "playlist": "gentle-jazz"
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "umbrella_by",
                    "timestamp": "2025-07-06T10:30:00",
                    "update": {
                        "position": 0
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_22",
        "instruction": "\n        The credit-card payment is due today (2025-08-15):\n        \u2022 Display the bill-payment reminder and CC Robert's e-mail on it.\n        \u2022 Flash the master-bedroom ceiling light at 09:55 with a brightness level of 25 and switch it off at\n          10:30.\n        ",
        "actions": [
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "list_all_names_ids"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "get",
                    "reminder_id": "rem_94f92a43"
                },
            },
            {
                "name": "ListMembers",
                "arguments": {
                {}
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "update",
                    "reminder_id": "rem_94f92a43",
                    "updates": {
                        "meta": {
                            "email_cc": "robert@example.com"
                        }
                    }
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_br_ceiling",
                    "timestamp": "2025-08-15T09:55:00",
                    "timestamp_end": "2025-08-15T10:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 25
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
        "instruction": "\n        Prepare for the annual car maintenance (scheduled for 2025-12-01):\n        \u2022 Reactivate the dormant reminder associated with it.\n        \u2022 On the due date at 07:55, activate the living-room ceiling light to a warm orange (brightness 100, hue 30, saturation 90), and switch it off at\n          17:00.\n        ",
        "actions": [
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "list_all_names_ids"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "get",
                    "reminder_id": "rem_8f9fd8ae"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "update",
                    "reminder_id": "rem_8f9fd8ae",
                    "updates": {
                        "status": "active"
                    }
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-12-01T07:55:00",
                    "timestamp_end": "2025-12-01T17:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 100,
                        "color": {
                            "hue": 30,
                            "saturation": 90
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
        "user_id": "res_24",
        "instruction": "\n        Anticipate Grandma and Grandpa's visit on 2025-07-25:\n        \u2022 Schedule a reminder for 2025-07-28 10am to handle the guest linens (reminder id: rem_laundry_guest, name: Wash guest linens,priority: normal, notify via mobile push).\n        \u2022 On 2025-07-25 22:00, ensure the east-bedroom curtain is closed and the ceiling light is set to a cosy\n          dim blue-white (brightness 40, hue 210, saturation 40), then ensure this light is turned off at 23:00.\n        \u2022 Automatically open the curtain again the following day at 10am.\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "create",
                    "reminder_id": "rem_laundry_guest",
                    "reminder": {
                        "reminder_id": "rem_laundry_guest",
                        "target": {
                            "type": "note",
                            "text": "Wash guest linens"
                        },
                        "trigger": {
                            "datetime": "2025-07-28T10:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_be",
                    "timestamp": "2025-07-25T22:00:00",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_be_ceiling",
                    "timestamp": "2025-07-25T22:00:00",
                    "timestamp_end": "2025-07-25T23:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 40,
                        "color": {
                            "hue": 210,
                            "saturation": 40
                        }
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_be",
                    "timestamp": "2025-07-26T10:00:00",
                    "update": {
                        "position": 100
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
        "instruction": "\n        On 2025-07-06, host a dinner for Michael and Jennifer:\n        \u2022 At 18:20, adjust the living-room ceiling light to a warm glow with 70% brightness (hue 50, saturation 70).\n        \u2022 Turn the light off at 21:30.\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-07-06T18:20:00",
                    "timestamp_end": "2025-07-06T21:30:00",
                    "update": {
                        "power": "on",
                        "brightness": 70,
                        "color": {
                            "hue": 50,
                            "saturation": 70
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
        "user_id": "res_26",
        "instruction": "\n        Ensure the system provides the trigger time for your shopping-list reminder (reminder_id: rem_4fb3637f).\n        Five minutes prior, flash the living-room ceiling light bright yellow (brightness 100, hue 50, saturation 100) and turn it off five minutes afterward.\n        ",
        "actions": [
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "list_all_names_ids"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "get",
                    "reminder_id": "rem_4fb3637f"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-06-29T08:55:00",
                    "timestamp_end": "2025-06-29T09:05:00",
                    "update": {
                        "power": "on",
                        "brightness": 100,
                        "color": {
                            "hue": 50,
                            "saturation": 100
                        }
                    }
                }
            }
        ],
        "outputs": [
                "2025-06-29T09:00:00-07:00"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_27",
        "instruction": "\n        Initiating tonight (2025-07-28) and at the same time every night at 20:55:\n        \u2022 Flash the master bedroom's bedside lamp (lamp_br_night) in bright red (brightness 100, hue 0, saturation 100) as a reminder to take medication,\n          then reduce it after 10 minutes to 30% brightness, turning it off at 21:10.\n        \u2022 Adjust the default snooze for the medication reminder to 10 minutes.\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "timestamp": "2025-07-28T20:55:00",
                    "timestamp_end": "2025-07-28T21:10:00",
                    "update": {
                        "power": "on",
                        "brightness": 100,
                        "color": {
                            "hue": 0,
                            "saturation": 100
                        }
                    },
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "timestamp": "2025-07-28T21:05:00",
                    "update": {
                        "brightness": 30
                    },
                    "rrule": "FREQ=DAILY"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "list_all_names_ids"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "get",
                    "reminder_id": "rem_254afa34"
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "update",
                    "reminder_id": "rem_254afa34",
                    "updates": {
                        "meta": {
                            "snooze_default_min": 10
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
        "user_id": "res_28",
        "instruction": "\n        For Dad's birthday celebration (2025-09-12):\n        \u2022 At 17:45 illuminate the living-room ceiling light with a warm festive glow (brightness 60, hue 30, saturation 70).\n        \u2022 Ensure it is turned off at 19:00.\n        \u2022 Schedule a reminder two days prior (2025-09-10) at 9 AM to purchase him a gift, pushing it to mobile.\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-09-12T17:45:00",
                    "timestamp_end": "2025-09-12T19:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 60,
                        "color": {
                            "hue": 30,
                            "saturation": 70
                        }
                    }
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "create",
                    "reminder_id": "rem_dads_gift",
                    "reminder": {
                        "reminder_id": "rem_dads_gift",
                        "trigger": {
                            "datetime": "2025-09-10T09:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
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
        "user_id": "res_29",
        "instruction": "\n        Initiate HVAC-filter maintenance on 2025-07-30:\n        \u2022 Create a list titled \"HVAC Filter Replacements\" (list id: list_hvac_filter, name: HVAC Filter Replacements, tags: maintenance, hvac).\n        \u2022 Schedule a reminder for 2025-09-01 09:00 utilizing that list (reminder id: rem_hvac_filter, name: Replace HVAC filter, priority: normal, notify via mobile push).\n        \u2022 At 09:05 on the same day, ensure the main heater is turned off for safety.\n        ",
        "actions": [
            {
                "name": "ManageCustomList",
                "arguments": {
                    "action": "create",
                    "list_id": "list_hvac_filter",
                    "name": "HVAC Filter Replacements",
                    "tags": [
                        "maintenance",
                        "hvac"
                    ]
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "create",
                    "reminder_id": "rem_hvac_filter",
                    "reminder": {
                        "reminder_id": "rem_hvac_filter",
                        "target": {
                            "type": "entity",
                            "entity_type": "list",
                            "entity_id": "list_hvac_filter"
                        },
                        "trigger": {
                            "datetime": "2025-09-01T09:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
                        "meta": {
                            "priority": "normal"
                        }
                    }
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "heater"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "heater_home",
                    "timestamp": "2025-09-01T09:05:00",
                    "update": {
                        "power": "off"
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
        "instruction": "\n        Arrange the west-bedroom for Chris's weekend stay (visit spans 07-12 \u2192\n        07-14):\n        \u2022 Update Chris's guest profile to include his visit dates.\n        \u2022 Draw the west-bedroom blackout curtain shut and adjust its ceiling light to 30 %.\n        \u2022 Set a reminder for 07-15 09:00 to launder Chris's guest linens (reminder id: rem_linen_wash_mb, name: Wash Chris guest linens, priority: normal, notify via mobile push).\n        \u2022 Deactivate that ceiling light at 23:00 this evening (2025-07-10).\n        ",
        "actions": [
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "UpsertMember",
                "arguments": {
                    "id": "michael_wilson",
                    "profile": {
                        "visit_next_start": "2025-07-12",
                        "visit_next_end": "2025-07-14"
                    }
                },
            },
            {
                "name": "UpdateDeviceState",
                "arguments": {
                    "device_id": "curtain_bw",
                    "update": {
                        "position": 0
                    }
                },
            },
            {
                "name": "UpdateDeviceStateTimer",
                "arguments": {
                    "device_id": "light_bw_ceiling",
                    "timestamp_end": "2025-07-10T23:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 30
                    }
                },
            },
            {
                "name": "ManageReminders",
                "arguments": {
                    "action": "create",
                    "reminder_id": "rem_linen_wash_mb",
                    "reminder": {
                        "reminder_id": "rem_linen_wash_mb",
                        "target": {
                            "type": "note",
                            "text": "Wash Chris guest linens"
                        },
                        "trigger": {
                            "datetime": "2025-07-15T09:00:00"
                        },
                        "actions": [
                            {
                                "type": "notify",
                                "channel": "mobile_push"
                            }
                        ],
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
        "user_id": "res_31",
        "instruction": "\n        On 2025-07-30, initiate the existing \"Good Morning\" scene at 06:30.\n        After five minutes, increase the\n        living-room ceiling light to 80% brightness and completely open Emma's west-bedroom curtain.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_good_morning",
                    "timestamp": "2025-07-30T06:30:00"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-07-30T06:35:00",
                    "update": {
                        "power": "on",
                        "brightness": 80
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_bw",
                    "timestamp": "2025-07-30T06:35:00",
                    "update": {
                        "position": 100
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_32",
        "instruction": "\n        On the night of 2025-07-28, activate the \"Good Night\" scene at 22:00; at 22:30, reduce the night-stand\n        lamp brightness to 5% and adjust the central-heater set-point to 19 \u00b0C.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "heater"
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_good_night",
                    "timestamp": "2025-07-28T22:00:00"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "timestamp": "2025-07-28T22:30:00",
                    "update": {
                        "brightness": 5
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "heater_home",
                    "timestamp": "2025-07-28T22:30:00",
                    "update": {
                        "setpoint_c": 19
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_33",
        "instruction": "\n        Set up a new scene named \"Homework Time\":\n        \u2022 Adjust the East-bedroom ceiling light to cool-white at 90 %.\n        \u2022 Change the East-bedroom ceiling light color to kelvin 5000.\n        \u2022 Set the East-bedroom bedside lamp to bright white at 100 %.\n        \u2022 Adjust the East-bedroom bedside light color to kelvin 5000.\n        \u2022 Close the East-bedroom curtain.\n        Plan for this scene to activate at 4pm on 2025-07-01.\n        Define it as Bright focus lighting after school.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "id": "scene_homework_time",
                    "name": "Homework Time",
                    "description": "Bright focus lighting after school.",
                    "actions": [
                        {
                            "device_id": "light_be_ceiling",
                            "update": {
                                "power": "on",
                                "brightness": 90,
                                "color": {
                                    "kelvin": 5000
                                }
                            }
                        },
                        {
                            "device_id": "lamp_be_bedside",
                            "update": {
                                "power": "on",
                                "brightness": 100,
                                "color": {
                                    "kelvin": 5000
                                }
                            }
                        },
                        {
                            "device_id": "curtain_be",
                            "update": {
                                "position": 0
                            }
                        }
                    ]
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_homework_time",
                    "timestamp": "2025-07-01T16:00:00"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_34",
        "instruction": "\n        On Saturday (2025-07-05) at 19:00, initiate \"Movie Time\".\n        Two hours afterward, adjust the living-room ceiling light back to 60 % brightness (kelvin 3000),\n        partially open the curtain, and switch the AC to auto fan.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "ac"
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_movie_time",
                    "timestamp": "2025-07-05T19:00:00"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_ceiling",
                    "timestamp": "2025-07-05T21:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 60,
                        "color": {
                            "kelvin": 3000
                        }
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_lr",
                    "timestamp": "2025-07-05T21:00:00",
                    "update": {
                        "position": 50
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "ac_home",
                    "timestamp": "2025-07-05T21:00:00",
                    "update": {
                        "fan_speed": "auto"
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
        "instruction": "\n        Arrange the installation of a smart humidifier in the master bedroom\n        - ID: humidifier_br\n        - Type: humidifier\n        - Name: Master-Bedroom Humidifier\n        - Location: Master Bedroom\n        - Vendor: Levoit\n        - Model: Vital 200S\n        - Firmware version: 1.0.0\n        - State parameters: power, mode, humidity_setpoint_pct\n        - State: power=off, mode=auto, humidity_setpoint_pct=45\n        At 22:00 on 2025-07-28, enable it in sleep-mode and deactivate it at 03:00 the following morning.\n        ",
        "actions": [
            {
                "name": "CreateDevice",
                "arguments": {
                    "id": "humidifier_br",
                    "type": "humidifier",
                    "location": "Master Bedroom",
                    "vendor": "Levoit",
                    "model": "Vital 200S",
                    "firmware_version": "1.0.0",
                    "state_params": [
                        "power",
                        "mode",
                        "humidity_setpoint_pct"
                    ],
                    "state": {
                        "power": "off",
                        "mode": "auto",
                        "humidity_setpoint_pct": 45
                    }
                },
            },
            {
                "name": "AddDeviceToRoom",
                "arguments": {
                    "room_id": "bedroom_master",
                    "device_id": "humidifier_br"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "humidifier_br",
                    "timestamp": "2025-07-28T22:00:00",
                    "timestamp_end": "2025-07-29T03:00:00",
                    "update": {
                        "power": "on",
                        "mode": "sleep"
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
        "instruction": "\n        Develop an \"Away Mode\" scene that turns off every light (all ceiling lights, floor lamp, night lamps, and desk lamps) along with the HVAC.\n        Activate it immediately (2025-07-29 11:00).\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "id": "scene_away_mode",
                    "name": "Away Mode",
                    "description": "Shuts off all lights and HVAC.",
                    "actions": [
                        {
                            "device_id": "light_lr_ceiling",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "light_lr_floor",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "light_br_ceiling",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "lamp_br_night",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "light_bw_ceiling",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "lamp_bw_desk",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "light_be_ceiling",
                            "update": {
                                "power": "off"
                            }
                        },
                        {
                            "device_id": "lamp_be_bedside",
                            "update": {
                                "power": "off"
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
                                "power": "off"
                            }
                        }
                    ]
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_away_mode",
                    "timestamp": "2025-07-29T11:00:00"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_37",
        "instruction": "\n        On 2025-07-28 at 21:00, automatically initiate the scene \"Good Night\".\n        Switch on the night-stand lamp to 100 % brightness, and switch it off 15 minutes later.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_good_night",
                    "timestamp": "2025-07-28T21:00:00"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "lamp_br_night",
                    "timestamp": "2025-07-28T21:00:00",
                    "timestamp_end": "2025-07-28T21:15:00",
                    "update": {
                        "brightness": 100
                    }
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_38",
        "instruction": "\n        Arrange a \"Family Movie Marathon\" for Friday, 2025-08-18:\n        \u2022 At 16:00, activate the existing \"Movie Time\" scene.\n        \u2022 Concurrently, dim the living-room floor lamp to 10 %\n        \u2022 At 18:30, return the floor lamp to 60 %, and fully open the living-room\n        curtain.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "light"
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "curtain"
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_movie_time",
                    "timestamp": "2025-08-18T16:00:00"
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "timestamp": "2025-08-18T16:00:00",
                    "update": {
                        "power": "on",
                        "brightness": 10
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "light_lr_floor",
                    "timestamp": "2025-08-18T18:30:00",
                    "update": {
                        "brightness": 60
                    }
                },
            },
            {
                "name": "ScheduleDeviceUpdate",
                "arguments": {
                    "device_id": "curtain_lr",
                    "timestamp": "2025-08-18T18:30:00",
                    "update": {
                        "position": 100
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
        "instruction": "\n        Handle the creation of an \"Evacuate\" scene: all lights full-bright, curtains open,\n        HVAC off. The system should notify you if the bedroom smoke detector reports CO.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpsertScene",
                "arguments": {
                    "id": "scene_evacuate",
                    "actions": [
                        {
                            "device_id": "light_lr_ceiling",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_lr_floor",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_br_ceiling",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_br_night",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_bw_ceiling",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_bw_desk",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_be_ceiling",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "light_be_bedside",
                            "update": {
                                "power": "on",
                                "brightness": 100
                            }
                        },
                        {
                            "device_id": "curtain_lr",
                            "update": {
                                "position": 100
                            }
                        },
                        {
                            "device_id": "curtain_br",
                            "update": {
                                "position": 100
                            }
                        },
                        {
                            "device_id": "curtain_bw",
                            "update": {
                                "position": 100
                            }
                        },
                        {
                            "device_id": "curtain_be",
                            "update": {
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
                                "power": "off"
                            }
                        }
                    ]
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSensorState",
                "arguments": {
                    "sensor_id": "sensor_bed_smoke"
                }
            }
        ],
        "outputs": [
                "\"co_detected\": false"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "res_40",
        "instruction": "\n        On August 1 2025 at 08:00, initiate \"Good Morning\" and subsequently run the dishwasher for 2 hours.\n        ",
        "actions": [
            {
                "name": "ListScenes",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListSensorNamesIds",
                "arguments": {
                {}
                },
            },
            {
                "name": "ListDevices",
                "arguments": {
                    "type": "dishwasher"
                },
            },
            {
                "name": "ScheduleSceneRun",
                "arguments": {
                    "scene_id": "scene_good_morning",
                    "timestamp": "2025-08-01T08:00:00"
                },
            },
            {
                "name": "ScheduleDeviceUpdateTimer",
                "arguments": {
                    "device_id": "dishwasher_kt",
                    "timestamp": "2025-08-01T08:00:00",
                    "timestamp_end": "2025-08-01T10:00:00",
                    "update": {
                        "power": "on"
                    }
                }
            }
        ],
        "outputs": []
    }
]
