from .result import SearchResult, ListResult
from .service import Service
from typing import List


class Pyjstage:
    def __init__(self, domain: str = 'http://api.jstage.jst.go.jp/searchapi/do?'):
        self.domain = domain
        pass

    def list(
            self,
            service: Service,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: str = None,
            issn: str = None,
            cdjournal: str = None,
            volorder: str = None
    ) -> List[ListResult]:
        return [ListResult()]

    def search(
            self,
            service: Service,
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
    ) -> List[SearchResult]:
        """

        start: How many offsets you want to set, default 0.
        count: How many results you want to fetch, max & default is 1000.
        """
        return [SearchResult()]

    def build_query(self, **kwargs):
        return self.domain + '&'.join([f'{k}={v}' for k, v in kwargs.items()])
