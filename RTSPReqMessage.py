
class RTSPReqMessage:

    def __init__(self):
        self.method = ""
        self.URI = ""
        self.RTSPVersion = ""

        self.header = {'CSeq': '-1'}