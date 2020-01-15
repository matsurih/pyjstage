from src.pyjstage import Pyjstage
from service import Service


class TestPyjstage:
    def __init__(self):
        self.pyjstage = Pyjstage()

    def test_list(self):
        self.pyjstage.list(issn='test')

    def test_search(self):
        self.pyjstage.search(abst='統合失調症', count=3)

    def test_build_query(self):
        query = self.pyjstage.build_query(
            service=Service.LIST.value,
            pubyearfrom=2017,
            pubyearto=2018,
            material='material',
            issn='issn',
            cdjournal='cdjournal',
            volorder='volorder'
        )
        assert query == 'http://api.jstage.jst.go.jp/searchapi/do?service=2&pubyearfrom=2017&pubyearto=2018' \
                        '&material=material&issn=issn&cdjournal=cdjournal&volorder=volorder'

        query = self.pyjstage.build_query(
            service=Service.SEARCH.value,
            pubyearfrom=2015,
            pubyearto=2019,
            material='material',
            article='article',
            author='author',
            affile='affile',
            keyword='keyword',
            abst='abst',
            text='text',
            issn='issn',
            cdjournal='cdjournal',
            sortfig='sortfig',
            vol='vol',
            no='no',
            start='start',
            count='count'
        )
        assert query == 'http://api.jstage.jst.go.jp/searchapi/do?service=3&pubyearfrom=2015&pubyearto=2019' \
                        '&material=material&article=article&author=author&affile=affile&keyword=keyword&abst=abst' \
                        '&text=text&issn=issn&cdjournal=cdjournal&sortfig=sortfig&vol=vol&no=no&start=start&count=count'
