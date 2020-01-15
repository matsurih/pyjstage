from src.result import Parser


class TestResult:
    @staticmethod
    def test_parse_search():
        parser = Parser()
        with open('resources/search.xml', 'r') as f:
            xml_result = f.read()
        return parser.parse(xml_result.encode('utf-8'))


if __name__ == '__main__':
    result = TestResult.test_parse_search()
    print(result.__dict__.items())