from core.controller import Controller
from app.kernel.provider import Provider
from app.kernel.providers.comando_to import ComandoTo
from app.models import TitleModel
from app.views import SearchView

PAGE_SIZE = 1

class SearchController(Controller):
  def __init__(self):
    self.__providers = [ComandoTo()]

  def search(self, term: str | None) -> str:
    magnet_links = []
    if term:
      for provider in self.__providers:
        results = provider.search(term)[:PAGE_SIZE]
        for result in results:
          magnet_links.append({
            "host": provider.host(),
            "items": provider.get(result)
          })

    return self.render(SearchView(), { "data": magnet_links })
