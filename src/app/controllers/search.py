from threading import Thread

from __core.controller import Controller
from __core.env import Env
from app.kernel.provider import Provider
from app.kernel.providers.bf_torrent import BFTorrent
from app.kernel.providers.capitao_filmes import CapitaoFilmes
from app.kernel.providers.comando_to import ComandoTo
from app.kernel.providers.pirate_torrents import PirateTorrents
from app.kernel.providers.mega_torrent import MegaTorrent
from app.models import TitleModel
from app.views import SearchView

def _handle_search(
  provider: Provider,
  term: str,
  fetch_size: int,
  result: list[TitleModel]
) -> None:
  data = provider.search(term)[:fetch_size]
  for item in data:
    torrent = provider.get(item)
    result.append(torrent)


FETCH_SIZE = int(Env.Get("FETCH_SIZE") or 1)

class SearchController(Controller):
  def __init__(self):
    self.__providers = [
      BFTorrent(),
      ComandoTo(),
      PirateTorrents(),
      MegaTorrent(),
      CapitaoFilmes()
    ]

  def search_page(self, term: str | None, fetch_size: str | None) -> str:
    fetch_size = int(fetch_size or FETCH_SIZE)
    return self.render(SearchView(), {
      "data": self.__search(term, fetch_size),
      "term": term
    })

  def search_json(self, term: str, fetch_size: str | None) -> str:
    if not term or len(term.strip()) == 0:
      raise Exception("Invalid search term")

    fetch_size = int(fetch_size or FETCH_SIZE)
    return self.json([
      item.to_dict() for item in self.__search(term, fetch_size)
    ])

  def __search(self, term: str, fetch_size: int) -> list[TitleModel]:
    result = []
    if term:
      tgroup = []
      for provider in self.__providers:
        thread = Thread(
          target=_handle_search,
          args=[provider, term, fetch_size, result]
        )
        thread.start()
        tgroup.append(thread)

      for thread in tgroup:
        thread.join()

    return result
