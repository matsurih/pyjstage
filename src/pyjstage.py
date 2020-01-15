from src.result import SearchResult, ListResult
from src.service import Service
from typing import List
from urllib.parse import quote
import requests


class Pyjstage:
    def __init__(self, domain: str = 'http://api.jstage.jst.go.jp/searchapi/do?'):
        self.domain = domain
        pass

    def list(
            self,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: str = None,
            issn: str = None,
            cdjournal: str = None,
            volorder: str = None
    ) -> str:
        url = self.build_query(
            service=2,
            pubyearfrom=pubyearfrom,
            pubyearto=pubyearto,
            material=material,
            issn=issn,
            cdjournal=cdjournal,
            volorder=volorder)
        print(url)
        result = requests.get(url)
        return result.text

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
    ) -> str:
        """

        start: How many offsets you want to set, default 0.
        count: How many results you want to fetch, max & default is 1000.
        """
        url = self.build_query(
            service=3,
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
        print(url)
        result = requests.get(url)
        result.encoding = result.apparent_encoding
        print(result.encoding)
        return result.text

    def build_query(self, **kwargs):
        return self.domain + '&'.join(
            [f'{quote(k, encoding="utf8")}={quote(str(v), encoding="utf8")}' for k, v in kwargs.items() if v is not None]
        )


if __name__ == '__main__':
    pyjstage = Pyjstage()
    res = pyjstage.search(abst='統合失調症', count=3)
    print(res)
