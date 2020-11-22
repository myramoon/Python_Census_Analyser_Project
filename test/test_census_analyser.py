import pytest
from main.CensusAnalyserException import CensusAnalyserError

STATE_CENSUS_DATA_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'
WRONG_STATE_CENSUS_DATA_PATH = 'Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.json'
IMPROPER_STATE_CENSUS_HEADER = '/Users/nusrat/PycharmProjects/census_analyser_project/main/MissingHeader_IndiaStateCensusData.csv'
WRONG_DELIMITER_STATE_CENSUS = '/Users/nusrat/PycharmProjects/census_analyser_project/main/Delimiter_IndiaStateCensusData.csv'
STATE_CODE_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.csv'
WRONG_STATE_CODE_DATA_PATH = 'Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.json'
WRONG_DELIMITER_STATE_CODE = '/Users/nusrat/PycharmProjects/census_analyser_project/main/Wrong_Delimiter_IndiaStateCode.csv'
IMPROPER_STATE_CODE_HEADER = '/Users/nusrat/PycharmProjects/census_analyser_project/main/Missing_Header_IndiaStateCode.csv'


def test_count_records_in_census_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(STATE_CENSUS_DATA_PATH)
    assert count_of_records == 29


@pytest.mark.parametrize("file_path , expected" , [
    (WRONG_STATE_CENSUS_DATA_PATH , CensusAnalyserError),
    (WRONG_FILE_EXTENSION , CensusAnalyserError),
    (WRONG_DELIMITER_STATE_CENSUS , CensusAnalyserError),
    (IMPROPER_STATE_CENSUS_HEADER , CensusAnalyserError)
])
def test_given_wrong_file_path_or_extension_should_raise_appropriate_exception(instance_of_census_analyser ,file_path , expected ):
    with pytest.raises(expected):
        instance_of_census_analyser.load_census_data(file_path)

def test_count_records_in_state_code_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_state_code_data(STATE_CODE_PATH)
    assert count_of_records == 37


@pytest.mark.parametrize("file_path , expected" , [
    (IMPROPER_STATE_CODE_HEADER , CensusAnalyserError),
    (WRONG_DELIMITER_STATE_CODE , CensusAnalyserError),
    (WRONG_STATE_CODE_DATA_PATH , CensusAnalyserError),
    (WRONG_STATE_CODE_FILE_EXTENSION , CensusAnalyserError),

])
def test_given_wrong_file_path_or_extension_should_raise_appropriate_exception(instance_of_census_analyser ,file_path , expected ):
    with pytest.raises(expected):
        instance_of_census_analyser.load_state_code_data(file_path)


