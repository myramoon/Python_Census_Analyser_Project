import csv
import logging
from main.CensusAnalyserException import CensusAnalyserError, ExceptionType

logging.basicConfig(filename='log_census_analyser.log', level=logging.DEBUG, format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')

class CensusAnalyser:


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
        self.validate_extension(csv_file_path)
        try:
            with open(csv_file_path , 'r') as census_data:
                self.validate_delimiter(csv_file_path)
                csv_reader = csv.DictReader(census_data)
                count = 0
                for row in csv_reader:
                    count += 1
                    print(row['State'],row['Population'],row['AreaInSqKm'],row['DensityPerSqKm'])
                logging.debug('Number of records: {}'.format(count))

        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise CensusAnalyserError(ExceptionType.FilePathError , "Please enter correct file path")
        except KeyError:
            logging.exception('Exception occurred due to improper header')
            raise CensusAnalyserError(ExceptionType.ImproperHeader, "Please check csv file's header")

        return count

    def load_state_code_data(self , csv_file_path):
        """
        :param csv_file_path:path containing csv file to be opened
        :return: number of records excluding header in csv file
        """
        self.validate_extension(csv_file_path)
        try:
            with open(csv_file_path , 'r') as census_data:
                self.validate_delimiter(csv_file_path)
                csv_reader = csv.DictReader(census_data , delimiter = ',')
                count = 0
                for row in csv_reader:
                    count += 1
                    print(row['SrNo'],row['State Name'],row['TIN'],row['StateCode'])
                logging.debug('Number of records: {}'.format(count))
        except FileNotFoundError:
            logging.exception('Exception occurred due to wrong file path')
            raise CensusAnalyserError(ExceptionType.FilePathError , "Please enter correct file path")
        except KeyError:
            logging.exception('Exception occurred due to improper header')
            raise CensusAnalyserError(ExceptionType.ImproperHeader, "Please check csv file's header")

        return count

