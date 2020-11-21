import pytest
from main.CensusAnalyserException import WrongFilePathError, WrongFileExtensionError

STATE_CENSUS_DATA_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'
WRONG_STATE_CENSUS_DATA_PATH = 'Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.json'
STATE_CODE_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.csv'
WRONG_STATE_CODE_DATA_PATH = 'Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.json'


@pytest.mark.parametrize("file_path , expected" , [
    (STATE_CENSUS_DATA_PATH , 29),
    (STATE_CODE_PATH , 37)
])
def test_count_records_in_census_data_csv_file(file_path , expected ,instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(file_path)
    assert count_of_records == expected


@pytest.mark.parametrize("file_path , expected" , [
    (WRONG_STATE_CENSUS_DATA_PATH , WrongFilePathError),
    (WRONG_STATE_CODE_DATA_PATH , WrongFilePathError),
    (WRONG_FILE_EXTENSION , WrongFileExtensionError),
    (WRONG_STATE_CODE_FILE_EXTENSION , WrongFileExtensionError)
])
def test_given_wrong_file_path_or_extension_should_raise_appropriate_exception(instance_of_census_analyser ,file_path , expected ):
    with pytest.raises(expected):
        instance_of_census_analyser.load_census_data(file_path)
