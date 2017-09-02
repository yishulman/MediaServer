from RTSPMessageParser import RTSPMessageParser
from RTSPRespMessage import RTSPRespMessage
class ConnectionManager:

    IDLE = 0

    ConnectionState = IDLE

    def __init__(self, connection):
        (self.conn, self.address) = connection
        print "New connection from %s on port %s" %  (self.address[0], self.address[1])
        self.rtspMessageParser = RTSPMessageParser(connection)
        self.main()

    def main(self):
        while True:
            reqMessage = self.rtspMessageParser.messageQueue.get()
            print reqMessage