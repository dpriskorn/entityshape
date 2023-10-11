import re
from re import Pattern
from typing import Any, Dict

import requests
from pydantic import BaseModel

from entityshape.exceptions import EntityIdError, LangError
from entityshape.models.compareshape import CompareShape
from entityshape.models.result import Result
from entityshape.models.shape import Shape


class Entity(BaseModel):
    entity_id: str
    entity_id_regex: Pattern = re.compile(r"[QL]\d+")
    entity_data: Dict[str, Any]
    entity_schema_data: Dict[str, Any]
    eid: str  # entityshape
    lang: str = "en"  # language defaults to English
    result: Result = Result()
    compare_shape_result: Dict[str, Any] = {}
    wikibase_url: str = "http://www.wikidata.org"
    mediawiki_api_url: str = "https://www.wikidata.org/w/api.php"
    user_agent: str = "entityshape (https://github.com/dpriskorn/entityshape)"

    def __check_inputs__(self):
        if not 2 <= len(self.lang) <= 3:
            raise LangError("Language code is not correct length")
        if not re.match(self.entity_id_regex, self.entity_id):
            raise EntityIdError(
                "The entity id has to be Q or L followed by only numbers like this: Q100"
            )

    def __validate__(self):
        shape: Shape = Shape(
            entity_schema_id=self.eid,
            language=self.lang,
            entity_schema_data=self.entity_schema_data,
        )
        comparison: CompareShape = CompareShape(
            shape=shape.get_schema_shape(),
            entity=self.entity_id,
            entity_data=self.entity_data,
            language=self.lang,
            wikibase_url=self.wikibase_url,
            mediawiki_api_url=self.mediawiki_api_url,
        )
        self.compare_shape_result = {
            "general": comparison.get_general(),
            "properties": comparison.get_properties(),
            "statements": comparison.get_statements(),
        }

    def __parse_result__(self) -> None:
        if self.compare_shape_result:
            self.result = Result(**self.compare_shape_result)
            self.result.lang = self.lang
            self.result.analyze()

    def check_and_validate(self) -> None:
        """This method checks if we got the 3 parameters we need and
        gets the results and return them"""
        self.__check_inputs__()
        self.__validate__()
        self.__parse_result__()

    def __get_entity_data__(self):
        """Only used for testing"""
        url = f"{self.wikibase_url}/wiki/Special:EntityData/{self.entity_id}.json"
        response = requests.get(url)
        self.entity_data = response.json()
