import json

class PostmanParser(object):

    def __init__(self, collection):

        with open(collection) as json_file:
            self.collection = json.load(json_file)
        
        self.library = {
            "name": "",
            "items": []
        }

    def get_library_from_collection(self):

        if self.collection["info"]["schema"] != "https://schema.getpostman.com/json/collection/v2.1.0/collection.json":
            raise Exception('The schema of the collection is invalid expecting v2.1.0')

        self.library["name"] = self.collection["info"]["name"]

        for item in self.collection["item"]:
            self.library["items"].append(self.get_keyword_from_item(item))

        return self.library

    def get_keyword_from_item(self, item):

        request =  item["request"]

        keyword = {
            "def_name": item["name"].replace(" ", "_"),
            "method": request["method"],
            "url": request["url"]["raw"],
            "header": {h["key"]: h["value"] for h in request["header"]},
            "body": "",
            "documentation": request["description"] if "description" in request else ""
        }

        keyword["body"] = self.body_switcher(item)

        return keyword

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
        
        
        