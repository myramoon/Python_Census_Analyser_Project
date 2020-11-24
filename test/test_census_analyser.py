import pytest
from main.CensusAnalyserException import CensusAnalyserError

STATE_CENSUS_DATA_PATH = '../main/IndiaStateCensusData.csv'
WRONG_STATE_CENSUS_DATA_PATH = 'rmain/IndiaStateCensusData.csv'
WRONG_FILE_EXTENSION = '../main/IndiaStateCensusData.json'
IMPROPER_STATE_CENSUS_HEADER = '../main/MissingHeader_IndiaStateCensusData.csv'
WRONG_DELIMITER_STATE_CENSUS = '../main/Delimiter_IndiaStateCensusData.csv'
STATE_CODE_PATH = '../main/IndianStateCode.csv'
WRONG_STATE_CODE_DATA_PATH = 'project/main/IndianStateCode.csv'
WRONG_STATE_CODE_FILE_EXTENSION = '../main/IndianStateCode.json'
WRONG_DELIMITER_STATE_CODE = '../main/Wrong_Delimiter_IndiaStateCode.csv'
IMPROPER_STATE_CODE_HEADER = '../main/Missing_Header_IndiaStateCode.csv'


def test_count_records_in_census_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(STATE_CENSUS_DATA_PATH)
    assert count_of_records == 29


@pytest.mark.parametrize("file_path , expected" , [
    (WRONG_STATE_CENSUS_DATA_PATH , CensusAnalyserError),
    (WRONG_FILE_EXTENSION , CensusAnalyserError),
    (WRONG_DELIMITER_STATE_CENSUS , CensusAnalyserError),
    (IMPROPER_STATE_CENSUS_HEADER , CensusAnalyserError)
])
def test_given_wrong_file_should_raise_appropriate_exception(instance_of_census_analyser ,file_path , expected ):
    with pytest.raises(expected):
        instance_of_census_analyser.load_census_data(file_path)

def test_count_records_in_state_code_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(STATE_CODE_PATH)
    assert count_of_records == 37


@pytest.mark.parametrize("file_path , expected" , [
    (IMPROPER_STATE_CODE_HEADER , CensusAnalyserError),
    (WRONG_DELIMITER_STATE_CODE , CensusAnalyserError),
    (WRONG_STATE_CODE_DATA_PATH , CensusAnalyserError),
    (WRONG_STATE_CODE_FILE_EXTENSION , CensusAnalyserError),

])
def test_given_wrong_file_path_or_extension_should_raise_appropriate_exception(instance_of_census_analyser ,file_path , expected ):
    with pytest.raises(expected):
        instance_of_census_analyser.load_census_data(file_path)

def test_start_state_in_sort_state_method_in_state_census_csv_file(instance_of_census_analyser):
    state_tuple = instance_of_census_analyser.sort_by_state(STATE_CENSUS_DATA_PATH)
    assert state_tuple[0] == "Andhra Pradesh"

def test_end_state_in_sort_state_method_in_state_census_csv_file(instance_of_census_analyser):
    state_tuple = instance_of_census_analyser.sort_by_state(STATE_CENSUS_DATA_PATH)
    assert state_tuple[1] == "West Bengal"

def test_start_state_in_sort_state_code_method_in_state_code_csv_file(instance_of_census_analyser):
    state_tuple = instance_of_census_analyser.sort_by_state_code(STATE_CODE_PATH)
    assert state_tuple[0] == "AD"

def test_end_state_in_sort_state_code_method_in_state_code_csv_file(instance_of_census_analyser):
    state_tuple = instance_of_census_analyser.sort_by_state_code(STATE_CODE_PATH)
    assert state_tuple[1] == "WB"

def test_most_populous_state_in_sort_population_method_in_state_census_csv_file(instance_of_census_analyser):
    most_populous = instance_of_census_analyser.sort_by_population(STATE_CENSUS_DATA_PATH)
    assert most_populous == 199812341

def test_most_densely_populous_state_in_sort_population_density_method_in_state_census_csv_file(instance_of_census_analyser):
    most_densely_populous = instance_of_census_analyser.sort_by_population_density(STATE_CENSUS_DATA_PATH)
    assert most_densely_populous == 1102

def test_largest_state_by_area_in_sort_area_method_in_state_census_csv_file(instance_of_census_analyser):
    largest_area = instance_of_census_analyser.sort_by_area(STATE_CENSUS_DATA_PATH)
    assert largest_area == 342239

