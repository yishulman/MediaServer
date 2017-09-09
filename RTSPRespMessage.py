from collections import OrderedDict
class RTSPRespMessage:

    def __init__(self):
        self.RTSPVersion = 'RTSP/1.0'
        self.statusCode = ''
        self.reasonPhrase = ''

        self.header =  OrderedDict();
        self.header['CSeq'] = '-1'

        self.entity_header = OrderedDict();

        self.entity_body = ""

    















    