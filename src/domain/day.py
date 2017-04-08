import json
from domain.encounter import Encounter


class Day:
    def __init__(self, day_id, load_from_json=True, encounters=[], starting_stage =0):
        """
        Load from config files
        """
        self.day_id = day_id
        if load_from_json:
            with open('resource/json/day{}.json'.format(day_id)) as json_file:
                day_json = json.load(json_file)
                self.starting_stage = day_json["starting_stage"]
                self.boss_complains = day_json["boss_complains"]

                self.encounters = [ Encounter(enc) for enc in day_json["encounters"]]
        else:
            self.encounters = encounters
            self.starting_stage = starting_stage
            self.boss_complains = [""]

    def pop_triggable_encounter(self, active_flags):
        while len(self.encounters) > 0:
            encounter = self.encounters.pop(0)
            if encounter.is_encounter_triggable(active_flags):
                return encounter
        return None

    def say_boss_complain(self):
        from random import sample
        return sample(self.boss_complains, 1)[0]



    @property
    def start_stage(self):
        return self.starting_stage