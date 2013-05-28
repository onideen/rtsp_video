import sys

class TrafficSimulator:

    def main(self, serverHost, serverPort, packetsPerSecond, payloadSizeInBytes, secondsToRun):
        self.serverHost = serverHost
        self.serverPort = int(serverPort)
        self.packetsPerSecond = int(packetsPerSecond)
        self.payloadSizeInBytes = int(payloadSizeInBytes)
        self.secondsToRun = int(secondsToRun)


        print "got here"

        def open


if __name__ == "__main__":

    try:
        serverHost = sys.argv[1]
        serverPort = sys.argv[2]
        packetsPerSecond = sys.argv[3]
        payloadSizeInBytes = sys.argv[4]
        secondsToRun = sys.argv[5]

    except:
        print "[Usage: TrafficSimulator.py server_host server_port packet_per_second payload_size_in_bytes seconds_to_run]\n"    
        sys.exit(1)



    (TrafficSimulator()).main(serverHost, serverPort, packetsPerSecond, payloadSizeInBytes, secondsToRun)