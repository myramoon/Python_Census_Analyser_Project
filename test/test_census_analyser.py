

STATE_CENSUS_DATA_PATH = '/Users/nusrat/PycharmProjects/PythonProjects/census_analyser_project/main/IndiaStateCensusData.csv'

def test_count_records_in_census_data_csv_file(instance_of_census_analyser):
    count_of_records = instance_of_census_analyser.load_census_data(STATE_CENSUS_DATA_PATH)
    assert count_of_records == 29

