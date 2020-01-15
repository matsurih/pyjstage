from src.pyjstage import Pyjstage
from service import Service
from datetime import datetime


class TestPyjstage:
    def __init__(self):
        self.pyjstage = Pyjstage()

    def test_list(self):
        self.pyjstage.list(issn='2186-6619')

    def test_search(self):
        ret = self.pyjstage.search(issn='2186-6619', count=1)
        assert ret.status == 0
        assert ret.link == 'http://api.jstage.jst.go.jp/searchapi/do?service=3&issn=2186-6619&count=1'
        assert ret.servicecd == 3
        assert ret.message is None
        assert ret.total_results > 0
        assert ret.start_index == 1
        assert ret.items_per_page == 1
        assert len(ret.entries) == 1

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


if __name__ == '__main__':
    tp = TestPyjstage()
    tp.test_search()
