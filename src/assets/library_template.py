import requests

class {{ name }}:
{% for item in items %}
    def {{item.def_name}}(self):
        """
        {{item.documentation}}
        """

        url = "{{item.url}}"
        method = "{{item.method}}"
        headers = {{item.header}}
        {% if item.body != "" %}data = "{{item.body | replace('\n','\\n') | replace('\"','\\"')}}"{% endif %}
        response = requests.request(method, url, headers=headers{% if item.body != "" %}, data=data{% endif %})

        return response.text
{% endfor %}