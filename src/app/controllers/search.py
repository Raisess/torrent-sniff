from core.controller import Controller
from app.kernel.provider import Provider
from app.kernel.providers.comando_to import ComandoTo
from app.models import TitleModel
from app.views import SearchView

class SearchController(Controller):
  def __init__(self):
    self.__providers = [ComandoTo()]

  def search(self, term: str) -> str:
    magnet_links = []
    for provider in self.__providers:
      results = provider.search(term)[:3]
      for result in results:
        magnet_links.append({
          "host": provider.host(),
          "items": provider.get(result)
        })

    return self.render(SearchView(), { "data": magnet_links })
