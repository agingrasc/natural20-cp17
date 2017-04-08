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

    def has_boss_complain(self):
        return "boss_complains" in self.raw_json

    def say_boss_complain(self):
        if self.has_boss_complain():
            return sample(self.raw_json["boss_complains"], 1)[0]
        else:
            return [""]

    def is_encounter_triggable(self, active_flags):
        for cond in self["include"]:
            if not cond in active_flags:
                return False
        for cond in self["exclude"]:
            if cond in active_flags:
                return False
        return True

    @property
    def name(self):
        return self["client_name"]

    @property
    def tips(self):
        return self["tips"]

    @property
    def dialogs(self):
        return self["dialog"]

    @property
    def stage_src(self):
        return self["stage_src"]

    @property
    def stage_dest(self):
        return self["stage_dest"]

    @property
    def penality(self):
        if "penality" in self.raw_json:
            return self["penality"]
        else:
            return 0


    @property
    def ignore_client_flag(self):
        return self["ignore_client_flag"]
    @property
    def ignore_dest_flag(self):
        return self["ignore_dest_flag"]
    @property
    def happy_ending_flag(self):
        return self["happy_ending_flag"]





class EncounterBuilder:
    def __init__(self):
        self.raw_json = {
            "include":[],
            "exclude":[],
            "stage_src": 1,
            "stage_dest": 2,
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

    def with_stage_src(self, src):
        self.raw_json["stage_src"] = src
        return self

    def with_stage_dest(self, dest):
        self.raw_json["stage_dest"] = dest
        return self


    def build(self):
        return Encounter(self.raw_json)
