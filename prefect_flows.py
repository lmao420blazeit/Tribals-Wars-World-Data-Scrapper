from baseserver import Server
from prefect import task, flow
import os
import json
from datetime import datetime

def fetch_prototype(worlds, filename, flowname):
    @flow(name=flowname)
    def flow(worlds, filename):
        for obj in worlds:
            data = json.dumps(obj.get_player())
            #data = json.loads(data)

            if not os.path.exists(filename):
                os.makedirs(filename)

            json_path = '{}/{}-{}.json'.format(filename, filename, getattr(obj, "gameworld"))
            with open(json_path, 'w') as f:
                json.dump(data, f)
        return

    flow(worlds, filename)
    return    

@flow(name="Get player data")
def fetch_player_data(worlds):
    for obj in worlds:
        data = json.dumps(obj.get_player())
        #data = json.loads(data)

        if not os.path.exists("player-data"):
            os.makedirs("player-data")

        if not os.path.exists("player-data/{}".format(str(datetime.now().strftime("%Y-%m-%d")))):
            os.makedirs("player-data/{}".format(str(datetime.now().strftime("%Y-%m-%d"))))

        json_path = 'player-data/{}/{}.json'.format(str(datetime.now().strftime("%Y-%m-%d")), getattr(obj, "gameworld"))
        with open(json_path, 'w') as f:
            json.dump(data, f)

    return

@flow(name="Get ally data")
def fetch_ally_data(worlds):
    for obj in worlds:
        data = json.dumps(obj.get_ally())
        #data = json.loads(data)

        if not os.path.exists("ally-data"):
            os.makedirs("ally-data")

        if not os.path.exists("ally-data/{}".format(str(datetime.now().strftime("%Y-%m-%d")))):
            os.makedirs("ally-data/{}".format(str(datetime.now().strftime("%Y-%m-%d"))))

        json_path = 'ally-data/{}/{}.json'.format(str(datetime.now().strftime("%Y-%m-%d")), getattr(obj, "gameworld"))
        with open(json_path, 'w') as f:
            json.dump(data, f)

    return

@flow(name="Get ODD data")
def fetch_defense_data(worlds):
    for obj in worlds:
        data = json.dumps(obj.get_odd())
        #data = json.loads(data)

        if not os.path.exists("defense-data"):
            os.makedirs("defense-data")

        if not os.path.exists("defense-data/{}".format(str(datetime.now().strftime("%Y-%m-%d")))):
            os.makedirs("defense-data/{}".format(str(datetime.now().strftime("%Y-%m-%d"))))

        json_path = 'defense-data/{}/{}.json'.format(str(datetime.now().strftime("%Y-%m-%d")), getattr(obj, "gameworld"))
        with open(json_path, 'w') as f:
            json.dump(data, f)

    return

@flow(name="Get ODA data")
def fetch_attack_data(worlds):
    for obj in worlds:
        data = json.dumps(obj.get_odd())
        #data = json.loads(data)

        if not os.path.exists("attack-data"):
            os.makedirs("attack-data")

        if not os.path.exists("attack-data/{}".format(str(datetime.now().strftime("%Y-%m-%d")))):
            os.makedirs("attack-data/{}".format(str(datetime.now().strftime("%Y-%m-%d"))))

        json_path = 'attack-data/{}/{}.json'.format(str(datetime.now().strftime("%Y-%m-%d")), getattr(obj, "gameworld"))
        with open(json_path, 'w') as f:
            json.dump(data, f)

    return

@flow(name="Get village data")
def fetch_village_data(worlds):
    for obj in worlds:
        data = json.dumps(obj.get_village())
        #data = json.loads(data)

        if not os.path.exists("village-data"):
            os.makedirs("village-data")

        if not os.path.exists("village-data/{}".format(str(datetime.now().strftime("%Y-%m-%d")))):
            os.makedirs("village-data/{}".format(str(datetime.now().strftime("%Y-%m-%d"))))

        json_path = 'village-data/{}/{}.json'.format(str(datetime.now().strftime("%Y-%m-%d")), getattr(obj, "gameworld"))
        with open(json_path, 'w') as f:
            json.dump(data, f)

    return

@flow(name="Get data for all endpoints")
def main_flow() -> None:
    tribalwars_server_list = ["tribalwars.com.pt",
                              "die-staemme.de",
                              "guerretribale.fr",
                              "tribalwars.com.br",
                              "guerrastribales.es"]

    for server in tribalwars_server_list:
        obj_list = Server(server).generate_worlds()
        fetch_player_data(obj_list)
        fetch_ally_data(obj_list)
        fetch_defense_data(obj_list)
        fetch_attack_data(obj_list)
        fetch_village_data(obj_list)

    return

if __name__ == "__main__":
    main_flow()
