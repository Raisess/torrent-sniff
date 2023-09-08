from threading import Thread

from core.controller import Controller
from app.kernel.provider import Provider
from app.kernel.providers.bf_torrent import BFTorrent
from app.kernel.providers.comando_to import ComandoTo
from app.kernel.providers.pirate_torrents import PirateTorrents
from app.models import TitleModel
from app.views import SearchView

PAGE_SIZE = 1

def handle_search(provider: Provider, term: str, magnet_links: list[dict]) -> None:
  results = provider.search(term)[:PAGE_SIZE]
  for result in results:
    magnet_links.append({
      "host": provider.host(),
      "items": provider.get(result)
    })


class SearchController(Controller):
  def __init__(self):
    self.__providers = [BFTorrent(), ComandoTo(), PirateTorrents()]

  def search(self, term: str | None) -> str:
    magnet_links = []
    if term:
      tgroup = []
      for provider in self.__providers:
        thread = Thread(target=handle_search, args=[provider, term, magnet_links])
        thread.start()
        tgroup.append(thread)

      for thread in tgroup:
        thread.join()

    return self.render(SearchView(), { "data": magnet_links })
