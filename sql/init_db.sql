CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    canonical_name TEXT,
    brand TEXT,
    model TEXT,
    category TEXT,
    description TEXT,
    image_url TEXT
);

CREATE TABLE offers (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    website_name TEXT,
    price NUMERIC,
    url TEXT,
    date_parsed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attributes (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    attribute_name TEXT,
    attribute_value TEXT
);