from pyjstage.result import Result
from pyjstage.parser import Parser
from pyjstage.service import Service
from pyjstage.order import ListOrder, SearchOrder
from urllib.parse import quote
import requests


class Pyjstage:
    """Pyjstage Class

    Attributes:
        domain: J-STAGE API domain
        parser: Parser object
    """
    # FIXME: 「同一パラメータで複数の検索条件（AND 条件）を指定するときは、半角スペースで区切ります」の対応
    def __init__(self, domain: str = 'http://api.jstage.jst.go.jp/searchapi/do?'):
        """Initialize Pyjstage class

        Args:
            domain: (Optional) J-STAGE API domain
        """
        self.domain: str = domain
        self.parser: Parser = Parser()

    def list(
            self,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: str = None,
            issn: str = None,
            cdjournal: str = None,
            volorder: ListOrder = None
    ) -> Result:
        # FIXME: docstring
        """Access LIST API

        Args:
            pubyearfrom: (Optional) Year you want to search when papers were published from.
            pubyearto: (Optional) Year you want to search when papers were published to.
            material: (Optional) xxxx
            issn: (Optional) ISSN you want to search.
            cdjournal: (Optional) Journal code you want to search.
            volorder: (Optional) How order are responses sorted.
        Returns:
            Result object which contains meta data and contents
        Raises:
            JstageError: Error caused by J-STAGE API
            JstageWarning: Warning caused by J-STAGE API
        """
        url = self.build_query(
            service=Service.LIST.value,
            pubyearfrom=pubyearfrom,
            pubyearto=pubyearto,
            material=material,
            issn=issn,
            cdjournal=cdjournal,
            volorder=volorder.value)
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
            sortfig: SearchOrder = None,
            vol: int = None,
            no: int = None,
            start: int = None,
            count: int = None
    ) -> Result:
        """Access SEARCH API

        Longer detail

        Args:
            pubyearfrom: xxx
            pubyearto: xxx
            material: xxx
            article: xxx
            author: xxx
            affile: xxx
            keyword: xxx
            abst: xxx
            text: xxx
            issn: xxx
            cdjournal: xxx
            sortfig: xxx
            vol: xxx
            no: xxx
            start: How many offsets you want to set, default 0.
            count: How many results you want to fetch, max & default is 1000.
        Returns:
            Xxxx
        Raises:
            xxxError: xxx
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
            sortfig=sortfig.value,
            vol=vol,
            no=no,
            start=start,
            count=count
        )
        response = requests.get(url)
        result = self.parser.parse(response.text.encode('utf-8'))
        return result

    def build_query(self, **kwargs):
        """Build url with queries

        Args:
            kwargs: key-value pairs for querying
        Returns:
            URL-string which can access J-STAGE API
        Raises:
            xxxError: Error
        """
        return self.domain + '&'.join(
            [
                f'{quote(k, encoding="utf8")}={quote(str(v), encoding="utf8")}'
                for k, v in kwargs.items() if v is not None
            ]
        )
