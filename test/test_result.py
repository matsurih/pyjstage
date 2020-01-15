from parser import Parser
from service import Service
from status import Status


class TestResult:
    def __init__(self):
        self.parser = Parser()

    def test_parse_search(self):
        with open('resources/search.xml', 'r') as f:
            xml_result = f.read()
        ret = self.parser.parse(xml_result.encode('utf-8'))
        assert ret.status == Status.OK.value
        assert ret.servicecd == Service.SEARCH.value
        assert ret.message is None
        assert ret.total_results > 0
        assert ret.start_index == 1
        assert ret.items_per_page == 3
        assert len(ret.entries) == 3

    def test_parse_list(self):
        with open('resources/list.xml', 'r') as f:
            xml_result = f.read()
        ret = self.parser.parse(xml_result.encode('utf-8'))
        assert ret.status == Status.OK.value
        assert ret.servicecd == Service.LIST.value
        assert ret.message is None
        assert ret.total_results > 0
        assert ret.start_index == 1
        assert ret.items_per_page == 1
        assert len(ret.entries) == 1


if __name__ == '__main__':
    tr = TestResult()
    tr.test_parse_list()
    tr.test_parse_search()
