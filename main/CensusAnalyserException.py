import enum

class ExceptionType(enum.Enum):

    FilePathError = "Please give proper file path"
    FileExtensionError = "Please check file extension"
    ImproperHeader = "Please check csv file's header"
    DelimiterError = "Could not determine delimiter"

class CensusAnalyserError(Exception):

    def __init__(self, *args):
        """
        :param message:custom message to be displayed
        """
        self.type = args[0]
        self.message = args[1]

