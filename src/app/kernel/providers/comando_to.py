from urllib import parse

from app.kernel.provider import Provider
from app.models import TitleModel

class ComandoTo(Provider):
  def __init__(self):
    super().__init__("https://comando.la")

  def search(self, term: str) -> list[str]:
    data = self._fetch(f"?s={parse.quote(term)}")
    result = data.find_all("h2", attrs={ "class": "entry-title" })
    urls = [item.find("a").get("href") for item in result]
    ids = [item.split("/")[-2:][0] for item in urls]
    return ids

  def get(self, id: str) -> list[TitleModel]:
    data = self._fetch(id)
    name = data.find("h1", attrs={ "class": "entry-title" }).get_text()
    result = data.find_all("a", attrs={ "class": "customButton" })
    if len(result) == 0:
      result = data.find_all("a")
      _ = []
      for item in result:
        if item.get("href") and item.get("href").startswith("magnet:?"):
          _.append(item)

      result = _

    return [TitleModel(name, item.get("href")) for item in result]
