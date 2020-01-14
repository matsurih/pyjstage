from src.pyjstage import Pyjstage
from src.service import Service


class TestPyjstage:
    def __init__(self):
        self.pyjstage = Pyjstage()

    def test_list(self):
        self.pyjstage.list(service=Service())

    def test_search(self):
        self.pyjstage.search(service=Service())

    def test_build_query(self):
        self.pyjstage.build_query()
