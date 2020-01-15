from typing import List, Dict
import re
from lxml import etree
from datetime import datetime


class Entry:
    article_title = {}
    article_link = None
    author = None
    cdjournal = None
    material_title = None
    issn = None
    eissn = None
    volume = None
    number = None
    starting_page = None
    ending_page = None
    pubyear = None
    doi = None
    systemcode = None
    systemname = None
    title = None
    link = None
    id = None
    updated = None

    def __str__(self):
        return str(self.__dict__.items())


class Result:
    encoding = None
    xml_version = None
    xmlns: Dict[str, str] = None
    xmlns_prism: str = None
    xmlns_opensearch: str = None
    xml_lang: str = None
    status: int = None
    message: str = None
    title: str = None
    link: str = None
    id: int = None
    servicecd: int = None
    updated: datetime = None
    total_results = None
    start_index = None
    items_per_page = None
    entries = []


class ErrorResult(Result):
    def __init__(self, result: Result = None):
        print(result.status, result.message)


class SearchResult(Result):
    def __init__(self, result: Result):
        self.encoding = result.encoding
        self.xml_version = result.xml_version
        self.xmlns = result.xmlns
        self.xml_lang = result.xml_lang
        self.status = result.status
        self.message = result.message
        self.title = result.title
        self.link = result.link
        self.id = result.id
        self.servicecd = result.servicecd
        self.updated = result.updated
        self.total_results = result.total_results
        self.start_index = result.start_index
        self.items_per_page = result.items_per_page
        self.entries_temp = result.entries
        self.entries = []
        regex = re.compile(r'{.+\}')
        for e in self.entries_temp:
            ent = Entry()
            ent.article_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./article_title', self.xmlns)
            }
            ent.article_link = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./article_link', self.xmlns)
            }
            ent.author = {
                regex.sub('', t.tag): list(t)[0].text.replace('\n', '').strip() for t in e.find('./author', self.xmlns)
            }
            ent.article_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./article_title', self.xmlns)
            }
            ent.cdjournal = e.find('./cdjournal', self.xmlns).text.replace('\n', '').strip()
            ent.material_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./material_title', self.xmlns)
            }
            ent.issn = e.find('./prism:issn', self.xmlns).text.replace('\n', '').strip()
            ent.eissn = e.find('./prism:eIssn', self.xmlns).text.replace('\n', '').strip()
            ent.volume = int(e.find('./prism:volume', self.xmlns).text.replace('\n', '').strip())
            ent.number = int(e.find('./prism:number', self.xmlns).text.replace('\n', '').strip())
            ent.starting_page = int(e.find('./prism:startingPage', self.xmlns).text.replace('\n', '').strip())
            ent.ending_page = int(e.find('./prism:endingPage', self.xmlns).text.replace('\n', '').strip())
            ent.pubyear = int(e.find('./pubyear', self.xmlns).text.replace('\n', '').strip())
            ent.doi = e.find('./prism:doi', self.xmlns).text.replace('\n', '').strip()
            ent.systemcode = int(e.find('./systemcode', self.xmlns).text.replace('\n', '').strip())
            ent.systemname = e.find('./systemname', self.xmlns).text.replace('\n', '').strip()
            ent.title = e.find('./title', self.xmlns).text.replace('\n', '').strip()
            ent.link = e.find('./link', self.xmlns).attrib['href'].replace('\n', '').strip()
            ent.id = e.find('./id', self.xmlns).text.replace('\n', '').strip()
            ent.updated = datetime.fromisoformat(e.find('./updated', self.xmlns).text.replace('\n', '').strip())
            self.entries.append(ent)
        self.finish_setup()

    def finish_setup(self):
        del self.entries_temp

    def __str__(self):
        return str(self.__dict__.items())


class ListResult(Result):
    def __init__(self, root, result: Result = None):
        pass


class Parser:
    def __init__(self):
        pass

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
        result.link = root.find('./link', result.xmlns).attrib['href']
        result.id = root.find('./id', result.xmlns).text
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
            return ErrorResult(root, result)
        return rresult





