import requests
import xmltodict
from urllib.parse import unquote
from datetime import datetime
import itertools
import re
from world import World

class ServerBaseClass:

    def __init__(self):
        pass
        
    def get_active_servers(self, server: str = "tribalwars.com.pt") -> dict:
        base_server = server
        """
        returns: dict
        {'pts1': 'https://pts1.tribalwars.com.pt', 'ptc1': 'https://ptc1.tribalwars.com.pt', 
        'ptc2': 'https://ptc2.tribalwars.com.pt', 'ptp5': 'https://ptp5.tribalwars.com.pt', 
        'pt88': 'https://pt88.tribalwars.com.pt', 'pt90': 'https://pt90.tribalwars.com.pt', 
        'pt91': 'https://pt91.tribalwars.com.pt', 'pt92': 'https://pt92.tribalwars.com.pt'}
        """
        server_list = f"http://{base_server}/backend/get_servers.php"
        re_text = re.findall(r'(\".+?\")', requests.get(server_list).text)
        re_text = [x.strip('"') for x in re_text]
        pairs = itertools.zip_longest(*[iter(re_text)] * 2, fillvalue=None)
        dct = {key: value for key, value in pairs}
        return(dct)
    
class Server(ServerBaseClass):

    def __init__(self, server):
        self.server = server

    def generate_worlds(self):
        server_dict = self.get_active_servers(self.server)
        worlds_list = []
        for gameworld, server in server_dict.items():
            worlds_list.append(World(gameworld, server))

        return(worlds_list)
