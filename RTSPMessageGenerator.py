
from RTSPRespMessage import RTSPRespMessage
from RTSPConstants import RTSPConstants

class RTSPMessageGenerator:

    def __init__(self, statusCode, CSeq):
        self.respMesage =  RTSPRespMessage()
        self.respMesage.statusCode = statusCode;
        self.respMesage.reasonPhrase = RTSPConstants.statusDict[statusCode]
        self.respMesage.header['CSeq'] = CSeq

    def getMessage(self):
        statusLine = self.respMesage.RTSPVersion + RTSPConstants.SP + self.respMesage.statusCode +\
                     RTSPConstants.SP + self.respMesage.reasonPhrase + RTSPConstants.CRLF

        header = ''
        for key, value in self.respMesage.header.iteritems():
            header += key + ': ' + str(value).strip('[]').replace('\'','') + RTSPConstants.CRLF

        return statusLine + header + RTSPConstants.CRLF