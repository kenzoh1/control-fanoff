import sys
from mycroft import MycroftSkill, intent_file_handler
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = 'aio_tXdx47EvDnkAcLJCm0ezSMpo3w8D'
ADAFRUIT_IO_USERNAME = 'Kenzo16'

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect()
client.loop_background()


class FanoffControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_file_handler('fanoff.control.intent')
    def handle_jarvis_introducing(self, message):
        self.speak_dialog('fanoff.control')
        client.publish('Fan', 0)


def create_skill():
    return FanControl()

