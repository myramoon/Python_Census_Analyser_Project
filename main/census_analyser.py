import csv
import logging
from main.CensusAnalyserException import WrongFileExtensionError , WrongFilePathError


class CensusAnalyser:
    logging.basicConfig(filename='census_analyser.log',filemode='w', level = logging.DEBUG , format = '%(name)s | %(levelname)s | %(asctime)s | %(message)s' )

    def validate_extension(self , csv_file_path):
        """
        :param csv_file_path: takes in csv file path to check extension
        :return: no argument
        """
        if not csv_file_path.endswith(".csv"):
            logging.exception('Exception occurred due to wrong file extension')
            raise WrongFileExtensionError("Please enter correct file extension")

    def load_census_data(self , csv_file_path):
        """
        :param csv_file_path:path containing csv file to be opened
        :return: number of records excluding header in csv file
        """
        self.validate_extension(csv_file_path)
        try:
            with open(csv_file_path , 'r') as census_data:
                csv_reader = csv.reader(census_data)
                next(csv_reader)
                count = len(list(csv_reader))
                logging.debug('Number of records: {}'.format(count))

        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise WrongFilePathError("Please enter correct file path")

        return count