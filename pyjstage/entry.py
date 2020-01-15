class Entry:
    """Base class for Entry

    Attributes:
        issn: xxx
        eissn: xxx
        cdjournal: xxx
        material_title: xxx
        volume: xxx
        number: xxx
        starting_page: xxx
        pubyear: xxx
        systemcode: xxx
        systemname: xxx
        title: xxx
        link: xxx
        id: xxx
        updated: xxx
    """
    def __init__(self):
        """Initialize Entry class"""
        self.issn = None
        self.eissn = None
        self.cdjournal = None
        self.material_title = None
        self.volume = None
        self.number = None
        self.starting_page = None
        self.pubyear = None
        self.systemcode = None
        self.systemname = None
        self.title = None
        self.link = None
        self.id = None
        self.updated = None

    def __str__(self):
        return str(self.__dict__.items())


class ListEntry(Entry):
    """Entry class for List API

    Attributes:
        vols_title: xxx
        vols_link: xxx
        publisher_name: xxx
        publisher_url: xxx
    """
    def __init__(self):
        """Initialize ListEntry class"""
        super().__init__()
        self.vols_title = {}
        self.vols_link = {}
        self.publisher_name = None
        self.publisher_url = {}


class SearchEntry(Entry):
    """Entry class for Search API

    Attributes:
        article_title: xxx
        article_link: xxx
        author: xxx
        ending_page: xxx
        doi: xxx
    """
    def __init__(self):
        """Initialize SearchEntry class"""
        super().__init__()
        self.article_title = {}
        self.article_link = None
        self.author = None
        self.ending_page = None
        self.doi = None
