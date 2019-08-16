*** Settings ***
Documentation     A test suite with a single test for valid login.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Library           ./postman_libraries/newmanTest.py

*** Test Cases ***
Valid Library
    GET with URL Params
    POST with JSON body
    DELETE request
    PUT with form data
