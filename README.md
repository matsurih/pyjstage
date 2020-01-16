# pyjstage
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/matsurih/pyjstage/Python%20package)

## Description
[J-STAGE WebAPI](https://www.jstage.jst.go.jp/static/pages/OtherJstageServices/TAB2/-char/ja) Wrapper for Python

## Requirements
- Python >= 3.6

## Setup
```shell script
$ pip install -r requirements.txt  # If you're a developer, use requirements-dev.txt
$ python setup.py install
```

## Usage
```python
from pyjstage.pyjstage import Pyjstage


jstage = Pyjstage()

ret_search = jstage.search(issn='2186-6619', count=1)
ret_list = jstage.list(issn='2186-6619')

# ret_(search/list) is a (Search/List)Result Object.
```

## License
- MIT License, see [LICENSE](https://github.com/matsurih/pyjstage/blob/master/LICENSE) file.
