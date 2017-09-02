class RTSPConstants:
    #Constatnts
    CR = "\r"
    LF = "\n"
    HT = "\t"
    SP = " "
    CRLF = CR + LF
    RTSP_Version = "RTSP/1.0"

    #6.1 Request Line Methods
    method  =   ['DESCRIBE', 'ANNOUNCE', 'GET_PARAMETER', 'OPTIONS', 'PAUSE', 'PLAY', 'RECORD', 'REDIRECT', 'SETUP', 'SET_PARAMETER', 'TEARDOWN']

    statusDict = {'100': 'Continue',
                  '200': 'OK', '201': 'Created', '250': 'Low on Storage Space',
                  '300': 'Multiple Choices', '301': 'Moved Permanently', '302': 'Moved Temporarily', '303': 'See Other',
                  '304': 'Not Modified', '305': 'Use Proxy',
                  '400': 'Bad Request', '401': 'Unauthorized', '402': 'Payment Required', '403': 'Forbidden',
                  '404': 'Not Found', '405': 'Method Not Allowed', '406': 'Not Acceptable',
                  '407': 'Proxy Authentication Required', '408': 'Request Time-out', '410': 'Gon',
                  '411': 'Length Required', '412': 'recondition Failed', '413': 'Request Entity Too Large',
                  '414': 'Request-URI Too Large', '415': 'Unsupported Media Type', '451': 'Parameter Not Understood',
                  '452': 'Conference Not Found', '453': 'Not Enough Bandwidth', '454': 'Session Not Found',
                  '455': 'Method Not Valid in This State', '456': 'Header Field Not Valid for Resource',
                  '457': 'Invalid Range',
                  '458': 'Parameter Is Read-Only', '459': 'Aggregate operation not allowed',
                  '460': 'Only aggregate operation allowed',
                  '461': 'Unsupported transport', '462': 'Destination unreachable',
                  '500': 'Internal Server Error', '501': 'Not Implemented', '502': 'Bad Gateway',
                  '503': 'Service Unavailable',
                  '504': 'Gateway Time-out', '505': 'RTSP Version not supported', '551': 'Option not supported'}

    public = ['DESCRIBE', 'SETUP', 'TEARDOWN', 'PLAY', 'PAUSE']