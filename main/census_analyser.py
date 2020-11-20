import csv
import logging
from main.CensusAnalyserException import WrongFilePathError


class CensusAnalyser:
    logging.basicConfig(filename='census_analyser.log', level = logging.DEBUG , format = '%(name)s | %(levelname)s | %(asctime)s | %(message)s' )

    def load_census_data(self , csv_file_path):
        """
        :param csv_file_path:path containing csv file to be opened
        :return: number of records excluding header in csv file
        """
        try:
            with open(csv_file_path , 'r') as census_data:
                csv_reader = csv.reader(census_data)
                next(csv_reader)
                count = (len(list(csv_reader)))
                logging.debug('Number of records: {}'.format(count))
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise WrongFilePathError("Please enter correct file path")

        return count