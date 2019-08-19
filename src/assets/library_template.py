import requests

{% if variables|length > 0 -%}from string import Template{% endif %}

class {{ name }}:
{%- for item in items %}

    def {{item.def_name}}(self{% for var in item.variables %},{{var}}{% endfor %}):
        """
        {{item.documentation}}
        """

        url = {% if item.variables|length > 0 %}Template("{{item.url}}").substitute({% for var in item.variables %}{{var}}={{var}}{{ "," if not loop.last }}{% endfor %}){% else %}"{{item.url}}"{% endif %}
        method = "{{item.method}}"
        headers = {{item.header}}
        {% if item.body != "" %}data = {% if item.variables|length > 0 %}Template("{{item.body | replace('\n','\\n') | replace('\"','\\"')}}").substitute({% for var in item.variables %}{{var}}={{var}}{{ "," if not loop.last }}{% endfor %}){% else %}"{{item.body | replace('\n','\\n') | replace('\"','\\"')}}"{% endif %}{% endif %}
        response = requests.request(method, url, headers=headers{% if item.body != "" %}, data=data{% endif %})

        return response.text
{%- endfor -%}