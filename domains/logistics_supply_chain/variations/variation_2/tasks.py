# Copyright Sierra

tasks = [
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_001",
        "instruction": "\n        Handle the role of logistics planner in charge of managing incoming shipments.\n        Evaluate shipment SHIP-0004, ensuring the assigned carrier's operational status is verified.\n        Your responsibility is to obtain the shipment details and ascertain the active status of the designated carrier.\n        Should the carrier be inactive, it is essential to identify an alternative by accessing the list of active carriers, choosing the top-rated one, and updating the shipment with the change.\n        If multiple carriers have identical top ratings, choose the one with the superior on-time delivery percentage as the replacement.\n        After reassignment, make certain the shipment details accurately reflect the new carrier to uphold continuity in the supply chain process.\n    ",
        "actions": [
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "POCL"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetTopRatedCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "carrier_name": "Global Parcel Service",
                        "carrier_scac": "GPLS"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                }
            }
        ],
        "outputs": [
                "GPLS"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_002",
        "instruction": "\n            Coordinate a list of all active carriers in the system, organizing them by their average rating.\n            Determine the overall minimum of these carriers' average ratings.\n            For each carrier with a rating matching the overall minimum, update their profile by adding a new attribute called \"warning\" with the value \"Least Rated\".\n            Subsequently, examine the updated profiles of all carriers flagged as least rated, and return the scacs of pertinent carriers.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetTopRatedCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MTRL",
                    "updates": {
                        "warning": "Least Rated"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "PSLN",
                    "updates": {
                        "warning": "Least Rated"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "MTRL",
                        "PSLN"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"MTRL\",\n  \"PSLN\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_003",
        "instruction": "\n        As a supply chain analyst in charge of overseeing inbound logistics as of June 5, 2024, your objective is to identify all inbound shipments that are delayed, signified by arrival dates that have elapsed without marking them as arrived.\n        Generate this list and amend the status of each delayed shipment to \u201cDelayed.\n        \u201d After all relevant shipments are updated, concentrate on the last modified shipment and assess its carrier's status.\n        If the carrier remains active, further action is unnecessary.\n        In the event the carrier is inactive, identify the highest-rated active carrier by average rating.\n        If multiple carriers hold the top rating, opt for the one with superior on-time delivery percentage.\n        Amend the shipment's carrier to this leading carrier, and then retrieve the updated shipment details to verify all modifications are correctly applied.\n    ",
        "actions": [
            {
                "name": "GetDelayedShipments",
                "arguments": {
                    "today": "2024-06-05"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0014",
                    "updates": {
                        "status": "Delayed"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                }
            }
        ],
        "outputs": [
                "\"status\": \"Delayed\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_004",
        "instruction": "\n        Organize a list of all carriers that are currently active in the system.\n        Determine the overall minimum of these carriers' on-time delivery percentages.\n        For each carrier whose rating meets the overall minimum, adjust their profile by adding a new attribute called \"warning\" with the value \"Poor Delivery.\n        \" Following this, inspect the updated profiles of all carriers marked for poor delivery, followed by returning the scacs of the updated carriers.\n    ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MTRL",
                    "updates": {
                        "warning": "Poor Delivery"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "MTRL"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"MTRL\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_005",
        "instruction": "\n        Compile a list of all currently active carriers in the system and arrange them according to their average rating.\n        Identify the overall maximum of these carriers' average ratings.\n        For every carrier whose rating matches the overall maximum, enhance their record by adding a new attribute called \"highlight\" with the value \"Best Rated.\n        \" Conclusively, review the modified details of all carriers highlighted as best rated, and ultimately return the scacs of these updated carriers.\n    ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetTopRatedCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "DFC",
                    "updates": {
                        "highlight": "Best Rated"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "highlight": "Best Rated"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "DFC",
                        "GPLS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"DFC\",\n  \"GPLS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_006",
        "instruction": "\n            Handle the listing of all carriers currently active in the system.\n            Determine the overall maximum of their on-time delivery percentages.\n            For each carrier with a rating matching this overall maximum, modify their record by adding a new attribute titled \"highlight\" with the value \"Best Delivery.\n            \" Lastly, review the details of all carriers marked for best delivery.\n            Conclude by returning the scacs of the updated carriers.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "highlight": "Best Delivery"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "GPLS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"GPLS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_007",
        "instruction": "\n        Coordinate the monitoring of inventory integrity as a warehouse inventory coordinator.\n        Identify all inventory items with a damaged quantity greater than zero.\n        Once identified, update their records to mark them for review, ensuring they are flagged for further inspection or action.\n        After completing the updates, retrieve and review the details of one affected inventory record to confirm the changes.\n    ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0002",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0005",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0006",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0007",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0013",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0016",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0017",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0018",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0021",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0022",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0023",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0025",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                }
            }
        ],
        "outputs": [
                "\"status\": \"Under Review\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_008",
        "instruction": "\n        As a warehouse operations analyst, you are responsible for monitoring storage utilization.\n        Begin by retrieving the details of the owned warehouses.\n        Evaluate their current utilization percentages, and if any percentage is found to be below (not equal but only below) 60%, update the warehouse record to include a flag indicating it is underused.\n        After applying these updates, retrieve the warehouse details once more to ensure the flag has been correctly added.\n    ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "updates": {
                        "underused_flag": true
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                }
            }
        ],
        "outputs": [
                "\"underused_flag\": true"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_009",
        "instruction": "\n        Your role as a warehouse operations analyst involves monitoring storage utilization.\n        Start by retrieving details of the leased warehouses.\n        Check their current utilization percentages, and if any are found to be below (not equal but only below) 80%, update the warehouse record by including a flag to signify it is underused.\n        Once these updates have been made, retrieve the warehouse details again to verify that the flag has been correctly added.\n    ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Leased"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "underused_flag": true
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                }
            }
        ],
        "outputs": [
                "\"underused_flag\": true"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_010",
        "instruction": "\n        Acquire all outbound orders with a total value exceeding 100,000.\n        Determine if these orders have a priority level of \"High\" or not.\n        If the priority level is not high, alter their priority status to \u201cHigh\u201d for expedited processing.\n        Verify details of the updated orders.\n        Finally, report the ids of the revised orders.\n    ",
        "actions": [
            {
                "name": "GetHighValueOutboundOrders",
                "arguments": {
                    "min_value": 100000
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0002"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0007"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0009"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0013"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0015"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0016"
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0005",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0006",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0007",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0009",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0010",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0013",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0015",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0016",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0005"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0007"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0009"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0013"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0015"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0016"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "ORD-0005",
                        "ORD-0006",
                        "ORD-0007",
                        "ORD-0009",
                        "ORD-0010",
                        "ORD-0013",
                        "ORD-0015",
                        "ORD-0016"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"ORD-0005\",\n  \"ORD-0006\",\n  \"ORD-0007\",\n  \"ORD-0009\",\n  \"ORD-0010\",\n  \"ORD-0013\",\n  \"ORD-0015\",\n  \"ORD-0016\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_011",
        "instruction": "\n        As the logistics coordinator, your role is to oversee and handle shipment schedules.\n        Consider only shipments categorized under priority_level medium.\n        Access the shipment details and check their current status.\n        If any shipment is labeled as \u201cIn Transit,\u201d adjust the shipment's estimated arrival date by extending it by 3 days from the present expected arrival date.\n        Upon updating, verify the new expected_arrival_date to ensure the modification has been implemented.\n        Lastly, report the IDs of shipments where updates occurred.\n    ",
        "actions": [
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "priority_level",
                    "value": "Medium"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0005"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0017"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0018"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0001",
                    "updates": {
                        "expected_arrival_date": "2024-06-23"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0003",
                    "updates": {
                        "expected_arrival_date": "2024-06-18"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0005",
                    "updates": {
                        "expected_arrival_date": "2024-06-23"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0009",
                    "updates": {
                        "expected_arrival_date": "2024-06-19"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "updates": {
                        "expected_arrival_date": "2024-06-28"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0015",
                    "updates": {
                        "expected_arrival_date": "2024-06-20"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0018",
                    "updates": {
                        "expected_arrival_date": "2024-06-25"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0023",
                    "updates": {
                        "expected_arrival_date": "2024-06-09"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0025",
                    "updates": {
                        "expected_arrival_date": "2024-06-22"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0028",
                    "updates": {
                        "expected_arrival_date": "2024-07-04"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0005"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0018"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0023",
                        "SHIP-0025",
                        "SHIP-0028"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0001\",\n  \"SHIP-0003\",\n  \"SHIP-0005\",\n  \"SHIP-0009\",\n  \"SHIP-0011\",\n  \"SHIP-0015\",\n  \"SHIP-0018\",\n  \"SHIP-0023\",\n  \"SHIP-0025\",\n  \"SHIP-0028\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_012",
        "instruction": "\n            You need to assess the performance of current carriers operating with the service mode Air.\n            Initially, retrieve all carriers that are marked as active.\n            Among these, identify carriers that specifically operate using Air transport.\n            Determine the highest on-time delivery percentage and the top average rating for these air carriers.\n            Multiple carriers might meet these criteria.\n            If A and B achieve the highest on-time delivery percentage and B and C attain the highest average rating, consider all three for updates.\n            For each of these carriers, modify their record by adding a note with the text \"Best Performance by Air\".\n            Finally, provide the list of SCACs for all carriers whose records were updated with this note.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Air",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "SKEX",
                        "DLOG",
                        "DFC",
                        "SWDL",
                        "SCF",
                        "ALFS",
                        "GPLS",
                        "AAC",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "SKEX",
                        "DLOG",
                        "DFC",
                        "SWDL",
                        "SCF",
                        "ALFS",
                        "GPLS",
                        "AAC",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "notes": "Best Performance by Air"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "DFC",
                    "updates": {
                        "notes": "Best Performance by Air"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "GPLS",
                        "DFC"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"GPLS\",\n  \"DFC\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_013",
        "instruction": "\n        As the inventory control specialist, it is your responsibility to ensure product quality and compliance.\n        As of today's date, June 20, 2025, retrieve any inventory items that have surpassed their expiration date.\n        For each item found to be expired, update its status in the inventory system to \u201cExpired\u201d to reflect its actual condition.\n        After completing the updates, select one of these updated items to review its details and confirm the status change was properly executed.\n    ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2025-06-20"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "updates": {
                        "status": "Expired"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0008",
                    "updates": {
                        "status": "Expired"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Expired"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                }
            }
        ],
        "outputs": [
                "\"status\": \"Expired\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_014",
        "instruction": "\n            It is your task to assess the performance of active carriers operating with the service mode Sea.\n            Start by acquiring all carriers that are currently listed as active.\n            From there, pinpoint the carriers that specifically use the Sea mode of transport.\n            For these sea carriers, compute both the highest on-time delivery percentage and the top average rating.\n            There may be several carriers that fit these criteria.\n            If A and B reach the highest on-time delivery percentage and B and C obtain the highest average rating, consider all three carriers for updates.\n            For each of these outstanding carriers, change their record by appending a note with the phrase \"Best Performance by Sea\".\n            Finally, compile a list of the SCACs for all carriers that were updated with this note.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Sea",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "PSLN",
                        "SATL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "PSLN",
                        "SATL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "updates": {
                        "notes": "Best Performance by Sea"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "ALFS",
                    "updates": {
                        "notes": "Best Performance by Sea"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SKEX",
                        "ALFS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SKEX\",\n  \"ALFS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_015",
        "instruction": "\n                Your task is to evaluate the performance of active carriers operating with the service mode Truck.\n                First, gather all carriers that are recognized as active.\n                From this selection, filter for carriers that primarily operate with Truck transport.\n                Within these truck carriers, assess both the highest on-time delivery percentage and the top average rating.\n                Several carriers may fit these descriptors.\n                If A and B achieve the maximum on-time delivery percentage and B and C achieve the maximum average rating, include all three carriers for updates.\n                Update each of these high-performing carriers' records by inserting a note with the words \"Best Performance by Truck\".\n                Finally, deliver a list of the SCACs for all carriers whose records included this note.\n            ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Truck",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "SWDL",
                        "MTRL",
                        "ALFS",
                        "GPLS",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "SWDL",
                        "MTRL",
                        "ALFS",
                        "GPLS",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "notes": "Best Performance by Truck"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "GPLS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"GPLS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_016",
        "instruction": "\n        As the product data analyst, your task is to ensure correct storage classifications.\n        Start by obtaining the information of all products classified under \u201cPharmaceuticals.\n        \u201d Examine each product entry to assess whether refrigerated storage is needed.\n        For those requiring it, update the product record to include a \u201cCold Chain\u201d flag to reflect special handling needs.\n        Once updates are made, gather and verify the details of one of the updated products to ensure the changes took effect.\n    ",
        "actions": [
            {
                "name": "GetProductsByCategory",
                "arguments": {
                    "category": "Pharmaceuticals"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "refrigerated"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "updates": {
                        "cold_chain_flag": true
                    }
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-DRUG-S19",
                    "updates": {
                        "cold_chain_flag": true
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-DRUG-S19"
                }
            }
        ],
        "outputs": [
                "\"cold_chain_flag\": true"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_017",
        "instruction": "\n        As the inventory quality control analyst, your job is to oversee warehouse stock conditions.\n        Identify inventory items in warehouse WH-03 with any damaged quantity greater than zero.\n        Acquire these items and modify their status to \u201cUnder Review\u201d to start quality inspection processes.\n        Following the record updates, compute and present the total units marked as damaged among these items for supporting further actions.\n    ",
        "actions": [
            {
                "name": "GetInventoryByWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "list_of_ids": [
                        "INV-0002",
                        "INV-0014",
                        "INV-0017",
                        "INV-0021",
                        "INV-0025"
                    ]
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0002",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0017",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0021",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0025",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0002"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0021"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inventory",
                    "key": "inventory_id",
                    "value": "quantity_damaged",
                    "list_of_ids": [
                        "INV-0002",
                        "INV-0017",
                        "INV-0021",
                        "INV-0025"
                    ]
                }
            }
        ],
        "outputs": [
                "22"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_018",
        "instruction": "\n                Your responsibility is to assess the active carriers' performance operating in the Rail service mode.\n                Commence by collecting all carriers currently identified as active.\n                From this selection, single out carriers that operate particularly using the Rail mode of transport.\n                For these rail carriers, ascertain both the maximum on-time delivery percentage and the highest average rating.\n                Multiple carriers may align with these criteria.\n                If A and B match the max on-time delivery percentage and B and C match the max average rating, consider all three carriers for updates.\n                Update the records of each top-performing carrier by appending an attribute notes with the value \"Best Performance by Rail\".\n                Lastly, deliver a list comprising the SCACs of all carriers updated with this note.\n            ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Rail",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MTRL",
                        "GOCN",
                        "ALFS"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MTRL",
                        "GOCN",
                        "ALFS"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "SKEX",
                    "updates": {
                        "notes": "Best Performance by Rail"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "ALFS",
                    "updates": {
                        "notes": "Best Performance by Rail"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SKEX",
                        "ALFS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SKEX\",\n  \"ALFS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_019",
        "instruction": "\n                Your responsibility is to assess the active carriers' performance operating in the Parcel service mode.\n                Commence by collecting all carriers currently identified as active.\n                From this selection, single out carriers that operate particularly using the Parcel mode of transport.\n                For these parcel carriers, ascertain both the maximum on-time delivery percentage and the highest average rating.\n                Multiple carriers may align with these criteria.\n                If A and B match the max on-time delivery percentage and B and C match the max average rating, consider all three carriers for updates.\n                Update the records of each top-performing carrier by appending an attribute notes with the value \"Best Performance by Parcel\".\n                Lastly, deliver a list comprising the SCACs of all carriers updated with this note.\n            ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Parcel",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "SWDL",
                        "GPLS",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "SWDL",
                        "GPLS",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "notes": "Best Performance by Parcel"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "GPLS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"GPLS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_020",
        "instruction": "\n            In reviewing supplier compliance and performance, for both a particular case and broader preferred supplier evaluation, begin by acquiring supplier details for supplier ID SUP-1015.\n            Determine if this supplier is designated as preferred and possesses at least one certification.\n            Should either condition not be met, modify the supplier's record by including a compliance_alert attribute to indicate non-compliance.\n            After updating, report the supplier's certifications, relationship_status, and the newly added compliance_alert.\n            Then, examine all preferred suppliers within the system that also hold at least one certification.\n            Identify the supplier(s) with the top performance rating among this group.\n            If several suppliers share this peak performance rating, encompass all in the evaluation.\n            Return the list of supplier IDs for these versatile, top-rated, preferred, and certified suppliers.\n        ",
        "actions": [
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1015"
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1015",
                    "updates": {
                        "compliance_alert": true
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1015"
                },
            },
            {
                "name": "GetPreferredSuppliers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCertifiedSuppliers",
                "arguments": {
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1005",
                        "SUP-1010",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019",
                        "SUP-1029"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "supplier_master",
                    "key": "supplier_id",
                    "value": "performance_rating",
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1005",
                        "SUP-1010",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019",
                        "SUP-1029"
                    ]
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1010",
                        "SUP-1016",
                        "SUP-1029"
                    ]
                }
            }
        ],
        "outputs": [
                "[\"SUP-1002\", \"SUP-1010\", \"SUP-1016\", \"SUP-1029\"]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_021",
        "instruction": "\n        As a logistics planner, you are tasked with optimizing carrier assignments for inbound shipments.\n        Start by checking the shipment with ID SHIP-0021 to verify if the assigned carrier is currently active.\n        Should the carrier be active, proceed to identify the active carrier with the best on-time delivery percentage.\n        Reassign the shipment to this leading carrier.\n        Upon completion of the update, confirm the modifications by retrieving and reviewing the updated shipment details.\n    ",
        "actions": [
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "updates": {
                        "carrier_scac": "GPLS",
                        "carrier_name": "Global Parcel Service"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                }
            }
        ],
        "outputs": [
                "\"carrier_name\": \"Global Parcel Service\"",
                "\"carrier_scac\": \"GPLS\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_022",
        "instruction": "\n                As a logistics coordinator, your responsibility is to manage delayed inbound shipments.\n                Start by pinpointing all inbound shipments presently marked as delayed and review their specifics.\n                For each shipment, establish the associated warehouse.\n                Next, evaluate the inventory stored within those warehouses.\n                Among this inventory, find the one with the minimal number of damaged units.\n                Select the shipment connected to the warehouse linked with this inventory.\n                After pinpointing, change the status of that inbound shipment to \"Planned\" to reschedule its processing.\n            ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Delayed"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0022"
                },
            },
            {
                "name": "GetInventoryByWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetInventoryByWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "list_of_ids": [
                        "INV-0015",
                        "INV-0018",
                        "INV-0016",
                        "INV-0020"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "inventory",
                    "key": "inventory_id",
                    "value": "quantity_damaged",
                    "list_of_ids": [
                        "INV-0015",
                        "INV-0018",
                        "INV-0016",
                        "INV-0020"
                    ]
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0018"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "status": "Planned"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                }
            }
        ],
        "outputs": [
                "\"status\": \"Planned\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_023",
        "instruction": "\n        Your role as a shipment analyst is to ensure the reliability of carrier assignments for outbound orders.\n        Initiate by reviewing all outbound orders currently marked as \u201cShipped\u201d and check if their assigned carriers are active.\n        For any order linked to an inactive carrier, determine the top-rated active carrier from the available list.\n        If two or more carriers share the top average rating, select the one with the superior on-time delivery percentage.\n        Update the affected orders with the information of this top-rated carrier.\n        Once all updates are finalized, confirm the modifications by reviewing the updated order data.\n    ",
        "actions": [
            {
                "name": "GetOrdersByStatus",
                "arguments": {
                    "status": "Shipped"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0003"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0006"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0007"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0012"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "SWDL",
                        "NSTS",
                        "OCBR",
                        "KCSM"
                    ]
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetTopRatedCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0012",
                    "updates": {
                        "carrier_scac": "GPLS",
                        "carrier_name": "Global Parcel Service"
                    }
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0012"
                }
            }
        ],
        "outputs": [
                "\"carrier_name\": \"Global Parcel Service\"",
                "\"carrier_scac\": \"GPLS\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_024",
        "instruction": "\n                As a warehouse manager, you are responsible for assessing storage conditions and inventory quality.\n                Begin your task by reviewing all expired inventory items that also have a damaged quantity exceeding 0, using 2025-06-20 as today's date for determining expiry.\n                For each of these inventory items, change the status to \"Replacement Needed\" and find the associated warehouse.\n                For each associated warehouse, update its status to \"Needs Expansion\".\n                Lastly, verify the updates by examining the details of the affected inventories and warehouses.\n                Return the list of updated inventories.\n            ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2025-06-20"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "list_of_ids": [
                        "INV-0003",
                        "INV-0008",
                        "INV-0024"
                    ]
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "updates": {
                        "status": "Replacement Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Replacement Needed"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "updates": {
                        "status": "Needs Expansion"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "Needs Expansion"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0003",
                        "INV-0024"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0003\",\n  \"INV-0024\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_025",
        "instruction": "\n        As a supply chain analyst, your duty is to evaluate outbound orders valued over $100,000 that necessitate temperature control.\n        For each order, check if the products are categorized as hazardous, fragile, or both.\n        If an order includes hazardous products, append the note \"BEWARE HAZARDOUS\" to its extra notes.\n        If it includes fragile products, append \"BEWARE FRAGILE.\n        \" For orders that are both hazardous and fragile, append the combined note \"BEWARE HAZARDOUS & FRAGILE.\n        \" After these updates, retrieve and verify the details of the updated orders to ensure the adjustments.\n    ",
        "actions": [
            {
                "name": "GetHighValueOutboundOrders",
                "arguments": {
                    "min_value": 100000
                },
            },
            {
                "name": "GetOrdersRequiringTemperatureControl",
                "arguments": {
                    "list_of_ids": [
                        "ORD-0002",
                        "ORD-0005",
                        "ORD-0006",
                        "ORD-0007",
                        "ORD-0008",
                        "ORD-0009",
                        "ORD-0010",
                        "ORD-0011",
                        "ORD-0013",
                        "ORD-0015",
                        "ORD-0016"
                    ]
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0011",
                    "updates": {
                        "extra_note": "BEWARE FRAGILE"
                    }
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                }
            }
        ],
        "outputs": [
                "\"extra_note\": \"BEWARE FRAGILE\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_026",
        "instruction": "\n        As a procurement specialist tasked with supplier qualifications oversight, examine the preferred suppliers roster to pinpoint those without valid ISO certifications.\n        For any supplier missing this certification, adjust their certification_status to \"ISO Certification Pending.\n        \" Once you've made these adjustments, fetch and verify the details for one of the amended suppliers to confirm the updates were applied accurately.\n    ",
        "actions": [
            {
                "name": "GetPreferredSuppliers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCertifiedSuppliers",
                "arguments": {
                    "certification": "ISO",
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1005",
                        "SUP-1010",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019",
                        "SUP-1029"
                    ]
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1005",
                    "updates": {
                        "certification_status": "ISO Certification Pending"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "updates": {
                        "certification_status": "ISO Certification Pending"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1029",
                    "updates": {
                        "certification_status": "ISO Certification Pending"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1029"
                }
            }
        ],
        "outputs": [
                "\"certification_status\": \"ISO Certification Pending\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_027",
        "instruction": "\n        Serving as an inventory controller focused on maintaining stock quality in warehouses, on May 25, 2025, evaluate all warehouses holding expired inventory items.\n        For each such warehouse, change its status to \u201cRestock Needed\u201d and set all expired inventory to \u201cOn Hold\u201d to stop further use.\n        After executing these updates, fetch and review the inventory details to verify the status changes are correctly enacted.\n    ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2025-05-25"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "updates": {
                        "stock_status": "On Hold"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "stock_status": "On Hold"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "updates": {
                        "status": "Restock Needed"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "Restock Needed"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                }
            }
        ],
        "outputs": [
                "\"stock_status\": \"On Hold\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_028",
        "instruction": "\n                As a shipment auditor, your role is to ensure compliance of carriers handling inbound shipments.\n                Initiate by examining all inbound shipments labeled as \"In Transit.\n                \"\n                For each one, confirm if the designated carrier is still active.\n                Identify the active carrier with the top average rating.\n                Check all shipments to find the one linked to this carrier and annotate those shipments with \"Best Carrier.\n                \"\n                After handling all relevant shipments, document the top average rating.\n            ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "In Transit"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0005"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0008"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0012"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0018"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0024"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0026"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "DLOG",
                        "MEDL",
                        "MTRL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "SATL",
                        "NAC"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "DLOG",
                        "MEDL",
                        "MTRL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "SATL",
                        "NAC"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0014",
                    "updates": {
                        "notes": "Best Carrier"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0023",
                    "updates": {
                        "notes": "Best Carrier"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                }
            }
        ],
        "outputs": [
                "4.9"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_029",
        "instruction": "\n                In your role as a product manager reviewing pharmaceutical storage needs, first, obtain a list of products requiring refrigeration.\n                Analyze the details, focusing on their weight specifically.\n                Determine the product with the smallest weight.\n                Upon identification, append a note labeled \"LOW WEIGHT PRODUCT\" to this product to emphasize its lightness.\n                Lastly, review and validate the updated product details.\n            ",
        "actions": [
            {
                "name": "GetProductsByCategory",
                "arguments": {
                    "category": "Pharmaceuticals"
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "refrigerated",
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "PHRM-DRUG-S19"
                    ]
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "product_master",
                    "key": "sku",
                    "value": "weight_kg",
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "PHRM-DRUG-S19"
                    ]
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "updates": {
                        "notes": "LOW WEIGHT PRODUCT"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                }
            }
        ],
        "outputs": [
                "\"sku\": \"PHRM-VACC-D4\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_030",
        "instruction": "\n                As an inventory specialist, your task is to manage damaged stock.\n                Start by identifying all inventory entries where the damaged quantity exceeds 0.\n                For each of these, revise the status attribute to \"Pending Restock\" to denote pending resolution or replacement.\n                After the updates, check the details of the inventory items to assure the modifications are accurately applied.\n                Finally, compile and return the updated inventory IDs.\n            ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                {}
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0002",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0005",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0006",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0007",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0013",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0016",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0017",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0018",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0021",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0022",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0023",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0025",
                    "updates": {
                        "status": "Pending Restock"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0002"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0006"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0007"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0013"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0018"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0021"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0022"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0001",
                        "INV-0002",
                        "INV-0003",
                        "INV-0005",
                        "INV-0006",
                        "INV-0007",
                        "INV-0010",
                        "INV-0013",
                        "INV-0015",
                        "INV-0016",
                        "INV-0017",
                        "INV-0018",
                        "INV-0020",
                        "INV-0021",
                        "INV-0022",
                        "INV-0023",
                        "INV-0024",
                        "INV-0025"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0001\",\n  \"INV-0002\",\n  \"INV-0003\",\n  \"INV-0005\",\n  \"INV-0006\",\n  \"INV-0007\",\n  \"INV-0010\",\n  \"INV-0013\",\n  \"INV-0015\",\n  \"INV-0016\",\n  \"INV-0017\",\n  \"INV-0018\",\n  \"INV-0020\",\n  \"INV-0021\",\n  \"INV-0022\",\n  \"INV-0023\",\n  \"INV-0024\",\n  \"INV-0025\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_031",
        "instruction": "\n                You are a carrier analyst.\n                Your responsibility is to initiate by accessing the details of shipment SHIP-0004 and determine the designated carrier.\n                Verify if this carrier is presently active.\n                In case the carrier is not active, continue to search for an active carrier that utilizes the same mode of transport and possesses the highest average rating among those available.\n                If two or more carriers share the highest average rating, select the carrier among them with the highest on-time delivery percentage.\n                Upon identification, update the inbound shipment to allocate this top-rated active carrier.\n            ",
        "actions": [
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "POCL"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "carrier_scac": "ALFS",
                        "carrier_name": "Alpine Freight Solutions"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                }
            }
        ],
        "outputs": [
                "\"carrier_scac\": \"ALFS\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_032",
        "instruction": "\n                As an inventory manager, start by finding all warehouses with inventory records containing damaged items.\n                Among these warehouses, ascertain which one exhibits the lowest current utilization percentage.\n                Once identified, update that warehouse by adding an attribute note with the value \"Lowest Utilization Percent\" to flag it for operational review.\n            ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0002"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0006"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0007"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0013"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0018"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0021"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0022"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "warehouses",
                    "key": "warehouse_id",
                    "value": "current_utilization_percentage",
                    "list_of_ids": [
                        "WH-01",
                        "WH-02",
                        "WH-03",
                        "WH-04",
                        "WH-05",
                        "WH-07",
                        "WH-08",
                        "WH-09",
                        "WH-10",
                        "WH-12",
                        "WH-14",
                        "WH-15"
                    ]
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "updates": {
                        "note": "Lowest Utilization Percent"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                }
            }
        ],
        "outputs": [
                "\"note\": \"Lowest Utilization Percent\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_033",
        "instruction": "\n                You are a product compliance officer.\n                Commence by locating all hazardous products listed in the inventory.\n                Examine each of these products to confirm whether their storage requirements include the term \"hazmat\".\n                For any product where this requirement is absent or incorrect, update the product record by adding a notes attribute with the value \"BEWARE HAZMAT\" to ensure proper handling protocols are followed.\n                After updating, assess the details of the affected products.\n                Check the inventories associated with these products and verify that those inventories have quantities available.\n                Ultimately, return the list of SKUs of all products that were updated.\n            ",
        "actions": [
            {
                "name": "GetHazmatProducts",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "hazmat",
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "CHEM-SOLV-K11",
                        "TECH-BATT-Q17",
                        "ELEC-SMART-W23"
                    ]
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "updates": {
                        "notes": "BEWARE HAZMAT"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "updates": {
                        "notes": "BEWARE HAZMAT"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "PHRM-VACC-D4"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "ELEC-SMART-W23"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "ELEC-SMART-W23"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"PHRM-VACC-D4\",\n  \"ELEC-SMART-W23\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_034",
        "instruction": "\n        As a shipment coordinator, your duty is to manage inbound shipments with a status of \u201cDelayed.\n        \u201d Examine all such shipments and identify any that are assigned to inactive carriers.\n        For each affected shipment, reassign it to an active carrier to ensure timely handling.\n        After completing the reassignments, obtain and examine the details of the updated shipments to confirm that the changes have been applied correctly.\n    ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Delayed"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0022"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "POCL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "carrier_scac": "GOCN",
                        "carrier_name": "Global Ocean Carriers"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                }
            }
        ],
        "outputs": [
                "\"carrier_scac\": \"GOCN\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_035",
        "instruction": "\n            As a supplier relations manager, scrutinize preferred suppliers and verify their certification status by reviewing details.\n            If preferred suppliers lack ISO certifications, update them with the attribute note \"ISO certification required\".\n            Among preferred suppliers with certifications \"ISO\",\n            Identify the supplier with the least standard lead time days.\n            Update the supplier with the attribute note \"Least Standard Lead Time Days\".\n        ",
        "actions": [
            {
                "name": "GetPreferredSuppliers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1002"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1016"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1019"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1029"
                },
            },
            {
                "name": "GetCertifiedSuppliers",
                "arguments": {
                    "certification": "ISO",
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1005",
                        "SUP-1010",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019",
                        "SUP-1029"
                    ]
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1005",
                    "updates": {
                        "note": "ISO certification required"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "updates": {
                        "note": "ISO certification required"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1029",
                    "updates": {
                        "note": "ISO certification required"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1029"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "supplier_master",
                    "key": "supplier_id",
                    "value": "standard_lead_time_days",
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019"
                    ]
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1019",
                    "updates": {
                        "note": "Least Standard Lead Time Days"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1019"
                }
            }
        ],
        "outputs": [
                "\"supplier_id\": \"SUP-1019\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_036",
        "instruction": "\n        As a warehouse replenishment officer, handle the identification of all inventory with an available quantity less than 100, ensuring there is no damaged stock (quantity_damaged == 0).\n        Such items must be flagged for replenishment by updating their status to \u201cLOW STOCK\u201d.\n        After applying updates, verify a selection of them and ultimately return the ids of the inventory marked as LOW STOCK.\n    ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "less_than_threshold": "True",
                    "threshold": 1
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0008"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0009"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0012"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0014"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0019"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0009",
                    "updates": {
                        "status": "LOW STOCK"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0014",
                    "updates": {
                        "status": "LOW STOCK"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0009"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0014"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0009",
                        "INV-0014"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0009\",\n  \"INV-0014\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_037",
        "instruction": "\n            Taking on the role of a warehouse replenishment officer, your task is to pinpoint all inventory with an available quantity below 100 and damaged stock less than 10.\n            These items should be identified for replenishment by setting their status to \u201cLOW STOCK\u201d.\n            When the updates are completed, check a few and then provide the ids of the inventory noted as LOW STOCK.\n        ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "less_than_threshold": "True",
                    "threshold": 10
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0002"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0006"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0008"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0009"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0012"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0013"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0014"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0018"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0019"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0021"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0022"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0009",
                    "updates": {
                        "status": "LOW STOCK"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0014",
                    "updates": {
                        "status": "LOW STOCK"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0009"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0014"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0009",
                        "INV-0014"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0009\",\n  \"INV-0014\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_038",
        "instruction": "\n                As a warehouse operations manager, start by observing all warehouses that currently contain any inventory items with damage.\n                Identify warehouses where at least one inventory item has a damaged quantity greater than zero.\n                Modify the status of these warehouses to \"Attention Required\" to signal the necessity for inspection or corrective measures.\n                Lastly, review and confirm all updated warehouse details to ensure that status changes have been accurately implemented.\n            ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0002"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0006"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0007"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0013"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0018"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0021"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0022"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-08",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "status": "Attention Required"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "WH-01",
                        "WH-02",
                        "WH-03",
                        "WH-04",
                        "WH-05",
                        "WH-07",
                        "WH-08",
                        "WH-09",
                        "WH-10",
                        "WH-12",
                        "WH-14",
                        "WH-15"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"WH-01\",\n  \"WH-02\",\n  \"WH-03\",\n  \"WH-04\",\n  \"WH-05\",\n  \"WH-07\",\n  \"WH-08\",\n  \"WH-09\",\n  \"WH-10\",\n  \"WH-12\",\n  \"WH-14\",\n  \"WH-15\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_039",
        "instruction": "\n            Acting as a product manager, locate products requiring \"refrigerated\" storage conditions while ensuring their lifecycle status is active.\n            Assess the inventory associated with these products, and if the quantity damaged exceeds 0, append attribute notes \"Replacement Required\".\n            Determine the maximum unit price among these products.\n        ",
        "actions": [
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "refrigerated"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-FLWR-X24"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "PHRM-DRUG-S19"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0019"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "FOOD-FLWR-X24"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "notes": "Replacement Required"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "product_master",
                    "key": "sku",
                    "value": "unit_price",
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "PHRM-DRUG-S19",
                        "FOOD-FLWR-X24"
                    ]
                }
            }
        ],
        "outputs": [
                "\"sku\": \"PHRM-DRUG-S19\"",
                "\"unit_price\": 1800.0"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_040",
        "instruction": "\n                You must oversee the transfer of 300 units from inventory INV-0025 to an alternate one due to a problem with the original stock.\n                Start by confirming that the source inventory possesses at least 300 units available.\n                Then, identify another inventory bearing the same SKU but a distinct ID and review its present quantity.\n                Deduct 300 units from the source and add them to the destination inventory.\n                Add notes to both inventories regarding the changes so that employees could later adjust the total value.\n                The total value corresponding to 300 units should be subtracted from the source inventory, so add the note \"300 units removed, total value change pending\".\n                Similarly, the total value for 300 units should be included in the destination inventory, prompting the note \"300 units added, total value change pending\".\n                Finally, verify that the updates are accurately reflected in both inventories and return the current quantity available in the destination inventory.\n            ",
        "actions": [
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0025",
                    "updates": {
                        "quantity_on_hand": 7700,
                        "quantity_available": 7700
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "updates": {
                        "quantity_on_hand": 15300,
                        "quantity_available": 12800
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0025",
                    "updates": {
                        "note": "300 units removed, total value change pending"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0001",
                    "updates": {
                        "note": "300 units added, total value change pending"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                }
            }
        ],
        "outputs": [
                "12800"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_041",
        "instruction": "\n            As an order quality auditor, your task is to handle orders requiring temperature-controlled transport.\n            Verify that assigned carriers fulfill these criteria and remain active.\n            Distinguish between active and inactive assigned carriers within these orders.\n            Substitute inactive carriers with the highest rated active carriers for these orders.\n            If there's only one active carrier, you can skip checking for the highest rating.\n            Update orders with inactive carriers by assigning them to a qualified top-rated active carrier based on average rating.\n            Eventually, inspect the details of the modified orders and provide the list of those updated.\n        ",
        "actions": [
            {
                "name": "GetOrdersRequiringTemperatureControl",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0004"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "SWDL",
                        "LTMG",
                        "SAAW"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0008",
                    "updates": {
                        "carrier_scac": "SWDL",
                        "carrier_name": "SwiftDelivery"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0011",
                    "updates": {
                        "carrier_scac": "SWDL",
                        "carrier_name": "SwiftDelivery"
                    }
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "ORD-0008",
                        "ORD-0011"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"ORD-0008\",\n  \"ORD-0011\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_042",
        "instruction": "\n            As an inventory replenishment coordinator, your role is to locate expired inventory while assuming today's date is \"2026-07-20.\n            \"\n            Mark inventory in need of replenishment with 'notes' stating 'Replenishment Needed.\n            '\n            After this step, inspect the details of the updated inventory.\n            Provide the list of ids corresponding to the updated inventory.\n        ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2026-07-20"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0003",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0004",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0008",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0011",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0019",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0022",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "notes": "Replenishment Needed"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0008"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0019"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0022"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0003",
                        "INV-0004",
                        "INV-0008",
                        "INV-0011",
                        "INV-0019",
                        "INV-0022",
                        "INV-0024"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0003\",\n  \"INV-0004\",\n  \"INV-0008\",\n  \"INV-0011\",\n  \"INV-0019\",\n  \"INV-0022\",\n  \"INV-0024\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_043",
        "instruction": "\n        You are a supplier compliance officer in charge of checking the certification status of preferred suppliers for IEC compliance.\n        Pinpoint suppliers with expired or missing IEC certifications, and adjust their certification_status to \"Compliance Review\" to indicate the need for further action.\n        After executing these updates, fetch and assess the details of one updated supplier to ensure the changes are accurately reflected.\n    ",
        "actions": [
            {
                "name": "GetPreferredSuppliers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCertifiedSuppliers",
                "arguments": {
                    "certification": "IEC",
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1005",
                        "SUP-1010",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019",
                        "SUP-1029"
                    ]
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1002",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1005",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1010",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1013",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1016",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1019",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1029",
                    "updates": {
                        "certification_status": "Compliance Review"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1029"
                }
            }
        ],
        "outputs": [
                "\"certification_status\": \"Compliance Review\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_044",
        "instruction": "\n        Your duty as a warehouse performance analyst involves monitoring levels of inventory damage.\n        Detect any inventory items with counts exceeding 100 damaged goods and monitor the warehousing locations of these items.\n        For any warehouse that matches this condition, annotate it with a note indicating \u201cHigh Damaged Goods.\n        \u201d Once these updates are applied, examine and confirm the details of one of the highlighted warehouses to validate the note's presence.\n    ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 100
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "notes": "High Damaged Goods."
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "updates": {
                        "notes": "High Damaged Goods."
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "notes": "High Damaged Goods."
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "notes": "High Damaged Goods."
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                }
            }
        ],
        "outputs": [
                "\"notes\": \"High Damaged Goods.\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_045",
        "instruction": "\n            In the capacity of a product quality analyst, identify products marked as hazardous and evaluate each one individually.\n            If there are no storage requirements regarding hazmat class, append notes saying \"HAZMAT SPECIFICATION REQUIRED.\n            \"\n            At the end, review the details of the updated products and compile the list of SKUs for these products.\n        ",
        "actions": [
            {
                "name": "GetHazmatProducts",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "updates": {
                        "notes": "HAZMAT SPECIFICATION REQUIRED"
                    }
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "updates": {
                        "notes": "HAZMAT SPECIFICATION REQUIRED"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "ELEC-SMART-W23"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"PHRM-VACC-D4\",\n  \"ELEC-SMART-W23\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_046",
        "instruction": "\n            You are a shipment officer.\n            Examine inbound shipments marked as Planned.\n            Ensure the assigned carriers are operational.\n            Determine the highest average rating among the carriers.\n            Modify all relevant planned shipments to use the carrier with the best rating.\n            The goal is to select the optimal carrier for the planned shipments.\n            Provide the list of IDs for the shipments that were updated.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Planned"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "DFC",
                        "SCF",
                        "SKEX",
                        "EAC",
                        "NSC",
                        "ANAF"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "DFC",
                        "SCF",
                        "SKEX",
                        "EAC",
                        "NSC",
                        "ANAF"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0016",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0027",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0029",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0010",
                        "SHIP-0016",
                        "SHIP-0019",
                        "SHIP-0027",
                        "SHIP-0029"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0010\",\n  \"SHIP-0016\",\n  \"SHIP-0019\",\n  \"SHIP-0027\",\n  \"SHIP-0029\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_047",
        "instruction": "\n            You are a shipment officer.\n            Analyze inbound shipments labeled as Planned.\n            Verify that the assigned carriers have active status.\n            Identify the top insurance coverage limit among the carriers.\n            Adjust all these planned shipments, except the one with the carrier having the highest insurance coverage, to use the leading carrier in terms of insurance coverage.\n            The aim is to employ the best carrier for the planned shipments.\n            Furnish the list of IDs for the updated shipments.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Planned"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "DFC",
                        "SCF",
                        "SKEX",
                        "EAC",
                        "NSC",
                        "ANAF"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "insurance_details",
                    "value2": "coverage_limit_usd",
                    "list_of_ids": [
                        "DFC",
                        "SCF",
                        "SKEX",
                        "EAC",
                        "NSC",
                        "ANAF"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "SKEX",
                    "list_of_ids": [
                        "SHIP-0006",
                        "SHIP-0010",
                        "SHIP-0016",
                        "SHIP-0019",
                        "SHIP-0027",
                        "SHIP-0029",
                        "SHIP-0030"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0006",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0027",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0029",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0030",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0006",
                        "SHIP-0010",
                        "SHIP-0019",
                        "SHIP-0027",
                        "SHIP-0029",
                        "SHIP-0030"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0006\",\n  \"SHIP-0010\",\n  \"SHIP-0019\",\n  \"SHIP-0027\",\n  \"SHIP-0029\",\n  \"SHIP-0030\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_048",
        "instruction": "\n            You are a shipment officer.\n            Inspect inbound shipments having Planned status.\n            Check that assigned carriers are currently active.\n            Ascertain the highest on-time delivery percentage from among the carriers.\n            Revise all these planned shipments to utilize the carrier with the leading on-time delivery percentage.\n            The purpose is to apply the best carrier for the planned shipments.\n            Present the list of IDs for the shipments that have been updated.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Planned"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "DFC",
                        "SCF",
                        "SKEX",
                        "EAC",
                        "NSC",
                        "ANAF"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "DFC",
                        "SCF",
                        "SKEX",
                        "EAC",
                        "NSC",
                        "ANAF"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0010",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0016",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0019",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0027",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0029",
                    "updates": {
                        "carrier_scac": "DFC",
                        "carrier_name": "Desert Falcon Cargo"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0010",
                        "SHIP-0016",
                        "SHIP-0019",
                        "SHIP-0027",
                        "SHIP-0029"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0010\",\n  \"SHIP-0016\",\n  \"SHIP-0019\",\n  \"SHIP-0027\",\n  \"SHIP-0029\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_049",
        "instruction": "\n            You are a warehouse audit specialist.\n            Evaluate inventory with damage counts exceeding 50.\n            Analyze warehouse details of these damaged inventories to verify if their utilization percentage surpasses 50%.\n            Subsequently, change the warehouse status to 'Audit Completed' once reviewed.\n            Finally, identify the least number of damaged quantities from the inventories reviewed.\n            The aim is to determine a better threshold for what constitutes damaged inventory.\n        ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 50
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "status": "Audit Completed"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "updates": {
                        "status": "Audit Completed"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "status": "Audit Completed"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "Audit Completed"
                    }
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "inventory",
                    "key": "inventory_id",
                    "value": "quantity_damaged",
                    "list_of_ids": [
                        "INV-0010",
                        "INV-0015",
                        "INV-0020",
                        "INV-0024"
                    ]
                }
            }
        ],
        "outputs": [
                "\"quantity_damaged\": 120"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_050",
        "instruction": "\n            You are an orders management officer.\n            Locate all outbound orders necessitating temperature control.\n            Examine the specifics of these outbound orders.\n            Verify whether these orders are classified as hazmat.\n            Focus on orders that are non-hazmat.\n            Discover the maximum and minimum temperature considerations for these orders.\n            If the difference between maximum and minimum temperatures is less than 10,\n            tag these orders with the note \"Could be Grouped Together\".\n            Finally, review the information of these amended orders and supply the list of IDs for these updated orders.\n        ",
        "actions": [
            {
                "name": "GetOrdersRequiringTemperatureControl",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0004"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "outbound_orders",
                    "key": "order_id",
                    "value": "temperature_celsius",
                    "list_of_ids": [
                        "ORD-0004",
                        "ORD-0008",
                        "ORD-0011"
                    ]
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0004",
                    "updates": {
                        "notes": "Could be Grouped Together"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0008",
                    "updates": {
                        "notes": "Could be Grouped Together"
                    }
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0011",
                    "updates": {
                        "notes": "Could be Grouped Together"
                    }
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0004"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0008"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0011"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "ORD-0004",
                        "ORD-0008",
                        "ORD-0011"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"ORD-0004\",\n  \"ORD-0008\",\n  \"ORD-0011\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_051",
        "instruction": "\n        You serve as a logistics coordinator tasked with overseeing planned inbound shipments.\n        Start by examining all intended inbound shipments to single out the one with the earliest anticipated departure date.\n        Evaluate the carrier associated with this shipment to verify whether the carrier is active.\n        If the carrier is active, update the carrier with the note \"Shipment of highest priority scheduled\".\n        Additionally, annotate the shipment with \"Shipment of highest priority\".\n        As a final step, review the updated inbound shipment details to ensure the note has been correctly added.\n    ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Planned"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "ANAF",
                    "updates": {
                        "note": "Shipment of highest priority scheduled"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0029",
                    "updates": {
                        "note": "Shipment of highest priority"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                }
            }
        ],
        "outputs": [
                "\"note\": \"Shipment of highest priority\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_052",
        "instruction": "\n            You act as an inventory supervisor overseeing warehouse stock conditions.\n            Identify all warehouses that hold inventory items with at least 200 damaged goods.\n            For each warehouse identified, devise a restocking plan and update their status to \u201cRestocking Planned\u201d to ensure their prompt replenishment.\n            After completing all updates, verify that the modifications have been applied successfully by examining the refreshed warehouse records.\n        ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 200
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "status": "Restocking Planned"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "status": "Restocking Planned"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                }
            }
        ],
        "outputs": [
                "\"status\": \"Restocking Planned\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_053",
        "instruction": "\n            Your role as a product compliance specialist involves ensuring the correct handling of hazardous products.\n            Begin by locating all products labeled as hazardous and confirm that their storage requirements are correctly documented.\n            For any product lacking or having incorrect storage instructions, adjust the record as needed.\n            If the storage requirements fail to include the Hazmat class information, append the note \u201cHazmat Class mentioned\u201d to guarantee compliance.\n            After making these updates, inspect the updated product details to verify the changes have been accurately implemented.\n        ",
        "actions": [
            {
                "name": "GetHazmatProducts",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "hazmat",
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "CHEM-SOLV-K11",
                        "TECH-BATT-Q17",
                        "ELEC-SMART-W23"
                    ]
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "updates": {
                        "storage_requirements": "Hazmat Class mentioned"
                    }
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "updates": {
                        "storage_requirements": "Hazmat Class mentioned"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                }
            }
        ],
        "outputs": [
                "\"storage_requirements\": \"Hazmat Class mentioned\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_054",
        "instruction": "\n            You operate as a shipment performance analyst in charge of tracking delays in inbound shipments.\n            Identify all delayed inbound shipments.\n            Examine the carriers assigned to these shipments.\n            Verify if the carrier is presently active.\n            If active, no carrier replacement is required.\n            If inactive, identify the top-rated carrier.\n            Review carriers individually to find the highest-rated active carrier that employs the same mode of transportation and replace the current shipment carrier with this one.\n            Lastly, acquire and review the updated inbound shipment details or the shipment with the most imminent departure date to ensure the changes are correctly reflected.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Delayed"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0022"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "POCL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetTopRatedCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "carrier_scac": "SKEX",
                        "carrier_name": "Sakura Express"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                }
            }
        ],
        "outputs": [
                "\"carrier_scac\": \"SKEX\"",
                "\"carrier_name\": \"Sakura Express\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_055",
        "instruction": "\n            Your position as a warehouse quality inspector requires you to pinpoint critical inventory issues.\n            Identify all warehouses containing either expired inventory, using today's date as May 11, 2025, or inventory with at least 200 damaged goods.\n            For each warehouse meeting these criteria, change its status to \u201cIMMEDIATE ATTENTION NEEDED\u201d to mark it for urgent inspection.\n            After making the updates, verify them by reviewing the updated warehouse details.\n        ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2025-05-11"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 200
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "status": "IMMEDIATE ATTENTION NEEDED"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "status": "IMMEDIATE ATTENTION NEEDED"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "status": "IMMEDIATE ATTENTION NEEDED"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                }
            }
        ],
        "outputs": [
                "\"status\": \"IMMEDIATE ATTENTION NEEDED\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_056",
        "instruction": "\n            As a carrier evaluation officer, your role is to assess risk and insurance coverage for transportation partners.\n            Start by gathering the list of all active carriers in the system.\n            Compute the highest insurance coverage limit among these carriers.\n            Next, examine the insurance details of each active carrier to pinpoint those whose coverage limit equals this maximum.\n            If several carriers achieve this limit, include each of them.\n            Update each top carrier's record with a note: \"Highest Insurance Coverage\".\n            This process aids in making informed decisions regarding risk exposure and ensures that sensitive or high-value shipments are matched with adequately covered carriers.\n            Conclude by returning the carrier(s) with the highest insurance coverage.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "insurance_details",
                    "value2": "coverage_limit_usd",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "notes": "Highest Insurance Coverage"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                }
            }
        ],
        "outputs": [
                "GPLS"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_057",
        "instruction": "\n            As an inventory coordinator, your duties include analyzing product storage and pricing.\n            Start by locating all products with storage requirements labeled as \"Dry.\n            \"\n            Narrow down this group to products with an active lifecycle status.\n            Identify the minimum unit price among active products to aid inventory valuation and pricing strategy.\n            Examine each product for having this minimum unit price.\n            Products meeting this criterion should be updated with the note \"Cheapest Product\".\n        ",
        "actions": [
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "Dry"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "product_master",
                    "key": "sku",
                    "value": "unit_price",
                    "list_of_ids": [
                        "ELEC-CHIP-A1",
                        "AUTO-PAD-B2",
                        "FOOD-COFF-C3",
                        "MANU-PAPR-F6",
                        "HEVY-DRIL-I9",
                        "FURN-CHAIR-M13",
                        "TECH-ROBO-N14",
                        "APRL-TSHT-O15",
                        "MATR-COTT-R18",
                        "MATR-CORK-T20",
                        "FOOD-OLIV-V22"
                    ]
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-CHIP-A1"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "AUTO-PAD-B2"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-COFF-C3"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "MANU-PAPR-F6"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "HEVY-DRIL-I9"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FURN-CHAIR-M13"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "TECH-ROBO-N14"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "APRL-TSHT-O15"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "MATR-COTT-R18"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "MATR-CORK-T20"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-OLIV-V22"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "MATR-CORK-T20",
                    "updates": {
                        "notes": "Cheapest Product"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "MATR-CORK-T20"
                }
            }
        ],
        "outputs": [
                "MATR-CORK-T20"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_058",
        "instruction": "\n            In your role as a supplier compliance officer, you are tasked with monitoring the performance and certification of preferred suppliers.\n            Start by reviewing preferred suppliers to find those with at least one certification.\n            From this refined list, identify which supplier boasts the highest on-time delivery percentage to reinforce reliable sourcing and compliance.\n            Annotate this supplier's record with the note \"Best on time delivery percentage\" and review the updated supplier details.\n        ",
        "actions": [
            {
                "name": "GetPreferredSuppliers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1002"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1005"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1010"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1013"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1016"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1019"
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1029"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "supplier_master",
                    "key": "supplier_id",
                    "value": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "SUP-1002",
                        "SUP-1005",
                        "SUP-1010",
                        "SUP-1013",
                        "SUP-1016",
                        "SUP-1019",
                        "SUP-1029"
                    ]
                },
            },
            {
                "name": "UpdateSupplier",
                "arguments": {
                    "supplier_id": "SUP-1016",
                    "updates": {
                        "notes": "Best on time delivery percentage"
                    }
                },
            },
            {
                "name": "GetSupplierById",
                "arguments": {
                    "supplier_id": "SUP-1016"
                }
            }
        ],
        "outputs": [
                "\"SUP-1016\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_059",
        "instruction": "\n            As the warehouse operations lead, your responsibility is to oversee inventory conditions and space utilization.\n            Begin by finding all warehouses containing damaged inventory.\n            For these warehouses, evaluate their current utilization percentage.\n            Identify the warehouse with both damaged inventory and the highest utilization percentage to evaluate operational efficiency in constrained environments.\n            Annotate the warehouse record with \"Best Current Utilization Percentage, Damaged Inventory\".\n            Examine the details of this warehouse.\n        ",
        "actions": [
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0001"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0002"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0003"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0006"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0007"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0013"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0018"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0021"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0022"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0025"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "warehouses",
                    "key": "warehouse_id",
                    "value": "current_utilization_percentage",
                    "list_of_ids": [
                        "WH-01",
                        "WH-02",
                        "WH-03",
                        "WH-04",
                        "WH-05",
                        "WH-07",
                        "WH-08",
                        "WH-09",
                        "WH-10",
                        "WH-12",
                        "WH-14",
                        "WH-15"
                    ]
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "notes": "Best Current Utilization Percentage, Damaged Inventory"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                }
            }
        ],
        "outputs": [
                "WH-10"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_060",
        "instruction": "\n            As a price analyst, you are responsible for verifying the prices and safety standards of grocery products in the market.\n            Begin by evaluating all products categorized as \"Groceries.\n            \"\n            For each item, verify if its lifecycle status is active and if it's classified as hazardous.\n            From the eligible non-hazardous grocery items with an active lifecycle, single out the product with the lowest price to facilitate pricing and safety analysis.\n            Update the product details with the note \"Cheapest Grocery\" and inspect the product details.\n        ",
        "actions": [
            {
                "name": "GetProductsByCategory",
                "arguments": {
                    "category": "Groceries"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-COFF-C3"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-FISH-H8"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-OLIV-V22"
                },
            },
            {
                "name": "GetHazmatProducts",
                "arguments": {
                    "list_of_ids": [
                        "FOOD-COFF-C3",
                        "FOOD-FISH-H8",
                        "FOOD-OLIV-V22"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "min",
                    "json": "product_master",
                    "key": "sku",
                    "value": "unit_price",
                    "list_of_ids": [
                        "FOOD-COFF-C3",
                        "FOOD-FISH-H8",
                        "FOOD-OLIV-V22"
                    ]
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "FOOD-COFF-C3",
                    "updates": {
                        "notes": "Cheapest Grocery"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "FOOD-COFF-C3"
                }
            }
        ],
        "outputs": [
                "FOOD-COFF-C3"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_061",
        "instruction": "\n            Handle the role of a shipment scheduler tasked with ensuring timely and dependable outbound deliveries.\n            Start by identifying all outbound orders awaiting shipment.\n            For each order, verify whether the assigned carrier remains active.\n            Should the carrier be inactive or absent, obtain a list of other active carriers utilizing the same transportation mode.\n            From this list, determine the carrier with the top average rating.\n            Substitute the inactive or absent carrier in the pending order with this highly-rated active carrier.\n            Lastly, examine the details of the revised pending order to verify that the modifications have been successfully implemented.\n        ",
        "actions": [
            {
                "name": "GetOrdersByStatus",
                "arguments": {
                    "status": "Pending"
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0010"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "BLUJ"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "average_rating",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "SWDL",
                        "MTRL",
                        "ALFS",
                        "GPLS"
                    ]
                },
            },
            {
                "name": "UpdateOutboundOrder",
                "arguments": {
                    "order_id": "ORD-0010",
                    "updates": {
                        "carrier_scac": "GPLS",
                        "carrier_name": "Global Parcel Service"
                    }
                },
            },
            {
                "name": "GetOutboundOrderById",
                "arguments": {
                    "order_id": "ORD-0010"
                }
            }
        ],
        "outputs": [
                "\"carrier_name\": \"Global Parcel Service\"",
                "\"carrier_scac\": \"GPLS\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_062",
        "instruction": "\n            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.\n            Start by examining all carriers with global regional coverage and active status.\n            From this collection, pinpoint those operating via Air mode of transport.\n            Ascertain the maximum and minimum on-time delivery percentages from these active global air carriers to gauge overall performance in this area.\n            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Air mode of transport.\n            If linked shipments lack Air mode of transport, append carriers with the attribute note \"No Air Mode\".\n            Provide the list of scacs for updated carriers.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Air",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "SKEX",
                        "DLOG",
                        "DFC",
                        "SWDL",
                        "ALFS",
                        "GPLS",
                        "AAC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "DLOG"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "GPLS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "mode_of_transport",
                    "value": "Air"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "DLOG",
                    "updates": {
                        "note": "No Air Mode"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "note": "No Air Mode"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "DLOG",
                        "GPLS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"DLOG\",\n  \"GPLS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_063",
        "instruction": "\n            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.\n            Start by examining all carriers with global regional coverage and active status.\n            From this collection, pinpoint those operating via Sea mode of transport.\n            Ascertain the maximum and minimum on-time delivery percentages from these active global sea carriers to gauge overall performance in this area.\n            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Sea mode of transport.\n            If they are linked, update carriers with maximum values with the attribute rank \"Best Carrier with Inbound Shipment\"\n            And, update carriers with minimum values with the attribute rank \"Worst Carrier with Inbound Shipment\".\n            Provide the list of scacs for updated carriers.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Sea",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "PSLN",
                        "SATL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "OCBR"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "ALFS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "mode_of_transport",
                    "value": "Sea"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "OCBR",
                    "updates": {
                        "rank": "Worst Carrier with Inbound Shipment"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "ALFS",
                    "updates": {
                        "rank": "Best Carrier with Inbound Shipment"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "OCBR",
                        "ALFS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"OCBR\",\n  \"ALFS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_064",
        "instruction": "\n            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.\n            Start by examining all carriers with global regional coverage and active status.\n            From this collection, pinpoint those operating via Truck mode of transport.\n            Ascertain the maximum and minimum on-time delivery percentages from these active global truck carriers to gauge overall performance in this area.\n            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Truck mode of transport.\n            If linked shipments lack Truck mode of transport, append attribute note \"No Truck Mode\".\n            Provide the list of scacs for updated carriers.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Truck",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "SWDL",
                        "ALFS",
                        "GPLS",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "MEDL"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "GPLS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "mode_of_transport",
                    "value": "Truck"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MEDL",
                    "updates": {
                        "note": "No Truck Mode"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "MEDL"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"MEDL\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_065",
        "instruction": "\n            Coordinate evaluations as a carrier performance analyst responsible for assessing carrier efficiency and coverage.\n            Start by examining all carriers with global regional coverage and active status.\n            From this collection, pinpoint those operating via Rail mode of transport.\n            Ascertain the maximum and minimum on-time delivery percentages from these active global rail carriers to gauge overall performance in this area.\n            Verify if carriers with minimum and maximum percentages are linked to inbound shipments using Rail mode of transport.\n            If linked shipments lack Rail mode of transport, append carriers with the attribute note \"No Rail Mode\".\n            Provide the list of scacs for updated carriers.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Rail",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "GOCN",
                        "ALFS"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "GOCN"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "ALFS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "mode_of_transport",
                    "value": "Rail"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GOCN",
                    "updates": {
                        "note": "No Rail Mode"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "ALFS",
                    "updates": {
                        "note": "No Rail Mode"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "GOCN",
                        "ALFS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"GOCN\",\n  \"ALFS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_066",
        "instruction": "\n            As a carrier performance analyst, your task is to evaluate carrier efficiency and coverage.\n            Start by examining all carriers that have global regional coverage and are currently active.\n            Within this set, pinpoint those utilizing the Parcel mode of transport.\n            Determine the highest and lowest on-time delivery percentages among these active global parcel carriers to gauge performance in this segment.\n            Verify if carriers with these minimum and maximum values are linked to inbound shipments using Parcel mode of transport.\n            If they are linked, label carriers with maximum values with the note \"Best Carrier with Inbound Shipment\".\n            Similarly, label carriers with minimum values with the note \"Worst Carrier with Inbound Shipment\".\n            If these shipments lack Parcel mode, add the note \"No Parcel Mode\".\n            Provide the list of SCACs for carriers that have been updated.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarriersByMode",
                "arguments": {
                    "mode": "Parcel",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "OCBR",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "carriers",
                    "key": "scac",
                    "value": "performance_metrics",
                    "value2": "on_time_delivery_percentage",
                    "list_of_ids": [
                        "SWDL",
                        "GPLS",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "GPLS"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "mode_of_transport",
                    "value": "Parcel"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "SWDL",
                    "updates": {
                        "note": "Worst Carrier with Inbound Shipment"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GPLS",
                    "updates": {
                        "note": "Best Carrier with Inbound Shipment"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SWDL",
                        "GPLS"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SWDL\",\n  \"GPLS\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_067",
        "instruction": "\n            You are charged with coordinating warehouse audits, focusing on assessing warehouse assets.\n            Restrict your review to warehouses that are owned.\n            Figure out the average current utilization percentage for all owned warehouses to assess overall space efficiency.\n            Go through each warehouse's details and if its utilization is below the average, annotate it with \"Review Expected\".\n            Submit the IDs of warehouses that have been updated.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "warehouses",
                    "key": "warehouse_id",
                    "value": "current_utilization_percentage",
                    "list_of_ids": [
                        "WH-01",
                        "WH-03",
                        "WH-05",
                        "WH-07",
                        "WH-08",
                        "WH-10",
                        "WH-11",
                        "WH-13",
                        "WH-14",
                        "WH-16"
                    ]
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-03",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-08",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-11",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-13",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-16"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "WH-03",
                        "WH-07",
                        "WH-08",
                        "WH-11",
                        "WH-13"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"WH-03\",\n  \"WH-07\",\n  \"WH-08\",\n  \"WH-11\",\n  \"WH-13\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_068",
        "instruction": "\n            As a warehouse audit coordinator, you are responsible for evaluating warehouse assets.\n            Restrict your attention to warehouses that are leased.\n            Compute the average current utilization percentage across all leased warehouses to gauge overall space efficiency.\n            Check each warehouse detail and if it falls below the average utilization percentage, mark it with \"Review Expected\".\n            Provide the IDs of warehouses that have been updated.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Leased"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "warehouses",
                    "key": "warehouse_id",
                    "value": "current_utilization_percentage",
                    "list_of_ids": [
                        "WH-02",
                        "WH-04",
                        "WH-06",
                        "WH-09",
                        "WH-12",
                        "WH-15"
                    ]
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "note": "Review Expected"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "WH-06",
                        "WH-12",
                        "WH-15"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"WH-06\",\n  \"WH-12\",\n  \"WH-15\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_069",
        "instruction": "\n            Your role as a warehouse audit coordinator involves assessing warehouse assets.\n            Concentrate on warehouses that are owned.\n            Calculate the average current utilization percentages for these owned warehouses to evaluate the variance in space usage.\n            Analyze each warehouse detail, and if its utilization surpasses the average, label it with \"Top Used\".\n            Return the IDs of the warehouses updated.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "warehouses",
                    "key": "warehouse_id",
                    "value": "current_utilization_percentage",
                    "list_of_ids": [
                        "WH-01",
                        "WH-03",
                        "WH-05",
                        "WH-07",
                        "WH-08",
                        "WH-10",
                        "WH-11",
                        "WH-13",
                        "WH-14",
                        "WH-16"
                    ]
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-01",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-05",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-10",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-14",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-16"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-16",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-16"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "WH-01",
                        "WH-05",
                        "WH-10",
                        "WH-14",
                        "WH-16"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"WH-01\",\n  \"WH-05\",\n  \"WH-10\",\n  \"WH-14\",\n  \"WH-16\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_070",
        "instruction": "\n            As a coordinator for warehouse audits, your duty is to assess warehouse assets.\n            Limit your examination to leased warehouses.\n            Evaluate the average current utilization percentages for these leased warehouses to comprehend space usage variance.\n            Inspect each warehouse detail, and if its usage exceeds the average, annotate it with \"Top Used\".\n            Submit the IDs of the warehouses updated.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Leased"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "warehouses",
                    "key": "warehouse_id",
                    "value": "current_utilization_percentage",
                    "list_of_ids": [
                        "WH-02",
                        "WH-04",
                        "WH-06",
                        "WH-09",
                        "WH-12",
                        "WH-15"
                    ]
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "updates": {
                        "note": "Top Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "WH-02",
                        "WH-04",
                        "WH-09"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"WH-02\",\n  \"WH-04\",\n  \"WH-09\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_071",
        "instruction": "\n            You are a market analyst focused on inbound shipments.\n            Handle the review of all inbound shipments marked as \u201cIn Transit\u201d and compute the total sum of their values.\n            Identify the shipment with the highest total value and label it with the note \"Most valued In Transit shipment\".\n            The aim is to ascertain the complete value of goods presently in transit.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "In Transit"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0005"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0008"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0012"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0018"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0024"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0026"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "updates": {
                        "note": "Most valued In Transit shipment"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                }
            }
        ],
        "outputs": [
                "6820000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_072",
        "instruction": "\n            You are a market analyst focused on inbound shipments.\n            Conduct an assessment of all inbound shipments with the status \u201cPlanned\u201d and sum their total values.\n            Determine which shipment has the highest total value and mark it with a note saying \"Most valued Planned shipment\".\n            The goal is to comprehend the overall value of goods currently scheduled for arrival.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Planned"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0006"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0010"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0019"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0027"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0029"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0030"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0006",
                        "SHIP-0010",
                        "SHIP-0016",
                        "SHIP-0019",
                        "SHIP-0027",
                        "SHIP-0029",
                        "SHIP-0030"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0016",
                    "updates": {
                        "note": "Most valued Planned shipment"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0016"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0006",
                        "SHIP-0010",
                        "SHIP-0016",
                        "SHIP-0019",
                        "SHIP-0027",
                        "SHIP-0029",
                        "SHIP-0030"
                    ]
                }
            }
        ],
        "outputs": [
                "1905000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_073",
        "instruction": "\n            You are a market analyst focused on inbound shipments.\n            Process all inbound shipments noted as \u201cDelayed\u201d and compute the total of their values.\n            Pinpoint the shipment boasting the highest total value and annotate it with \"Most valued Delayed shipment\".\n            The goal is to identify the total value of goods presently experiencing delays.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Delayed"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0022"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0004",
                        "SHIP-0022"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "note": "Most valued Delayed shipment"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0004",
                        "SHIP-0022"
                    ]
                }
            }
        ],
        "outputs": [
                "575000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_074",
        "instruction": "\n            You are a market analyst focused on inbound shipments.\n            Examine all inbound shipments with the status \u201cReceived\u201d and add up their total values.\n            Highlight the shipment with the highest total value and tag it with the note \"Most valued Received shipment\".\n            The purpose is to find out the total value of goods that have been received so far.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Received"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0017"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "max",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0002",
                        "SHIP-0007",
                        "SHIP-0017"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0002",
                    "updates": {
                        "note": "Most valued Received shipment"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0002",
                        "SHIP-0007",
                        "SHIP-0017"
                    ]
                }
            }
        ],
        "outputs": [
                "325000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_075",
        "instruction": "\n            You are a market analyst focused on in transit inbound shipments.\n            Initially, calculate the average of the total values of these inbound shipments.\n            Review all the inbound shipments.\n            If the total values exceed the average, elevate their priority level to \"High\".\n            Then, ascertain the minimum and maximum total values among these shipments.\n            The aim is to carry out statistical analysis (minimum, maximum, and average) of total values for goods currently in transit.\n            Lastly, provide the determined minimum and maximum of total values.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "In Transit"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0001"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0003"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0005"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0008"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0009",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0009"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0011",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0011"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0012"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0013",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0013"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0014"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0015"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0018"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0020"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0023"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0024"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0025",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0025"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0026"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0028",
                    "updates": {
                        "priority_level": "High"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0028"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "both",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                }
            }
        ],
        "outputs": [
                "\"min_value\": 50000",
                "\"max_value\": 1200000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_076",
        "instruction": "\n            As a warehouse inventory manager, examine the inventory record for INV-0010.\n            The quantity_allocated has been successfully sold.\n            Subtract the allocated quantity from quantity_on_hand.\n            Set quantity_allocated to 0.\n            Recalculate total_value by subtracting unit_cost * quantity_allocated before.\n            If quantity_on_hand < reorder_point, label stock_status as \"Reorder Needed\".\n            Then, inspect the associated warehouse and its current utilization percentage.\n            If current utilization percentage < 80, update warehouse with attribute note as \"Less Used\".\n            If current utilization percentage >= 80, update warehouse with attribute note as \"More Used\".\n            Return the updated inventory record with: inventory_id, sku, quantity_on_hand, quantity_allocated, stock_status, and total_value.\n        ",
        "actions": [
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "quantity_on_hand": 15000
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "quantity_allocated": 0
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "total_value": 52500
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "note": "Less Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0010\"",
                "\"sku\": \"BLDG-TILE-J10\"",
                "\"quantity_on_hand\": 15000",
                "\"quantity_allocated\": 0",
                "\"total_value\": 52500",
                "\"stock_status\": \"In Stock\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_077",
        "instruction": "\n            In charge of luxury inventory, note that INV-0005 has sold all allocated units.\n            Reduce these units from quantity_on_hand.\n            Set quantity_allocated to 0.\n            Recalculate total_value by subtracting unit_cost * quantity_allocated before.\n            If the quantity_on_hand drops below the reorder_point, set stock_status to \"Reorder Needed\".\n            If current utilization percentage < 80, update warehouse with attribute note as \"Less Used\".\n            If current utilization percentage >= 80, update warehouse with attribute note as \"More Used\".\n            Return the updated inventory with new quantity_on_hand, quantity_allocated, total_value and stock_status).\n        ",
        "actions": [
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0005",
                    "updates": {
                        "quantity_on_hand": 120
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0005",
                    "updates": {
                        "quantity_allocated": 0
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0005",
                    "updates": {
                        "total_value": 102000
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-07",
                    "updates": {
                        "note": "Less Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0005"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0005\"",
                "\"quantity_on_hand\": 120",
                "\"quantity_allocated\": 0",
                "\"total_value\": 102000",
                "\"stock_status\": \"In Stock\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_078",
        "instruction": "\n            The allocated bottles of INV-0016 have been sold.\n            Decrease quantity_on_hand by quantity allocated before selling.\n            Set quantity_allocated to 0.\n            Recalculate total_value by subtracting unit_cost * quantity_allocated before.\n            If new quantity_on_hand < reorder_point, append \"Reorder Suggested\" to stock_status.\n            If current utilization percentage < 80, update warehouse with attribute note as \"Less Used\".\n            If current utilization percentage >= 80, update warehouse with attribute note as \"More Used\".\n            Return updated inventory_id, sku, quantity_on_hand, quantity_allocated, stock_status, storage_requirements, and total_value.\n        ",
        "actions": [
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0016",
                    "updates": {
                        "quantity_on_hand": 4500
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0016",
                    "updates": {
                        "quantity_allocated": 0
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0016",
                    "updates": {
                        "total_value": 81000
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "note": "More Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0016\"",
                "\"sku\": \"BEVG-WINE-P16\"",
                "\"quantity_on_hand\": 4500",
                "\"quantity_allocated\": 0",
                "\"stock_status\": \"In Stock\"",
                "\"storage_requirements\": \"Temp Control 12-14°C, Dark\"",
                "\"total_value\": 81000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_079",
        "instruction": "\n            Allocated inventory of INV-0004 has been processed.\n            Reduce quantity allocated before from quantity_on_hand.\n            Set quantity_allocated to 0.\n            Recalculate total_value by subtracting unit_cost * quantity_allocated before.\n            If quantity_on_hand < reorder_point, add tag: \"Critical Reorder\".\n            If current utilization percentage < 80, update warehouse with attribute note as \"Less Used\".\n            If current utilization percentage >= 80, update warehouse with attribute note as \"More Used\".\n            Return updated values for inventory_id, quantity_on_hand, quantity_allocated, total_value, and stock_status.\n        ",
        "actions": [
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0004",
                    "updates": {
                        "quantity_on_hand": 18000
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0004",
                    "updates": {
                        "quantity_allocated": 0
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0004",
                    "updates": {
                        "total_value": 279000
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "updates": {
                        "note": "More Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0004\"",
                "\"quantity_on_hand\": 18000",
                "\"quantity_allocated\": 0",
                "\"total_value\": 279000",
                "\"stock_status\": \"In Stock\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_080",
        "instruction": "\n            Sold out allocated stock of INV-0015.\n            Lessen quantity_on_hand by sold allocated stock.\n            Set quantity_allocated to 0.\n            Recalculate total_value by subtracting unit_cost * quantity_allocated before.\n            If new quantity_on_hand < reorder_point, set stock_status = \"Reorder Needed\".\n            If current utilization percentage < 80, update warehouse with attribute note as \"Less Used\".\n            If current utilization percentage >= 80, update warehouse with attribute note as \"More Used\".\n            Return changes including: inventory_id, sku, quantity_on_hand, quantity_allocated, total_value and stock_status.\n        ",
        "actions": [
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "updates": {
                        "quantity_on_hand": 22000
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "updates": {
                        "quantity_allocated": 0
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "updates": {
                        "total_value": 176000
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "updates": {
                        "note": "More Used"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                }
            }
        ],
        "outputs": [
                "\"inventory_id\": \"INV-0015\"",
                "\"sku\": \"APRL-TSHT-O15\"",
                "\"quantity_on_hand\": 22000",
                "\"quantity_allocated\": 0",
                "\"total_value\": 176000",
                "\"stock_status\": \"In Stock\""
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_081",
        "instruction": "\n            As a market analyst focusing on inbound shipments,\n            compute the average total value of these shipments.\n            Your initial task is to ascertain the average value of goods currently delayed.\n            Then, assess shipments and their associated carriers to verify if any of those shipments have inactive carriers.\n            For each shipment with an inactive carrier, determine if the total value exceeds the average total value.\n            If it does, annotate the shipment with \"Carrier Replacement Required\" in the notes.\n            Conclude by returning the ids of the shipments that were updated.\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Delayed"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0004",
                        "SHIP-0022"
                    ]
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "POCL"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0022"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0004",
                    "updates": {
                        "notes": "Carrier Replacement Required"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0004"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0004"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0004\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_082",
        "instruction": "\n            As a market analyst focusing on incoming shipments,\n            compute the average total value of these shipments.\n            Your primary goal is to find out the average value of goods currently received.\n            Afterward, evaluate shipments and their active carriers only.\n            Should the total value of a shipment with an active carrier fall below the average, update its notes with \"Lower than Average.\n            \"\n            Conversely, if a shipment's total value is above the average, annotate it with \"Higher than Average.\n            \"\n            Finally, provide the ids of shipments marked with notes \"Higher than Average.\n            \".\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Received"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0002",
                        "SHIP-0007",
                        "SHIP-0017"
                    ]
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0017"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0002",
                    "updates": {
                        "notes": "Higher than Average"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0007",
                    "updates": {
                        "notes": "Lower than Average"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0017",
                    "updates": {
                        "notes": "Higher than Average"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0017"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0002",
                        "SHIP-0017"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0002\",\n  \"SHIP-0017\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_083",
        "instruction": "\n            As a logistics manager overseeing carrier performance,\n            identify all active carriers handling the \"Global\" region that have an on-time delivery rate below 95%.\n            Update each qualifying carrier's status to \"Under Review.\n            \"\n            Submit the list of carriers whose status was modified.\n            If no carriers fall below the 95% benchmark, no updates are required and an empty list should be returned.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MEDL",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "OCBR",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GOCN",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "NRMC",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "PSLN",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "NSTS",
                        "MEDL",
                        "OCBR",
                        "GOCN",
                        "NRMC",
                        "PSLN"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"NSTS\",\n  \"MEDL\",\n  \"OCBR\",\n  \"GOCN\",\n  \"NRMC\",\n  \"PSLN\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_084",
        "instruction": "\n            In your role as a logistics manager monitoring carrier performance, determine all active carriers in the \"Global\" region with on-time delivery percentages under 95%.\n            Alter the status of such carriers to \"Under Review.\n            \" \n            Supply the updated list of carriers.\n            Should no carriers fall short of the 95% threshold, simply return an empty list with no updates.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DLOG"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "DFC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ALFS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GPLS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SATL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EWDL"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "NSTS",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MEDL",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "OCBR",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "GOCN",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "NRMC",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "PSLN",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSTS"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MEDL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "OCBR"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "GOCN"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NRMC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "PSLN"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "NSTS",
                        "MEDL",
                        "OCBR",
                        "GOCN",
                        "NRMC",
                        "PSLN"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"NSTS\",\n  \"MEDL\",\n  \"OCBR\",\n  \"GOCN\",\n  \"NRMC\",\n  \"PSLN\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_085",
        "instruction": "\n            Acting as a logistics manager for overseeing carrier performance, locate all active carriers in the \"North America\" region whose punctuality in deliveries is under 95%.\n            Change the status of each identified carrier to \"Under Review.\n            \"\n            Provide the list of carriers that had their status altered.\n            If no carriers fit this criteria, return an empty list as no updates are required.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "North America",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MTRL",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "MTRL"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"MTRL\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_086",
        "instruction": "\n            As a logistics manager, oversee the performance of carriers operating in specific regions only, not globally.\n            Begin by reviewing active carriers.\n            Identify which of these active carriers have global coverage.\n            Validate regional presence and assess the on-time delivery rates of active carriers that do not operate globally, using detailed information.\n            Change the status of each non-global active carrier found to \"Under Review.\n            \" Provide the list of carriers whose status was updated.\n            If no carriers qualify for this update, it is unnecessary to make any changes, so return an empty list.\n        ",
        "actions": [
            {
                "name": "GetActiveCarriers",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Global",
                    "list_of_scacs": [
                        "NSTS",
                        "SKEX",
                        "DLOG",
                        "MEDL",
                        "DFC",
                        "SWDL",
                        "MTRL",
                        "OCBR",
                        "SCF",
                        "GOCN",
                        "ALFS",
                        "NRMC",
                        "GPLS",
                        "PSLN",
                        "AAC",
                        "SATL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC",
                        "EWDL"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "MTRL",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "SCF",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "EAC",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "NAC",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateCarrier",
                "arguments": {
                    "carrier_scac": "NSC",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "MTRL",
                        "SCF",
                        "EAC",
                        "NAC",
                        "NSC"
                    ]
                }
            }
        ],
        "outputs": [
                "[\"MTRL\", \"SCF\", \"EAC\", \"NAC\", \"NSC\"]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_087",
        "instruction": "\n            Taking on the role of an inventory controller, your task is to oversee the quality and availability of stock.\n            As of December 12, 2024, locate all inventory items that are either past expiration or have 200 or more of damaged quantities.\n            Additionally, pinpoint items that fall below their reorder threshold.\n            Merge these items\u2014expired, damaged, or under reorder point\u2014and adjust their status to \u201cUnder Review.\n            \u201d Conclude by providing the list of updated inventory item IDs.\n        ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2024-12-12"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 200
                },
            },
            {
                "name": "GetInventoryBelowReorderPoint",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0010",
                        "INV-0020",
                        "INV-0024"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0010\",\n  \"INV-0020\",\n  \"INV-0024\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_088",
        "instruction": "\n            In the capacity of an inventory controller, ensure the supervision of stock quality and availability.\n            As of June 12, 2024, determine which inventory items are expired or have damaged quantities reaching 150 or more.\n            Equally, identify any items that are under their reorder level.\n            Consolidate these groups\u2014expired, damaged, or under reorder point\u2014and modify their status to \u201cUnder Review.\n            \u201d Finally, deliver the list of IDs for all the inventory items that have been updated.\n        ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2024-06-12"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 150
                },
            },
            {
                "name": "GetInventoryBelowReorderPoint",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0010",
                        "INV-0020"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0010\",\n  \"INV-0020\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_089",
        "instruction": "\n            Acting as an inventory controller, your duty is to manage stock quality and availability.\n            By May 12, 2025, you should identify inventory items that are expired or have damaged amounts of 100 or more.\n            Additionally, check for items beneath their reorder point.\n            Combine these\u2014expired, damaged, or below reorder level\u2014and revise their status to \u201cUnder Review.\n            \u201d Conclude the task by submitting the list of IDs of all inventory items adjusted.\n        ",
        "actions": [
            {
                "name": "GetExpiredInventory",
                "arguments": {
                    "today": "2025-05-12"
                },
            },
            {
                "name": "GetInventoryWithDamage",
                "arguments": {
                    "threshold": 100
                },
            },
            {
                "name": "GetInventoryBelowReorderPoint",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0010",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0015",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0020",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "UpdateInventory",
                "arguments": {
                    "inventory_id": "INV-0024",
                    "updates": {
                        "status": "Under Review"
                    }
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0010"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0015"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0020"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0024"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "INV-0010",
                        "INV-0015",
                        "INV-0020",
                        "INV-0024"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"INV-0010\",\n  \"INV-0015\",\n  \"INV-0020\",\n  \"INV-0024\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_090",
        "instruction": "\n            As a compliance officer, your responsibility is to review warehouse and product safety protocols.\n            Start by compiling data on all company-owned warehouses.\n            Then, pinpoint all products that necessitate special storage conditions, with a focus on those labeled as \u201cHazmat.\n            \u201d\n            Check if the company-owned warehouses are capable of supporting hazmat storage.\n            Subsequently, cross-verify inventory records to ensure these products are stored in warehouses that are both company-owned and equipped for hazmat storage.\n            Should a product's inventory match an owned warehouse that includes adequate hazmat facilities, it is deemed compliant.\n            Tag products lacking specific owned warehouse suitable for hazmat by noting \"SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE\".\n            Lastly, furnish the list of product IDs allocated to appropriate owned warehouses fit for hazmat storage.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "GetHazmatProducts",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "PHRM-VACC-D4"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "TECH-BATT-Q17"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "ELEC-SMART-W23"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "PHRM-VACC-D4",
                    "updates": {
                        "notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "TECH-BATT-Q17",
                    "updates": {
                        "notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "ELEC-SMART-W23",
                    "updates": {
                        "notes": "SUITABLE CONDITION NOT PROVIDED FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "PHRM-VACC-D4"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "TECH-BATT-Q17"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "ELEC-SMART-W23"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "CHEM-SOLV-K11"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"CHEM-SOLV-K11\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_091",
        "instruction": "\n            You are a compliance officer tasked with reviewing warehouse and product safety protocols.\n            Your goal is to locate products needing special storage conditions, like \u201cHazmat,\u201d that are either not assigned to any warehouse or assigned to owned warehouses unsuitable for hazmat storage.\n            Start by obtaining the list of all company-owned warehouses and identifying which are equipped for hazmat storage.\n            Next, find all products with \u201cHazmat\u201d storage requirements.\n            For each of these products, verify inventory details to determine if a warehouse has been designated.\n            If any product is without a warehouse assignment, or linked to an owned warehouse lacking hazmat readiness, mark it.\n            Update products with the appropriate owned warehouse suitable for hazmat by appending attribute notes \"SUITABLE CONDITION PROVIDED FOR HAZMAT STORAGE\".\n            Conclude by returning the list of product IDs falling into these categories.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "GetHazmatProducts",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "PHRM-VACC-D4"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "TECH-BATT-Q17"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "ELEC-SMART-W23"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0004"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0017"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0023"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "updates": {
                        "notes": "SUITABLE CONDITION PROVIDED FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "PHRM-VACC-D4",
                        "TECH-BATT-Q17",
                        "ELEC-SMART-W23"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"PHRM-VACC-D4\",\n  \"TECH-BATT-Q17\",\n  \"ELEC-SMART-W23\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_092",
        "instruction": "\n            You are a compliance officer tasked with reviewing warehouse and product safety protocols.\n            Your goal is to ascertain whether leased warehouses are properly equipped to manage products requiring \u201cHazmat\u201d storage.\n            Initiate by collecting all leased warehouses, then evaluate each to confirm if it has the necessary equipment for hazmat storage (using special capabilities attribute).\n            For any warehouse lacking hazmat readiness, amend the record by appending a note stating \"NOT SUITABLE FOR HAZMAT STORAGE\".\n            Verify the updated warehouse information for correctness.\n            Finally, compile the list of warehouse IDs that fail to meet hazmat storage suitability.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Leased"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-02",
                    "updates": {
                        "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-04",
                    "updates": {
                        "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-06",
                    "updates": {
                        "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-09",
                    "updates": {
                        "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-12",
                    "updates": {
                        "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "UpdateWarehouse",
                "arguments": {
                    "warehouse_id": "WH-15",
                    "updates": {
                        "notes": "NOT SUITABLE FOR HAZMAT STORAGE"
                    }
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "WH-02",
                        "WH-04",
                        "WH-06",
                        "WH-09",
                        "WH-12",
                        "WH-15"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"WH-02\",\n  \"WH-04\",\n  \"WH-06\",\n  \"WH-09\",\n  \"WH-12\",\n  \"WH-15\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_093",
        "instruction": "\n            You are tasked as a compliance officer for reviewing warehouse and product safety protocols.\n            Your objective is to find products needing special storage like \u201cTemp Control\u201d stored in owned warehouses that meet this specification.\n            Start by retrieving all company-owned warehouses and check which are equipped for temperature-controlled storage.\n            Then, identify all products requiring \u201cTemp Control\u201d as part of their storage needs.\n            Refer to inventory data to confirm these products are assigned to warehouses.\n            When the designated warehouse is owned and properly equipped for temperature control, deem the product compliant.\n            For such compliant products, append attribute notes \"STORED IN TEMP CONTROL OWNED WAREHOUSE\"\n            Finally, return the list of product IDs stored in such compliant owned warehouses.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "Temp"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "updates": {
                        "notes": "STORED IN TEMP CONTROL OWNED WAREHOUSE"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "CHEM-SOLV-K11"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"CHEM-SOLV-K11\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_094",
        "instruction": "\n            You are assigned as a compliance officer for reviewing warehouse and product safety protocols.\n            Your goal is to find products that need special storage conditions, for instance, \u201cTemp Control,\u201d but are not stored in suitable owned warehouses.\n            Initially, gather information on all company-owned warehouses and identify which are fitted for temperature-controlled storage.\n            Next, locate all products needing \u201cTemp Control.\n            \u201d\n            Review inventory records to verify these products are assigned to warehouses.\n            If any product is unassigned or transferred to an owned warehouse lacking temperature control capabilities, mark it.\n            For non-compliant products, update with attribute notes \"NOT STORED IN TEMP CONTROL OWNED WAREHOUSE\"\n            Finally, list the product IDs that do not have access to suitable owned warehouses for temperature-controlled storage.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Owned"
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "Temp"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-01"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-03"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-05"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-07"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-08"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-10"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-13"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-14"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "BEVG-WINE-P16",
                    "updates": {
                        "notes": "NOT STORED IN TEMP CONTROL OWNED WAREHOUSE"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "BEVG-WINE-P16"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"BEVG-WINE-P16\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_095",
        "instruction": "\n            You are charged as a compliance officer with reviewing warehouse and product safety protocols.\n            Your aim is to spot products requiring specific storage conditions such as \u201cTemp Control\u201d and housed in leased warehouses meeting the requirement.\n            Commence by identifying all leased warehouses, assessing which are equipped for temperature-controlled storage.\n            Then, highlight all products with \u201cTemp Control\u201d storage demands.\n            Use inventory data to judge if these products are allocated to warehouses.\n            If any product is located in a leased warehouse that satisfies temperature control requirements, confirm it as compliant.\n            For these compliant products, update with attribute notes \"STORED IN TEMP CONTROL LEASED WAREHOUSE\"\n            Finally, provide the list of product IDs located in such compliant leased warehouses.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Leased"
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "Temp"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "BEVG-WINE-P16",
                    "updates": {
                        "notes": "STORED IN TEMP CONTROL LEASED WAREHOUSE"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "BEVG-WINE-P16"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"BEVG-WINE-P16\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_096",
        "instruction": "\n            As a compliance officer reviewing warehouse and product safety protocols, your task is to pinpoint products that need temperature-controlled storage (\"Temp Control\") but are improperly stored in leased warehouses lacking this feature.\n            Begin by obtaining a list of all leased warehouses to establish which ones are equipped for temperature-controlled storage.\n            Subsequently, compile a list of all products that necessitate \"Temp Control\".\n            Utilize inventory records to verify if these products are allocated to a warehouse.\n            Should a product be unassigned to a warehouse or assigned to a leased warehouse without temperature control, it must be flagged.\n            For each such product, update its record to include a note with \"NOT STORED IN TEMP CONTROL LEASED WAREHOUSE\".\n            Conclude by providing the list of product IDs lacking suitable leased warehouse storage for temperature-controlled requirements.\n        ",
        "actions": [
            {
                "name": "GetWarehousesByOwnershipStatus",
                "arguments": {
                    "ownership_status": "Leased"
                },
            },
            {
                "name": "GetProductsByStorageRequirement",
                "arguments": {
                    "keyword": "Temp"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-02"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-04"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-06"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-09"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-12"
                },
            },
            {
                "name": "GetWarehouseById",
                "arguments": {
                    "warehouse_id": "WH-15"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "BEVG-WINE-P16"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0016"
                },
            },
            {
                "name": "FilterInventory",
                "arguments": {
                    "key": "sku",
                    "value": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "GetInventoryById",
                "arguments": {
                    "inventory_id": "INV-0011"
                },
            },
            {
                "name": "UpdateProduct",
                "arguments": {
                    "sku": "CHEM-SOLV-K11",
                    "updates": {
                        "notes": "NOT STORED IN TEMP CONTROL LEASED WAREHOUSE"
                    }
                },
            },
            {
                "name": "GetProductBySku",
                "arguments": {
                    "sku": "CHEM-SOLV-K11"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "CHEM-SOLV-K11"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"CHEM-SOLV-K11\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_097",
        "instruction": "\n            As a logistics performance manager evaluating carrier efficiency in the North American region, initiate by retrieving all active carriers covering \u201cNorth America.\n            \u201d\n            Following this, pinpoint all inbound shipments presently \u201cIn Transit\u201d associated with these carriers.\n            Modify these shipments by assigning the attribute carrier_coverage \"North America\".\n            Examine the specifics of these shipments and finally, compute the total value of the shipments to evaluate the cumulative worth of goods currently in transit with active North American carriers.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "North America"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "MTRL",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "MTRL"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "status",
                    "value": "In Transit"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "MTRL",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "EAC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "NAC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "ANAF",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "NSC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0008",
                    "updates": {
                        "carrier_coverage": "North America"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0008"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "updates": {
                        "carrier_coverage": "North America"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0008",
                        "SHIP-0021"
                    ]
                }
            }
        ],
        "outputs": [
                "610000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_098",
        "instruction": "\n            As a market analyst concentrating on inbound shipments, your initial goal is to ascertain the average weight of goods recently received.\n            Compute the average total weight in kg of these shipments.\n            Next, scrutinize shipments and the carriers linked to them, focusing solely on shipments connected with active carriers.\n            If a shipment's total weight with an active carrier is below the average, append the shipment with the note \"Lower than Average\".\n            Conversely, if the total weight exceeds the average, append the shipment with the note \"Higher than Average\".\n            Ultimately, provide the IDs of shipments amended with the note \"Lower than Average\".\n        ",
        "actions": [
            {
                "name": "GetShipmentsByStatus",
                "arguments": {
                    "status": "Received"
                },
            },
            {
                "name": "CalculateAggregate",
                "arguments": {
                    "agg": "avg",
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_weight_kg",
                    "list_of_ids": [
                        "SHIP-0002",
                        "SHIP-0007",
                        "SHIP-0017"
                    ]
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SKEX"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SWDL"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0017"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "AAC"
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0002",
                    "updates": {
                        "notes": "Higher than Average"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0007",
                    "updates": {
                        "notes": "Lower than Average"
                    }
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0017",
                    "updates": {
                        "notes": "Higher than Average"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0002"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0007"
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0017"
                },
            },
            {
                "name": "ReturnIds",
                "arguments": {
                    "list_of_ids": [
                        "SHIP-0007"
                    ]
                }
            }
        ],
        "outputs": [
                "[\n  \"SHIP-0007\"\n]"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_099",
        "instruction": "\n            As a logistics performance manager appraising carrier activities in the Asian region, start by gathering all active carriers with regional coverage including \u201cAsia.\n            \u201d\n            Then, identify all inbound shipments currently labeled as \u201cIn Transit\u201d serviced by these carriers.\n            Update these shipments by assigning the attribute carrier_coverage \"Asia\".\n            Examine the details of these shipments and, in conclusion, aggregate the value of these shipments to estimate the worth of goods currently in transit with active carriers serving Asia.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Asia"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "SCF",
                        "EAC",
                        "NAC"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "status",
                    "value": "In Transit"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "SCF",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "EAC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "NAC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "updates": {
                        "carrier_coverage": "Asia"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0021"
                    ]
                }
            }
        ],
        "outputs": [
                "550000"
        ]
    }
    ,
    {
        "annotator": ArpanMahatra1999,
        "user_id": "task_100",
        "instruction": "\n            As a logistics performance manager evaluating carrier operations in the European region, begin by retrieving all active carriers covering \u201cEurope.\n            \u201d\n            Then, ascertain all inbound shipments marked as \u201cIn Transit\u201d associated with these carriers.\n            Modify these shipments by setting the attribute carrier_coverage \"Europe\".\n            Review the shipment details and finally, calculate the cumulative value of these shipments to gauge the total worth of goods currently in transit with active carriers in Europe.\n        ",
        "actions": [
            {
                "name": "GetCarriersByRegion",
                "arguments": {
                    "region": "Europe"
                },
            },
            {
                "name": "GetActiveCarriers",
                "arguments": {
                    "list_of_scacs": [
                        "SCF",
                        "EAC",
                        "NAC",
                        "ANAF",
                        "NSC"
                    ]
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "SCF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "EAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NAC"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "ANAF"
                },
            },
            {
                "name": "GetCarrierByScac",
                "arguments": {
                    "carrier_scac": "NSC"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "status",
                    "value": "In Transit"
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "SCF",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "EAC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "NAC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "ANAF",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "FilterInboundShipments",
                "arguments": {
                    "key": "carrier_scac",
                    "value": "NSC",
                    "list_of_ids": [
                        "SHIP-0001",
                        "SHIP-0003",
                        "SHIP-0005",
                        "SHIP-0008",
                        "SHIP-0009",
                        "SHIP-0011",
                        "SHIP-0012",
                        "SHIP-0013",
                        "SHIP-0014",
                        "SHIP-0015",
                        "SHIP-0018",
                        "SHIP-0020",
                        "SHIP-0021",
                        "SHIP-0023",
                        "SHIP-0024",
                        "SHIP-0025",
                        "SHIP-0026",
                        "SHIP-0028"
                    ]
                },
            },
            {
                "name": "UpdateInboundShipment",
                "arguments": {
                    "shipment_id": "SHIP-0021",
                    "updates": {
                        "carrier_coverage": "Europe"
                    }
                },
            },
            {
                "name": "GetShipmentById",
                "arguments": {
                    "shipment_id": "SHIP-0021"
                },
            },
            {
                "name": "CalculateTotal",
                "arguments": {
                    "json": "inbound_shipments",
                    "key": "shipment_id",
                    "value": "total_value",
                    "list_of_ids": [
                        "SHIP-0021"
                    ]
                }
            }
        ],
        "outputs": [
                "550000"
        ]
    }
]
