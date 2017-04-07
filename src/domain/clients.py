
from random import sample, randrange

class Client:
    def __init__(self, client_raw):
        if isinstance(client_raw, Client):
            self.raw_json = client_raw.raw_json
        else:
            self.raw_json = client_raw

    def __getitem__(self, item):
        return self.raw_json[item]

    def __eq__(self, other):
        if isinstance(other, Client):
            res = self.raw_json == other.raw_json
            return res
        return False

    def greet(self):
        return sample(self.raw_json["greeting"],1)

    def sayFarewell(self):
        return sample(self.raw_json["farewell"], 1)

    def getTip(self):
        return randrange(self["tip_min"], self["tip_max"])

    @property
    def name(self):
        return self["name"]

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