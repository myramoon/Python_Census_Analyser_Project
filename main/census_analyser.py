import csv
import logging

class CensusAnalyser:

    logging.basicConfig(filename='census_analyser.log', level = logging.DEBUG , format = '%(name)s | %(levelname)s | %(asctime)s | %(message)s' )


    def load_census_data(self , csv_file_path):
        """
        :param csv_file_path:path containing csv file to be opened
        :return: number of records excluding header in csv file
        """
        with open(csv_file_path , 'r') as census_data:
            csv_reader = csv.reader(census_data)
            next(csv_reader)
            count = (len(list(csv_reader)))
            logging.debug('Number of records: {}'.format(count))
            return count

