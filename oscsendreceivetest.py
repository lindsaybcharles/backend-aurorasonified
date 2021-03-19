from pythonosc import dispatcher            #  to catch and map input from osc
from pythonosc import osc_server            #  to create and send OSC messages
from pythonosc import osc_message_builder   #  to package osc messages 
from pythonosc import udp_client            #  to listen for messages
from pythonosc.osc_server import AsyncIOOSCUDPServer
import argparse                             #  to understand messages that come in
import asyncio
import time


def get_osc_messages(data_path, data_sent):
    print("Osc Messages Received", data_sent)
    #print(data_path)

def send_osc_messages(sendport):
    count = 0
    while count<50:
        if count == 50:
            break
        else:
            client.send_message("/osc_message_from_python1", 1.5)
            client.send_message("/osc_message_from_python2", 2.5)
            print("message sent on port:", sendport)
            count += 1
            time.sleep(1)

if __name__ == '__main__':
    ip = "127.0.0.1"
    sendport = 7000
    inport = 8000   

    ##sendind osc messages on
    client = udp_client.SimpleUDPClient(ip,sendport)
    send_osc_messages(sendport)
    ##catching osc messages or receiving osc messages
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/osc_message_to_python", get_osc_messages) #creating the variables we want to receive osc messages for

    #set up server to listen for osc messages
    server = osc_server.ThreadingOSCUDPServer((ip,inport),dispatcher)
    print("servering on {}".format(server.server_address))
    server.serve_forever()
 