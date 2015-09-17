__author__ = 'bibla'

from layer import EchoLayer
from yowsup.layers.auth import YowCryptLayer, YowAuthenticationProtocolLayer
from yowsup.layers.coder import YowCoderLayer
from yowsup.layers.network import YowNetworkLayer
from yowsup.layers.protocol_messages import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator import YowStanzaRegulator
from yowsup.layers.protocol_receipts import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks import YowAckProtocolLayer
from yowsup.stacks import YowStack
from yowsup.common import YowConstants
from yowsup.layers import YowLayerEvent
from yowsup import env
from yowsup.layers.axolotl import YowAxolotlLayer

#Config me!
PHONE = ""  # ex. 79271112233


class whatsappAnswer:

    def __init__(self):
        pass

    def create_stack(self):
        CREDENTIALS = (PHONE, "F5vqaa/9jCXDDMoTSWysyhOI0BU=")  # replace with your phone and password

        layers = (
            EchoLayer,
            (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer),
            YowAxolotlLayer,
            YowCoderLayer,
            YowCryptLayer,
            YowStanzaRegulator,
            YowNetworkLayer
        )

        stack = YowStack(layers)
        stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)  # setting credentials
        stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])  # whatsapp server address
        stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
        stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())  # info about us as WhatsApp client

        stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))  # sending the connect signal
        return stack

    def send_message(self, data):
        stack = self.create_stack()
        stack.send(data)


    def receive_message(self, stack):
        stack.loop()
