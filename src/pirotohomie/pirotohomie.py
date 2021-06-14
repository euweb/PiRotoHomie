import logging

from homie.device_roto_rollershutter import DeviceRotoRollershutter

logger = logging.getLogger(__name__)

class ObjectView(object):

    def __init__(self, d):
        self.__dict__ = d


class PiRotoHomie:

    def __init__(self, config):
        self.config = ObjectView(config)
        self.items = []
        for channel in self.config.PiRotoWindow:
            window = DeviceRotoRollershutter()