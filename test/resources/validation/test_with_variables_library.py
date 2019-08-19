import requests

from string import Template

class newmanTest:

    def GET_with_URL_Params(self,param,param2):
        """
        Simple GET request with URL Parameters
        """

        url = Template("http://httpbin.org/get?lol=${param}&haha=${param2}").substitute(param=param,param2=param2)
        method = "GET"
        headers = {}
        
        response = requests.request(method, url, headers=headers)

        return response.text

    def POST_with_JSON_body(self,something_else):
        """
        
        """

        url = Template("http://httpbin.org/post").substitute(something_else=something_else)
        method = "POST"
        headers = {'Content-Type': 'application/json'}
        data = Template("{\n    \"something\": \"${something_else}\"\n}").substitute(something_else=something_else)
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

    def PUT_with_form_data(self,a_number):
        """
        
        """

        url = Template("http://httpbin.org/put").substitute(a_number=a_number)
        method = "PUT"
        headers = {}
        data = Template("quotient=${a_number}").substitute(a_number=a_number)
        response = requests.request(method, url, headers=headers, data=data)

        return response.text