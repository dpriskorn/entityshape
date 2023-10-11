from typing import Any, Dict
from unittest import TestCase

from entityshape.models.result import Result

hiking_path_with_1_missing_required_property: Dict[Any, Any] = {
    "error": "",
    "general": {},
    "name": "hiking path",
    "properties": {
        "P10467": {
            "name": "naturkartan.se ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P112": {
            "name": "founded by",
            "necessity": "optional",
            "response": "missing",
        },
        "P131": {
            "name": "located in the administrative territorial entity",
            "necessity": "required",
            "response": "present",
        },
        "P1343": {
            "name": "described by source",
            "necessity": "optional",
            "response": "missing",
        },
        "P137": {
            "name": "operator",
            "necessity": "optional",
            "response": "missing",
        },
        "P138": {
            "name": "named after",
            "necessity": "optional",
            "response": "missing",
        },
        "P1427": {
            "name": "start point",
            "necessity": "optional",
            "response": "missing",
        },
        "P1444": {
            "name": "destination point",
            "necessity": "optional",
            "response": "missing",
        },
        "P15": {
            "name": "route map",
            "necessity": "optional",
            "response": "missing",
        },
        "P1545": {
            "name": "series ordinal",
            "necessity": "optional",
            "response": "missing",
        },
        "P1552": {
            "name": "has quality",
            "necessity": "optional",
            "response": "missing",
        },
        "P1589": {
            "name": "lowest point",
            "necessity": "optional",
            "response": "missing",
        },
        "P17": {"name": "country", "necessity": "required", "response": "present"},
        "P18": {"name": "image", "necessity": "optional", "response": "missing"},
        "P1997": {
            "name": "Facebook Places ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P2043": {"name": "length", "necessity": "required", "response": "missing"},
        "P206": {
            "name": "located in or next to body of water",
            "necessity": "optional",
            "response": "missing",
        },
        "P214": {"name": "VIAF ID", "necessity": "optional", "response": "missing"},
        "P2347": {"name": "YSO ID", "necessity": "optional", "response": "missing"},
        "P242": {
            "name": "locator map image",
            "necessity": "optional",
            "response": "missing",
        },
        "P2671": {
            "name": "Google Knowledge Graph ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P2789": {
            "name": "connects with",
            "necessity": "optional",
            "response": "missing",
        },
        "P30": {
            "name": "continent",
            "necessity": "optional",
            "response": "missing",
        },
        "P3018": {
            "name": "located in protected area",
            "necessity": "optional",
            "response": "missing",
        },
        "P31": {
            "name": "instance of",
            "necessity": "optional",
            "response": "correct",
        },
        "P3173": {
            "name": "offers view on",
            "necessity": "optional",
            "response": "missing",
        },
        "P361": {"name": "part of", "necessity": "optional", "response": "missing"},
        "P373": {
            "name": "Commons category",
            "necessity": "optional",
            "response": "missing",
        },
        "P402": {
            "name": "OpenStreetMap relation ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P4552": {
            "name": "mountain range",
            "necessity": "optional",
            "response": "missing",
        },
        "P527": {
            "name": "has part(s)",
            "necessity": "optional",
            "response": "missing",
        },
        "P559": {
            "name": "terminus",
            "necessity": "optional",
            "response": "missing",
        },
        "P571": {
            "name": "inception",
            "necessity": "optional",
            "response": "missing",
        },
        "P609": {
            "name": "terminus location",
            "necessity": "optional",
            "response": "missing",
        },
        "P610": {
            "name": "highest point",
            "necessity": "optional",
            "response": "missing",
        },
        "P6104": {
            "name": "maintained by WikiProject",
            "necessity": "optional",
            "response": "missing",
        },
        "P625": {
            "name": "coordinate location",
            "necessity": "absent",
            "response": "missing",
        },
        "P646": {
            "name": "Freebase ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P691": {
            "name": "NL CR AUT ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P706": {
            "name": "located in/on physical feature",
            "necessity": "optional",
            "response": "missing",
        },
        "P7127": {
            "name": "AllTrails trail ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P7252": {
            "name": "degree of difficulty",
            "necessity": "optional",
            "response": "missing",
        },
        "P856": {
            "name": "official website",
            "necessity": "optional",
            "response": "missing",
        },
        "P910": {
            "name": "topic's main category",
            "necessity": "optional",
            "response": "missing",
        },
        "P973": {
            "name": "described at URL",
            "necessity": "optional",
            "response": "present",
        },
    },
    "schema": "E375",
    "statements": {
        "Q119845590$11794598-A67C-4978-8D1D-359B90E5EE15": {
            "necessity": "optional",
            "property": "P973",
            "response": "allowed",
        },
        "Q119845590$1CEFCE58-826A-4243-A9D2-CF47BF9F493E": {
            "necessity": "required",
            "property": "P131",
            "response": "allowed",
        },
        "Q119845590$72CEF06C-C5AE-40DE-AB61-D530914AFD4E": {
            "necessity": "optional",
            "property": "P31",
            "response": "correct",
        },
        "Q119845590$9C7FBBB4-7302-423F-AF51-C46A07F680CD": {
            "necessity": "required",
            "property": "P131",
            "response": "allowed",
        },
        "Q119845590$D036FE30-1DFD-461A-8AA2-AA0CB977E22D": {
            "necessity": "required",
            "property": "P17",
            "response": "allowed",
        },
    },
    "validity": {},
}  # P2043 length is missing
campsite_missing_correct_p31: Dict[Any, Any] = {
    "error": "",
    "general": {},
    "name": "campsite",
    "properties": {
        "P10467": {
            "name": "naturkartan.se ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P11177": {
            "name": "Camp Wild ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P131": {
            "name": "located in the administrative territorial entity",
            "necessity": "required",
            "response": "present",
        },
        "P137": {
            "name": "operator",
            "necessity": "required",
            "response": "present",
        },
        "P138": {
            "name": "named after",
            "necessity": "optional",
            "response": "missing",
        },
        "P1448": {
            "name": "official name",
            "necessity": "optional",
            "response": "missing",
        },
        "P17": {"name": "country", "necessity": "required", "response": "present"},
        "P18": {"name": "image", "necessity": "optional", "response": "missing"},
        "P206": {
            "name": "located in or next to body of water",
            "necessity": "optional",
            "response": "missing",
        },
        "P242": {
            "name": "locator map image",
            "necessity": "optional",
            "response": "missing",
        },
        "P2670": {
            "name": "has part(s) of the class",
            "necessity": "optional",
            "response": "missing",
        },
        "P276": {
            "name": "location",
            "necessity": "optional",
            "response": "present",
        },
        "P30": {
            "name": "continent",
            "necessity": "optional",
            "response": "missing",
        },
        "P3018": {
            "name": "located in protected area",
            "necessity": "optional",
            "response": "missing",
        },
        "P31": {
            "name": "instance of",
            "necessity": "required",
            "response": "not enough correct statements",
        },
        "P3173": {
            "name": "offers view on",
            "necessity": "optional",
            "response": "missing",
        },
        "P373": {
            "name": "Commons category",
            "necessity": "optional",
            "response": "missing",
        },
        "P402": {
            "name": "OpenStreetMap relation ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P4552": {
            "name": "mountain range",
            "necessity": "optional",
            "response": "missing",
        },
        "P527": {
            "name": "has part(s)",
            "necessity": "optional",
            "response": "missing",
        },
        "P571": {
            "name": "inception",
            "necessity": "optional",
            "response": "missing",
        },
        "P5775": {
            "name": "image of interior",
            "necessity": "absent",
            "response": "missing",
        },
        "P625": {
            "name": "coordinate location",
            "necessity": "required",
            "response": "present",
        },
        "P706": {
            "name": "located in/on physical feature",
            "necessity": "optional",
            "response": "missing",
        },
        "P7418": {
            "name": "image of frontside",
            "necessity": "optional",
            "response": "missing",
        },
        "P8517": {"name": "view", "necessity": "optional", "response": "missing"},
        "P856": {
            "name": "official website",
            "necessity": "optional",
            "response": "missing",
        },
        "P912": {
            "name": "has facility",
            "necessity": "optional",
            "response": "missing",
        },
        "P9676": {
            "name": "Vindskyddskartan.se ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P973": {
            "name": "described at URL",
            "necessity": "optional",
            "response": "present",
        },
    },
    "schema": "E376",
    "statements": {
        "Q119853974$20823AE2-6F1A-43FB-9C9C-A6C2CC772446": {
            "necessity": "required",
            "property": "P137",
            "response": "allowed",
        },
        "Q119853974$3F1F91A9-693C-41AA-A5C7-54E711D83594": {
            "necessity": "required",
            "property": "P17",
            "response": "allowed",
        },
        "Q119853974$4A29484F-6C84-4B5A-B9E9-25344162CFCB": {
            "necessity": "required",
            "property": "P625",
            "response": "allowed",
        },
        "Q119853974$4BCAA6A7-8857-4056-B286-7B646A2D72C9": {
            "necessity": "required",
            "property": "P131",
            "response": "allowed",
        },
        "Q119853974$8E8612BE-78F7-463A-8E35-96F53277E3B4": {
            "necessity": "optional",
            "property": "P276",
            "response": "allowed",
        },
        "Q119853974$AA270DBF-B117-45DD-AF68-8F1A7AFC56F1": {
            "necessity": "required",
            "property": "P31",
            "response": "allowed",
        },
        "Q119853974$C25AF244-F0D9-4E19-8126-42092C0FA4FB": {
            "necessity": "optional",
            "property": "P973",
            "response": "allowed",
        },
        "Q119853974$CD71CE83-F045-486B-873F-F7A8FB437E2A": {
            "necessity": "required",
            "property": "P131",
            "response": "allowed",
        },
    },
    "validity": {},
}
campsite_not_allowed_p625: Dict[Any, Any] = {
    "error": "",
    "general": {},
    "name": "hiking path",
    "properties": {
        "P10467": {
            "name": "naturkartan.se ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P112": {
            "name": "founded by",
            "necessity": "optional",
            "response": "missing",
        },
        "P131": {
            "name": "located in the administrative territorial entity",
            "necessity": "required",
            "response": "present",
        },
        "P1343": {
            "name": "described by source",
            "necessity": "optional",
            "response": "missing",
        },
        "P137": {
            "name": "operator",
            "necessity": "optional",
            "response": "present",
        },
        "P138": {
            "name": "named after",
            "necessity": "optional",
            "response": "missing",
        },
        "P1427": {
            "name": "start point",
            "necessity": "optional",
            "response": "missing",
        },
        "P1444": {
            "name": "destination point",
            "necessity": "optional",
            "response": "missing",
        },
        "P15": {
            "name": "route map",
            "necessity": "optional",
            "response": "missing",
        },
        "P1545": {
            "name": "series ordinal",
            "necessity": "optional",
            "response": "missing",
        },
        "P1552": {
            "name": "has quality",
            "necessity": "optional",
            "response": "missing",
        },
        "P1589": {
            "name": "lowest point",
            "necessity": "optional",
            "response": "missing",
        },
        "P17": {"name": "country", "necessity": "required", "response": "present"},
        "P18": {"name": "image", "necessity": "optional", "response": "missing"},
        "P1997": {
            "name": "Facebook Places ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P2043": {"name": "length", "necessity": "required", "response": "missing"},
        "P206": {
            "name": "located in or next to body of water",
            "necessity": "optional",
            "response": "missing",
        },
        "P214": {"name": "VIAF ID", "necessity": "optional", "response": "missing"},
        "P2347": {"name": "YSO ID", "necessity": "optional", "response": "missing"},
        "P242": {
            "name": "locator map image",
            "necessity": "optional",
            "response": "missing",
        },
        "P2671": {
            "name": "Google Knowledge Graph ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P276": {"name": "location", "necessity": "absent"},
        "P2789": {
            "name": "connects with",
            "necessity": "optional",
            "response": "missing",
        },
        "P30": {
            "name": "continent",
            "necessity": "optional",
            "response": "missing",
        },
        "P3018": {
            "name": "located in protected area",
            "necessity": "optional",
            "response": "missing",
        },
        "P31": {
            "name": "instance of",
            "necessity": "optional",
            "response": "present",
        },
        "P3173": {
            "name": "offers view on",
            "necessity": "optional",
            "response": "missing",
        },
        "P361": {"name": "part of", "necessity": "optional", "response": "missing"},
        "P373": {
            "name": "Commons category",
            "necessity": "optional",
            "response": "missing",
        },
        "P402": {
            "name": "OpenStreetMap relation ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P4552": {
            "name": "mountain range",
            "necessity": "optional",
            "response": "missing",
        },
        "P527": {
            "name": "has part(s)",
            "necessity": "optional",
            "response": "present",
        },
        "P559": {
            "name": "terminus",
            "necessity": "optional",
            "response": "missing",
        },
        "P571": {
            "name": "inception",
            "necessity": "optional",
            "response": "missing",
        },
        "P609": {
            "name": "terminus location",
            "necessity": "optional",
            "response": "missing",
        },
        "P610": {
            "name": "highest point",
            "necessity": "optional",
            "response": "missing",
        },
        "P6104": {
            "name": "maintained by WikiProject",
            "necessity": "optional",
            "response": "missing",
        },
        "P625": {
            "name": "coordinate location",
            "necessity": "absent",
            "response": "too many statements",
        },
        "P646": {
            "name": "Freebase ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P691": {
            "name": "NL CR AUT ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P706": {
            "name": "located in/on physical feature",
            "necessity": "optional",
            "response": "missing",
        },
        "P7127": {
            "name": "AllTrails trail ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P7252": {
            "name": "degree of difficulty",
            "necessity": "optional",
            "response": "missing",
        },
        "P856": {
            "name": "official website",
            "necessity": "optional",
            "response": "missing",
        },
        "P910": {
            "name": "topic's main category",
            "necessity": "optional",
            "response": "missing",
        },
        "P912": {"name": "has facility", "necessity": "absent"},
        "P973": {
            "name": "described at URL",
            "necessity": "optional",
            "response": "present",
        },
    },
    "schema": "E375",
    "statements": {
        "Q119853967$36193CA1-6DF5-4DAC-910E-0319812671FB": {
            "necessity": "required",
            "property": "P131",
            "response": "allowed",
        },
        "Q119853967$43477af1-49e1-e0fd-8672-fbad6c66dd96": {
            "necessity": "optional",
            "property": "P527",
            "response": "allowed",
        },
        "Q119853967$5C65C2A6-DA72-4C71-83E2-0C626C906506": {
            "property": "P276",
            "response": "not in schema",
        },
        "Q119853967$5DF7E848-400D-4AEE-B2AD-A06D92ACA2DD": {
            "necessity": "absent",
            "property": "P625",
            "response": "allowed",
        },
        "Q119853967$736c7261-4e8c-e754-e817-e8b253ae5e7b": {
            "property": "P912",
            "response": "not in schema",
        },
        "Q119853967$7A4E524F-12CE-40C1-B709-4876A2C465D6": {
            "necessity": "optional",
            "property": "P137",
            "response": "allowed",
        },
        "Q119853967$7F83F435-83AC-4210-A717-ED3DE033319D": {
            "necessity": "required",
            "property": "P17",
            "response": "allowed",
        },
        "Q119853967$874d280c-427c-8c9d-8ccb-3bd107e7d6a4": {
            "necessity": "optional",
            "property": "P527",
            "response": "allowed",
        },
        "Q119853967$C30A3085-F06D-4834-A887-CDDBC314EE7F": {
            "necessity": "required",
            "property": "P131",
            "response": "allowed",
        },
        "Q119853967$C98E6C4A-98F8-47EA-8791-C4C85262FC9B": {
            "necessity": "optional",
            "property": "P973",
            "response": "allowed",
        },
        "Q119853967$D8462BF0-2599-4F62-8147-E84465529B19": {
            "necessity": "optional",
            "property": "P31",
            "response": "allowed",
        },
    },
    "validity": {},
}
party_member_missing_p37: Dict[Any, Any] = {
    "general": {},
    "properties": {
        "P21": {
            "name": "sex or gender",
            "necessity": "required",
            "response": "correct",
        },
        "P31": {"name": "instance of", "necessity": "required", "response": "correct"},
        "P102": {
            "name": "member of political party",
            "necessity": "required",
            "response": "present",
        },
        "P569": {
            "name": "date of birth",
            "necessity": "required",
            "response": "present",
        },
        "P570": {
            "name": "date of death",
            "necessity": "optional",
            "response": "present",
        },
        "P27": {
            "name": "country of citizenship",
            "necessity": "required",
            "response": "correct",
        },
        "P106": {"name": "occupation", "necessity": "required", "response": "correct"},
        "P735": {"name": "given name", "necessity": "required", "response": "present"},
        "P18": {"name": "image", "necessity": "required", "response": "present"},
        "P1343": {
            "name": "described by source",
            "necessity": "required",
            "response": "present",
        },
        "P39": {
            "name": "position held",
            "necessity": "optional",
            "response": "not enough correct statements",
        },
        "P119": {
            "name": "place of burial",
            "necessity": "optional",
            "response": "present",
        },
        "P1412": {
            "name": "languages spoken, written or signed",
            "necessity": "required",
            "response": "correct",
        },
        "P937": {
            "name": "work location",
            "necessity": "required",
            "response": "correct",
        },
        "P1559": {"name": "name in native language", "necessity": "absent"},
        "P3222": {"name": "NE.se ID", "necessity": "absent"},
        "P19": {
            "name": "place of birth",
            "necessity": "required",
            "response": "present",
        },
        "P20": {
            "name": "place of death",
            "necessity": "optional",
            "response": "present",
        },
        "P734": {"name": "family name", "necessity": "required", "response": "present"},
        "P373": {
            "name": "Commons category",
            "necessity": "required",
            "response": "present",
        },
        "P4602": {"name": "date of burial or cremation", "necessity": "absent"},
        "P646": {"name": "Freebase ID", "necessity": "absent"},
        "P4819": {
            "name": "Swedish Portrait Archive ID",
            "necessity": "required",
            "response": "present",
        },
        "P3368": {"name": "Prabook ID", "necessity": "absent"},
        "P2600": {
            "name": "Geni.com profile ID",
            "necessity": "optional",
            "response": "present",
        },
        "P2561": {"name": "name", "necessity": "absent"},
        "P551": {"name": "residence", "necessity": "optional", "response": "present"},
        "P509": {
            "name": "cause of death",
            "necessity": "optional",
            "response": "present",
        },
        "P535": {
            "name": "Find a Grave memorial ID",
            "necessity": "optional",
            "response": "present",
        },
        "P109": {"name": "signature", "necessity": "optional", "response": "present"},
        "P1442": {
            "name": "image of grave",
            "necessity": "optional",
            "response": "present",
        },
        "P1196": {
            "name": "manner of death",
            "necessity": "optional",
            "response": "missing",
        },
        "P3373": {"name": "sibling", "necessity": "optional", "response": "missing"},
        "P22": {"name": "father", "necessity": "optional", "response": "missing"},
        "P25": {"name": "mother", "necessity": "optional", "response": "missing"},
        "P40": {"name": "child", "necessity": "optional", "response": "missing"},
        "P97": {"name": "noble title", "necessity": "optional", "response": "missing"},
        "P5056": {
            "name": "patronym or matronym for this person",
            "necessity": "optional",
            "response": "missing",
        },
        "P512": {
            "name": "academic degree",
            "necessity": "optional",
            "response": "missing",
        },
        "P69": {"name": "educated at", "necessity": "optional", "response": "missing"},
        "P2949": {
            "name": "WikiTree person ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P9713": {
            "name": "Swedish National Archive agent ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P485": {"name": "archives at", "necessity": "optional", "response": "missing"},
        "P9495": {
            "name": "National Historical Museums of Sweden ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P5101": {
            "name": "Swedish Literature Bank Author ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P3217": {
            "name": "Dictionary of Swedish National Biography ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P4963": {
            "name": "Svenskt kvinnobiografiskt lexikon ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P6821": {
            "name": "Uppsala University Alvin ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P5587": {"name": "Libris-URI", "necessity": "optional", "response": "missing"},
        "P7847": {
            "name": "DigitaltMuseum ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P1248": {
            "name": "KulturNav-ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P5259": {
            "name": "Swedish Gravestone ID",
            "necessity": "optional",
            "response": "missing",
        },
        "P3618": {
            "name": "base salary",
            "necessity": "optional",
            "response": "missing",
        },
    },
    "statements": {
        "q4802448$2B153142-5757-45BD-BB8E-EDBD6C505394": {
            "property": "P21",
            "necessity": "required",
            "response": "correct",
        },
        "Q4802448$6F4E8AEC-14A1-4AD0-AF79-AC26414E154C": {
            "property": "P31",
            "necessity": "required",
            "response": "correct",
        },
        "Q4802448$0484EB04-FF7F-4E06-8E30-EC45D00D5E6B": {
            "property": "P102",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$CE9C69A0-A0D2-498E-8159-3A4144412F64": {
            "property": "P569",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$396CFEEE-BDB5-40C3-85D4-A30C9CF6DB56": {
            "property": "P570",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$FFB1A0F8-D15F-41F0-958E-1B43F631558A": {
            "property": "P27",
            "necessity": "required",
            "response": "correct",
        },
        "Q4802448$D26A0B14-EA5B-4A9A-A5C0-5A20FD912612": {
            "property": "P106",
            "necessity": "required",
            "response": "correct",
        },
        "Q4802448$0B0473FD-7EF8-421D-9C85-C4D2D95F3FA2": {
            "property": "P106",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$4DBC9F21-F384-4DCB-B040-A6E5FA45D9D8": {
            "property": "P735",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$0277dd51-445e-5014-d5bf-2cffc1eb8e96": {
            "property": "P735",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$c5afc898-4b44-1e0f-370b-0952661b2263": {
            "property": "P735",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$F2F3B54D-1B41-4760-A129-98F292C4FEA8": {
            "property": "P18",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$D767380D-21DD-411B-B742-0FC06FCFAB5A": {
            "property": "P1343",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$584F3970-E62D-4F31-A925-2B7D9B3F9420": {
            "property": "P1343",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$ed53e939-46b3-9361-db57-9505ebc69970": {
            "property": "P1343",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$C2F6DC9B-9E34-436F-92BA-FBAF35678CA0": {
            "property": "P39",
            "necessity": "optional",
            "response": "missing",
        },
        "Q4802448$95649645-9282-47BF-B7CE-9F795A2562C0": {
            "property": "P119",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$51FCEBB3-4FB8-4EFB-95B7-0AA89B2F6137": {
            "property": "P1412",
            "necessity": "required",
            "response": "correct",
        },
        "Q4802448$7D198758-266A-401A-9AC1-6D6FA5E83FD4": {
            "property": "P937",
            "necessity": "required",
            "response": "correct",
        },
        "Q4802448$15A1D0F3-4843-4F01-A4ED-B412AF8D08A5": {
            "property": "P1559",
            "response": "not in schema",
        },
        "Q4802448$2C5BE492-0778-484F-8B9E-4FE2CFA57756": {
            "property": "P3222",
            "response": "not in schema",
        },
        "Q4802448$6ac93515-48dc-1964-cacf-e06c6c4be798": {
            "property": "P19",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$cf60fb00-4bf4-bfea-6b42-ace7fc8dc36d": {
            "property": "P20",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$0cb0962d-4d3a-4fdf-d784-d803348586bb": {
            "property": "P20",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$06F15D7F-E0CC-4704-BE7D-F1134E051485": {
            "property": "P734",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$04950009-6DAF-42C1-89E2-7093B26DF80C": {
            "property": "P373",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$22AA2038-D33F-4DA3-B725-C0A162A9A39D": {
            "property": "P4602",
            "response": "not in schema",
        },
        "Q4802448$FE68BD20-0633-4D7C-9BBB-1A65C60FAD73": {
            "property": "P646",
            "response": "not in schema",
        },
        "Q4802448$501fe9ac-4706-a3f6-224b-3c7da9ac8131": {
            "property": "P4819",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$bea3ccd9-4d8f-30c2-684b-e8590cfb7bf0": {
            "property": "P4819",
            "necessity": "required",
            "response": "allowed",
        },
        "Q4802448$BA25471E-6D65-4040-B541-04CBB60D8089": {
            "property": "P3368",
            "response": "not in schema",
        },
        "Q4802448$7EB5C10C-AF05-4CD2-9ECE-38C56FB0D72E": {
            "property": "P2600",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$FDE6987A-301E-4E67-B8E0-C035FA45FC63": {
            "property": "P2561",
            "response": "not in schema",
        },
        "Q4802448$db6affac-431e-5f76-6890-b29f00e90397": {
            "property": "P551",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$315e1e37-401d-1460-c876-f31c1071f6ed": {
            "property": "P509",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$8d6aa8d9-4a97-40bc-21fa-f47dbb1ce697": {
            "property": "P535",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$44d2c513-45d2-ebad-2181-32ffea9cf717": {
            "property": "P109",
            "necessity": "optional",
            "response": "allowed",
        },
        "Q4802448$103E30B9-C4F0-48DC-9145-8F00F3DB16DF": {
            "property": "P1442",
            "necessity": "optional",
            "response": "allowed",
        },
    },
}
furrywikibase_convention_with_1_missing_required_property: Dict[Any, Any] = {
    "error": "",
    "general": {},
    "name": "ConFuzzled 2019",
    "properties": {
        "P1": {
            "name": "instance of",
            "necessity": "required",
            "response": "missing",
        }
    },
    "schema": "E1",
    "statements": {},
    "validity": {},
}  # P1 instance of is missing (this is fabricated for test purposes)


class TestResult(TestCase):
    def setUp(self) -> None:
        self.hiking_path_with_1_missing_required_property_result = Result(
            **hiking_path_with_1_missing_required_property
        )
        self.hiking_path_with_1_missing_required_property_result.analyze()
        self.campsite_missing_correct_p31_result = Result(
            **campsite_missing_correct_p31
        )
        self.campsite_missing_correct_p31_result.analyze()
        self.campsite_not_allowed_p625_result = Result(**campsite_not_allowed_p625)
        self.campsite_not_allowed_p625_result.analyze()
        self.party_member_missing_p37_result = Result(**party_member_missing_p37)
        self.party_member_missing_p37_result.analyze()
        self.furrywikibase_convention_with_1_missing_required_property_result = Result(
            **furrywikibase_convention_with_1_missing_required_property
        )
        self.furrywikibase_convention_with_1_missing_required_property_result.analyze()

    def test___find_properties_with_too_many_statements__zero(self):
        assert (
            len(
                self.hiking_path_with_1_missing_required_property_result.properties_with_too_many_statements
            )
            == 0
        )

    def test__find_required_properties__three(self):
        assert (
            len(
                self.hiking_path_with_1_missing_required_property_result.required_properties
            )
            == 3
        )

    def test__find_missing_properties__(self):
        assert (
            len(
                self.hiking_path_with_1_missing_required_property_result.missing_properties
            )
            == 41
        )

    def test__find_required_properties_that_are_missing__(self):
        assert (
            len(
                self.hiking_path_with_1_missing_required_property_result.required_properties_that_are_missing
            )
            == 1
        )

    def test__find_optional_properties_that_are_missing__(self):
        assert (
            len(
                self.hiking_path_with_1_missing_required_property_result.optional_properties_that_are_missing
            )
            == 40
        )

    def test____find_incorrect_statements__(self):
        assert (
            len(
                self.hiking_path_with_1_missing_required_property_result.incorrect_statements
            )
            == 0
        )

    def test__find_properties_with_not_enough_correct_statements__(self):
        assert (
            len(
                self.campsite_missing_correct_p31_result.properties_without_enough_correct_statements
            )
            == 1
        )
        assert (
            self.party_member_missing_p37_result.properties_without_enough_correct_statements
            == {"P39"}
        )

    def test__find_statements_with_property_that_is_not_allowed__(self):
        assert (
            len(
                self.campsite_not_allowed_p625_result.statements_with_property_that_is_not_allowed
            )
            == 1
        )

    def test__repr__hiking_path_with_1_missing_required_property_result(self):
        assert (
            repr(self.hiking_path_with_1_missing_required_property_result)
            == "Valid: False\nRequired properties that are missing: length (P2043)"
        )

    def test__repr__campsite_not_allowed_p625_result(self):
        assert repr(self.campsite_not_allowed_p625_result) == (
            "Valid: False\n"
            "Properties with too many statements: coordinate location (P625)\n"
            "Required properties that are missing: length (P2043)"
        )

    def test__repr__party_member_missing_p37_result(self):
        assert repr(self.party_member_missing_p37_result) == (
            "Valid: False\n"
            "Properties without enough correct statements: position held (P39)"
        )

    def test__repr__campsite_missing_correct_p31_result(self):
        assert (
            repr(self.campsite_missing_correct_p31_result)
            == "Valid: False\nProperties without enough correct statements: instance of (P31)"
        )

    def test_danish_labels_in_result_output(self):
        self.party_member_missing_p37_result.lang = "da"
        assert repr(self.party_member_missing_p37_result) == (
            "Valid: False\nProperties without enough "
            "correct statements: embede (P39)"
        )

    def test_furrywikibase_convention_missing_p1(self):

        self.furrywikibase_convention_with_1_missing_required_property_result.wikibase_url = (
            "https://furry.wikibase.cloud"
        )
        self.furrywikibase_convention_with_1_missing_required_property_result.mediawiki_api_url = (
            "https://furry.wikibase.cloud/w/api.php"
        )
        assert (
            repr(self.furrywikibase_convention_with_1_missing_required_property_result)
            == "Valid: False\nRequired properties that are missing: instance of (P1)"
        )
