class Entry:
    issn = None
    eissn = None
    cdjournal = None
    material_title = None
    volume = None
    number = None
    starting_page = None
    pubyear = None
    systemcode = None
    systemname = None
    title = None
    link = None
    id = None
    updated = None


class ListEntry(Entry):
    vols_title = {}
    vols_link = {}
    publisher_name = None
    publisher_url = {}

    def __init__(self):
        super().__init__()

    def __str__(self):
        return str(self.__dict__.items())


class SearchEntry(Entry):
    article_title = {}
    article_link = None
    author = None
    ending_page = None
    doi = None

    def __init__(self):
        super().__init__()

    def __str__(self):
        return str(self.__dict__.items())
