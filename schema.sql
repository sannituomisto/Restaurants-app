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
    category TEXT,
    description TEXT
);

CREATE TABLE opening_hours (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants(id) ON DELETE CASCADE, 
    day INT,
    open TEXT,
    close TEXT,
    status TEXT
);

CREATE TABLE review(
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants(id) ON DELETE CASCADE, 
    username TEXT REFERENCES users(username) ON DELETE CASCADE,
    comment TEXT,
    rating INT,
    time DATE DEFAULT CURRENT_DATE
);

CREATE TABLE favorites(
    id SERIAL PRIMARY KEY,
    username TEXT REFERENCES users(username) ON DELETE CASCADE,
    restaurant_id INTEGER REFERENCES restaurants(id) ON DELETE CASCADE
);