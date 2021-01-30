from xmlExtractor.resources import XMLManager
from xmlExtractor.resources import AWSManager


def start():
    xml_obj = XMLManager()
    xml_obj.initiate_process()
    AWSManager(xml_obj.outfile)


if __name__ == '__main__':
    start()
