import json
from domain.clients import Clients


class Day:
    def __init__(self, day_id, clients = Clients(), load_from_json=True, nb_encounter=None):
        """
        Load from config files
        """
        self.day_id = day_id
        if load_from_json:
            with open('ressource/json/day{}.json'.format(day_id)) as json_file:
                day_json = json.load(json_file)
                nb_encounter = day_json["nb_random_encounter"]

        self.clients = clients.pick_client(day_id, nb_encounter)


    def pop_clients(self):
        return self.clients.pop()

