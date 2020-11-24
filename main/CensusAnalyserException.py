import enum

class ExceptionType(enum.Enum):
    """
    :param: enums associated to possible errors in census_analyser
    """
    FilePathError = "Please give proper file path"
    FileExtensionError = "Please check file extension"
    ImproperHeader = "Please check csv file's header"
    DelimiterError = "Could not determine delimiter"

class CensusAnalyserError(Exception):

    def __init__(self, *args):
        """
        :param args: type and message associated to exception
        """
        self.type = args[0]
        self.message = args[1]

