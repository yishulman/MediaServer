from RTSPMessageParser import RTSPMessageParser

class ConnectionManager:

    def __init__(self, connection):
        (self.conn, self.address) = connection
        print "New connection from %s on port %s" %  (self.address[0], self.address[1])
        rtspMessageParser = RTSPMessageParser(connection)
