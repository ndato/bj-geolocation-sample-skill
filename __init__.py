from mycroft import MycroftSkill, intent_file_handler


class BjGeolocationSample(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sample.geolocation.bj.intent')
    def handle_sample_geolocation_bj(self, message):
        self.speak_dialog('sample.geolocation.bj')


def create_skill():
    return BjGeolocationSample()

