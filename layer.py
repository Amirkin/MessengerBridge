from yowsup.layers.interface import ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers                                     import YowLayer

telegram_answer = None


class EchoLayer(YowLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            messageProtocolEntity.getBody(),
            to = messageProtocolEntity.getFrom()
        )

        telegram_answer.send_message(messageProtocolEntity.getBody())

        self.toLower(outgoingMessageProtocolEntity)

    def send_message(self, number, content):
        outgoingMessage = TextMessageProtocolEntity(content, to=number)
        self.toLower(outgoingMessage)

    def receive(self, protocolEntity):
        print protocolEntity.getTag()
        if protocolEntity.getTag() == "message":
            self.onMessage(protocolEntity)
