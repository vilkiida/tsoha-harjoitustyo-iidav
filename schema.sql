CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT,
  password TEXT,
  admin BOOLEAN
);

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  name TEXT,
  year INTEGER,
  genre TEXT,
  description TEXT,
  leading_roles TEXT
);

CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  user_id iNTEGER REFERENCES users,
  movie_id INTEGER REFERENCES movies,
  grade iNTEGER,
  review TEXT,
  time TIMESTAMP
);

CREATE TABLE suggestions (
  id SERIAL PRIMARY KEY,
  name TEXT,
  year INTEGER,
  genre TEXT,
  description TEXT,
  leading_roles TEXT,
  user_id INTEGER REFERENCES users,
  time TIMESTAMP,
  accepted INTEGER
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE movies_in_categories (
  category_id INTEGER REFERENCES categories,
  movie_id INTEGER REFERENCES movies
);

