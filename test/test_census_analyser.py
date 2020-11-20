import pytest
from main.CensusAnalyserException import WrongFilePathError, WrongFileExtensionError

STATE_CENSUS_DATA_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'
WRONG_STATE_CENSUS_DATA_PATH = 'Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.json'
STATE_CODE_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.csv'
WRONG_STATE_CODE_DATA_PATH = 'Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCode.json'

def test_count_records_in_census_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(STATE_CENSUS_DATA_PATH)
    assert count_of_records == 29

def test_given_wrong_file_path_should_raise_exception(instance_of_census_analyser):
    with pytest.raises(WrongFilePathError):
        instance_of_census_analyser.load_census_data(WRONG_STATE_CENSUS_DATA_PATH)

def test_given_wrong_file_extension_should_raise_exception(instance_of_census_analyser):
    with pytest.raises(WrongFileExtensionError):
        instance_of_census_analyser.load_census_data(WRONG_FILE_EXTENSION)

def test_count_records_in_state_code_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(STATE_CODE_PATH)
    assert count_of_records == 37

def test_given_wrong_state_code_file_path_should_raise_exception(instance_of_census_analyser):
    with pytest.raises(WrongFilePathError):
        instance_of_census_analyser.load_census_data(WRONG_STATE_CENSUS_DATA_PATH)

def test_given_wrong_state_code_file_extension_should_raise_exception(instance_of_census_analyser):
    with pytest.raises(WrongFileExtensionError):
        instance_of_census_analyser.load_census_data(WRONG_FILE_EXTENSION)
