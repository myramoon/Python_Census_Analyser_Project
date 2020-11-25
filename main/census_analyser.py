import csv
import json
import logging
from main.CensusAnalyserException import CensusAnalyserError, ExceptionType

logging.basicConfig(filename='log_census_analyser.log', level=logging.DEBUG, format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')


class CensusAnalyser:


    census_list = []
    def validate_csv(self, csv_file_path):
        self.validate_extension(csv_file_path)
        self.validate_delimiter(csv_file_path)
        self.check_header(csv_file_path)

    def validate_delimiter(self , csv_file_path):
        """
        checks whether the csv uses specified delimiter
        :param csv_file_path: takes in csv file path to check delimiter
        :return: no argument or raises exception
        """
        try:
            with open(csv_file_path, newline="") as csv_data:
                csv.Sniffer().sniff(csv_data.read(), delimiters=",")
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise CensusAnalyserError(ExceptionType.FilePathError, "Please enter correct file path")
        except:
            logging.exception('Exception occurred due to improper delimiter')
            raise CensusAnalyserError(ExceptionType.DelimiterError, "Could not determine delimiter")

    def check_header(self,csv_file_path):
        """
        checks whether header exists in csv
        :param csv_file_path: takes in csv file path to check header
        :return:no argument or raises exception
        """
        try:
            with open(csv_file_path, newline="") as csv_data:
                    if not csv.Sniffer().has_header(csv_data.read()):
                        logging.error('Exception occurred due to improper header',exc_info = True)
                        raise CensusAnalyserError(ExceptionType.ImproperHeader, "Please check csv file's header")
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise CensusAnalyserError(ExceptionType.FilePathError , "Please enter correct file path")

    def validate_extension(self , csv_file_path):
        """
        verifies .csv extension in file path
        :param csv_file_path: takes in csv file path to check extension
        :return: no argument
        """
        if not csv_file_path.endswith(".csv"):
            logging.error('Exception occurred due to wrong file extension' , exc_info=True)
            raise CensusAnalyserError(ExceptionType.FileExtensionError , "Please enter correct file extension")

    def load_census_data(self , csv_file_path):
        """
        loads and stores csv data into list
        :param csv_file_path:path containing csv file to be opened
        :return: number of records excluding header in csv file
        """
        try:
            self.validate_csv(csv_file_path)
            with open(csv_file_path , 'r',newline = '') as census_data:
                csv_reader = csv.DictReader(census_data, delimiter =',')
                for row in csv_reader:
                    census_list_dict = {}
                    for key in row:
                        census_list_dict[key] = row.get(key)
                    self.census_list.append(census_list_dict)
                logging.debug('Number of records: {}'.format(len(self.census_list)))
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise CensusAnalyserError(ExceptionType.FilePathError , "Please enter correct file path")
        return len(self.census_list)

    def convert_to_json_format(self , result):
        """
        converts sorted data into json format and stores  in list
        :param result: sorted data
        """
        sorted_list = []
        for list_item in result:
            sorted_list.append(json.dumps(list_item))

    def sort_by_state(self , csv_file_path):
        """
        sorts csv data by key 'State'
        :param csv_file_path: file path to load csv data
        :return: tuple containing states at extremes after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: x.get('State'))
        self.convert_to_json_format(result)
        logging.debug('start state and end state: {} {}'.format(result[0].get('State') , result[len(result) - 1].get('State') ))
        return  result

    def sort_by_state_code(self, csv_file_path):
        """
        sorts csv data by key 'StateCode'
        :param csv_file_path: file path to load csv data
        :return: tuple containing state codes at extremes after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key=lambda x: x.get('StateCode'))
        self.convert_to_json_format(result)
        logging.debug('start state and end state : {} {}'.format(result[0].get('StateCode') , result[len(result) - 1].get('StateCode') ))
        return result

    def create_json_file(self , json_file_name , sorted_list):
        """
        creates json file from data in sorted list
        :param json_file_name: file name to be used for json file
        :param sorted_list: contains sorted data by criterion
        """
        with open(json_file_name, 'w') as outfile:
            json.dump(sorted_list, outfile , indent = 4)

    def sort_by_population(self , csv_file_path):
        """
        sorts csv data by key 'Population'
        :param csv_file_path: file path to load csv data
        :return: most populous state after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: int(x.get('Population')) , reverse = True)
        self.create_json_file('sorted_by_population.json' , result)
        logging.debug('most populous state: {}'.format(int(result[0].get('Population'))))
        return result


    def sort_by_population_density(self , csv_file_path):
        """
        sorts csv data by key 'DensityPerSqKm'
        :param csv_file_path: file path to load csv data
        :return: most densely populous state after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: int(x.get('DensityPerSqKm')) , reverse = True)
        self.create_json_file('sorted_by_density_population.json', result)
        logging.debug('most densely populous state: {}'.format(int(result[0].get('DensityPerSqKm'))))
        return result

    def sort_by_area(self , csv_file_path):
        """
        sorts csv data by key 'AreaInSqKm'
        :param csv_file_path: file path to load csv data
        :return: largest area state after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: int(x.get('AreaInSqKm')) , reverse = True)
        self.create_json_file('sorted_by_area.json', result)
        logging.debug('largest area state: {}'.format(int(result[0].get('AreaInSqKm'))))
        return result




