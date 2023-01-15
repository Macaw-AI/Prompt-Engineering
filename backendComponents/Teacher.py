import json


class Teacher:
    def __init__(self, identifier, lang="en"):
        with open(f"Scenarios/{lang}/teachers/{identifier}.json", "r") as f:
            data = json.load(f)
        self.name = data["name"]
        self.character = data["character"]
        self.few_shots = "".join(data["few_shots"])

        self.voice = data["voice"]
        self.audioConfig = data["audioConfig"]


