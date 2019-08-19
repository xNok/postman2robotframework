import pytest
import json
import os

from src.postman_parser import PostmanParser

class Test_PostmanParser:


    def test_get_library_from_collection(self):

        # GIVEN: a simple postman collection
        parser = PostmanParser("./test/resources/test_simple_collection.json")
        
        # WHEN: i use get_keyworks_from_collection
        library = parser.get_library_from_collection()

        lib1 = {
            "def_name": "GET_with_URL_Params",
            "method": "GET",
            "url": "http://httpbin.org/get?lol=true",
            "header": {},
            "body": "",
            "variables": [],
            "documentation": "Simple GET request with URL Parameters"
        }

        lib2 = {
            "def_name": "POST_with_JSON_body",
            "method": "POST",
            "url": "http://httpbin.org/post",
            "header": {
                "Content-Type": "application/json"
            },
            "body": "{\n    \"something\": \"cool\"\n}",
            "variables": [],
            "documentation": ""
        }

        lib3 = {
            "def_name": "DELETE_request",
            "method": "DELETE",
            "url": "http://httpbin.org/delete",
            "header": {},
            "body": "",
            "variables": [],
            "documentation": ""
        }

        lib4 = {
            "def_name": "PUT_with_form_data",
            "method": "PUT",
            "url": "http://httpbin.org/put",
            "header": {},
            "body": "quotient=223",
            "variables": [],
            "documentation": ""
        }

        # THEN: I get 4 keywords
        assert len(library["items"]) == 4
        assert library["items"][0] == lib1
        assert library["items"][1] == lib2
        assert library["items"][2] == lib3
        assert library["items"][3] == lib4