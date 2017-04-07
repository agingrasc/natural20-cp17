import json


class Day:
    def __init__(self, clients, day_id):
        """
        Load from config files
        """
        self.day_id = day_id
        with open('ressource/json/day{}.json'.format(day_id)) as json_file:
            day_json = json.load(json_file)
            nb_encounter = day_json["nb_random_encounter"]

            self.clients = clients.pick_clients(day_id, nb_encounter)

    def __init__(self, clients, day_id, nb_encounter):
        """
        For UT
        """
        self.day_id = day_id
        self.clients = clients.pick_clients(day_id, nb_encounter)

