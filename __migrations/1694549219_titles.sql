CREATE TABLE IF NOT EXISTS titles(
  id         UUID PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
  name       VARCHAR(200) UNIQUE NOT NULL,
  provider   VARCHAR(100) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  updated_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE INDEX title_name ON titles(name);
