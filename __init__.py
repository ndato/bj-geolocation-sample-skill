from mycroft import MycroftSkill, intent_file_handler
from mycroft.api import GeolocationApi
import pprint

class BjGeolocationSample(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        self.geolocation_api = GeolocationApi()

    @intent_file_handler('sample.geolocation.bj.intent')
    def handle_sample_geolocation_bj(self, message):
        loc_string = message.data.get('location')
        self.log.info(loc_string)
        location = self.geolocation_api.get_geolocation(loc_string)
        
        pprint.pprint(location)
        self.speak_dialog('sample.geolocation.bj', {'location': loc_string})


def create_skill():
    return BjGeolocationSample()

