from urllib import parse

from app.kernel.provider import Provider
from app.models import TitleModel

class BFTorrent(Provider):
  def __init__(self):
    super().__init__("https://baixarfilmestorrent.org")

  def search(self, term: str) -> list[str]:
    data = self._fetch(f"?s={parse.quote(term)}")
    result = data.find_all("h2", attrs={ "class": "entry-title" })
    urls = [item.find("a").get("href") for item in result]
    ids = [item.split("/")[-2:][0] for item in urls]
    return ids

  def get(self, id: str) -> list[TitleModel]:
    data = self._fetch(id)
    name = data.find("h1", attrs={ "class": "entry-title" }).get_text()
    anchors = data.find_all("a")
    result = []
    for anchor in anchors:
      link = anchor.get("href")
      if link and link.startswith("magnet:?"):
        result.append(link)

    return [TitleModel(name, item) for item in result]
