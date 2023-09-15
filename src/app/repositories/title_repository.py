from app.models.title import TitleModel
from app.repositories.__repository import __Repository

class TitleRepository(__Repository):
  def create(self, title: TitleModel) -> None:
    try:
      [id] = self.query("INSERT INTO titles(name, provider) VALUES(%(name)s, %(provider)s) RETURNING id;", {
        "name": title.name,
        "provider": title.provider,
      })

      cc = 0
      for magnet_link in title.magnet_links:
        try:
          self.query("INSERT INTO magnet_links(title_id, magnet_link) VALUES(%(title_id)s, %(magnet_link)s);", {
            "magnet_link": magnet_link,
            "title_id": id,
          }, False)
          cc += 1
        except:
          pass

      if cc == 0:
        self.query("DELETE FROM titles WHERE id = %(id)", { "id", id }, False)
    except Exception as ex:
      print(str(ex.with_traceback()))

  def list(self, term: str) -> list[TitleModel]:
    titles = self.query("SELECT id, name, provider FROM titles WHERE LOWER(name) LIKE LOWER(%(term)s);", {
      "term": f"%{term}%"
    })

    result = []
    for title in titles:
      magnet_links = self.query("SELECT magnet_link FROM magnet_links WHERE title_id = %(title_id)s;", {
        "title_id": title.id,
      })
      result.append(TitleModel(
        title.name,
        title.provider,
        magnet_links,
        title.id
      ))

    return result
