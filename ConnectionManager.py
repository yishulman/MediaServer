from RTSPMessageParser import RTSPMessageParser
from RTSPRespMessage import RTSPRespMessage
from RTSPMessageGenerator import RTSPMessageGenerator
from RTSPConstants import RTSPConstants

class ConnectionManager:

    IDLE = 0

    ConnectionState = IDLE

    def __init__(self, connection):
        (self.conn, self.address) = connection
        print "New connection from %s on port %s" %  (self.address[0], self.address[1])
        self.rtspMessageParser = RTSPMessageParser(connection,self.prossessMessage)

    def prossessMessage(self, reqMessage):
        resp = None
        if reqMessage.method == 'OPTIONS':
            resp = RTSPMessageGenerator('200',reqMessage.header['CSeq'])
            resp.respMesage.header['Public'] = RTSPConstants.public
        else:
            #Methos not alowed
            print "Method " + reqMessage.method + " Not supported"
            resp = RTSPMessageGenerator('405',reqMessage.header['CSeq'])
            
        self.conn.send(resp.getMessage())