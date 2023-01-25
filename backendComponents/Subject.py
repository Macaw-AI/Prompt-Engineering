import json


class Subject:
    def __init__(self, identifier, lang="en"):
        with open(f"Scenarios/{lang}/subjects/{identifier}.json", "r") as f:
            data = json.load(f)
        self.name = data["name"]
        self.questions = data["questions"]
        self.related = data["related"]


