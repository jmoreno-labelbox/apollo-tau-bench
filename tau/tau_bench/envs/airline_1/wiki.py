WIKI = """
"If an operation needs aircraft_id but only tail_number is supplied, obtain aircraft_id by calling get_aircraft_by_tail_number with the given tail_number.",
    "In book_reservation, assign the user ID as the portion of the email address preceding the '@' symbol. For instance, for emma.smith8074@example.com, use 'mia.li3818' as the user ID.",
    "The airport_id should consist of the IATA code with the prefix 'ARP_'. For instance, if the IATA code is JFK, the airport_id will be 'ARP_JFK'.",
    "The crew_member_id must begin with 'CM_', and the employee_code must begin with 'EMP_'.",
    "When a new operational event is created, the event ID (OE*) must be assigned deterministically by incrementing the highest existing event ID in the dataset. For example, if the current highest event ID is 'OE025', the next event must be assigned 'OE026'. Similarly, when a maintenance log is created, the log ID (ML*) must be generated deterministically by incrementing the highest existing log ID in the dataset. For example, if the highest current log ID is 'ML025', the next log must be assigned 'ML026'.",
    "When a crew assignment is created, the ID (AS_*) must be assigned deterministically by incrementing the current highest assignment ID present in the dataset. For instance, if the highest existing event ID is 'AS_025', the subsequent event must be assigned 'AS_026'. When generating a baggage claim, the claim ID must adhere to the deterministic format: 'BCLAIM_[reservation
"""
