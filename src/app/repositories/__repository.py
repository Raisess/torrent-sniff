from postgres import Postgres

DB_NAME = "torrent-sniff"
DB_USER = "torrent-sniff"
DB_PASS = "torrent-sniff"
DB_HOST = "localhost"
DB_PORT = 5432

class __Repository:
  def __init__(self):
    url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    self.__conn = Postgres(url, maxconn=30)

  def query(
    self,
    sql: str,
    data: dict[str, str | int] = None,
    ret: bool = True
  ) -> list[dict]:
    if ret:
      return self.__conn.all(sql, data)

    self.__conn.run(sql, data)
    return []
