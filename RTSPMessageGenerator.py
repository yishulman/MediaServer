
from RTSPRespMessage import RTSPRespMessage
from RTSPConstants import RTSPConstants

class RTSPMessageGenerator:

    def __init__(self, statusCode, CSeq):
        self.respMesage =  RTSPRespMessage()
        self.respMesage.statusCode = statusCode;
        self.respMesage.reasonPhrase = RTSPConstants.statusDict[statusCode]
        self.respMesage.header['CSeq'] = CSeq


    def getMessage(self):

        if (self.respMesage.entity_header.has_key('Content-Type')):
            self.respMesage.entity_body = self.get_dsp_message()
            self.respMesage.entity_header['Content-Length'] = len(self.respMesage.entity_body) 

        statusLine = self.respMesage.RTSPVersion + RTSPConstants.SP + self.respMesage.statusCode +\
                     RTSPConstants.SP + self.respMesage.reasonPhrase + RTSPConstants.CRLF

        header = ''
        for key, value in self.respMesage.header.iteritems():
            header += key + ': ' + str(value).strip('[]').replace('\'','') + RTSPConstants.CRLF

        entity_header = ''
        for key, value in self.respMesage.entity_header.iteritems():
            entity_header += key + ': ' + str(value).strip('[]').replace('\'','') + RTSPConstants.CRLF



        return statusLine + header +  entity_header + RTSPConstants.CRLF + self.respMesage.entity_body

    def get_dsp_message(self):
        return                   'v=0'  + RTSPConstants.CRLF  \
                                  + 'o=- 15951401707883677857 15951401707883677857 IN IP4 DESKTOP-TKRJJ92' + RTSPConstants.CRLF  \
                                  + 's=Unnamed' + RTSPConstants.CRLF  \
                                  + 'i=N/A' + RTSPConstants.CRLF  \
                                  + 'c=IN IP4 0.0.0.0' + RTSPConstants.CRLF  \
                                  + 't=0 0' + RTSPConstants.CRLF  \
                                  + 'a=tool:vlc 2.2.6' + RTSPConstants.CRLF  \
                                  + 'a=recvonly' + RTSPConstants.CRLF  \
                                  + 'a=type:broadcast' + RTSPConstants.CRLF  \
                                  + 'a=charset:UTF-8' + RTSPConstants.CRLF  \
                                  + 'a=control:rtsp://169.254.19.202:8554/' + RTSPConstants.CRLF  \
                                  + 'm=audio 0 RTP/AVP 96' + RTSPConstants.CRLF  \
                                  + 'b=RR:0' + RTSPConstants.CRLF  \
                                  + 'a=rtpmap:96 mpeg4-generic/44100/2' + RTSPConstants.CRLF  \
                                  + 'a=fmtp:96 streamtype=5; profile-level-id=15; mode=AAC-hbr; config=1210; SizeLength=13; IndexLength=3; IndexDeltaLength=3; Profile=1;' + RTSPConstants.CRLF  \
                                  + 'a=control:rtsp://169.254.19.202:8554/trackID=0' + RTSPConstants.CRLF  \
                                  + 'm=video 0 RTP/AVP 96' + RTSPConstants.CRLF  \
                                  + 'b=RR:0' + RTSPConstants.CRLF  \
                                  + 'a=rtpmap:96 H264/90000' + RTSPConstants.CRLF  \
                                  + 'a=fmtp:96 packetization-mode=1;profile-level-id=64001f;sprop-parameter-sets=Z2QAH6zZQFAFuwEQAAADABAAAAMDKPGDGWA=,aOvvLA==;' + RTSPConstants.CRLF  \
                                  + 'a=control:rtsp://169.254.19.202:8554/trackID=1' + RTSPConstants.CRLF + RTSPConstants.CRLF