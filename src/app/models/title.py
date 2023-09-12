from uuid import uuid4
from core.model import Model, dataclass

@dataclass
class TitleModel(Model):
  name: str
  magnet_links: list[str]
  id: str = str(uuid4())
