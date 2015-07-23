-- must be within dc_apt_listing database

BEGIN;
CREATE TABLE raw_data (
  title text,
  url text PRIMARY KEY,
  price money,
  bedrooms real,
  maplink text,
  longitude real,
  latitude real,
  updated_on timestamptz,
  content text,
  image_links text[],
  attributes text[],
  size text,
  parsed_on timestamp
);
COMMIT;

BEGIN;
GRANT ALL PRIVILEGES ON TABLE raw_data TO dcapa;
COMMIT;
