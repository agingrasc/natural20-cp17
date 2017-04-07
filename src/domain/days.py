import json
from random import sample

class Client:
    def __init__(self, raw_json):
        self.raw_json = raw_json
    def __getitem__(self, item):
        return self.raw_json[item]

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.raw_json == other.raw_json
        return False

class Clients:
    def __init__(self):
        """
        Load from config files
        """
        with open('ressource/json/clients.json') as json_file:
            clients_json = json.load(json_file)
            self.clients = [Client(client_raw) for client_raw in clients_json["clients"]]

    def __init__(self, clients_raw):
        """
        For UT
        """
        self.clients = [Client(client_raw) for client_raw in clients_raw]

    def pick_client(self, day_id, nb_client):
        client_for_day = [client for client in self.clients if day_id in client["days"]]
        if len(client_for_day) < nb_client:
            raise Exception("No enough available client for day {}".format(day_id))
        if len(client_for_day) == 0:
            return []
        if len(client_for_day) == 1:
            return client_for_day
        return sample(client_for_day, nb_client)

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

