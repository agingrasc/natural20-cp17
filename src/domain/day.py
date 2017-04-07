import json
from domain.encounter import Encounter


class Day:
    def __init__(self, day_id, load_from_json=True, encounters=[]):
        """
        Load from config files
        """
        self.day_id = day_id
        if load_from_json:
            with open('resource/json/day{}.json'.format(day_id)) as json_file:
                day_json = json.load(json_file)

                self.encounters = [ Encounter(enc) for enc in day_json["encounters"]]
        else:
            self.encounters = encounters

    def pop_triggable_encounter(self, active_flags):
        while len(self.encounters) > 0:
            encounter = self.encounters.pop()
            if encounter.is_encounter_triggable(active_flags):
                return encounter
        return None

