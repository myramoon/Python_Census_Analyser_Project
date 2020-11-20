class CensusAnalyserError(Exception):
    def __init__(self, message):
        """
        :param message:custom message to be displayed
        """
        super().__init__(message)

class WrongFilePathError(CensusAnalyserError):
    pass

class WrongFileExtensionError(CensusAnalyserError):
    pass
