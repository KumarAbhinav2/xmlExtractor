from urllib.request import urlopen
from xmlExtractor.settings import XML_URL, XMLConstants as xconst
from lxml import etree
import requests
import zipfile
import io
from xmlExtractor.resources.csv_handler import CSVHandler

from xmlExtractor import logger

log = logger.getLogger(__name__)


class XMLManager:

    def __init__(self):
        self.doc = self._get_doc()
        self.ns = xconst.nmap
        self.outfile = './outcsv.csv'
        self.csvwriter = CSVHandler(self.outfile).get_handle()

    def _get_doc(self):
        var_url = urlopen(XML_URL)
        return etree.parse(var_url)

    def _fetch_zip_url(self):
        for tag in self.doc.iterfind(xconst.URL_TAG):
            for children in tag.items():
                if children[1] == xconst.URL_ATTRIBUTE:
                    url = tag.text
                    if url:
                        return url

    def _extract_zip(self, url):
        #r = requests.get('http://firds.esma.europa.eu/firds/DLTINS_20210117_01of01.zip')
        r = requests.get(url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        for name in z.namelist():
            ex_file = z.open(name)  # this is a file like object
            content = ex_file.read()
            return etree.fromstring(content)

    def process_core_xml(self, xml_url):
        root = self._extract_zip(xml_url)
        for act in root.findall(xconst.record_tag, self.ns):
            data = []
            for ch in act.findall(xconst.child1, self.ns):
                data.extend([c.text for c in ch])
            for el in act.findall(xconst.child2, self.ns):
                data.append(el.text)
            self.csvwriter.writerow(data)

    def initiate_process(self):
        url = self._fetch_zip_url()
        self.process_core_xml(url)