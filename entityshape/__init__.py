import asyncio
import logging
import re
from re import Pattern
from typing import Any, Dict, List

import aiohttp
import requests
from pydantic import BaseModel
from rich.console import Console

from entityshape.exceptions import (
    ApiError,
    EidError,
    EntityIdError,
    LangError,
    NoEntitySchemaDataError,
    WikibaseEntitySchemaDownloadError,
)
from entityshape.models.entity import Entity

console = Console()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class EntityShape(BaseModel):
    """Downloads and validates Wikidata entities"""

    entity_ids: List[str]
    eid: str  # entityshape
    lang: str = "en"  # language defaults to English
    eid_regex: Pattern = re.compile(r"E\d+")
    wikibase_url: str = "http://www.wikidata.org"
    mediawiki_api_url: str = "https://www.wikidata.org/w/api.php"
    user_agent: str = "entityshape (https://github.com/dpriskorn/entityshape)"
    entities: List[Entity] = []
    entity_schema_data: Dict[str, Any] = {}

    def __check_inputs__(self):
        if not 2 <= len(self.lang) <= 3:
            raise LangError("Language code is not correct length")
        if not re.match(self.eid_regex, self.eid):
            raise EidError("EID has to be E followed by only numbers like this: E100")
        if not self.entity_ids:
            raise EntityIdError("We need entity ids")
        # if not re.match(self.entity_id_regex, self.entity_id):
        #     raise QidError("QID has to be Q followed by only numbers like this: Q100")

    def download_and_validate(self):
        self.__check_inputs__()  # Check if inputs are valid
        self.download_schema()
        if not self.entity_schema_data:
            raise NoEntitySchemaDataError("Got no entity schema data from Wikidata")
        with console.status("Downloading entity json"):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.__download_json__())
        print(f"Downloaded {len(self.entities)} entities")
        if self.entities:
            with console.status("Validating entities"):
                [entity.check_and_validate() for entity in self.entities]
            print("Validation finished")
        else:
            print("No entities to validate")

    async def __download_json__(self) -> None:
        """Get all the JSON data we need asynchronously"""
        logger.debug("__download_json__: running")
        async with aiohttp.ClientSession() as session:
            # TODO add user agent
            # Create tasks for downloading JSON data for each entity_id
            tasks = [
                self._get_entity_json(entity_id, session)
                for entity_id in self.entity_ids
            ]

            # Gather and wait for all tasks to complete
            await asyncio.gather(*tasks)
            # self.json_responses = await asyncio.gather(*tasks)
            # Handle results as needed
            # We don't handle the results for now.

    async def _get_entity_json(self, entity_id: str, session) -> None:
        """
        Downloads the entity from Wikidata asynchronously
        """
        logger.debug("_get_entity_json: running")
        url = f"{self.wikibase_url}/wiki/Special:EntityData/{entity_id}.json"

        async with session.get(url) as response:
            if response.status == 200:
                entity_data = await response.json()
                self.entities.append(
                    Entity(
                        entity_id=entity_id,
                        entity_data=entity_data,
                        eid=self.eid,
                        entity_schema_data=self.entity_schema_data,
                    )
                )
            else:
                raise WikibaseEntitySchemaDownloadError(
                    f"Got {response.status} from {url}. "
                    f"Please check that the configuration is correct"
                )

    def download_schema(self):
        """
        Downloads the schema from wikidata
        """
        url: str = f"https://www.wikidata.org/wiki/EntitySchema:{self.eid}?action=raw"
        # todo add user agent
        response = requests.get(url)
        if response.status_code == 404:
            raise WikibaseEntitySchemaDownloadError()
        self.entity_schema_data: dict = response.json()
