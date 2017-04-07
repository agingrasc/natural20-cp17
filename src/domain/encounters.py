import json
from random import sample, randrange


class Encounter:
    def __init__(self, encounter_raw):
        if isinstance(encounter_raw, Encounter):
            self.raw_json = encounter_raw.raw_json
        else:
            self.raw_json = encounter_raw

    def __getitem__(self, item):
        return self.raw_json[item]

    def __eq__(self, other):
        if isinstance(other, Encounter):
            res = self.raw_json == other.raw_json
            return res
        return False

    def say_greeting(self):
        return sample(self.raw_json["greeting"],1)[0]

    def say_farewell(self):
        return sample(self.raw_json["farewell"], 1)[0]

    def say_insult(self):
        return sample(self.raw_json["insult"], 1)[0]

    def get_tip(self):
        return randrange(self["tip_min"], self["tip_max"])

    @property
    def name(self):
        return self["name"]


class ClientBuilder:
    def __init__(self):
        self.raw_json = {
            "name": "Steve",
            "days": [1],
            "greeting": "hello",
            "farewell": "bye",
            "tips_min": 1,
            "tips_max": 3
        }

    def with_days(self, days):
        self.raw_json["days"] = days
        return self

    def build(self):
        return Encounter(self.raw_json)
