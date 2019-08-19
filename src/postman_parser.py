import json
import re

class PostmanParser(object):

    def __init__(self, collection):

        with open(collection) as json_file:
            self.collection = json.load(json_file)
        
        self.library = {
            "name": "",
            "variables": set(),
            "items": []
        }

    def get_library_from_collection(self):

        if self.collection["info"]["schema"] != "https://schema.getpostman.com/json/collection/v2.1.0/collection.json":
            raise Exception('The schema of the collection is invalid expecting v2.1.0')

        self.library["name"]  = self.collection["info"]["name"]
        self.library["items"] = self.get_keyword_from_items(self.collection["item"])

        return self.library

    def get_keyword_from_items(self, items):

        keyword_name_list = set()
        keyword_list = []

        for item in items:
            if "item" in item:
                new_keywords = self.get_keyword_from_items(item["item"])
                keyword_list += [k for k in new_keywords if k["def_name"] not in keyword_name_list]
                keyword_name_list.update(k["def_name"] for k in new_keywords)
            else:

                request =  item["request"]

                keyword = {
                    "def_name": item["name"].replace(" ", "_"),
                    "method": request["method"],
                    "url": request["url"]["raw"],
                    "header": {h["key"]: h["value"] for h in request["header"]},
                    "body": "",
                    "documentation": request["description"] if "description" in request else "",
                    "variables": []
                }

                keyword["body"] = self.body_switcher(item)
                # if string contains {{foo}}
                keyword["url"], v = self.prepare_varibles(keyword["url"])
                keyword["variables"] += v
                keyword["body"], v = self.prepare_varibles(keyword["body"])
                keyword["variables"] += v

                keyword_list.append(keyword)
                keyword_name_list.add(keyword["def_name"])

        return keyword_list

    def prepare_varibles(self, s):
        # variable list
        v = []

        pattern = re.compile(r'{{(.*?)}}')

        if s != "" and pattern.search(s):

            for m in re.finditer(pattern, s):
                s = s.replace(m.group(0), "${" + m.group(1) + "}")
                v.append(m.group(1))

            self.library["variables"].update(v)

        return s, v

    def body_switcher(self, item):

        body = ""

        if "body" in item["request"]:

            body_obj = item["request"]["body"]

            if body_obj["mode"] == "raw":
                body = body_obj["raw"]
            elif body_obj["mode"] == "urlencoded":
                for param in body_obj["urlencoded"]:
                    body += param["key"] + "=" + param["value"]

        return body
        
        
        