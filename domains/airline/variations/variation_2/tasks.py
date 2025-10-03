# Copyright Sierra

tasks = [
    {
        "annotator": 0,
        "user_id": "task_1",
        "instruction": "Execute operations management at LAX and the time is 2024-05-22T03:10Z.A SIGMET is impacting inbound flights HAT170 and HAT124 with 120-minutes delay to the flights.You need to initiate the related protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Weather",
                    "details": "SIGMET impacts LAX operations; apply 120-minutes delay to affected flights.",
                    "event_timestamp_utc": "2024-05-22T03:10Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT170"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-22",
                    "delay_minutes": 120
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT170-2024-05-22",
                    "message": "Delay by 120 minutes for HAT170 (2024-05-22) at LAX."
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT124"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT124",
                    "date": "2024-05-22",
                    "delay_minutes": 120
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT124-2024-05-22",
                    "message": "Delay by 120 minutes for HAT124 (2024-05-22) at LAX."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_2",
        "instruction": "Handle crew scheduling at ATL. On 2024-05-01T06:50:00Z, flight HAT004 requires a last-minute crew change: employee EMP001 is unavailable and EMP004 is qualified substitute to HAT004 for employee EMP001 on that date.You need to initiate the related protocol for this case",
        "actions": [
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP001"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM001",
                    "new_status": "On Leave"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT004",
                    "crew_member_id": "CM004",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Crew Replacement",
                    "details": "Last-minute crew replacement required for HAT004 on 2024-05-01.",
                    "event_timestamp_utc": "2024-05-01T06:50:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_3",
        "instruction": "Handle maintenance control duties at DFW. On 2024-05-22T08:40:00Z, aircraft AC001 with tail number PR-GOL grounded for maintenance and assigned to HAT170 was declared AOG at DFW after engine vibration limits were exceeded on taxi.You need to set the flight status to canceled and then initiate the needed protocol for this case.",
        "actions": [
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT170"
                    ],
                    "date": "2024-05-22",
                    "new_status": "canceled"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-GOL grounded for maintenance, HAT170 on 2024-05-22.",
                    "technician_id": "TECH-DFW-01",
                    "event_timestamp_utc": "2024-05-22T08:40:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "flight_id": "HAT170",
                    "aircraft_id": "AC001",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-GOL grounded for maintenance, HAT170 on 2024-05-22.",
                    "event_timestamp_utc": "2024-05-22T08:40:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_4",
        "instruction": "Execute logistics management at DEN and the time is 2024-05-03T08:40:00ZHAT003 by aircraft AC001 with tail number PR-GOL is diverted to Boulder due to weather.You need to start the related diversion protocols and ensure records have been reflected in the logs and events.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DEN"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT003",
                    "date": "2024-05-03"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "Unscheduled maintenance for PR-GOL after diversion to DEN.",
                    "technician_id": "TECH-DEN-01",
                    "event_timestamp_utc": "2024-05-03T08:40:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DEN",
                    "event_type": "Diversion",
                    "details": "Diversion for HAT003 on 2024-05-03 - landed at DEN.",
                    "event_timestamp_utc": "2024-05-03T08:40:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT003"
                    ],
                    "date": "2024-05-03",
                    "new_status": "diverted"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "MaintenanceLogsForAircraft",
                "arguments": {
                    "aircraft_id": "AC001"
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_DEN",
                    "date": "2024-05-03"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_5",
        "instruction": "Coordinate crew training activities at ATL and the time is 2024-05-10T08:40:00Z. Captain EMP004 requires recurrent E195-E2 certificate on 2024-05-10.You need to initiate the needed protocol for this case.",
        "actions": [
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM004",
                    "certification_code": "E195-E2"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "crew_member_id": "CM004"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "date": "2024-05-10",
                    "flight_numbers": [
                        "HAT002",
                        "HAT011",
                        "HAT004",
                        "HAT003",
                        "HAT010"
                    ]
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM004",
                    "new_status": "Training"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Crew Training",
                    "details": "Training scheduled for CM004 on 2024-05-10 : E195-E2.",
                    "event_timestamp_utc": "2024-05-10T08:40:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "CM004",
                    "message": "Training scheduled for CM004 on 2024-05-10 : E195-E2."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_6",
        "instruction": "Execute operations management at DFW and the time is 2024-05-13T08:40:00ZMultiple passengers from flight HAT004 by AC002 aircraft (ATL -> DFW) have reported missing checked baggage and equipment faults are foundYou need to check the events at ATL and initiate the related protocol for this flight ensure records have been reflected in the events at DFW.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT004",
                    "date": "2024-05-13"
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "date": "2024-05-13"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "Baggage Irregularity: HAT004 from airport ARP_ATL to airport ARP_DFW on 2024-05-13.",
                    "event_timestamp_utc": "2024-05-13T08:40:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT004"
                    ],
                    "date": "2024-05-13",
                    "new_status": "baggage delay"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC002",
                    "maintenance_type": "Unscheduled",
                    "description": "Cargo door and forward hold equipment inspection for AC002 due to reported baggage delay case.",
                    "technician_id": "TECH-DFW-01",
                    "event_timestamp_utc": "2024-05-13T08:40:00Z"
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "date": "2024-05-13"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_7",
        "instruction": "Execute operations management at MCO. On 2024-05-16T08:40:00Z, a sudden fuel supply disruption is impacting outbound operations. HAT214 and HAT217 are high-priority flights and are doing to be delayed.You need to Initiate the needed protocol for MCO ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "origin": "MCO",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Fuel Disruption",
                    "details": "Fuel supply disruption at MCO on 2024-05-16; priorities: HAT214 and HAT217",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT214",
                        "HAT217"
                    ],
                    "date": "2024-05-16",
                    "new_status": "delayed"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT101",
                        "HAT299",
                        "HAT298",
                        "HAT028",
                        "HAT017",
                        "HAT075",
                        "HAT161",
                        "HAT153",
                        "HAT048"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Fuel program MCO: HAT214, HAT217 delayed, HAT101, HAT299, HAT298, HAT028, HAT017, HAT075, HAT161, HAT153, HAT048 canceled."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_8",
        "instruction": "Execute operations management at LAX and the time is 2024-05-16T08:40:00Z.Crew member with employee code EMP004 on HAT249 (LAX->SFO) is at risk of crew duty-limit exceedance due to inbound ATC congestion and EMP007 is standby crew member.You need to initiate the Crew Duty-Limit Mitigation protocol for HAT249 and set the flight status to delayed",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT249",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "flight_number": "HAT249"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM004",
                    "new_status": "Inactive"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP007"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT249",
                    "crew_member_id": "CM007",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT249"
                    ],
                    "date": "2024-05-16",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Crew Replacement",
                    "details": "Crew delay on HAT249; standby crew assigned: CM007.",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_9",
        "instruction": "Execute operations management at LAX and the time is 2024-05-16T08:40:00Z .An unattended piece of baggage has been discovered near Gate C12 at the main hub (LAX) and departure HAT155 is potentially impacted.You need to Initiate the needed protocol for this incident and ensure records have been reflected in the events.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "date": "2024-05-16"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT155",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT155",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "UNATTENDED_BAGGAGE",
                    "details": "Unattended baggage near Gate C12; boarding paused for HAT155.",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT155"
                    ],
                    "date": "2024-05-16",
                    "new_status": "security-hold"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lax",
                    "message": "Security advisory: temporary boarding pause for HAT155 at LAX."
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "date": "2024-05-16"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_10",
        "instruction": "Execute operations management at ATL and the time is 2024-05-16T08:40:00Z .flight HAT164 (ATL->LGA) is canceled due to a mechanical fault on grounded aircraft PR-GOL.You have to initiate the needed protocol and refund all reservations for this flight.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT164",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-GOL"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT164"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "RefundReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT164",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-GOL grounded for maintenance, HAT164 on 2024-05-16.",
                    "technician_id": "TECH-ATL-01",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-GOL grounded for maintenance, HAT164 on 2024-05-16.",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-atl",
                    "message": "Flight HAT164 on 2024-05-16 at ATL canceled."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_11",
        "instruction": "Coordinate connection protection at DFW and the time is 2024-05-22T05:45:00ZYou need to support connection protection for HAT170,HAT124 at DFW on 2024-05-22.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT170",
                    "event_timestamp_utc": "2024-05-22T05:45:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT170-2024-05-22",
                    "message": "Connection protection advisory for HAT170 on 2024-05-22: monitoring tight connections; alternatives under review."
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT124",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT124",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT124",
                    "event_timestamp_utc": "2024-05-22T05:45:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT124-2024-05-22",
                    "message": "Connection protection advisory for HAT124 on 2024-05-22: monitoring tight connections; alternatives under review."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_12",
        "instruction": "Coordinate group seating arrangements at ATL and the time is 2024-05-22T09:00:00ZA large family group on HAT299 (MCO->ATL) 2024-05-22 needs seat block changes.You need to initiate the needed protocol for parties harper_gonzalez_3796 and james_lee_6136.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT299",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT299",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "harper_gonzalez_3796"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "james_lee_6136"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Group seating assistance initiated for HAT299 (2024-05-22) for parties [harper_gonzalez_3796, james_lee_6136].",
                    "event_timestamp_utc": "2024-05-22T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-atl",
                    "message": "ATL res: HAT299 family group [harper_gonzalez_3796,james_lee_6136] requires coordinated seat adjustments; support engaged."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_13",
        "instruction": "Conduct reservations analysis at BOS and the time is 2024-05-16T09:00:00ZThere is possible duplicate bookings for customer raj_sanchez_7079 on same travel date.You need to initiate the needed protocol and refund latest duplicates.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "raj_sanchez_7079"
                },
            },
            {
                "name": "RefundReservation",
                "arguments": {
                    "reservation_id": "CPQKE9"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Duplicate booking scan executed for raj_sanchez_7079; potential overlaps flagged for review.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Duplicate booking advisory for customer raj_sanchez_7079-review and consolidate if needed."
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "REFUND",
                    "details": "Reservation CPQKE9 refunded.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "raj_sanchez_7079",
                    "message": "Reservation CPQKE9 refunded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_14",
        "instruction": "Supervise customer service operations at LAS and the time is 2024-05-20T09:00:00ZAircraft change reduces business capacity for HAT115 on 2024-05-20; involuntary downgrades required.You need to downgrade two business reservations to economy.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT115",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT115",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "WUBAI5",
                    "cabin": "economy"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "YMMK5P",
                    "cabin": "economy"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Involuntary downgrade process started for HAT115 (2024-05-20)",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT115"
                    ],
                    "date": "2024-05-20",
                    "new_status": "delayed"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-las",
                    "message": "HAT115 2024-05-20: reduced cabin capacity."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_15",
        "instruction": "Coordinate connection protection at LAS and the time is 2024-05-20T09:00:00ZConnection buffers for HAT115 (LAS) on 2024-05-20 are tighter than usual.You need to initiate the related protocols and since there are passengers with connecting flights, set 30 minutes delay to all connecting legs.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT115",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT115",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "date": "2024-05-20",
                    "origin": "LAS",
                    "status": [
                        "on time",
                        "available"
                    ]
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT200",
                    "date": "2024-05-20",
                    "delay_minutes": 30
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT148",
                    "date": "2024-05-20",
                    "delay_minutes": 30
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT115",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT115-2024-05-20",
                    "message": "Connection protection advisory for HAT115 on 2024-05-20: monitoring tight connections; alternatives under review."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_16",
        "instruction": "Execute manifest control duties at MCO and the time is 2024-05-23T09:00:00ZDuplicate passenger names detected on the HAT214 manifest at MCO for 2024-05-23.You need to initiate the manifest audit protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-23"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-23"
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "date": "2024-05-23"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Manifest audit",
                    "details": "Duplicate-name audit executed for HAT214 (2024-05-23) at MCO; identity checks initiated.",
                    "event_timestamp_utc": "2024-05-23T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Manifest audit: duplicate names on HAT214 (2024-05-23); ID verification in progress."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "lucas_kovacs_4017",
                    "message": "Manifest audit: Flight HAT214; Bring IDs to check-in."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "liam_garcia_8705",
                    "message": "Manifest audit: Flight HAT214; Bring IDs to check-in."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_17",
        "instruction": "Handle reservations duties at SEA and the time is 2024-05-12T09:00:00Z.Your goal is to book a basic_economy one-way trip for customer Isabella Brown (email: emma.smith8074@example.com) from SEA to ATLon 2024-05-16, selecting the lowest available fare.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "SEA",
                    "destination": "ATL",
                    "start_date": "2024-05-16",
                    "end_date": "2024-05-16",
                    "status": [
                        "available"
                    ]
                },
            },
            {
                "name": "FindUserByEmail",
                "arguments": {
                    "user_email": "emma.smith8074@example.com"
                },
            },
            {
                "name": "CreateReservation",
                "arguments": {
                    "user_email": "emma.smith8074@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT220",
                            "date": "2024-05-16",
                            "origin": "SEA",
                            "destination": "ATL"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Mia",
                            "last_name": "Li",
                            "dob": "1990-04-05"
                        }
                    ],
                    "cabin": "basic_economy"
                }
            }
        ],
        "outputs": [
                "reservation_id = RES9816",
                "flight number = HAT220",
                "date = 2024-05-16"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_18",
        "instruction": "Handle reservations duties at SEA and the time is 2024-05-12T09:00:00Z.Customer Isabella Brown (email: emma.smith8074@example.com) wants a one-way trip from SEA to ATLtraveling between 2024-05-13 and 2024-05-30, selecting the lowest available fare.You need to handle her request.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "SEA",
                    "destination": "ATL",
                    "start_date": "2024-05-13",
                    "end_date": "2024-05-30",
                    "status": [
                        "available"
                    ]
                },
            },
            {
                "name": "FindUserByEmail",
                "arguments": {
                    "user_email": "emma.smith8074@example.com"
                },
            },
            {
                "name": "CreateReservation",
                "arguments": {
                    "user_email": "emma.smith8074@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT220",
                            "date": "2024-05-16",
                            "origin": "SEA",
                            "destination": "ATL"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Mia",
                            "last_name": "Li",
                            "dob": "1990-04-05"
                        }
                    ],
                    "cabin": "basic_economy"
                }
            }
        ],
        "outputs": [
                "reservation_id = RES9816",
                "flight number = HAT220",
                "date = 2024-05-16"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_19",
        "instruction": "Handle reservations duties at PHX and the time is 2024-05-25T09:00:00Z.Ivan Anderson ( email: liam.taylor8460@example.com and user_id: sofia_rossi_7655 ) is here and wants to refund here flight from PHX to DTW on 2024-05-25.and book another flight the same flight number if available but on 2024-05-26.You need to handle her request.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "sofia_rossi_7655"
                },
            },
            {
                "name": "RefundReservation",
                "arguments": {
                    "reservation_id": "L6C0W3"
                },
            },
            {
                "name": "CreateReservation",
                "arguments": {
                    "user_email": "liam.taylor8460@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT106",
                            "date": "2024-05-26",
                            "origin": "PHX",
                            "destination": "DTW"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Sofia",
                            "last_name": "Rossi",
                            "dob": "1996-04-06"
                        }
                    ],
                    "cabin": "business"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "REFUND",
                    "details": "Reservation L6C0W3 refunded.",
                    "event_timestamp_utc": "2024-05-25T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "sofia_rossi_7655",
                    "message": "Reservation L6C0W3 refunded."
                }
            }
        ],
        "outputs": [
                "reservation_id = RES9816",
                "flight number = HAT106",
                "date = 2024-05-26"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_20",
        "instruction": "Handle reservations duties at LAS and the time is 2024-05-17T09:00:00Z.Flight number HAT137 from LAS to MCO is overbooked on 2024-05-17 and Isabella Lopez (user_id: olivia_gonzalez_2305 , email: harper.lopez8439@example.com ) is the last booker.The management decided to cancel her entire reservation and dind the the same flight (HAT137) for the same route on 2024-05-18 and upgrade her reservation to business for free.Handle the order.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "olivia_gonzalez_2305"
                },
            },
            {
                "name": "CancelReservation",
                "arguments": {
                    "reservation_id": "K67C4W"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "LAS",
                    "destination": "MCO",
                    "start_date": "2024-05-18",
                    "end_date": "2024-05-18",
                    "status": [
                        "available"
                    ]
                },
            },
            {
                "name": "CreateReservation",
                "arguments": {
                    "user_email": "harper.lopez8439@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT137",
                            "date": "2024-05-18",
                            "origin": "LAS",
                            "destination": "MCO"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Olivia",
                            "last_name": "Gonzalez",
                            "dob": "1988-06-13"
                        },
                        {
                            "first_name": "Mei",
                            "last_name": "Johansson",
                            "dob": "1981-09-25"
                        },
                        {
                            "first_name": "Yara",
                            "last_name": "Lopez",
                            "dob": "1975-09-15"
                        }
                    ],
                    "cabin": "business"
                }
            }
        ],
        "outputs": [
                "reservation_id = RES9816",
                "flight number = HAT137",
                "date = 2024-05-18"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_21",
        "instruction": "Supervise flight operations at ORD and the time is 2024-05-15T09:00:00Z.Crew on HAT139 (tail_number PT-MUI) detect an unusual odor in the cabin after pushback.You need to update flight as returned for inspection and then initiate the AOG protocol",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ORD"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PT-MUI"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT139"
                    ],
                    "date": "2024-05-15",
                    "new_status": "returned"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC006",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ORD",
                    "flight_id": "HAT139",
                    "aircraft_id": "AC006",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PT-MUI grounded for maintenance, HAT139 on 2024-05-15.",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC006",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PT-MUI grounded for maintenance, HAT139 on 2024-05-15.",
                    "technician_id": "TECH-ORD-01",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_22",
        "instruction": "Manage airport operations at EWR and the time is 2024-05-16T09:00:00Z.Flight HAT031 ( aircraft tail_number PT-MUI ) hits a flock of birds during landing at EWR.Follow the needed protocol to inspect the aircraft.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "EWR"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PT-MUI"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC006",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_EWR",
                    "flight_id": "HAT031",
                    "aircraft_id": "AC006",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "Due to Wildlife Strike, aircraft PT-MUI grounded for maintenance, HAT031 on 2024-05-16.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC006",
                    "maintenance_type": "Unscheduled",
                    "description": "Due to Wildlife Strike, aircraft PT-MUI grounded for maintenance, HAT031 on 2024-05-16.",
                    "technician_id": "TECH-EWR-01",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_23",
        "instruction": "Execute maintenance planning at ATL the time is 2024-05-16T09:00:00Z.You need to schedule A-Check maintenance for aircrafts that dont have A-Check log or the last A-check done more than 30 days ago.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "MaintenanceLogs",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetAircraftByAirport",
                "arguments": {
                    "airport_id": "ARP_ATL"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "A-Check",
                    "technician_id": "TECH-ATL-01",
                    "description": "Routine A-Check inspection.",
                    "corrective_action": "Scheduled inspection of systems and components.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC025",
                    "maintenance_type": "A-Check",
                    "technician_id": "TECH-ATL-01",
                    "description": "Routine A-Check inspection.",
                    "corrective_action": "Scheduled inspection of systems and components.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC025",
                    "new_status": "In Maintenance"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_24",
        "instruction": "Execute maintenance planning at LAX the time is 2024-05-16T09:00:00Z.You need to Schedule B-Check maintenance for aircrafts that dont have B-Check log or the last B-check done more than 180 days ago.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "MaintenanceLogs",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetAircraftByAirport",
                "arguments": {
                    "airport_id": "ARP_LAX"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC003",
                    "maintenance_type": "B-Check",
                    "technician_id": "TECH-LAX-01",
                    "description": "Routine B-Check inspection.",
                    "corrective_action": "Detailed inspection of systems and structure.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC003",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC018",
                    "maintenance_type": "B-Check",
                    "technician_id": "TECH-LAX-01",
                    "description": "Routine B-Check inspection.",
                    "corrective_action": "Detailed inspection of systems and structure.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC018",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC022",
                    "maintenance_type": "B-Check",
                    "technician_id": "TECH-LAX-01",
                    "description": "Routine B-Check inspection.",
                    "corrective_action": "Detailed inspection of systems and structure.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC022",
                    "new_status": "In Maintenance"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_25",
        "instruction": "Execute maintenance planning at MCO the time is 2024-05-16T09:00:00Z.You need to schedule C-Check maintenance for aircrafts that dont have C-Check log or the last C-check done more than 600 days ago.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "MaintenanceLogs",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetAircraftByAirport",
                "arguments": {
                    "airport_id": "ARP_MCO"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC004",
                    "maintenance_type": "C-Check",
                    "technician_id": "TECH-MCO-01",
                    "description": "Routine C-Check inspection.",
                    "corrective_action": "Scheduled heavy maintenance C-Check.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC004",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC012",
                    "maintenance_type": "C-Check",
                    "technician_id": "TECH-MCO-01",
                    "description": "Routine C-Check inspection.",
                    "corrective_action": "Scheduled heavy maintenance C-Check.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC012",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC015",
                    "maintenance_type": "C-Check",
                    "technician_id": "TECH-MCO-01",
                    "description": "Routine C-Check inspection.",
                    "corrective_action": "Scheduled heavy maintenance C-Check.",
                    "event_timestamp_utc": "2024-05-16T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC015",
                    "new_status": "In Maintenance"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_26",
        "instruction": "Manage network operations at DFW and the time is 2024-05-16T09:00:00Z.Route between BOS to SEA until 2024-05-18 need to be canceled.you need to cancel affected flights",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "BOS",
                    "destination": "SEA",
                    "status": [
                        "available"
                    ],
                    "start_date": "2024-05-16",
                    "end_date": "2024-05-18"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT006"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT006"
                    ],
                    "date": "2024-05-17",
                    "new_status": "canceled"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT006"
                    ],
                    "date": "2024-05-18",
                    "new_status": "canceled"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Flight HAT006 on 2024-05-16 at BOS canceled."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Flight HAT006 on 2024-05-17 at BOS canceled."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Flight HAT006 on 2024-05-18 at BOS canceled."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_27",
        "instruction": "Coordinate schedule changes at BOS and the time is 2024-05-20T09:00:00Z.Planned schedule retime needed for HAT006 on 2024-05-20.You need to Log an event with 'Planned retime executed for HAT006 on 2024-05-20; customer notifications dispatched.'Notify channel operation channel with 'Schedule change: HAT006 on 2024-05-20 retimed; check updated itinerary.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT006",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "SCHEDULE_CHANGE",
                    "details": "Planned retime executed for HAT006 on 2024-05-20; customer notifications dispatched.",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Schedule change: HAT006 on 2024-05-20 retimed; check updated itinerary."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_28",
        "instruction": "Coordinate gate operations at LAX and the time is 2024-05-15T15:20:00Z.Due to an aircraft swap, Flight HAT012 (LAX -> EWR, 2024-05-15) is reassigned from Gate A17 to Gate B21.Flight HAT022 (LAX -> DFW, 2024-05-15) is reassigned from Gate A16 to Gate A15.You need to initiate the needed protocol",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT012",
                    "date": "2024-05-15"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT012"
                    ],
                    "date": "2024-05-15",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT012 on 2024-05-15 at LAX: A17->B21",
                    "event_timestamp_utc": "2024-05-15T15:20:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lax",
                    "message": "Gate change: HAT012 2024-05-15 A17->B21 at LAX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT022",
                    "date": "2024-05-15"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT022"
                    ],
                    "date": "2024-05-15",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT022 on 2024-05-15 at LAX: A16->A15",
                    "event_timestamp_utc": "2024-05-15T15:20:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lax",
                    "message": "Gate change: HAT022 2024-05-15 A16->A15 at LAX"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_29",
        "instruction": "Coordinate gate operations at MCO and the time is 2024-05-18T15:20:00Z.A late-arriving aircraft requires Gate C15 for turnaround, prompting Flight HAT028 (MCO -> BOS, 2024-05-18) to move to Gate D8.You need to apply the needed protocol, and a 30-minute delay for HAT028.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT028",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT028"
                    ],
                    "date": "2024-05-18",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT028 on 2024-05-18 at MCO: C15->D8",
                    "event_timestamp_utc": "2024-05-18T15:20:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Gate change: HAT028 2024-05-18 C15->D8 at MCO"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT028"
                    ],
                    "date": "2024-05-18",
                    "new_status": "delayed-gate-change"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT028",
                    "date": "2024-05-18",
                    "delay_minutes": 30
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT028-2024-05-18",
                    "message": "Delay by 30 minutes for HAT028 (2024-05-18) at MCO."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_30",
        "instruction": "Coordinate gate operations at SFO and the time is 2024-05-25T09:32:00ZA late inbound arrival for HAT032 (PHX -> SFO, 2024-05-25) forces a gate reassignment from B12 to C07 at SFO. Apply the needed protocols for gate change and protect connections.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SFO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT032",
                    "date": "2024-05-25"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "date": "2024-05-25"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT032",
                    "date": "2024-05-25"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT032"
                    ],
                    "date": "2024-05-25",
                    "new_status": "delayed-gate-change"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SFO",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT032 on 2024-05-25 at SFO: B12->C07",
                    "event_timestamp_utc": "2024-05-25T09:32:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-sfo",
                    "message": "Gate change: HAT032 2024-05-25 B12->C07 at SFO"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SFO",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT032",
                    "event_timestamp_utc": "2024-05-25T09:32:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT032-2024-05-25",
                    "message": "Connection protection advisory for HAT032 on 2024-05-25: monitoring tight connections; alternatives under review."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_31",
        "instruction": "Execute operations management at DFW and the time is 2024-05-22T00:00:00ZA storm hit the airport and a SIGMET has to be issued for DFW on 2024-05-22 delays departure for HAT038 by 90 minutes. Aircraft (tail_number) PR-XBE for flight HAT170 got damaged and recovery is not possible, You need to Initiate SIGMET and the Aircraft AOG protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "Weather",
                    "details": "SIGMET impacts DFW operations; apply 90-minutes delay to affected flights.",
                    "event_timestamp_utc": "2024-05-22T00:00:00Z"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT038",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT038"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT038",
                    "date": "2024-05-22",
                    "delay_minutes": 90
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-XBE"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC002",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "flight_id": "HAT170",
                    "aircraft_id": "AC002",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-XBE grounded for maintenance, HAT170 on 2024-05-22.",
                    "event_timestamp_utc": "2024-05-22T00:00:00Z"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC002",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-XBE grounded for maintenance, HAT170 on 2024-05-22.",
                    "technician_id": "TECH-DFW-01",
                    "event_timestamp_utc": "2024-05-22T00:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_32",
        "instruction": "Lead security operations at JFK and the time is 2024-05-26T00:00:00Z.A diplomatic delegation arrives on HAT035 (aircraft tail number PR-GOL) at Gate A5.You need to apply the Diplomatic Arrival protocol and then the Unattended Baggage protocol for a suspicious bag at Gate A5",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "JFK"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT035",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-GOL"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_JFK",
                    "event_type": "Security Alert",
                    "details": "Diplomatic arrival HAT035; secure handling from arrival to deplaning; protocol compliance confirmed.",
                    "event_timestamp_utc": "2024-05-26T00:00:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT035"
                    ],
                    "date": "2024-05-26",
                    "new_status": "security-hold"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_JFK",
                    "event_type": "UNATTENDED_BAGGAGE",
                    "details": "Unattended baggage Gate A5; boarding paused for HAT035.",
                    "event_timestamp_utc": "2024-05-26T00:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-jfk",
                    "message": "Diplomatic arrival HAT035; secure handling from arrival to deplaning; protocol compliance confirmed."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-jfk",
                    "message": "Security advisory: temporary boarding pause for HAT035 at JFK."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_33",
        "instruction": "Coordinate passenger services at DFW and the time is 2024-05-18T10:00:00Z.On a high-traffic day, unusually long lines form at the security gates, and many passengers of HAT170 express concern about missing their flights.You need to Schedule a Minor delay at DFW by 30 minutes for HAT170 and ensure that all connecting flights are protected accordingly.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-18",
                    "delay_minutes": 30
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT170"
                    ],
                    "date": "2024-05-18",
                    "new_status": "delayed"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT170",
                    "event_timestamp_utc": "2024-05-18T10:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "Minor Delay",
                    "details": "Delay by 30 minutes for HAT170 (2024-05-18) at DFW.",
                    "event_timestamp_utc": "2024-05-18T10:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT170-2024-05-18",
                    "message": "Connection protection advisory for HAT170 on 2024-05-18: monitoring tight connections; alternatives under review."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT170-2024-05-18",
                    "message": "Delay by 30 minutes for HAT170 (2024-05-18) at DFW."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_34",
        "instruction": "Supervise air traffic operations at LAS and the time is 2024-05-16T00:00:00Z.Flight HAT155 (LAX -> SFO) aircraft tail number PR-GOL has requested an emergency landing in LAS due to a technical failure.Flight HAT173 is approaching LAS and must yield the airspace.You need to apply a 30-minute delay to HAT173, initiate the AOG protocol for HAT155, And check logs and operational events for maintenance.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-GOL"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-GOL grounded for maintenance, HAT155 on 2024-05-16.",
                    "technician_id": "TECH-LAS-01",
                    "event_timestamp_utc": "2024-05-16T00:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "flight_id": "HAT155",
                    "aircraft_id": "AC001",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-GOL grounded for maintenance, HAT155 on 2024-05-16.",
                    "event_timestamp_utc": "2024-05-16T00:00:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT173"
                    ],
                    "date": "2024-05-16",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT173",
                    "date": "2024-05-16",
                    "delay_minutes": 30
                },
            },
            {
                "name": "MaintenanceLogsForAircraft",
                "arguments": {
                    "aircraft_id": "AC001"
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "date": "2024-05-16"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_35",
        "instruction": "Manage health and safety operations at BOS and the time is 2024-05-07T10:00:00Z.During boarding for Flight HAT235 from BOS to MCO, the gate agent noticed a passenger (user_id ava_li_8840) showing signs of severe shortness of breath and dizziness.The passenger admitted to feeling unwell since the morning.You need to follow the Health Risk Possibility Protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "ava_li_8840"
                },
            },
            {
                "name": "RefundReservation",
                "arguments": {
                    "reservation_id": "VHG5XU"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Due to health risk possibility, passenger prevented from traveling on aircraft HAT235, Reservation VHG5XU, on 2024-05-07."
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "REFUND",
                    "details": "Reservation VHG5XU refunded.",
                    "event_timestamp_utc": "2024-05-07T10:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "Health risk",
                    "details": "Due to health risk possibility, passenger prevented from traveling on aircraft HAT235, Reservation VHG5XU, on 2024-05-07.",
                    "event_timestamp_utc": "2024-05-07T10:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ava_li_8840",
                    "message": "Reservation VHG5XU refunded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_36",
        "instruction": "Manage station operations at BOS and the time is 2024-05-23T09:10:00ZHAT216 ( tail number D-A-IGX) has arrived at Gate C11 and passengers are deboarding. During arrival inspection, suspected bird strike evidence is reported on the aircraft assigned to HAT216 (2024-05-23); the aircraft must be grounded.HAT210 is scheduled to depart from Gate C11 in few hours. You need to invoke the Wildlife Strike protocol to ground the affected aircraft, then reassign HAT210\u2019s departure to Gate C9 with 30-minute delay for HAT210.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "D-A-IGX"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC023",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "flight_id": "HAT216",
                    "aircraft_id": "AC023",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "Due to Wildlife Strike, aircraft D-A-IGX grounded for maintenance, HAT216 on 2024-05-23.",
                    "event_timestamp_utc": "2024-05-23T09:10:00Z"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC023",
                    "maintenance_type": "Unscheduled",
                    "description": "Due to Wildlife Strike, aircraft D-A-IGX grounded for maintenance, HAT216 on 2024-05-23.",
                    "technician_id": "TECH-BOS-01",
                    "event_timestamp_utc": "2024-05-23T09:10:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT210"
                    ],
                    "date": "2024-05-23",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT210 on 2024-05-23 at BOS: C11->C9",
                    "event_timestamp_utc": "2024-05-23T09:10:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Gate change: HAT210 2024-05-23 C11->C9 at BOS"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT210"
                    ],
                    "date": "2024-05-23",
                    "new_status": "delayed-gate-change"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT210",
                    "date": "2024-05-23",
                    "delay_minutes": 30
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT210-2024-05-23",
                    "message": "Delay by 30 minutes for HAT210 (2024-05-23) at BOS."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_37",
        "instruction": "Coordinate gate operations at MCO and the time is 2024-05-18T08:00:00Z.To improve passenger flow, Flight HAT028 (MCO -> BOS, 2024-05-18) moves from Gate F6 to F2. You need to run the Gate Change protocol and then Connection Protection for tight connections in BOS. ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT028",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT028",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT028"
                    ],
                    "date": "2024-05-18",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT028 on 2024-05-18 at MCO: F6->F2",
                    "event_timestamp_utc": "2024-05-18T08:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Gate change: HAT028 2024-05-18 F6->F2 at MCO"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT028",
                    "event_timestamp_utc": "2024-05-18T08:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT028-2024-05-18",
                    "message": "Connection protection advisory for HAT028 on 2024-05-18: monitoring tight connections; alternatives under review."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_38",
        "instruction": "Manage security operations at MCO and the time is 2024-05-21T10:00:00Z.During boarding for HAT214 (MCO -> PHX, 2024-05-21), a cabin crew member reports discovering a toy gun in a passenger\u2019s carry-on which is prohibited.The incident caused delay for 90 minutes for inspect the item. You need to handle the situation.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-21"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "CABIN_ITEMS",
                    "details": "Cabin items advisory: toy gun removed from passenger’s possession; item secured as non-threatening.",
                    "flight_id": "HAT214",
                    "event_timestamp_utc": "2024-05-21T10:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-phx",
                    "message": "Cabin items advisory issued for HAT214 (2024-05-21) - toy gun removed and secured."
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT214"
                    ],
                    "date": "2024-05-21",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-21",
                    "delay_minutes": 90
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_39",
        "instruction": "Coordinate maintenance operations at PHX and the time is 2024-05-22T08:45:00Z.A hydraulic leak on aircraft tail number PP-LTM has caused the cancellation of flight HAT249 on 2024-05-22, and the aircraft is now grounded.You need to cancel the flight for today, and aircraft PS-MND should be repositioned from MCO to PHX to cover operations until maintenance on PP-LTM is completed.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PP-LTM"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC003",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC003",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PP-LTM grounded for maintenance, HAT249 on 2024-05-22.",
                    "technician_id": "TECH-PHX-01",
                    "event_timestamp_utc": "2024-05-22T08:45:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "flight_id": "HAT249",
                    "aircraft_id": "AC003",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PP-LTM grounded for maintenance, HAT249 on 2024-05-22.",
                    "event_timestamp_utc": "2024-05-22T08:45:00Z"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT249",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT249"
                    ],
                    "date": "2024-05-22",
                    "new_status": "canceled"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-phx",
                    "message": "Flight HAT249 on 2024-05-22 at PHX canceled."
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PS-MND"
                },
            },
            {
                "name": "RelocateAircraft",
                "arguments": {
                    "aircraft_id": "AC012",
                    "new_location_airport_id": "ARP_PHX",
                    "new_location_iata": "PHX"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_40",
        "instruction": "Manage gate operations at PHX and the time is 2024-05-14T08:45:00Z.On flight HAT251, operating with aircraft tail number PP-PTM, a passenger\u2019s ( user_id mia_kovacs_8269 ) economy seat is damaged and unusable.You need to upgrade them to business class following protocols.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PP-PTM"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "mia_kovacs_8269"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "8JIA1I",
                    "cabin": "business"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "flight_id": "HAT251",
                    "aircraft_id": "AC008",
                    "event_type": "Cabin change",
                    "details": "In-flight cabin change for mia_kovacs_8269",
                    "event_timestamp_utc": "2024-05-14T08:45:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC008",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC008",
                    "maintenance_type": "Unscheduled",
                    "description": "In-flight cabin change for mia_kovacs_8269",
                    "technician_id": "TECH-PHX-01",
                    "event_timestamp_utc": "2024-05-14T08:45:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_41",
        "instruction": "Lead security operations at LGA and the time is 2024-05-12T11:05:00Z.Flight HAT219 from LGA to PHX  is going to board on gate A3 on 2024-05-12 is carrying a high-risk prisoner.Prisoner transport arrives 35 minutes late due to traffic.You need to delay departure by 20 minutes, use remote gate (D20) for discreet boarding.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "Minor Delay",
                    "details": "Delay by 20 minutes for HAT219 (2024-05-12) at LGA.",
                    "event_timestamp_utc": "2024-05-12T11:05:00Z"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT219",
                    "date": "2024-05-12"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT219"
                    ],
                    "date": "2024-05-12",
                    "new_status": "delayed-gate-change"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT219",
                    "date": "2024-05-12",
                    "delay_minutes": 20
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT219 on 2024-05-12 at LGA: A3->D20",
                    "event_timestamp_utc": "2024-05-12T11:05:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lga",
                    "message": "Gate change: HAT219 2024-05-12 A3->D20 at LGA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_42",
        "instruction": "Execute Cabin Safety Supervisor at LGA and the time is 2024-05-20T20:55:00Z.Pre-flight check for HAT219 to PHX on 2024-05-20 reveals a missing bain item (infant life vest).You need to apply a minor delay boarding by 20 minutes and then ask for a vest replacement.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "Minor Delay",
                    "details": "Delay by 20 minutes for HAT219 (2024-05-20) at LGA.",
                    "event_timestamp_utc": "2024-05-20T20:55:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT219"
                    ],
                    "date": "2024-05-20",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT219",
                    "date": "2024-05-20",
                    "delay_minutes": 20
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lga",
                    "message": "Delay by 20 minutes for HAT219 (2024-05-20) at LGA."
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "equipment_change",
                    "details": "Cabin equipment change needed for HAT219 on 2024-05-20; (infant life vest).",
                    "event_timestamp_utc": "2024-05-20T20:55:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lga",
                    "message": "Cabin equipment change needed for HAT219 on 2024-05-20; (infant life vest)."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_43",
        "instruction": "Execute Cabin Services Coordinator at ORD and the time is 2024-05-25T22:55:00Z.During the pre-flight check for HAT223 to ATL on 2024-05-25, a missing beverage cart was found in the rear galley.You need to arrange for a spare to be delivered and postpone boarding (minor delay) by 30 minutes.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ORD"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ORD",
                    "event_type": "Minor Delay",
                    "details": "Delay by 30 minutes for HAT223 (2024-05-25) at ORD.",
                    "event_timestamp_utc": "2024-05-25T22:55:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT223"
                    ],
                    "date": "2024-05-25",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT223",
                    "date": "2024-05-25",
                    "delay_minutes": 30
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-ord",
                    "message": "Delay by 30 minutes for HAT223 (2024-05-25) at ORD."
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ORD",
                    "event_type": "equipment_change",
                    "details": "Cabin equipment change needed for HAT223 on 2024-05-25; (beverage cart).",
                    "event_timestamp_utc": "2024-05-25T22:55:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-ord",
                    "message": "Cabin equipment change needed for HAT223 on 2024-05-25; (beverage cart)."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_44",
        "instruction": "Execute Passenger Services Supervisor at MCO and the time is 2024-05-21T10:00:00Z. Pre-boarding for HAT214 to PHX on 2024-05-21 reveals a shortage of wheelchairs for mobility-assistance passengers. You need to request additional units from ground services and delay boarding by 30 minutes until all required wheelchairs are available.",
        "actions": [
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-21"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "ASSISTANCE_SHORTAGE",
                    "details": "Wheelchair shortage for HAT214 on 2024-05-21; boarding delayed 30 minutes.",
                    "event_timestamp_utc": "2024-05-21T10:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Wheelchair shortage reported for HAT214 (2024-05-21); boarding delayed 30 minutes to arrange assistance."
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT214"
                    ],
                    "date": "2024-05-21",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-21",
                    "delay_minutes": 30
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_45",
        "instruction": "Execute Passenger Services Supervisor at LGA and the time is 2024-05-30T13:40:00Z. During boarding for HAT219 to PHX on 2024-05-30, the boarding wheelchair lift becomes inoperative. You need to request an alternate lift from ground services immediately and delay boarding by 45 minutes to ensure safe wheelchair boarding.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT219",
                    "date": "2024-05-30"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "GROUND_EQUIPMENT",
                    "details": "Boarding lift inoperative for HAT219 on 2024-05-30; alternate lift requested; boarding delayed 45 minutes.",
                    "event_timestamp_utc": "2024-05-30T13:40:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lga",
                    "message": "Boarding lift inoperative for HAT219 on 2024-05-30; alternate lift requested; boarding delayed 45 minutes."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-phx",
                    "message": "Boarding lift inoperative for HAT219 on 2024-05-30; alternate lift requested; boarding delayed 45 minutes."
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT219"
                    ],
                    "date": "2024-05-30",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT219",
                    "date": "2024-05-30",
                    "delay_minutes": 45
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT219-2024-05-30",
                    "message": "Delay by 45 minutes for HAT219 (2024-05-30) at LGA."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_46",
        "instruction": "Execute Ramp Supervisor at LAX and the time is 2024-05-20T21:10:00Z. Mid-boarding for HAT228 to EWR on 2024-05-20, one baggage cart becomes inoperative on the ramp. You need to request a replacement cart immediately then apply a 25-minute delay.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT228",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "Baggage cart breakdown for HAT228 on 2024-05-20; replacement requested; transfer bags prioritized; boarding/loading delayed 25 minutes.",
                    "event_timestamp_utc": "2024-05-20T21:10:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lax",
                    "message": "Baggage cart breakdown for HAT228 on 2024-05-20; replacement requested; transfer bags prioritized; boarding/loading delayed 25 minutes"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT228"
                    ],
                    "date": "2024-05-20",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT228",
                    "date": "2024-05-20",
                    "delay_minutes": 25
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT228-2024-05-20",
                    "message": "Delay by 25 minutes for HAT228 (2024-05-20) at LAX."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_47",
        "instruction": "Handle reservations duties at LGA and the time is 2024-05-14T09:00:00Z.Customer ethan_kovacs_5869 is here with a question about his travel starting today.He states that he is allergic to cat fur and wants to know if there will be any cats in the cabin.You need to check the reservations ( from today and later ) and answer the query in the exact format 'Total cat counts: {total_count}' using Customer Query Protocol and create a operational log.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "ethan_kovacs_5869"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-14"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT256",
                    "date": "2024-05-15"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT148",
                    "date": "2024-05-18"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT084",
                    "date": "2024-05-19"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Customer query answered.",
                    "event_timestamp_utc": "2024-05-14T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ethan_kovacs_5869",
                    "message": "Total cat counts: 0"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_48",
        "instruction": "Handle reservations duties at LGA and the time is 2024-05-02T09:00:00Z.Customer olivia_martin_3393 called you and since she already has an extensive personal insurance;She wants to opt out of insurance in all of her reservations.You task is to find all her reservations and do what she wants.",
        "actions": [
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "olivia_martin_3393"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "RH5QMP",
                    "insurance": "no"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "6E2AQ3",
                    "insurance": "no"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "SJWOFH",
                    "insurance": "no"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "R37DI8",
                    "insurance": "no"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "YDMCU8",
                    "insurance": "no"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "70US1E",
                    "insurance": "no"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "N3C95P",
                    "insurance": "no"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_49",
        "instruction": "Handle reservations duties at LGA and the time is 2024-05-02T09:00:00Z.User liam_santos_5621 has become a Silver member of the airline's customer club and is now entitled to one additional free baggage allowance for their reservations.You need to locate all of their reservations and their current total baggages and add an extra baggage to the current total baggages of his reservations.",
        "actions": [
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "liam_santos_5621"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "ZZSA4W",
                    "total_baggages": 1
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "V75SFJ",
                    "total_baggages": 1
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "EFIAC5",
                    "total_baggages": 1
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "T7RO4F",
                    "total_baggages": 1
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "96HBVR",
                    "total_baggages": 2
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "C2SZKK",
                    "total_baggages": 3
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "IDTRDM",
                    "total_baggages": 1
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_50",
        "instruction": "Coordinate gate operations at LAX and the time is 2024-05-15T15:20:00Z.Due to a system error, two flights ( HAT022, HAT012 ) have been assigned to Gate A17 at the same time.Reassign Flight HAT012 (LAX -> EWR, 2024-05-15) from Gate A17 to Gate B21.You need to initiate the Gate Change protocol And set 30 min delay for HAT012 flight.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT012 on 2024-05-15 at LAX: A17->B21",
                    "event_timestamp_utc": "2024-05-15T15:20:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lax",
                    "message": "Gate change: HAT012 2024-05-15 A17->B21 at LAX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT012",
                    "date": "2024-05-15"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Minor Delay",
                    "details": "Delay by 30 minutes for HAT012 (2024-05-15) at LAX.",
                    "event_timestamp_utc": "2024-05-15T15:20:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lax",
                    "message": "Delay by 30 minutes for HAT012 (2024-05-15) at LAX."
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT012"
                    ],
                    "date": "2024-05-15",
                    "new_status": "delayed-gate-change"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT012",
                    "date": "2024-05-15",
                    "delay_minutes": 30
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT012-2024-05-15",
                    "message": "Delay by 30 minutes for HAT012 (2024-05-15) at LAX."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_51",
        "instruction": "Manage health and safety operations at BOS and the time is 2024-05-07T10:00:00Z.During boarding for Flight HAT235 from BOS to MCO, the gate agent noticed a passenger is pregnant nearly 8 month (user_id isabella_khan_8788).The passenger doesnt have doctors permit to fly.You need to follow the Health Risk Possibility Protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "isabella_khan_8788"
                },
            },
            {
                "name": "RefundReservation",
                "arguments": {
                    "reservation_id": "2M27GS"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "Due to health risk possibility, passenger prevented from traveling on aircraft HAT235, Reservation 2M27GS, on 2024-05-07."
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "REFUND",
                    "details": "Reservation 2M27GS refunded.",
                    "event_timestamp_utc": "2024-05-07T10:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "Health risk",
                    "details": "Due to health risk possibility, passenger prevented from traveling on aircraft HAT235, Reservation 2M27GS, on 2024-05-07.",
                    "event_timestamp_utc": "2024-05-07T10:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "isabella_khan_8788",
                    "message": "Reservation 2M27GS refunded."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_52",
        "instruction": "Execute Flight Operations Supervisor and the time is 2024-05-22T16:25:00Z.During flight HAT236 (SEA -> PHX), the co-pilot reports feeling unwell in-flight.You need to divert to the nearest suitable ( MSY ) airport, coordinate with ground operations for medical assistance, and update operational events accordingly.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MSY"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT236",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Diversion",
                    "details": "In-flight crew medical diversion for HAT236 on 2024-05-22 - landed at MSY for crew medical assistance.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "Diversion",
                    "details": "In-flight crew medical diversion for HAT236 on 2024-05-22 - landed at MSY for crew medical assistance.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MSY",
                    "event_type": "Diversion",
                    "details": "In-flight crew medical diversion for HAT236 on 2024-05-22 - landed at MSY for crew medical assistance.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT236"
                    ],
                    "date": "2024-05-22",
                    "new_status": "diverted"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_53",
        "instruction": "Execute Flight Operations Supervisor and the time is 2024-05-22T16:25:00Z.During flight HAT236 (SEA -> PHX) in the aircraft ( tail number PR-GOL) a rat has been seen by several passengers.You need to initiate Rodent Onboard Emergency protocol by diverting to the nearest suitable ( airport id ARP_MSY ) airport.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT236",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Diversion",
                    "details": "In-flight rodent sighting for HAT236 on 2024-05-22 - landed at MSY for urgent maintenance and pest control.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "Diversion",
                    "details": "In-flight rodent sighting for HAT236 on 2024-05-22 - landed at MSY for urgent maintenance and pest control.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MSY",
                    "event_type": "Diversion",
                    "details": "In-flight rodent sighting for HAT236 on 2024-05-22 - landed at MSY for urgent maintenance and pest control.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT236"
                    ],
                    "date": "2024-05-22",
                    "new_status": "diverted"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-GOL"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-GOL grounded for maintenance, HAT236 on 2024-05-22.",
                    "technician_id": "TECH-MSY-01",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MSY",
                    "flight_id": "HAT236",
                    "aircraft_id": "AC001",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-GOL grounded for maintenance, HAT236 on 2024-05-22.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_54",
        "instruction": "Execute Flight Operations Supervisor and the time is 2024-05-26T16:25:00Z.During flight HAT237 (DTW -> MSP), a passenger becomes seriously unwell mid-flight.You need to divert to the nearest suitable ( MCO ) airport.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DTW"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MSP"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT237",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Diversion",
                    "details": "In-flight passenger medical emergency for HAT237 on 2024-05-26 - landed at MCO for urgent medical assistance.",
                    "event_timestamp_utc": "2024-05-26T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DTW",
                    "event_type": "Diversion",
                    "details": "In-flight passenger medical emergency for HAT237 on 2024-05-26 - landed at MCO for urgent medical assistance.",
                    "event_timestamp_utc": "2024-05-26T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MSP",
                    "event_type": "Diversion",
                    "details": "In-flight passenger medical emergency for HAT237 on 2024-05-26 - landed at MCO for urgent medical assistance.",
                    "event_timestamp_utc": "2024-05-26T16:25:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT237"
                    ],
                    "date": "2024-05-26",
                    "new_status": "diverted"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_55",
        "instruction": "Execute Flight Operations Supervisor and the time is 2024-05-22T16:25:00Z.During flight HAT236 (SEA -> PHX) in the aircraft ( tail number PR-GOL) a rat has been seen by several passengers.You need to initiate Rodent Onboard Emergency protocol ,closest airport is the origin so return there. ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT236",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Return",
                    "details": "In-flight rodent sighting for HAT236 on 2024-05-22 - landed at SEA for urgent maintenance and pest control.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-GOL"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-GOL grounded for maintenance, HAT236 on 2024-05-22.",
                    "technician_id": "TECH-SEA-01",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "flight_id": "HAT236",
                    "aircraft_id": "AC001",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-GOL grounded for maintenance, HAT236 on 2024-05-22.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_56",
        "instruction": "Manage airport operations at SEA and the time is 2024-05-15T09:00:00Z.An aircraft swap between flights number HAT236 and HAT253 on 2024-05-15requires updating the assigned gate from A10 to D22 for HAT236 and D22 to A10 for HAT253.Your job is to initiate Gate Change protocol for those two flights.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT236",
                    "date": "2024-05-15"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT236"
                    ],
                    "date": "2024-05-15",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT236 on 2024-05-15 at SEA: A10->D22",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-sea",
                    "message": "Gate change: HAT236 2024-05-15 A10->D22 at SEA"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT253",
                    "date": "2024-05-15"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT253"
                    ],
                    "date": "2024-05-15",
                    "new_status": "boarding-update"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Gate change",
                    "details": "Gate change for HAT253 on 2024-05-15 at SEA: D22->A10",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-sea",
                    "message": "Gate change: HAT253 2024-05-15 D22->A10 at SEA"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_57",
        "instruction": "Execute maintenance planning at MCO and the time is 2024-05-15T09:00:00Z.Aircrafts PS-AEF and PS-MND have successfully completed their C-Checks.You need to initiate the Maintenance Done Protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PS-AEF"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Maintenance Done",
                    "details": "Maintenance Done for PS-AEF on 2024-05-15 at MCO",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC004",
                    "new_status": "Active"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PS-MND"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Maintenance Done",
                    "details": "Maintenance Done for PS-MND on 2024-05-15 at MCO",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC012",
                    "new_status": "Active"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_58",
        "instruction": "Execute fleet operations manager at PHX and the time is 2024-05-15T09:00:00ZAircraft N-DXJ is being relocated to a new base LAS for a C-Check maintenance.You need to set the aircraft status to maintenance and update its base assignment and record the event at PHX with type AIRCRAFT_MOVED and message: 'Aircraft N-DXJ moved to LAS'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "N-DXJ"
                },
            },
            {
                "name": "RelocateAircraft",
                "arguments": {
                    "aircraft_id": "AC016",
                    "new_location_airport_id": "ARP_LAS",
                    "new_location_iata": "LAS"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC016",
                    "maintenance_type": "C-Check",
                    "description": "Routine C-Check inspection.",
                    "corrective_action": "Scheduled heavy maintenance C-Check.",
                    "technician_id": "TECH-LAS-01",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "aircraft_id": "AC016",
                    "event_type": "AIRCRAFT_MOVED",
                    "details": "Aircraft N-DXJ moved to LAS",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC016",
                    "new_status": "In Maintenance"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_59",
        "instruction": "Execute customer service agent at LGA and the time is 2024-05-02T09:00:00Z. Passenger William Brown (lucas_kovacs_3548) requests to move forward all of his flight dates for reservation HRLFDK for exactly one day. The current reservation has flights: HAT065 (LGA-CLT) on 2024-05-08, HAT262 (CLT-DEN) on 2024-05-08, HAT080 (DEN-PHL) on 2024-05-12, and HAT135 (PHL-LGA) on 2024-05-12. You need to retrieve the reservation details, verify the current flight information, and update all flight dates to be one day later.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "lucas_kovacs_3548"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT065",
                    "date": "2024-05-08"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT262",
                    "date": "2024-05-08"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT080",
                    "date": "2024-05-12"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT135",
                    "date": "2024-05-12"
                },
            },
            {
                "name": "UpdateReservationDetails",
                "arguments": {
                    "reservation_id": "HRLFDK",
                    "flights": [
                        {
                            "origin": "LGA",
                            "destination": "CLT",
                            "flight_number": "HAT065",
                            "date": "2024-05-09"
                        },
                        {
                            "origin": "CLT",
                            "destination": "DEN",
                            "flight_number": "HAT262",
                            "date": "2024-05-09"
                        },
                        {
                            "origin": "DEN",
                            "destination": "PHL",
                            "flight_number": "HAT080",
                            "date": "2024-05-13"
                        },
                        {
                            "origin": "PHL",
                            "destination": "LGA",
                            "flight_number": "HAT135",
                            "date": "2024-05-13"
                        }
                    ]
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_60",
        "instruction": "Manage network operations at PHX and the time is 2024-05-16T09:00:00Z.Due to a severe fire in LAS cancel all the flights from PHX to there until 2024-05-16You need to confirm the route and affected flight numbers and update their status to canceled",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "date": "2024-05-16",
                    "destination": "LAS",
                    "origin": "PHX"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT173",
                        "HAT027",
                        "HAT259"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-phx",
                    "message": "Flight HAT173, HAT027, HAT259 on 2024-05-16 at PHX canceled."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_61",
        "instruction": "Handle reservations duties at LGA and the time is 2024-05-20T19:00:00Z. Olivia Anderson (user_id: raj_kovacs_4682 , date of birth 1976-10-03, email: isabella.anderson3802@example.com) is here and his flight (HAT219) from LGA to PHX on 2024-05-20 was canceled earlier.You need to book the closest available flight from LGA to PHX for him.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "FindReservationsByUser",
                "arguments": {
                    "user_id": "raj_kovacs_4682"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "LGA",
                    "destination": "PHX",
                    "start_date": "2024-05-20",
                    "status": "available"
                },
            },
            {
                "name": "CreateReservation",
                "arguments": {
                    "user_email": "isabella.anderson3802@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT150",
                            "date": "2024-05-20",
                            "origin": "LGA",
                            "destination": "PHX"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Raj",
                            "last_name": "Kovacs",
                            "dob": "1976-10-03"
                        }
                    ],
                    "cabin": "economy"
                }
            }
        ],
        "outputs": [
                "reservation_id = RES9816",
                "flight number = HAT150",
                "date = 2024-05-20"
        ]
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_62",
        "instruction": "Execute operations management at LAX and the time is 2024-05-22T03:10:00ZDue to fatigues of the crew caused by delayed landing, crew members need some rest.You need to apply 120 minutes minor delay to flight HAT170 and ensure its reflected in the event logs.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Minor Delay",
                    "details": "Delay by 120 minutes for HAT170 (2024-05-22) at LAX.",
                    "event_timestamp_utc": "2024-05-22T03:10:00Z"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT170"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT170",
                    "date": "2024-05-22",
                    "delay_minutes": 120
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "date": "2024-05-22"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_63",
        "instruction": "Coordinate crew training activities at LAX and the time is 2024-05-10T08:45:00Z. Captain EMP004 requires recurrent E195-E2 certificate on 2024-05-10.You need to initiate the Crew Recertification protocol for this case.and find the replacement (from any base) for him and set EMP004 status to 'Training'",
        "actions": [
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM004"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "crew_member_id": "CM004"
                },
            },
            {
                "name": "ScanFlightsByDate",
                "arguments": {
                    "date": "2024-05-10",
                    "flight_numbers": [
                        "HAT002",
                        "HAT011",
                        "HAT004",
                        "HAT003",
                        "HAT010"
                    ]
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM004",
                    "new_status": "Training"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Crew Training",
                    "details": "Training scheduled for CM004 on 2024-05-10 : E195-E2.",
                    "event_timestamp_utc": "2024-05-10T08:45:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "CM004",
                    "message": "Training scheduled for CM004 on 2024-05-10 : E195-E2."
                },
            },
            {
                "name": "FindAvailableCrew",
                "arguments": {
                    "role": "Captain",
                    "status": "Active"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT002",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT011",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT004",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT003",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT010",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_64",
        "instruction": "Execute Flight Operations Supervisor and the time is 2024-05-22T16:25:00Z.During flight HAT236 (SEA -> PHX), the pilot ( crew member id CM004) reports feeling unwell in-flight.You need to divert to the nearest suitable ( ATL ) airport, coordinate with ground operations for medical assistance, and update operational events accordingly.Find a replacement for him at for him there to continue and set CM004 status to 'Sick Leave'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT236",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Diversion",
                    "details": "In-flight crew medical diversion for HAT236 on 2024-05-22 - landed at ATL for crew medical assistance.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "Diversion",
                    "details": "In-flight crew medical diversion for HAT236 on 2024-05-22 - landed at ATL for crew medical assistance.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Diversion",
                    "details": "In-flight crew medical diversion for HAT236 on 2024-05-22 - landed at ATL for crew medical assistance.",
                    "event_timestamp_utc": "2024-05-22T16:25:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT236"
                    ],
                    "date": "2024-05-22",
                    "new_status": "diverted"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM004",
                    "new_status": "Sick Leave"
                },
            },
            {
                "name": "FindAvailableCrew",
                "arguments": {
                    "role": "Captain",
                    "status": "Active",
                    "home_base_iata": "ATL"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT236",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_65",
        "instruction": "Execute operations management at LAX and the time is 2024-05-22T05:45:00Z.Due to a system issue at the Immigration Office, passport control is experiencing heavy congestion.You need to apply a 120-minute delay to the flight HAT186 and initiate the Connection Protection Protocol.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT186",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT186"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT186",
                    "date": "2024-05-22",
                    "delay_minutes": 120
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT186",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "FindReservationsByFlightDay",
                "arguments": {
                    "flight_number": "HAT186",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "CUSTOMER_COMMUNICATION",
                    "details": "Connection protection monitoring initiated for HAT186",
                    "event_timestamp_utc": "2024-05-22T05:45:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "pass-HAT186-2024-05-22",
                    "message": "Connection protection advisory for HAT186 on 2024-05-22: monitoring tight connections; alternatives under review."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_66",
        "instruction": "Execute Cabin Safety Supervisor at SEA and the time is 2024-05-20T20:55:00Z.Pre-flight check for HAT220 on 2024-05-20 reveals a missing First Aid Kit box.Your job is to ask a spare and delay boarding by 20 minutes.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Minor Delay",
                    "details": "Delay by 20 minutes for HAT220 (2024-05-20) at SEA.",
                    "event_timestamp_utc": "2024-05-20T20:55:00Z"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT220",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT220"
                    ],
                    "date": "2024-05-20",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT220",
                    "date": "2024-05-20",
                    "delay_minutes": 20
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-sea",
                    "message": "Delay by 20 minutes for HAT220 (2024-05-20) at SEA."
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "equipment_change",
                    "details": "Cabin equipment change needed for HAT220 on 2024-05-20; (First Aid Kit box).",
                    "event_timestamp_utc": "2024-05-20T20:55:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-sea",
                    "message": "Cabin equipment change needed for HAT220 on 2024-05-20; (First Aid Kit box)."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_67",
        "instruction": "Execute crew scheduler at ATL. On 2024-05-01T06:50:00Z, flight HAT004 requires a last-minute crew change: employee EMP001 is unavailable. You need to initiate the Last-Minute Crew Replacement protocol for this caseAssign a qualified substitute (EMP004) to HAT004 for employee EMP001 on that date, and ensure that records reflect the change appropriately.Aircraft is Embraer E195-E2 which needs a E195-E2 certificate. make sure the new crew has it and its valid.",
        "actions": [
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP001"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM001",
                    "new_status": "On Leave"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "crew_member_id": "CM001",
                    "flight_number": "HAT004"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT004",
                    "crew_member_id": "CM004",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Crew Replacement",
                    "details": "Last-minute crew replacement required for HAT004 on 2024-05-01.",
                    "event_timestamp_utc": "2024-05-01T06:50:00Z"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM004"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_68",
        "instruction": "Execute crew scheduler at ATL and the time is 2021-11-26T06:50:00ZHAT004 by a Embraer E195-E2 aircraft is scheduled for today.You need to check for the Captains certificates to fly with this aircraft ( needs E195-E2 )If the certificate is expired. Initiate the Last-Minute Crew Replacement protocol for this caseAssign a qualified substitute (EMP004) to HAT004 for employee EMP001 on that date, and ensure that records reflect the change appropriately.Ensure newly assigned captain has a valid certificate.",
        "actions": [
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP001"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM001"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM001",
                    "new_status": "On Leave"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "crew_member_id": "CM001",
                    "flight_number": "HAT004"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT004",
                    "crew_member_id": "CM004",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Crew Replacement",
                    "details": "Last-minute crew replacement required for HAT004 on 2021-11-26.",
                    "event_timestamp_utc": "2021-11-26T06:50:00Z"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM004"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_69",
        "instruction": "Handle reservations duties at LAX and the time is 2024-05-16T09:00:00Z.You need to book the first economy one-way trip for customer Susan Wilson (email: liam.garcia1258@example.com) from LAX to EWR",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "EWR"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "LAX",
                    "destination": "EWR",
                    "start_date": "2024-05-16",
                    "status": "available"
                },
            },
            {
                "name": "FindFlights",
                "arguments": {
                    "origin": "EWR",
                    "destination": "DFW",
                    "start_date": "2024-05-17",
                    "end_date": "2024-05-17",
                    "status": "available"
                },
            },
            {
                "name": "FindUserByEmail",
                "arguments": {
                    "user_email": "liam.garcia1258@example.com"
                },
            },
            {
                "name": "CreateReservation",
                "arguments": {
                    "user_email": "liam.garcia1258@example.com",
                    "flight_details": [
                        {
                            "flight_number": "HAT228",
                            "date": "2024-05-16",
                            "origin": "LAX",
                            "destination": "EWR"
                        }
                    ],
                    "passengers": [
                        {
                            "first_name": "Aarav",
                            "last_name": "Nguyen",
                            "dob": "1974-01-01"
                        }
                    ],
                    "cabin": "economy"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_70",
        "instruction": "Execute operations management at LAX and the time is 2024-05-22T01:10:00Z.A SIGMET issued at is impacting outbound flights flight in LAX.You need to initiate the SIGMET delay protocol, applying a 120-minutes delay to the flights scheduled departure time less than 3 hours (HAT094, HAT103).",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Weather",
                    "details": "SIGMET impacts LAX operations; apply 120-minutes delay to affected flights.",
                    "event_timestamp_utc": "2024-05-22T01:10:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT094"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT094",
                    "date": "2024-05-22",
                    "delay_minutes": 120
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT103"
                    ],
                    "date": "2024-05-22",
                    "new_status": "delayed"
                },
            },
            {
                "name": "DelayFlightActualTimesForDate",
                "arguments": {
                    "flight_number": "HAT103",
                    "date": "2024-05-22",
                    "delay_minutes": 120
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_71",
        "instruction": "Handle maintenance control duties at LAX and the time is 2024-05-26T08:40:00ZAircraft PR-GOL, assigned to flight HAT186, was declared AOG at LAX due to hail damage to the hull paint.You need to set the flight status to 'canceled' and initiate the Aircraft AOG protocol for this case.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PR-GOL"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC001",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC001",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PR-GOL grounded for maintenance, HAT186 on 2024-05-26.",
                    "technician_id": "TECH-LAX-01",
                    "event_timestamp_utc": "2024-05-26T08:40:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "flight_id": "HAT186",
                    "aircraft_id": "AC001",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PR-GOL grounded for maintenance, HAT186 on 2024-05-26.",
                    "event_timestamp_utc": "2024-05-26T08:40:00Z"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT186",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT186"
                    ],
                    "date": "2024-05-26",
                    "new_status": "canceled"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_72",
        "instruction": "Execute operations management at ATL and the time is 2024-05-26T08:40:00Z.Multiple passengers from flight HAT004 on 2024-05-26 reported missing baggage.It was determined that the bags were mistakenly loaded onto another aircraft at the origin airport and transported to LAS.You need to Initiate the Baggage Irregularity protocol for this flight. Log the event for all three involved airports ( ATL, DFW, LAS ) . Also cargo equipment inspection not needed.",
        "actions": [
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT004",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "Baggage Irregularity: HAT004 from airport ARP_ATL to airport ARP_DFW on 2024-05-26.",
                    "event_timestamp_utc": "2024-05-26T08:40:00Z"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "Baggage Irregularity: HAT004 from airport ARP_ATL to airport ARP_DFW on 2024-05-26.",
                    "event_timestamp_utc": "2024-05-26T08:40:00Z"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "Baggage Irregularity: HAT004 from airport ARP_ATL to airport ARP_DFW on 2024-05-26.",
                    "event_timestamp_utc": "2024-05-26T08:40:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT004"
                    ],
                    "date": "2024-05-26",
                    "new_status": "baggage delay"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_73",
        "instruction": "Execute operations management at MCO. On 2024-05-16T08:40:00Z, a sudden fuel supply disruption is impacting outbound operations.You need to initiate the Fuel Supply Disruption protocol for MCO with HAT101, HAT299, HAT298, HAT028 as low-priority and cancel them separately.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Fuel Disruption",
                    "details": "Fuel supply disruption at MCO on 2024-05-16; priorities: HAT101, HAT299, HAT298, HAT028",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT101"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT299"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT298"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT028"
                    ],
                    "date": "2024-05-16",
                    "new_status": "canceled"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Fuel program MCO: HAT101, HAT299, HAT298, HAT028 canceled."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_74",
        "instruction": "Execute operations management at ATL. EMP004 On 2024-05-16T08:40:00Z, HAT004 (ATL->DFW) is at risk of crew duty-limit exceedance.You need to initiate the Crew Duty-Limit Mitigation protocol for HAT004 and find a replacement for that employee and set the flight status to delayed.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT004",
                    "date": "2024-05-16"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "flight_number": "HAT004"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP004"
                },
            },
            {
                "name": "ComputeCrewDutyCounts",
                "arguments": {
                    "crew_member_id": "CM004",
                    "reference_date": "2024-05-16"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM004",
                    "new_status": "Inactive"
                },
            },
            {
                "name": "FindAvailableCrew",
                "arguments": {
                    "role": "Captain",
                    "status": "Active",
                    "home_base_iata": "ATL"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT004",
                    "crew_member_id": "CM001",
                    "assigned_role": "Captain"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT004"
                    ],
                    "date": "2024-05-16",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Crew Replacement",
                    "details": "Crew delay on HAT004; standby crew assigned: CM001.",
                    "event_timestamp_utc": "2024-05-16T08:40:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_75",
        "instruction": "Supervise flight operations at DEN and the time is 2024-05-20T09:00:00Z.On flight HAT140 (tail number PT-MUI), two of the four toilets are inoperative, causing significant passenger delays.Aircraft is returned for maintenance.You need to Initiate AOG protocol, and update the flight status to returned.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DEN"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PT-MUI"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC006",
                    "new_status": "In Maintenance"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT140"
                    ],
                    "date": "2024-05-20",
                    "new_status": "returned"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DEN",
                    "flight_id": "HAT140",
                    "aircraft_id": "AC006",
                    "event_type": "AIRCRAFT_AOG",
                    "details": "aircraft PT-MUI grounded for maintenance, HAT140 on 2024-05-20.",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                },
            },
            {
                "name": "AppendMaintenanceLog",
                "arguments": {
                    "aircraft_id": "AC006",
                    "maintenance_type": "Unscheduled",
                    "description": "aircraft PT-MUI grounded for maintenance, HAT140 on 2024-05-20.",
                    "technician_id": "TECH-DEN-01",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_76",
        "instruction": "Execute maintenance planning at MCO and the time is 2024-05-15T09:00:00Z.Aircrafts D-A-VJW and PP-VBT were here from LAX for maintenance and have successfully completed their C-Checks.Your need to Initiate the Maintenance Done Protocol and relocate the aircraft to its main base LAX",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "D-A-VJW"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Maintenance Done",
                    "details": "Maintenance Done for D-A-VJW on 2024-05-15 at MCO",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC013",
                    "new_status": "Active"
                },
            },
            {
                "name": "GetAircraftByTail",
                "arguments": {
                    "tail_number": "PP-VBT"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Maintenance Done",
                    "details": "Maintenance Done for PP-VBT on 2024-05-15 at MCO",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SetAircraftStatus",
                "arguments": {
                    "aircraft_id": "AC014",
                    "new_status": "Active"
                },
            },
            {
                "name": "RelocateAircraft",
                "arguments": {
                    "aircraft_id": "AC013",
                    "new_location_airport_id": "ARP_LAX"
                },
            },
            {
                "name": "RelocateAircraft",
                "arguments": {
                    "aircraft_id": "AC014",
                    "new_location_airport_id": "ARP_LAX"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_77",
        "instruction": "Execute compliance auditor at LAX and the time is 2024-05-15T09:00:00Z.Execute verifying type-rating validity and duty records.You need to confirm that crew member EMP003 holds certification A220-300 , crew member EMP005 holds certification IR crew member EMP007 holds certification ATR72-600, and they all are valid.log the audit as 'Audit completed on {date}: {employee_code} holds {certificate_code} {valid/invalid}'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAX"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP003"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP005"
                },
            },
            {
                "name": "GetCrewMemberByEmployeeCode",
                "arguments": {
                    "employee_code": "EMP007"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM003"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM005"
                },
            },
            {
                "name": "GetCrewCertifications",
                "arguments": {
                    "crew_member_id": "CM007"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Compliance audit",
                    "details": "Audit completed on 2024-05-15: EMP003 holds A220-300 valid",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Compliance audit",
                    "details": "Audit completed on 2024-05-15: EMP005 holds IR valid",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAX",
                    "event_type": "Compliance audit",
                    "details": "Audit completed on 2024-05-15: EMP007 holds ATR72-600 valid",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_78",
        "instruction": "Execute airport operations director at SEA and the time is 2024-05-15T09:00:00ZExecute handling a critical runway closure emergency on 2024-05-15 that requires immediate diversion of a inbound flight.You need to divert flight HAT038 (flying from DFW to SEA) with aircraft (AC007) to DEN",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DEN"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DFW"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DEN",
                    "event_type": "Diversion",
                    "details": "Diversion for HAT038 on 2024-05-15 - landed at DEN.",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Diversion",
                    "details": "Diversion for HAT038 on 2024-05-15 - landed at DEN.",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DFW",
                    "event_type": "Diversion",
                    "details": "Diversion for HAT038 on 2024-05-15 - landed at DEN.",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT038"
                    ],
                    "date": "2024-05-15",
                    "new_status": "diverted"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_79",
        "instruction": "Execute inflight operations manager at LGA and the time is 2024-05-15T09:00:00Z.A Flight attendant ( CM003 ) falls ill during HAT002 (LGA -> PHX), impacting service coverage.You need to log the event and assign CM025 as the replacement and notify ops channel with the same message as the log event.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "UpdateCrewMemberStatus",
                "arguments": {
                    "crew_member_id": "CM003",
                    "new_status": "Sick Leave"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "crew_member_id": "CM003",
                    "flight_number": "HAT002"
                },
            },
            {
                "name": "GetCrewAssignments",
                "arguments": {
                    "crew_member_id": "CM025"
                },
            },
            {
                "name": "CreateCrewAssignment",
                "arguments": {
                    "flight_number": "HAT002",
                    "crew_member_id": "CM025",
                    "assigned_role": "Flight Attendant"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "flight_id": "HAT002",
                    "event_type": "Crew Replacement",
                    "details": "Last-minute crew replacement required for HAT002 on 2024-05-15.",
                    "event_timestamp_utc": "2024-05-15T09:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lga",
                    "message": "Last-minute crew replacement required for HAT002 on 2024-05-15."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_80",
        "instruction": "Execute night shift operations manager at MIA on 2024-05-14T22:00:00Z. Due to freezing conditions expected later in the night, flights HAT019 (MIA -> LAX) and HAT031 (MIA -> EWR)must depart one hour earlier than originally scheduled to avoid worsening weather. Update both the scheduled departure and arrival times (estimated) by moving them back by one hour.You need to log the event with message: 'Flight {flight_number} departure and arrival moved 1 hour earlier due to forecast freezing conditions.'Send notification to ops channel with the same message.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MIA"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT019",
                    "date": "2024-05-14"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT019",
                    "scheduled_departure_time_est": "14:00:00",
                    "scheduled_arrival_time_est": "19:00:00"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MIA",
                    "event_type": "SCHEDULE_CHANGE",
                    "details": "Flight HAT019 departure and arrival moved 1 hour earlier due to forecast freezing conditions.",
                    "event_timestamp_utc": "2024-05-14T22:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mia",
                    "message": "Flight HAT019 departure and arrival moved 1 hour earlier due to forecast freezing conditions."
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT031",
                    "date": "2024-05-14"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT031",
                    "scheduled_departure_time_est": "09:00:00",
                    "scheduled_arrival_time_est": "12:00:00"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MIA",
                    "event_type": "SCHEDULE_CHANGE",
                    "details": "Flight HAT031 departure and arrival moved 1 hour earlier due to forecast freezing conditions.",
                    "event_timestamp_utc": "2024-05-14T22:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mia",
                    "message": "Flight HAT031 departure and arrival moved 1 hour earlier due to forecast freezing conditions."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_81",
        "instruction": "Execute night shift operations manager at BOS on 2024-12-15T22:10:00Z. Due to sub-freezing temps and rapid icing risk on the runway, advance the last outbound bank ( HAT247 , HAT182 , HAT145 ) by 60 minutes. Move both departure time and arrival time one hour earlier for the affected flights.You need to log the event with message: 'Advanced last outbound bank by {minutes} minutes due to overnight icing risk. Flights: {flight_numbers}.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT247"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT247",
                    "date": "2024-12-15"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT247",
                    "scheduled_departure_time_est": "07:00:00",
                    "scheduled_arrival_time_est": "11:00:00"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT182"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT182",
                    "date": "2024-12-15"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT182",
                    "scheduled_departure_time_est": "03:00:00",
                    "scheduled_arrival_time_est": "06:30:00"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT145"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT145",
                    "date": "2024-12-15"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT145",
                    "scheduled_departure_time_est": "15:00:00",
                    "scheduled_arrival_time_est": "18:30:00"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "SCHEDULE_CHANGE",
                    "details": "Advanced last outbound bank by 60 minutes due to overnight icing risk. Flights: HAT247, HAT182, HAT145.",
                    "event_timestamp_utc": "2024-12-15T22:10:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_82",
        "instruction": "Execute night shift operations manager at BOS on 2024-12-15T22:10:00Z. Due to sub-freezing temps and rapid icing risk on the runway, You need to advance the last outbound bank ( HAT247 , HAT182 , HAT145 ) by 60 minutes. Move both departure time and arrival time one hour earlier for the affected flights.Log the event with message: 'Advanced last outbound bank by {minutes} minutes due to overnight icing risk. Flights: {flight_numbers}.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT247"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT247",
                    "date": "2024-12-15"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT247",
                    "scheduled_departure_time_est": "07:00:00",
                    "scheduled_arrival_time_est": "11:00:00"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT182"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT182",
                    "date": "2024-12-15"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT182",
                    "scheduled_departure_time_est": "03:00:00",
                    "scheduled_arrival_time_est": "06:30:00"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT145"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT145",
                    "date": "2024-12-15"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT145",
                    "scheduled_departure_time_est": "15:00:00",
                    "scheduled_arrival_time_est": "18:30:00"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "SCHEDULE_CHANGE",
                    "details": "Advanced last outbound bank by 60 minutes due to overnight icing risk. Flights: HAT247, HAT182, HAT145.",
                    "event_timestamp_utc": "2024-12-15T22:10:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_83",
        "instruction": "Execute network scheduling analyst at BOS on 2024-12-16T00:00:00Z. Based on historical performance, flights HAT182, HAT145, and HAT247 are chronically late by ~30 minutes even when operating 'on time'. Apply a proactive schedule adjustment (not an operational delay): increase their scheduled arrival time estimate by +30 minutes at the baseline schedule level.You need to log the event with message: 'Advanced arriving time by 30 minutes due to adjust correct arriving time. Flights: {flight_numbers}.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT182"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT182",
                    "scheduled_arrival_time_est": "08:00:00"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT145"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT145",
                    "scheduled_arrival_time_est": "20:00:00"
                },
            },
            {
                "name": "GetFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT247"
                },
            },
            {
                "name": "UpdateFlightScheduledTimes",
                "arguments": {
                    "flight_number": "HAT247",
                    "scheduled_departure_time_est": "08:00:00",
                    "scheduled_arrival_time_est": "12:30:00"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "SCHEDULE_CHANGE",
                    "details": "Advanced arriving time by 30 minutes due to adjust correct arriving time. Flights: HAT182, HAT145, HAT247.",
                    "event_timestamp_utc": "2024-12-16T00:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_84",
        "instruction": "Execute ops manager at MIA on 2024-05-22T14:30:00Z. Volcanic ash advisory southeast of Florida requires suspending MIA arrivals. You need to cancel JFK->MIA HAT209 , HAT014 and HAT060 for today and log the suspension.Log the event ar MIA airport with message: 'Volcanic ash advisory: {airport_code} arrivals suspended; {flight_numbers} canceled.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MIA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "JFK"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT209",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT014",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT060",
                    "date": "2024-05-22"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT209",
                        "HAT014",
                        "HAT060"
                    ],
                    "date": "2024-05-22",
                    "new_status": "canceled"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MIA",
                    "event_type": "Weather",
                    "details": "Volcanic ash advisory: MIA arrivals suspended; HAT209, HAT014, HAT060 canceled.",
                    "event_timestamp_utc": "2024-05-22T14:30:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_85",
        "instruction": "Execute station lead at LAS on 2024-05-27T09:10:00Z.Fuel farm contamination forces arrival shutdown. You need to cancel inbound HAT112 and HAT173 at-once and log at LAS .Log the event at LAS with message: 'Fuel contamination at LAS: inbounds {flight_numbers} canceled.' , notify the LAS ops with the same message.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT112",
                        "HAT173"
                    ],
                    "date": "2024-05-27",
                    "new_status": "canceled"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "event_type": "Fuel Disruption",
                    "details": "Fuel contamination at LAS: inbounds HAT112 , HAT173 canceled.",
                    "event_timestamp_utc": "2024-05-27T09:10:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-las",
                    "message": "Fuel contamination at LAS: inbounds HAT112 , HAT173 canceled."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_86",
        "instruction": "Execute ramp supervisor at SFO on 2024-05-27T17:40:00Z. Main baggage belt outage slows unloading. You need to mark HAT032 Delayed and log at SFO and PHX.Log the BAGGAGE_HANDLING with message in the related airports: 'SFO belt outage: HAT032 arrival handling delayed.' ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SFO"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT032",
                    "date": "2024-05-27"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT032"
                    ],
                    "date": "2024-05-27",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SFO",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "SFO belt outage: HAT032 arrival handling delayed.",
                    "event_timestamp_utc": "2024-05-27T17:40:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "BAGGAGE_HANDLING",
                    "details": "SFO belt outage: HAT032 arrival handling delayed.",
                    "event_timestamp_utc": "2024-05-27T17:40:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_87",
        "instruction": "Execute terminal ops at CLT on 2024-05-21T13:25:00Z. Terminal security sweep in progress; You need to set inbounds HAT215 and HAT270 from EWR as delayed.Log the operational event for origin and destination as 'Security sweep delay: HAT215 & HAT270 Delayed.' Notify operation channel at CLT with: 'CLT terminal sweep-HAT215 & HAT270 set Delayed. Hold gate changes until clear'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "CLT"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "EWR"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT215",
                    "date": "2024-05-21"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT270",
                    "date": "2024-05-21"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT215"
                    ],
                    "date": "2024-05-21",
                    "new_status": "delayed"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT270"
                    ],
                    "date": "2024-05-21",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_CLT",
                    "event_type": "Security Alert",
                    "details": "Security sweep delay: HAT215 & HAT270 Delayed.",
                    "event_timestamp_utc": "2024-05-21T13:25:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_EWR",
                    "event_type": "Security Alert",
                    "details": "Security sweep delay: HAT215 & HAT270 Delayed.",
                    "event_timestamp_utc": "2024-05-21T13:25:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-clt",
                    "message": "CLT terminal sweep-HAT215 & HAT270 set Delayed. Hold gate changes until clear."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_88",
        "instruction": "Execute NOC controller on 2024-05-23T15:10:00Z. VIP TFR around EWR requires diverting HAT179 and HAT181 to PHL; You need to set them Diverted and log at EWR/PHL.Notify operation channel in NOC with message: 'EWR VIP TFR-HAT179 & HAT181 divert to PHL. Coordinate gates/handling.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "EWR"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHL"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT179",
                        "HAT181"
                    ],
                    "date": "2024-05-23",
                    "new_status": "diverted"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_EWR",
                    "event_type": "Diversion",
                    "details": "Diversion for HAT181 on 2024-05-23 - landed at PHL.",
                    "event_timestamp_utc": "2024-05-23T15:10:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHL",
                    "event_type": "Diversion",
                    "details": "Diversion for HAT179 on 2024-05-23 - landed at PHL.",
                    "event_timestamp_utc": "2024-05-23T15:10:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-noc",
                    "message": "EWR VIP TFR-HAT179 & HAT181 divert to PHL. Coordinate gates/handling."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_89",
        "instruction": "Execute maintenance control at IAH on 2024-05-27T20:45:00Z. Cabin odor after push: You need to mark HAT180 and HAT072 to SFO Returned and log at IAH and SFO.Log the return event as 'Cabin odor-HAT180 & HAT072 Returned for checks.'Notify the operation channel at IAH with the same message",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "IAH"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SFO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT180",
                    "date": "2024-05-27"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT072",
                    "date": "2024-05-27"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT180"
                    ],
                    "date": "2024-05-27",
                    "new_status": "returned"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT072"
                    ],
                    "date": "2024-05-27",
                    "new_status": "returned"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_IAH",
                    "event_type": "Return",
                    "details": "Cabin odor-HAT180 & HAT072 Returned for checks.",
                    "event_timestamp_utc": "2024-05-27T20:45:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SFO",
                    "event_type": "Return",
                    "details": "Cabin odor-HAT180 & HAT072 Returned for checks.",
                    "event_timestamp_utc": "2024-05-27T20:45:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-iah",
                    "message": "Cabin odor-HAT180 & HAT072 Returned for checks."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_90",
        "instruction": "Execute ramp supervisor at MCO on 2024-05-25T18:00:00Z. Lightning within 3NM-ramp closed. You need to mark HAT153 and HAT157 Delayed and log closure.Use message 'Lightning alert-ramp closed. HAT153 & HAT157 Delayed. Resume after all-clear.' for notifying the operation channel and operational log. and ensure records have been reflected in the events.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT153",
                    "date": "2024-05-25"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT157",
                    "date": "2024-05-25"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT153",
                        "HAT157"
                    ],
                    "date": "2024-05-25",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "event_type": "Weather",
                    "details": "Lightning alert-ramp closed. HAT153 & HAT157 Delayed. Resume after all-clear.",
                    "event_timestamp_utc": "2024-05-25T18:00:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Lightning alert-ramp closed. HAT153 & HAT157 Delayed. Resume after all-clear."
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_MCO",
                    "date": "2024-05-25"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_91",
        "instruction": "Execute tower coordination at PHX on 2024-05-25T16:35:00Z.Runway incursion investigation; you job is to mark HAT214 from MCO and HAT216 from CLT Delayed.Log the Security Alert with message 'Runway incursion: HAT214 & HAT216 delayed pending clearance.'Notify the PHX,MCO,CLT operation channel with the same message.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "MCO"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "CLT"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT214",
                    "date": "2024-05-25"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT216",
                    "date": "2024-05-25"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT214"
                    ],
                    "date": "2024-05-25",
                    "new_status": "delayed"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT216"
                    ],
                    "date": "2024-05-25",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "Security Alert",
                    "details": "Runway incursion: HAT214 & HAT216 delayed pending clearance.",
                    "event_timestamp_utc": "2024-05-25T16:35:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-phx",
                    "message": "Runway incursion: HAT214 & HAT216 delayed pending clearance."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-mco",
                    "message": "Runway incursion: HAT214 & HAT216 delayed pending clearance."
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-clt",
                    "message": "Runway incursion: HAT214 & HAT216 delayed pending clearance."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_92",
        "instruction": "Execute crew scheduling at LAS on 2024-05-30T05:20:00Z. No legal crew before duty window closes; You need to cancel HAT175 and HAT266 from LAS to IAH.Log the Crew shortage with details as 'Crew legality exceeded; HAT175 & HAT266 canceled.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LAS"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "IAH"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT175",
                    "date": "2024-05-30"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT266",
                    "date": "2024-05-30"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT175",
                        "HAT266"
                    ],
                    "date": "2024-05-30",
                    "new_status": "canceled"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LAS",
                    "event_type": "Crew shortage",
                    "details": "Crew legality exceeded; HAT175 & HAT266 canceled.",
                    "event_timestamp_utc": "2024-05-30T05:20:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_93",
        "instruction": "Execute SEA ATC liaison on 2024-05-20T09:00:00Z. Low Visibility Procedures (LVP) are in effect at SEA. You need to set inbound flights HAT021 and HAT025 separately to Delayed, log the ground stop at SEA and at each flight\u2019s origin (LGA for HAT021, ORD for HAT025), log the weather event with 'Downline SEA LVP ground stop impacting HAT021, HAT025.' ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "SEA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ORD"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT021",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT025",
                    "date": "2024-05-20"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT021"
                    ],
                    "date": "2024-05-20",
                    "new_status": "delayed"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT025"
                    ],
                    "date": "2024-05-20",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_SEA",
                    "event_type": "Weather",
                    "details": "Downline SEA LVP ground stop impacting HAT021, HAT025.",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "Weather",
                    "details": "Downline SEA LVP ground stop impacting HAT021.",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ORD",
                    "event_type": "Weather",
                    "details": "Downline SEA LVP ground stop impacting HAT025.",
                    "event_timestamp_utc": "2024-05-20T09:00:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_94",
        "instruction": "Execute station ops at LGA on 2024-05-28T11:10:00Z. Gate power outage delays deplaning for two inbound flights. You need to set HAT087 and HAT091 to Delayed, log the issue at LGA, and notify ops with: 'Gate power outage; HAT087 & HAT091 marked Delayed.' and ensure records have been reflected in the events.",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "LGA"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT087",
                    "date": "2024-05-28"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT091",
                    "date": "2024-05-28"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT087",
                        "HAT091"
                    ],
                    "date": "2024-05-28",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "event_type": "Technical Issue",
                    "details": "Gate power outage; HAT087 & HAT091 marked Delayed.",
                    "event_timestamp_utc": "2024-05-28T11:10:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-lga",
                    "message": "Gate power outage; HAT087 & HAT091 marked Delayed."
                },
            },
            {
                "name": "EventsAtAirportOn",
                "arguments": {
                    "airport_id": "ARP_LGA",
                    "date": "2024-05-28"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_95",
        "instruction": "Execute IT liaison at BOS on 2024-05-28T07:45:00Z. A DCS outage is impacting check-in at BOS. You need to set HAT260 and HAT262 to delayed, log the disruption at BOS, and notify ops with: 'BOS DCS outage; HAT260 & HAT262 marked delayed.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT260",
                    "date": "2024-05-28"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT262",
                    "date": "2024-05-28"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT260"
                    ],
                    "date": "2024-05-28",
                    "new_status": "delayed"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT262"
                    ],
                    "date": "2024-05-28",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "Technical Issue",
                    "details": "BOS DCS outage; HAT260 & HAT262 marked delayed.",
                    "event_timestamp_utc": "2024-05-28T07:45:00Z"
                },
            },
            {
                "name": "SendUserNotification",
                "arguments": {
                    "channel_or_user_id": "ops-bos",
                    "message": "BOS DCS outage; HAT260 & HAT262 marked delayed."
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_96",
        "instruction": "Execute station ops at PHX on 2024-05-26T10:20:00Z. A TSA baggage screening backlog is impacting throughput. You need to set HAT081 and HAT085 to delayed, create a Security Alert operational event at PHX with details 'PHX TSA screening backlog; HAT081 & HAT085 marked delayed.', ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "PHX"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT081",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT085",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT081",
                        "HAT085"
                    ],
                    "date": "2024-05-26",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_PHX",
                    "event_type": "Security Alert",
                    "details": "PHX TSA screening backlog; HAT081 & HAT085 marked delayed.",
                    "event_timestamp_utc": "2024-05-26T10:20:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_97",
        "instruction": "Execute airfield ops at DEN on 2024-05-23T04:55:00Z. Ramp fuel spill closures are in effect. You need to set inbound flights HAT076 and HAT078 to canceled, create a Security Alert operational event at DEN with details 'DEN ramp fuel spill; HAT076 & HAT078 marked canceled.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "DEN"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT076",
                    "date": "2024-05-23"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT078",
                    "date": "2024-05-23"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT076",
                        "HAT078"
                    ],
                    "date": "2024-05-23",
                    "new_status": "canceled"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_DEN",
                    "event_type": "Security Alert",
                    "details": "DEN ramp fuel spill; HAT076 & HAT078 marked canceled.",
                    "event_timestamp_utc": "2024-05-23T04:55:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_98",
        "instruction": "Execute tower coordination at ATL on 2024-05-24T06:25:00Z. An unscheduled runway inspection is extending arrival spacing at ATL. You need to set HAT223 and HAT227 to delayed, create a Minor Delay operational event at ATL with details 'ATL runway inspection; HAT223 & HAT227 marked delayed.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "ATL"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT223",
                    "date": "2024-05-24"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT227",
                    "date": "2024-05-24"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT223",
                        "HAT227"
                    ],
                    "date": "2024-05-24",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_ATL",
                    "event_type": "Minor Delay",
                    "details": "ATL runway inspection; HAT223 & HAT227 marked delayed.",
                    "event_timestamp_utc": "2024-05-24T06:25:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_99",
        "instruction": "Execute crew desk at JFK on 2024-05-26T09:15:00Z. A cabin crew shortage requires a delay. You need to set HAT060 and HAT064 to delayed, create a Minor Delay operational event at JFK with details 'JFK crew shortage; HAT060 & HAT064 marked delayed.'",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "JFK"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT060",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT064",
                    "date": "2024-05-26"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT060",
                        "HAT064"
                    ],
                    "date": "2024-05-26",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_JFK",
                    "event_type": "Minor Delay",
                    "details": "JFK crew shortage; HAT060 & HAT064 marked delayed.",
                    "event_timestamp_utc": "2024-05-26T09:15:00Z"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": 0,
        "user_id": "task_100",
        "instruction": "Execute winter ops at BOS on 2024-05-29T23:10:00Z. A deicing queue backlog at BOS requires upstream departure holds. You need to set inbound flights HAT194 and HAT253 to delayed, create a Weather operational event at BOS with details 'BOS deicing backlog; HAT194 & HAT253 marked delayed.', ",
        "actions": [
            {
                "name": "GetAirportByCode",
                "arguments": {
                    "iata_code": "BOS"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT194",
                    "date": "2024-05-29"
                },
            },
            {
                "name": "LookupFlightDay",
                "arguments": {
                    "flight_number": "HAT253",
                    "date": "2024-05-29"
                },
            },
            {
                "name": "UpdateFlightStatusForDate",
                "arguments": {
                    "flight_numbers": [
                        "HAT194",
                        "HAT253"
                    ],
                    "date": "2024-05-29",
                    "new_status": "delayed"
                },
            },
            {
                "name": "CreateOperationalEvent",
                "arguments": {
                    "airport_id": "ARP_BOS",
                    "event_type": "Weather",
                    "details": "BOS deicing backlog; HAT194 & HAT253 marked delayed.",
                    "event_timestamp_utc": "2024-05-29T23:10:00Z"
                }
            }
        ],
        "outputs": []
    }
]
