# postman2robotframework

Command line too to create a [Robotframework](https://robotframework.org/) library using a [Postman](https://www.getpostman.com/) collection

## Command line usage

```
POSTMAN TO ROBOTFRAMEWORK

Usage:
  postman2robot [--ifile <inputfile>] [--ofile <outputfile>] [options]
  postman2robot -h

Options:
  -i <inputfile>, --ifile <inputfile>       Path to the postman collection. [default: collection.json]
  -o <outputfile>, --ofile <outputfile>     Path to the output folder. [default: ./postman_libraries]
Options-Flags:
  -h, --help                                Show the help screen.
```

## Generated library usage

### EXAMPLE of generated library

```
import requests

class newmanTest:

    def GET_with_URL_Params(self):
        """
        Simple GET request with URL Parameters
        """

        url = "http://httpbin.org/get?lol=true"
        method = "GET"
        headers = {}
        
        response = requests.request(method, url, headers=headers)

        return response.text
```

### EXAMPLE using the generated library

```
*** Settings ***
Documentation     A test suite with a single test to validate the library.
...

Library           ./postman_libraries/newmanTest.py

*** Test Cases ***
Valid Library
    GET with URL Params
```