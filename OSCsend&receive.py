from pythonosc import dispatcher            #  to catch and map input from osc
from pythonosc import osc_server            #  to create and send OSC messages
from pythonosc import osc_message_builder   #  to package osc messages 
from pythonosc import udp_client            #  to listen for messages
from pythonosc.osc_server import AsyncIOOSCUDPServer
import argparse                             #  to understand messages that come in
import asyncio


ip = "127.0.0.1"
sendport = 7000
inport = 8000 

def get_osc_messages(unused_addr, args):
    print("Osc Messages Received")

def send_osc_messages(sendport):
    client.send_message("/osc_message_sent", 1.5)
    print("message sent on port:", sendport)


# if __name__ == '__main__':
#     ip = "127.0.0.1"
#     sendport = 7000
#     inport = 8000   

#     #sendind osc messages on
#     client = udp_client.SimpleUDPClient(ip,sendport)
#     send_osc_messages(sendport)
#     #catching osc messages or receiving osc messages
#     dispatcher = dispatcher.Dispatcher()
#     dispatcher.map("/osc_message_receive", get_osc_messages) #creating the variables we want to receive osc messages for

#     #set up server to listen for osc messages
#     server = osc_server.ThreadingOSCUDPServer((ip,inport),dispatcher)
#     print("servering on {}".format(server.server_address))
#     server.serve_forever()



async def loop():
    """Example main loop that only runs for 10 iterations before finishing"""
    for i in range(10):
        print(f"Loop {i}")
        await asyncio.sleep(1)


async def init_main():
    
    ip = "127.0.0.1"
    sendport = 7000
    inport = 8000   

    #sendind osc messages on
    client = udp_client.SimpleUDPClient(ip,sendport)
    send_osc_messages(sendport)

    #catching osc messages or receiving osc messages
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/osc_message_receive", get_osc_messages) #creating the variables we want to receive osc messages for

    #set up server to listen for osc messages
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    print("servering on {}".format(server.server_address))
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving


    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint


asyncio.run(init_main())
