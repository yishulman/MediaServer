
import re, threading
from RTSPConstants import RTSPConstants
from RTSPReqMessage import RTSPReqMessage

class RTSPMessageParser:

    requestLine = re.compile('(\S+)\s+(\S+)\s+(\S+)')
    headerField = re.compile('(\S+):\s*(\S+)')

    def __init__(self, connection):
        (self.conn, self.address) = connection
        threading.Thread(target=self.recvRtspRequest()).start()

    def recvRtspRequest(self):
        """Receive RTSP request from the client."""
        while True:
            data = self.conn.recv(4096)  ###
            if data:
                print '-' * 60 + "\nData received:\n" + '-' * 60
                self.parseRequest(data)
            else:
                break

    def parseRequest(self,message):
        #create new req inst
        rtspMessage = RTSPReqMessage()

        # spilt message with CRLF separator
        messageLines = message.split(RTSPConstants.CRLF)
        print messageLines

        # Extract request and save to req inst
        m = self.requestLine.match(messageLines.pop(0))
        (rtspMessage.method, rtspMessage.URI, rtspMessage.RTSPVersion) = m.groups()

        # Extract Header fields and values
        for h in messageLines:
            if h != '':
                m = self.headerField.match(h)
                rtspMessage.header[m.group(1)] = m.group(2)
        print rtspMessage.header

