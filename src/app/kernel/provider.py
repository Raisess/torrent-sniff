from base64 import b64decode
from bs4 import BeautifulSoup
from urllib import request

from app.models import TitleModel

class Provider:
  def __init__(self, host: str):
    self.__host = b64decode(bytes(host, "utf-8")).decode("utf-8")

  def host(self) -> str:
    return self.__host

  def search(self, term: str) -> list[str]:
    raise NotImplemented()

  def get(self, id: str) -> list[TitleModel]:
    raise NotImplemented()

  def _fetch(self, path: str) -> BeautifulSoup:
    req = request.Request(f"{self.__host}/{path}", method="GET", headers={
      "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
      "accept-encoding": "text/html",
      "accept-language": "en-US,en;q=0.8",
      "cache-control": "max-age=0",
      "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
      "upgrade-insecure-requests": "1"
    })
    with request.urlopen(req) as response:
      data = response.read()
      response.close()

    return BeautifulSoup(data, "lxml")
