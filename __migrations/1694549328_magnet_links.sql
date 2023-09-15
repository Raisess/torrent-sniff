CREATE TABLE IF NOT EXISTS magnet_links(
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title_id    UUID NOT NULL,
  magnet_link TEXT NOT NULL UNIQUE,
  created_at  TIMESTAMP NOT NULL DEFAULT now(),
  updated_at  TIMESTAMP NOT NULL DEFAULT now(),

  CONSTRAINT fk_title
    FOREIGN KEY(title_id) 
	  REFERENCES titles(id)
);
