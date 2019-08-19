import requests

class newmanTest:

    def GET_with_URL_Params_true(self):
        """
        Simple GET request with URL Parameters
        """

        url = "http://httpbin.org/get?lol=true"
        method = "GET"
        headers = {}
        
        response = requests.request(method, url, headers=headers)

        return response.text

    def POST_with_JSON_body(self):
        """
        
        """

        url = "http://httpbin.org/post"
        method = "POST"
        headers = {'Content-Type': 'application/json'}
        data = "{\n    \"something\": \"cool\"\n}"
        response = requests.request(method, url, headers=headers, data=data)

        return response.text

    def DELETE_request(self):
        """
        
        """

        url = "http://httpbin.org/delete"
        method = "DELETE"
        headers = {}
        
        response = requests.request(method, url, headers=headers)

        return response.text

    def PUT_with_form_data(self):
        """
        
        """

        url = "http://httpbin.org/put"
        method = "PUT"
        headers = {}
        data = "quotient=223"
        response = requests.request(method, url, headers=headers, data=data)

        return response.text

    def GET_with_URL_Params_false(self):
        """
        Simple GET request with URL Parameters
        """

        url = "http://httpbin.org/get?lol=false"
        method = "GET"
        headers = {}
        
        response = requests.request(method, url, headers=headers)

        return response.text
