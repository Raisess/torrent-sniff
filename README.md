# Torrent Sniff

A website to search for magnet links from a list of providers.

### Setup

Installing locally:

```shell
python3 -m pip install -r ./requirements.txt
python3 ./src/main.py
```

Using podman/docker:

```shell
./setup.sh
```

### Creating a new provider

The providers are just web scrapping classes who uses [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/),
follow the base example:

```python
# src/app/kernel/providers/my_provider.py

from app.kernel.provider import Provider
from app.models import TitleModel

class MyProvider(Provider):
  def __init__(self):
    super().__init__("https://HOST")

  def search(self, term: str) -> list[str]:
    beautiful_soup_of_the_page = self._fetch(f"path/{term}")
    # Return a list of ids for the get method

  def get(self, id: str) -> list[TitleModel]:
    beautiful_soup_of_the_page = self._fetch(f"path/sub/{id}")
    # Return a list of titles with magnet links (TitleModel)
```

Now you just need to add the provider to the `__providers` list on the `SearchController` (src/app/controllers/search.py).
