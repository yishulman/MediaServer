
import sys, socket, argparse

from ConnectionManager import ConnectionManager

class MediaServer:

    connections = []

    def main(self,argv):
        #comand line parser
        parser = argparse.ArgumentParser()
        parser.add_argument('-port', type=int, required=True, help='Port number for the server to listen')
        args = parser.parse_args()

        # open socket and start listen
        rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rtspSocket.bind(('', args.port))
        print ("RTSP Listing to incoming request on port %d" % args.port)
        rtspSocket.listen(5)

        #wait for connection
        while True:
            connection = rtspSocket.accept()
            self.connections.insert(0,ConnectionManager(connection))

if __name__ == "__main__":
    rtsp_server = MediaServer()
    rtsp_server.main(sys.argv)
