CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    is_admin BOOLEAN
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name TEXT, 
    address TEXT UNIQUE,
    price_range INT,
    category TEXT
);