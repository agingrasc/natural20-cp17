import json

class Day:
    def __init__(self, day_id):
        """
        Load from config files
        """
        with open('ressource/json/day{}.json'.format(day_id)) as json_file:
            day_json = json.load(json_file)
            nb_encounter = day_json["nb_random_encounter"]
