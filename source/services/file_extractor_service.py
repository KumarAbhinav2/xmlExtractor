import csv
from source import logger
from source.models.file_paths import FilePaths
from source.constants import CSVConstants as cconst
from source.exceptions import CSVExtractionError
from source.services.file_extractor_service_interface import FileExtractorServiceInterface

log = logger.getLogger(__name__)


class CSVExtractorService(FileExtractorServiceInterface):
    """
    CSVExtractorService

    This class takes care of writing data buffer to csv file.
    currently, writes the file on the disk

    Attributes:
    ----------
    path: object
        instance of the filePath model
    outfile: str
        path of the output csv file
    writer: object
        handle of the csv writer

    Methods:
    --------
    set_output_file_path(outfile)
        saves the outfile path
    csv_writer
        simple csv file writer
    get_writer
        returns writer handle
    get_outfile
        returns output file path
    """

    def __init__(self):
        self.path = FilePaths()
        # TODO - make this dynamic with unique name
        self.outfile = cconst.output_file
        self.writer = self.csv_writer()

    def set_output_file_path(self, outfile):
        """
        Saves the output file path
        Args:
            outfile (str): path to the file
        """
        return self.path.output_file_path(outfile)

    def csv_writer(self):
        """
        Simple csv file writer
        """
        try:
            log.info(f"Initiating extracting csv from xml at {self.outfile}")
            data = open(self.outfile, 'w', newline='', encoding='utf-8')
            csvwriter = csv.writer(data)
            csvwriter.writerow(cconst.cols)
            return csvwriter
        except Exception:
            raise CSVExtractionError

    def get_writer(self):
        """
        returns writer handle
        """
        return self.writer

    def get_outfile(self):
        """
        returns output file path
        """
        return self.outfile
