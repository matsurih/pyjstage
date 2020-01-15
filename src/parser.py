from lxml import etree
from src.result import Result, ErrorResult, ListResult, SearchResult
from datetime import datetime
import re


class Parser:
    def __init__(self):
        self.regex = re.compile(r'\n* +')

    def parse(self, xml_text: bytes) -> Result:
        result = Result()

        root = etree.fromstring(xml_text)
        result.xmlns = root.nsmap
        result.xmlns['xml'] = 'http://www.w3.org/XML/1998/namespace'
        result.xml_lang = root.find('[@xml:lang]', result.xmlns).attrib.values()[0]
        result.xml_version = etree.ElementTree(root).docinfo.xml_version
        result.encoding = etree.ElementTree(root).docinfo.encoding
        result.servicecd = int(root.find('./servicecd', result.xmlns).text)
        result.title = root.find('./title', result.xmlns).text
        result.link = self.regex.sub('', root.find('./link', result.xmlns).attrib['href'])
        result.id = self.regex.sub('', root.find('./id', result.xmlns).text)
        result.updated = datetime.fromisoformat(root.find('./updated', result.xmlns).text)
        result.total_results = int(root.find('./opensearch:totalResults', result.xmlns).text)
        result.start_index = int(root.find('./opensearch:startIndex', result.xmlns).text)
        result.items_per_page = int(root.find('./opensearch:itemsPerPage', result.xmlns).text)
        result.entries = list(root.findall('./entry', result.xmlns))
        result.status = int(root.find('./result/status', result.xmlns).text)
        result.message = root.find('./result/message', result.xmlns).text
        if result.status != 0:
            return ErrorResult(result)
        if result.servicecd == 2:
            rresult = ListResult(result)
        elif result.servicecd == 3:
            rresult = SearchResult(result)
        else:
            return ErrorResult(result)
        return rresult


