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
        return sample(self.raw_json["greeting"], 1)[0]

    def say_farewell(self):
        return sample(self.raw_json["farewell"], 1)[0]

    def say_insult(self):
        return sample(self.raw_json["insult"], 1)[0]

    def is_encounter_trigger(self, active_flags):
        for cond in self["include"]:
            if not cond in active_flags:
                return False
        for cond in self["exclude"]:
            if cond in active_flags:
                return False
        return True

    @property
    def name(self):
        return self["name"]

    @property
    def tips(self):
        return self["tips"]

    @property
    def dialogs(self):
        return self["dialog"]



class EncounterBuilder:
    def __init__(self):
        self.raw_json = {
            "include":[],
            "exclude":[],
            "client_name": "Steve",
            "greeting": ["hello"],
            "dialog": ["To be or not to be"],
            "insult": ["You sucks at your job!"],
            "farewell": ["byebye"],
            "ignore_client_flag": [],
            "ignore_dest_flag": [],
            "happy_ending_flag": [],
            "tips": 30
        }

    def with_greeting(self, greeting):
        self.raw_json["greeting"] = greeting
        return self

    def with_dialog(self, dialog):
        self.raw_json["dialog"] = dialog
        return self

    def with_insult(self, insult):
        self.raw_json["insult"] = insult
        return self

    def with_farewell(self, farewell):
        self.raw_json["farewell"] = farewell
        return self

    def with_include(self, include):
        self.raw_json["include"] = include
        return self

    def with_exclude(self, exclude):
        self.raw_json["exclude"] = exclude
        return self

    def build(self):
        return Encounter(self.raw_json)
