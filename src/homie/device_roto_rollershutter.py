import logging

from homie.device_base import Device_Base
from homie.node.node_base import Node_Base
from homie.node.node_state import Node_State

from homie.node.property.property_enum import Property_Enum

logger = logging.getLogger(__name__)

MQTT_DEFAULT_SETTINGS = {
    "MQTT_BROKER": "localhost",
    "MQTT_PORT": 1883,
}

VALUES = "OPEN,OPENING,STOP,CLOSING,CLOSED"


class DeviceRotoRollershutter(Device_Base):
    def __init__(self,
                 device_id="roto",
                 name="Roto Roof Window",
                 homie_settings=None,
                 mqtt_settings=MQTT_DEFAULT_SETTINGS,
                 ):
        super().__init__(device_id, name, homie_settings, mqtt_settings)

        node = Node_Base(self, "controls", "Controls", "controls")

        node.add_property(Property_Enum(self, data_format="UP,DOWN,STOP"))

        self.add_node(node)

        self.add_node(Node_State(self, state_values=VALUES,
                      set_state=self.set_state))

        logger.info('done')

        self.start()

    def set_state(value):
        logger.debug(value)
