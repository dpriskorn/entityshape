import asyncio
import time
from unittest import TestCase

from entityshape import EntityShape, WikibaseEntitySchemaDownloadError
from entityshape.models.result import Result

# from rich.console import Console


class TestEntityShape(TestCase):

    # TODO this fails because of ?
    # def test_get_result_valid(self):
    #     e = EntityShape(eid="E376", lang="en", qid="Q96308969")
    #     e.get_result()
    #     print(e.result)
    #     assert isinstance(e.result, Result)
    #     assert e.result.is_valid is True

    # def test_get_result_invalid_missing_operator(self):
    #     e = EntityShape(eid="E376", lang="en", entity_id="Q96308969")
    #     e.validate_and_get_result()
    #     # print(e.result)
    #     assert isinstance(e.result, Result)
    #     assert e.result.is_valid is False
    #     assert e.result.required_properties_that_are_missing == {"P137"}

    # this fails because of https://github.com/dpriskorn/entityshape/issues/2
    # def test_get_result_invalid_wrong_schema(self):
    #     e = EntityShape(eid="E375", lang="en", entity_id="Q119853967")
    #     e.get_result()
    #     print(e.result)
    #     assert isinstance(e.result, Result)
    #     assert e.result.is_valid is False
    #     assert e.result.required_properties_that_are_missing == {"P2043"}
    #     assert e.result.properties_that_are_not_allowed == {"P912", "P625", "P276"}

    # def test_get_result_missing_statement_response(self):
    #     e = EntityShape(eid="E395", lang="en", entity_id="Q4802448")
    #     e.validate_and_get_result()
    #     # print(e.compare_shape_result)
    #     # console = Console()
    #     # console.print(e.result)
    #     assert isinstance(e.result, Result)
    #     assert e.result.is_valid is False
    #     assert e.result.properties_without_enough_correct_statements == {"P39"}
    #
    # def test_get_result_weird_statement_response_party_person(self):
    #     e = EntityShape(eid="E395", lang="en", entity_id="Q20727")
    #     e.validate_and_get_result()
    #     assert isinstance(e.result, Result)
    #     assert e.result.is_valid is True
    #
    # def test_lexeme(self):
    #     # wbi_config['USER_AGENT'] = 'WikibaseIntegrator in PAWS by So9q'
    #     # wbi = WikibaseIntegrator()
    #     # # This query was build in a few seconds using https://query.wikidata.org/querybuilder/?uselang=en :)
    #     # results = execute_sparql_query("""
    #     # SELECT ?lexemeId ?lemma WHERE {
    #     #   ?lexemeId dct:language wd:Q9027;
    #     #             wikibase:lexicalCategory wd:Q1084;
    #     #             wikibase:lemma ?lemma.
    #     # }
    #     # limit 10
    #     # """)
    #     # bindings = results["results"]["bindings"]
    #     # print(f"Found {len(bindings)} results")
    #     # count = 1
    #     # for result in bindings:
    #     #     print(result)
    #     #     # Get the entity id from the URI
    #     #     entity_id = result["lexemeId"]["value"].split("/")[-1]
    #     #     print(f"Working on: {entity_id}")
    #     #     entity = wbi.lexeme.get(entity_id)
    #     e = EntityShape(entity_id="L41172", eid="E34", lang="en")
    #     e.validate_and_get_result()
    #     print(e.result)
    #     # try:
    #     #     result = e.validate_and_get_result()
    #     #     # Ignore the invalid shelters missing an operator P137
    #     #     if result.is_valid is False and result.required_properties_that_are_missing == {"P137"}:
    #     #         print("Skipping item only missing an operator")
    #     #     # Ignore the invalid items with too many P625
    #     #     elif result.is_valid is False and result.properties_with_too_many_statements == {"P625"}:
    #     #         print("Skipping item that only invalidates because it has a coordinate")
    #     #     elif result.is_valid is True:
    #     #         print("Skipping valid item - they are boring!")
    #     #     else:
    #     #         print(repr(result) + f"\nSee {entity.get_entity_url()}")
    #     # except KeyError:
    #     #     print(
    #     #         f"Got a keyerror for the entity {entity_id}, this is a known bug with entityshape, see https://github.com/dpriskorn/entityshape/issues/2")
    #
    # def test_labels_from_custom_wikibase_valid_qid(self):
    #     eid = "E1"  # see https://furry.wikibase.cloud/wiki/EntitySchema:E1
    #     wikibase_url = "https://furry.wikibase.cloud"
    #     mediawiki_api_url = "https://furry.wikibase.cloud/w/api.php"
    #     e = EntityShape(
    #         entity_id="Q3",
    #         eid=eid,
    #         lang="en",
    #         mediawiki_api_url=mediawiki_api_url,
    #         wikibase_url=wikibase_url,
    #     )
    #     e.validate_and_get_result()
    #     print(e.result)

    def test__download_json(self):
        es = EntityShape(eid="E395", lang="en", entity_ids=["Q20727"])
        # es.__download_json__()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(es.__download_json__())
        assert len(es.entities) == 1
        # test that we got any json data back
        assert es.entities[0].entity_data != {}

    def test_download_and_validate_one_item(self):
        es = EntityShape(eid="E395", lang="en", entity_ids=["Q20727"])
        es.download_and_validate()
        assert len(es.entities) == 1
        assert es.entities[0].entity_data != {}
        result = es.entities[0].result
        assert result.analyzed is True
        assert result.is_valid is True
        # print(es.entities[0].result)
        # assert es.entities[0].result == Result()

    def test_download_and_validate_ten_items(self):
        entity_ids = [
            "Q115097016",
            "Q115097023",
            "Q115097021",
            "Q115097029",
            "Q115097038",
            "Q115097037",
            "Q115097040",
            "Q115097051",
            "Q115097057",
            "Q115097060",
        ]

        start_time = time.time()  # Record the start time
        es = EntityShape(eid="E375", lang="en", entity_ids=entity_ids)
        es.download_and_validate()
        end_time = time.time()  # Record the end time

        execution_time = end_time - start_time
        print(f"Test execution time: {execution_time} seconds")

        assert len(es.entities) == 10
        # for entity in es.entities:
        #     print(entity.result)
        #     print(entity.result.model_dump())
        # assert es.entities[0].entity_data != {}
        # result = es.entities[0].result
        # assert result.analyzed is True
        # assert result.is_valid is True
        # print(es.entities[0].result)
        # assert es.entities[0].result == Result()

    def test_get_result_invalid_eid(self):
        es = EntityShape(eid="eeeE1", entity_ids=[])
        with self.assertRaises(WikibaseEntitySchemaDownloadError):
            es.download_schema()
