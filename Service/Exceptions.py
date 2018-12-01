class NoneContextException(Exception):
    def __init__(self, message):
        super(NoneContextException, self).__init__(message)
