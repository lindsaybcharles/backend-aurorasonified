from pythonosc import dispatcher            #  to catch and map input from osc
from pythonosc import osc_server            #  to create and send OSC messages
from pythonosc import osc_message_builder   #  to package osc messages 
from pythonosc import udp_client            #  to listen for messages

import argparse                             #  to understand messages that come in

def get_osc_messages():
    print("Osc Messages Received")

def send_osc_messages(sendport):
    client.send_message("/osc_message_sent", 1.5)
    print("message sent on port:", sendport)


if __name__ == '__main__':
    ip = "127.0.0.1"
    sendport = 7000
    inport = 8000

    #sendind osc messages on
    client = udp_client.SimpleUDPClient(ip,sendport)

    #catching osc messages or receiving osc messages
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/osc_message_receive", get_osc_messages) #creating the variables we want to receive osc messages for

    #set up server to listen for osc messages
    server = osc_server.ThreadingOSCUDPServer((ip,inport),dispatcher)
    print("servering on {}".format(server.server_address))
    server.serve_forever()

    send_osc_messages(sendport)
