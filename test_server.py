#!/usr/bin/env python2

import socket
import configparser
import datetime

def Main():

    shutdown = False
    today = datetime.datetime.now()

    config = configparser.ConfigParser()
    config.read('server.cfg')

    log = open("test_server.log" , "a")
   
    host = config['DEFAULT']['host'] #Server ip
    port = int(config['DEFAULT']['port'])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print(today.strftime("%c") + " fm_server starting on port " + str(port))
    log.write(today.strftime("%c") + " fm_server starting on port " + str(port)+ "\n")

    #s1.set_cent_freq(94700000)
    while not shutdown:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        log.write("Message from: " + str(addr) + "\n")
        print("From connected user: " + data)
        log.write("From connected user: " + data + "\n")


        data = data.upper()
        print("Sending: " + data)
        log.write("Sending: " + data + "\n")
        s.sendto(data.encode('utf-8'), addr)
    s.close()
    log.close()

if __name__=='__main__':
    Main()