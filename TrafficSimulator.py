import sys, time, signal, threading, os
from socket import *

class TrafficSimulator:

    def makePayload(self, packetInSequence):

        info = "%s:%d:%d:%d:%d"%(self.USERNAME, packetInSequence, self.packetsPerSecond, self.payloadSizeInBytes, self.runningTime)
        numberOfRandomBytes = self.payloadSizeInBytes - len(info)
        numberOfRandomBytes = numberOfRandomBytes if numberOfRandomBytes > 0 else 0
        return info + bytearray(os.urandom(numberOfRandomBytes))


    def openUDPsocket(self):
        self.UDPSocket = socket(AF_INET,SOCK_DGRAM)
    

    def main(self, serverHost, serverPort, packetsPerSecond, payloadSizeInBytes, runningTime):

        self.USERNAME = 'vegaen'

        self.serverHost = serverHost
        self.serverPort = int(serverPort)
        self.packetsPerSecond = int(packetsPerSecond)
        self.payloadSizeInBytes = int(payloadSizeInBytes)
        self.runningTime = int(runningTime)

        startTime = time.time()

        self.UDPSocket = socket(AF_INET,SOCK_DGRAM)
        wait = 1.0/self.packetsPerSecond  
        packetNumber = 0
        while time.time() - startTime < self.runningTime:
            t1 = time.time()
            packetNumber = packetNumber + 1
            payload = self.makePayload(packetNumber)
            self.UDPSocket.sendto(payload, (self.serverHost,self.serverPort))
            t2= time.time()


            #time.sleep( wait - (t2-t1))

        print "Packets sent: %d"%packetNumber


def signal_handler(signal, frame):
    print '\nExit!'
    sys.exit(0)


if __name__ == "__main__":

    signal.signal(signal.SIGINT,signal_handler)

    try:
        serverHost = sys.argv[1]
        serverPort = sys.argv[2]
        packetsPerSecond = sys.argv[3]
        payloadSizeInBytes = sys.argv[4]
        runningTime = sys.argv[5]

    except:
        print "[Usage: TrafficSimulator.py server_host server_port packet_per_second payload_size_in_bytes seconds_to_run]\n"    
        sys.exit(1)


    threading.Thread(target=(TrafficSimulator()).main(serverHost, serverPort, packetsPerSecond, payloadSizeInBytes, runningTime)).start()
    