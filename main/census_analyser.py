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
        :param csv_file_path: takes in csv file path to check delimiter
        :return: no argument or raises exception
        """
        with open(csv_file_path, newline="") as csv_data:
            try:
                csv.Sniffer().sniff(csv_data.read(), delimiters=",")
            except:
                logging.exception('Exception occurred due to improper delimiter')
                raise CensusAnalyserError(ExceptionType.DelimiterError, "Could not determine delimiter")

    def check_header(self,csv_file_path):
        """
        :param csv_file_path: takes in csv file path to check header
        :return:no argument or raises exception
        """
        with open(csv_file_path, newline="") as csv_data:
                if not csv.Sniffer().has_header(csv_data.read()):
                    logging.error('Exception occurred due to improper header',exc_info = True)
                    raise CensusAnalyserError(ExceptionType.ImproperHeader, "Please check csv file's header")

    def validate_extension(self , csv_file_path):
        """
        :param csv_file_path: takes in csv file path to check extension
        :return: no argument
        """
        if not csv_file_path.endswith(".csv"):
            logging.error('Exception occurred due to wrong file extension' , exc_info=True)
            raise CensusAnalyserError(ExceptionType.FileExtensionError , "Please enter correct file extension")

    def load_census_data(self , csv_file_path):
        """
        :param csv_file_path:path containing csv file to be opened
        :return: number of records excluding header in csv file
        """
        try:
            self.validate_csv(csv_file_path)
            with open(csv_file_path , 'r',newline = '') as census_data:
                csv_reader = csv.DictReader(census_data, delimiter =',' )
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

    def sort_by_state(self , csv_file_path):
        """
        :param csv_file_path: file path to load csv data
        :return: tuple containing states at extremes after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: x.get('State'))
        sorted_list = []
        for list_item in result:
            sorted_list.append(json.dumps(list_item))
        logging.debug('start state and end state: {} {}'.format(result[0].get('State') , result[len(result) - 1].get('State') ))
        return result[0].get('State') , result[len(result) - 1].get('State')

    def sort_by_population(self , csv_file_path):
        """
        :param csv_file_path: file path to load csv data
        :return: most populous state after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: int(x.get('Population')) , reverse = True)
        with open('sorted_by_population.json', 'w') as outfile:
            json.dump(result, outfile , indent = 4)
        logging.debug('most populous state: {}'.format(int(result[0].get('Population'))))
        return int(result[0].get('Population'))

    def sort_by_state_code(self, csv_file_path):
        """
        :param csv_file_path: file path to load csv data
        :return: tuple containing state codes at extremes after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key=lambda x: x.get('StateCode'))
        sorted_list = []
        for list_item in result:
            sorted_list.append(json.dumps(list_item))
        logging.debug('start state and end state : {} {}'.format(result[0].get('StateCode') , result[len(result) - 1].get('StateCode') ))
        return result[0].get('StateCode'), result[len(result) - 1].get('StateCode')

    def sort_by_population_density(self , csv_file_path):
        """
        :param csv_file_path: file path to load csv data
        :return: most densely populous state after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: int(x.get('DensityPerSqKm')) , reverse = True)
        with open('sorted_by_density_population.json', 'w') as outfile:
            json.dump(result, outfile , indent = 4)
        logging.debug('most densely populous state: {}'.format(int(result[0].get('DensityPerSqKm'))))
        return int(result[0].get('DensityPerSqKm'))

    def sort_by_area(self , csv_file_path):
        """
        :param csv_file_path: file path to load csv data
        :return: largest area state after sorting
        """
        self.load_census_data(csv_file_path)
        result = sorted(self.census_list, key = lambda x: int(x.get('AreaInSqKm')) , reverse = True)
        with open('sorted_by_area.json', 'w') as outfile:
            json.dump(result, outfile , indent = 4)
        logging.debug('largest area state: {}'.format(int(result[0].get('AreaInSqKm'))))
        return int(result[0].get('AreaInSqKm'))


