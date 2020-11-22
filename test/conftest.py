import pytest
from main.census_analyser import CensusAnalyser


@pytest.fixture
def instance_of_census_analyser():
    census_analyser = CensusAnalyser()
    return census_analyser