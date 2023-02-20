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
    price_range TEXT,
    category TEXT,
    description TEXT
);

CREATE TABLE opening_hours (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants, 
    day INT,
    open TIME,
    close TIME
);

CREATE TABLE review(
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants, 
    username TEXT,
    comment TEXT,
    rating INT,
    time TIMESTAMP
);