from core.model import Model, dataclass, field

@dataclass
class MagnetLink(Model):
  link: str
  id: str = field(default_factory=Model.GenUUID)


@dataclass
class TitleModel(Model):
  name: str
  provider: str
  magnet_links: list[MagnetLink]
  id: str = field(default_factory=Model.GenUUID)
