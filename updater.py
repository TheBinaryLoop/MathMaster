import requests

class Updater:
    """ Simple updater class """

    def __init__(self):
        self.online_version = ''

    def check_for_update(self, local_version):
        self.online_version = requests.get('https://thebinaryloop.github.io/MathMaster/version').text
        print(self.online_version)
