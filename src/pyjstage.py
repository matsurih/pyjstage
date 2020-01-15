from src.result import Result
from src.parser import Parser
from src.service import Service
from urllib.parse import quote
import requests


class Pyjstage:
    def __init__(self, domain: str = 'http://api.jstage.jst.go.jp/searchapi/do?'):
        self.domain = domain
        self.parser = Parser()

    def list(
            self,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: str = None,
            issn: str = None,
            cdjournal: str = None,
            volorder: str = None
    ) -> Result:
        url = self.build_query(
            service=Service.LIST.value,
            pubyearfrom=pubyearfrom,
            pubyearto=pubyearto,
            material=material,
            issn=issn,
            cdjournal=cdjournal,
            volorder=volorder)
        response = requests.get(url)
        return self.parser.parse(response.text.encode('utf-8'))

    def search(
            self,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: str = None,
            article: str = None,
            author: str = None,
            affile: str = None,
            keyword: str = None,
            abst: str = None,
            text: str = None,
            issn: str = None,
            cdjournal: str = None,
            sortfig: str = None,
            vol: int = None,
            no: int = None,
            start: int = None,
            count: int = None
    ) -> Result:
        """

        start: How many offsets you want to set, default 0.
        count: How many results you want to fetch, max & default is 1000.
        """
        url = self.build_query(
            service=Service.SEARCH.value,
            pubyearfrom=pubyearfrom,
            pubyearto=pubyearto,
            material=material,
            article=article,
            author=author,
            affile=affile,
            keyword=keyword,
            abst=abst,
            text=text,
            issn=issn,
            cdjournal=cdjournal,
            sortfig=sortfig,
            vol=vol,
            no=no,
            start=start,
            count=count
        )
        response = requests.get(url)
        result = self.parser.parse(response.text.encode('utf-8'))
        return result

    def build_query(self, **kwargs):
        return self.domain + '&'.join(
            [f'{quote(k, encoding="utf8")}={quote(str(v), encoding="utf8")}' for k, v in kwargs.items() if v is not None]
        )


if __name__ == '__main__':
    pyjstage = Pyjstage()
    res = pyjstage.search(abst='統合失調症', count=3)
    print(res)
