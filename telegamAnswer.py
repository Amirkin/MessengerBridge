#coding: utf-8
import json
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

__author__ = 'bibla'

import socket

#Config me!
PHONE = ""  # ex. 79271112233
NAME = ""  # name of telegram


class TelegramAnswer:

    def __init__(self):
        self.s = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.stack = None

    def connect(self):
        #now connect to the web server on port 80
        # - the normal http port
        self.s.connect(("localhost", 1122))

    def send_main_session(self):
        self.s.send("main_session\n")

    def send_message(self, text):
        self.s.send("msg " + NAME + " " + text + "\n")

    def set_stack(self, stack):
        self.stack = stack
        pass

    def recieve_message(self):
        self.s.recv(1024)
        f = self.s.makefile()
        while True:
            answer = ""
            for line in f.readline():
                answer += line

            try:
                dump = json.loads(answer)
                if dump["event"] == "message" and dump["to"]["phone"] == PHONE:

                    data = TextMessageProtocolEntity(
                        dump["text"],
                        to=PHONE + "@s.whatsapp.net"
                    )
                    self.stack.send(data)

            except Exception as ex:
                print ex
                continue



if __name__ == '__main__':
    t = TelegramAnswer()
    t.connect()
    t.send_main_session()
    t.recieve_message()