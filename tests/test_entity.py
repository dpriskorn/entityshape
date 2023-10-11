from unittest import TestCase

from entityshape import Entity, EntityIdError, LangError
from entityshape.exceptions import MissingInformationError


class TestEntity(TestCase):
    def test_invalid_lang(self):
        # es = EntityShape(eid="E376", entity_ids=[])
        # es.download_schema()
        e = Entity(
            eid="E376",
            lang="",
            entity_id="Q119853967",
            entity_data={},
            entity_schema_data={},
        )
        with self.assertRaises(LangError):
            e.check_and_validate()
        # assert e.result.is_valid is True
        # print(e.result)
        # assert e.result != {}

    def test_valid_lang(self):
        # es = EntityShape(eid="E376", entity_ids=[])
        # es.download_schema()
        e = Entity(
            eid="E376",
            lang="en",
            entity_id="Q119853967",
            entity_data={},
            entity_schema_data={},
        )
        with self.assertRaises(MissingInformationError):
            e.check_and_validate()

    def test_get_result_invalid_entity_id(self):
        e = Entity(
            eid="E1",
            lang="en",
            entity_id="qqqqQ1",
            entity_data={},
            entity_schema_data={},
        )
        with self.assertRaises(EntityIdError):
            e.check_and_validate()
        # print(e.result)
        # assert e.result != {}
